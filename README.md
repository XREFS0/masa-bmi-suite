# MASA Body Composition & BMI Suite

A desktop biometric analysis utility calculating Body Mass Index (BMI) in compliance with World Health Organization (WHO) classification standards.

## Technical Architecture

The codebase follows modular software engineering patterns and OOP structure, designed for reliability, high maintainability, and clean separation of concerns:

- **Component Layering**: User interface and computational state are decoupled into specialized controllers and event loops.
- **Defensive Engineering**: Comprehensive validation guards protect against malformed inputs and runtime exceptions.
- **Modern Design Tokens**: Designed with a high-contrast dark aesthetic adhering to modern developer tooling visual standards.

## Features

- Metric unit ingestion (height in centimeters, weight in kilograms).
- Dynamic canvas-rendered visual gauge with live pointer synchronization.
- Standardized classification tiers from Underweight to Class II/Severe Obesity.
- Contextual health recommendations based on computed index.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter
```

## Execution

Initialize and run the module via the command line:

```bash
python "Body Mass Index Calculator App Using Tkinter in Python/Python_BMI_GUI.py"
```

## Project Structure

```
.
├── Body Mass Index Calculator App Using Tkinter in Python
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
