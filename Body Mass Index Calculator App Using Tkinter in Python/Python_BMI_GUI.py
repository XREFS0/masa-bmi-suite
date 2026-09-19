"""
MASA Precision Body Mass Index (BMI) Health Suite
Developer: MASA
"""

import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaBmiSuite(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MASA Health - BMI Analytics")
        self.geometry("450x640")
        self.resizable(False, False)
        self.configure(fg_color="#090D16")

        self._build_ui()

    def _build_ui(self):
        header = ctk.CTkFrame(self, fg_color="#131B2E", corner_radius=16)
        header.pack(fill="x", padx=20, pady=(20, 15))

        title = ctk.CTkLabel(
            header,
            text="MASA BODY COMPOSITION",
            font=ctk.CTkFont(family="Segoe UI", size=17, weight="bold"),
            text_color="#10B981",
        )
        title.pack(pady=(14, 2))

        subtitle = ctk.CTkLabel(
            header,
            text="Body Mass Index & Fitness Classification",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#94A3B8",
        )
        subtitle.pack(pady=(0, 14))

        input_card = ctk.CTkFrame(self, fg_color="#131B2E", corner_radius=16)
        input_card.pack(fill="x", padx=20, pady=5)

        lbl_name = ctk.CTkLabel(input_card, text="FULL NAME", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8")
        lbl_name.pack(anchor="w", padx=20, pady=(15, 2))
        self.name_entry = ctk.CTkEntry(input_card, placeholder_text="e.g. MASA", font=ctk.CTkFont(size=13))
        self.name_entry.pack(fill="x", padx=20, pady=(0, 10))

        row_measurements = ctk.CTkFrame(input_card, fg_color="transparent")
        row_measurements.pack(fill="x", padx=20, pady=(0, 15))
        row_measurements.grid_columnconfigure(0, weight=1)
        row_measurements.grid_columnconfigure(1, weight=1)

        lbl_h = ctk.CTkLabel(row_measurements, text="HEIGHT (CM)", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8")
        lbl_h.grid(row=0, column=0, sticky="w", pady=(0, 2))
        self.height_entry = ctk.CTkEntry(row_measurements, placeholder_text="175", font=ctk.CTkFont(size=13))
        self.height_entry.grid(row=1, column=0, sticky="ew", padx=(0, 8))

        lbl_w = ctk.CTkLabel(row_measurements, text="WEIGHT (KG)", font=ctk.CTkFont(size=11, weight="bold"), text_color="#94A3B8")
        lbl_w.grid(row=0, column=1, sticky="w", pady=(0, 2))
        self.weight_entry = ctk.CTkEntry(row_measurements, placeholder_text="70", font=ctk.CTkFont(size=13))
        self.weight_entry.grid(row=1, column=1, sticky="ew", padx=(8, 0))

        btn_calc = ctk.CTkButton(
            self,
            text="Analyze Health Metrics",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#059669",
            hover_color="#047857",
            height=42,
            corner_radius=12,
            command=self._calculate_bmi,
        )
        btn_calc.pack(fill="x", padx=20, pady=12)

        self.display_card = ctk.CTkFrame(self, fg_color="#131B2E", corner_radius=16)
        self.display_card.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.bmi_score_lbl = ctk.CTkLabel(
            self.display_card,
            text="--.-",
            font=ctk.CTkFont(family="Segoe UI", size=48, weight="bold"),
            text_color="#F8FAFC",
        )
        self.bmi_score_lbl.pack(pady=(15, 2))

        self.status_badge = ctk.CTkLabel(
            self.display_card,
            text="Awaiting User Input",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#94A3B8",
            fg_color="#1E293B",
            corner_radius=12,
            padx=14,
            pady=4,
        )
        self.status_badge.pack(pady=(0, 15))

        self.canvas = ctk.CTkCanvas(self.display_card, width=380, height=45, bg="#131B2E", highlightthickness=0)
        self.canvas.pack(pady=5)
        self._render_bar_scale()

        self.guidance_lbl = ctk.CTkLabel(
            self.display_card,
            text="Standard World Health Organization BMI thresholds applied.",
            font=ctk.CTkFont(size=11),
            text_color="#64748B",
            wraplength=360,
        )
        self.guidance_lbl.pack(pady=(10, 15))

    def _render_bar_scale(self, pointer_val=None):
        self.canvas.delete("all")
        bar_w = 360
        start_x = 10
        y1, y2 = 20, 32

        segments = [
            (0, 18.5, "#F59E0B"),
            (18.5, 25.0, "#10B981"),
            (25.0, 30.0, "#FBBF24"),
            (30.0, 35.0, "#F97316"),
            (35.0, 50.0, "#EF4444"),
        ]

        total_range = 50.0
        for seg_start, seg_end, color in segments:
            x_left = start_x + (seg_start / total_range) * bar_w
            x_right = start_x + (seg_end / total_range) * bar_w
            self.canvas.create_rectangle(x_left, y1, x_right, y2, fill=color, width=0)

        if pointer_val is not None:
            clamped = max(0.0, min(50.0, pointer_val))
            px = start_x + (clamped / total_range) * bar_w
            self.canvas.create_polygon(
                px - 6, 8,
                px + 6, 8,
                px, y1 - 2,
                fill="#F8FAFC",
                outline="#090D16",
            )
            self.canvas.create_line(px, y1, px, y2 + 5, fill="#F8FAFC", width=2)

    def _calculate_bmi(self):
        try:
            h_cm = float(self.height_entry.get().strip())
            w_kg = float(self.weight_entry.get().strip())
            name = self.name_entry.get().strip() or "Client"
            if h_cm <= 0 or w_kg <= 0:
                raise ValueError
        except ValueError:
            self.status_badge.configure(text="Invalid Height / Weight", text_color="#EF4444", fg_color="#3B1219")
            return

        h_m = h_cm / 100.0
        bmi = w_kg / (h_m * h_m)

        if bmi < 18.5:
            cat, color, badge_bg = "Underweight", "#F59E0B", "#382506"
            tip = f"{name}, your BMI indicates you are below the optimal weight range."
        elif bmi < 24.9:
            cat, color, badge_bg = "Normal Weight (Optimal)", "#10B981", "#052E1E"
            tip = f"Excellent shape, {name}! Your weight is perfectly balanced for your height."
        elif bmi < 29.9:
            cat, color, badge_bg = "Overweight", "#FBBF24", "#3D2E05"
            tip = f"{name}, your BMI suggests a moderate surplus. Regular cardio is advised."
        elif bmi < 34.9:
            cat, color, badge_bg = "Class I Obesity", "#F97316", "#3A1B07"
            tip = f"Notice: {name}, elevated health risks detected. Consider consulting a nutritionist."
        else:
            cat, color, badge_bg = "Class II / Severe Obesity", "#EF4444", "#3D0E13"
            tip = f"High alert: {name}, high obesity classification. Medical guidance is strongly recommended."

        self.bmi_score_lbl.configure(text=f"{bmi:.1f}", text_color=color)
        self.status_badge.configure(text=cat, text_color=color, fg_color=badge_bg)
        self.guidance_lbl.configure(text=tip)
        self._render_bar_scale(bmi)


if __name__ == "__main__":
    app = MasaBmiSuite()
    app.mainloop()
