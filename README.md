<h1 align = center> QR Code Generator using Python</h1>

<p align="center">
  <b>A Python project exploring QR code generation, image customization, and error correction.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Library-qrcode-informational" />
  <img src="https://img.shields.io/badge/Image%20Processing-Pillow-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 Table of Contents

- [1. Project Overview](#-1-project-overview)
- [2. Problem Statement](#-2-problem-statement)
- [3. Project Objectives](#-3-project-objectives)
- [4. Software Requirements Specification (SRS)](#-4-software-requirements-specification-srs)
- [5. Project Features](#-5-project-features)
- [6. Project Structure](#-6-project-structure)
- [7. Technologies and Libraries](#-7-technologies-and-libraries)
- [8. Understanding QR Codes](#-8-understanding-qr-codes)
- [9. Simple QR Code Generator](#-9-simple-qr-code-generator)
- [10. Advanced QR Code Generator](#-10-advanced-qr-code-generator)
- [11. Understanding the Advanced Implementation](#-11-understanding-the-advanced-implementation)
- [12. Installation and Setup](#-12-installation-and-setup)
- [13. Execution Guide](#-13-execution-guide)
- [14. System Workflow](#-14-system-workflow)
- [15. Testing and Validation](#-15-testing-and-validation)
- [16. Common Errors and Troubleshooting](#-16-common-errors-and-troubleshooting)
- [17. Core Concepts Learned](#-17-core-concepts-learned)
- [18. Interview Questions and Answers](#-18-interview-questions-and-answers)
- [19. Limitations](#-19-limitations)
- [20. Future Enhancements](#-20-future-enhancements)
- [21. Author](#-21-author)

---

# 📖 1. Project Overview

The **QR Code Generator** is a Python-based project that demonstrates how digital information can be converted into machine-readable QR codes.

The project contains two implementations:

| Implementation | Description |
|---|---|
| Simple QR Generator | Generates QR codes using a straightforward approach. |
| Advanced QR Generator | Generates customized QR codes with configurable properties such as error correction, box size, border, and colors. |

The advanced implementation generates a QR code that redirects users to my GitHub profile.

**GitHub Profile:** https://github.com/palaksharma032

The project uses the `qrcode` library for QR code generation and Pillow for image-related operations.

### Why this project?

This project was developed to understand:

- How QR codes are generated programmatically.
- How Python libraries can simplify complex operations.
- How to configure QR code properties.
- How error correction improves QR code reliability.
- How generated images can be customized and saved.

---

# 🎯 2. Problem Statement

Sharing digital information through long URLs or manually entered text can be inconvenient.

A QR code provides a compact and convenient way to encode information that can be accessed by scanning it with a compatible device.

The objective of this project is to develop a Python-based solution that converts text or URLs into QR code images, with both basic and customized generation approaches.

---

# 🎯 3. Project Objectives

1. Understand the fundamentals of QR code generation.
2. Implement QR code generation using Python.
3. Explore external Python libraries.
4. Learn how to configure QR code properties.
5. Understand error correction in QR codes.
6. Customize QR code appearance using colors.
7. Save generated QR codes as image files.
8. Develop a foundation for more advanced image-generation applications.

---

# 📋 4. Software Requirements Specification (SRS)

## 4.1 Introduction

The Software Requirements Specification defines the functional and non-functional requirements of the QR Code Generator.

The system is designed as a lightweight Python application that generates QR code images from digital information.

## 4.2 Scope

The project supports two approaches to QR code generation:

- Basic QR code creation.
- Advanced QR code creation with customization.

The generated QR code can be scanned using a QR-compatible camera or scanner.

## 4.3 Functional Requirements

| ID | Requirement | Description |
|---|---|---|
| FR-01 | QR Generation | The system should generate QR codes. |
| FR-02 | Data Encoding | The system should encode supported text or URL data. |
| FR-03 | Image Generation | The system should convert QR data into an image. |
| FR-04 | Customization | The advanced implementation should support custom colors. |
| FR-05 | Error Correction | The advanced implementation should support error correction configuration. |
| FR-06 | Image Saving | The generated QR code should be saved as an image file. |

## 4.4 Non-Functional Requirements

- **Usability:** The application should be simple to execute.
- **Performance:** QR code generation should complete efficiently for ordinary inputs.
- **Reliability:** Generated QR codes should remain readable when configured appropriately.
- **Maintainability:** The code should be easy to understand and modify.
- **Portability:** The project should run on systems supporting Python and its dependencies.

## 4.5 Hardware Requirements

- Computer or laptop.
- Minimum 2 GB RAM recommended.
- Sufficient storage for Python and required packages.
- Camera or smartphone for testing generated QR codes.

## 4.6 Software Requirements

| Component | Requirement |
|---|---|
| Programming Language | Python 3.x |
| QR Generation Library | qrcode |
| Image Processing Library | Pillow |
| Code Editor | VS Code / PyCharm |
| Operating System | Windows / Linux / macOS |

## 4.7 Assumptions and Constraints

- Python must be installed.
- Required dependencies must be available.
- The generated image must be accessible for scanning.
- The encoded URL or text must be valid for its intended use.
- The advanced implementation currently uses a predefined GitHub profile URL.

---

# ✨ 5. Project Features

## Simple QR Code Generator

- Basic QR code generation.
- Encoding of digital information.
- Generation of QR code images.
- Straightforward implementation.

## Advanced QR Code Generator

- Custom QR code configuration.
- High error correction.
- Custom foreground and background colors.
- Adjustable box size and border.
- Automatic QR code fitting.
- PNG image export.

---

# 📁 6. Project Structure

```text
QR-Code-Generator/
│
├── simple_qr.py
├── advanced_qr.py
├── Palak Sharma Github Profile.png
│
└── README.md
```

**File descriptions:**

| File | Purpose |
|---|---|
| `simple_qr.py` | Basic QR code generation implementation. |
| `advanced_qr.py` | Customized QR code generation implementation. |
| `Palak Sharma Github Profile.png` | Generated QR code image from the advanced implementation. |
| `README.md` | Project documentation. |

---

# 🛠️ 7. Technologies and Libraries

## 7.1 Python

Python is the primary programming language used in this project.

It provides a simple syntax and a rich ecosystem of libraries for automation, image processing, data handling, and application development.

## 7.2 qrcode

The `qrcode` library is used to generate QR codes.

It provides functionality for:

- Creating QR code objects.
- Adding data.
- Configuring QR code parameters.
- Generating QR code images.

Installation:

```bash
pip install qrcode[pil]
```

## 7.3 Pillow (PIL)

Pillow is a Python imaging library used to create, manipulate, and save image files.

In this project, it supports image generation through the QR code library.

Import:

```python
from PIL import Image
```

---

# 📚 8. Understanding QR Codes

## 8.1 What is a QR Code?

QR stands for **Quick Response**.

A QR code is a two-dimensional barcode that stores information using a pattern of black and white or differently colored modules.

Unlike traditional one-dimensional barcodes, QR codes store information horizontally and vertically.

They can encode:

- URLs
- Text
- Contact information
- Email addresses
- Wi-Fi credentials
- Other supported data formats

## 8.2 How Does a QR Code Work?

The general process involves:

1. Information is provided to the QR generator.
2. The information is encoded into a QR code structure.
3. The encoded data is represented through a pattern of modules.
4. The QR code is generated as an image.
5. A scanner reads the image and decodes the information.

## 8.3 Important QR Code Components

- **Finder Patterns:** Large square patterns near three corners that help scanners locate and orient the QR code.
- **Timing Patterns:** Alternating modules that help determine the grid structure.
- **Alignment Patterns:** Help correct distortion and improve scanning.
- **Data Modules:** Store the encoded information.
- **Quiet Zone:** The empty border surrounding the QR code.

## 8.4 QR Code Versions

QR codes have 40 standardized versions.

| Version | Module Dimensions |
|---|---|
| Version 1 | 21 × 21 |
| Version 2 | 25 × 25 |
| Version 3 | 29 × 29 |
| Version 4 | 33 × 33 |
| Version 5 | 37 × 37 |
| Version 40 | 177 × 177 |

The number of modules increases by four in each dimension with every version.

A higher version generally allows more data to be stored, depending on the data type and error correction level.

## 8.5 Error Correction Levels

QR codes use Reed-Solomon error correction to recover information when some parts of the code are damaged or obscured.

There are four standard error correction levels:

| Level | Approximate Recovery Capacity |
|---|---|
| L | 7% |
| M | 15% |
| Q | 25% |
| H | 30% |

**Important:** These percentages represent approximate restoration capacity, not a guarantee that the same percentage of any QR image can be removed while preserving readability.

Higher error correction generally increases the amount of redundancy in the QR code and may require a larger version for the same data.

---

# 🟢 9. Simple QR Code Generator

The simple implementation focuses on the basic process of generating a QR code.

### Main Operations

1. Import the required QR code library.
2. Create a QR code using the provided data.
3. Generate the QR code image.
4. Save the resulting image.

### Concepts Demonstrated

- Importing Python libraries.
- Working with external packages.
- Encoding information.
- Creating image files.
- Basic file handling.

### Learning Outcome

The simple implementation introduces the fundamental QR code generation process without requiring extensive configuration.

---

# 🔵 10. Advanced QR Code Generator

The advanced implementation introduces QR code customization and configuration.

It generates a customized QR code that links to my GitHub profile.

### Generated QR Code Configuration

| Parameter | Value |
|---|---|
| Version | 1 |
| Error Correction | H |
| Box Size | 10 |
| Border | 4 |
| Foreground Color | Blue |
| Background Color | Beige |
| Output Format | PNG |

### Generated Output

**File Name:** `Palak Sharma Github Profile.png`

**Encoded URL:** https://github.com/palaksharma032

---

# 💡 11. Understanding the Advanced Implementation

The following section explains the actual operations performed by `advanced_qr.py`.

## 11.1 Importing Libraries

```python
import qrcode
from PIL import Image
```

**Explanation:**

- `import qrcode` imports the QR code generation library.
- `from PIL import Image` imports the Image class from Pillow.

These libraries provide the functionality required for QR code generation and image handling.

## 11.2 Creating the QR Code Object

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
```

This statement creates a QRCode object with specific configuration parameters.

### Understanding Each Parameter

**1. version=1**

Specifies the initial QR code version.

Version 1 has a grid of 21 × 21 modules.

The `fit=True` option used later allows the library to adjust the version when required.

**2. error_correction**

```python
qrcode.constants.ERROR_CORRECT_H
```

Specifies the highest standard QR error correction level.

The four available constants are:

```python
qrcode.constants.ERROR_CORRECT_L
qrcode.constants.ERROR_CORRECT_M
qrcode.constants.ERROR_CORRECT_Q
qrcode.constants.ERROR_CORRECT_H
```

Level H provides approximately 30% error recovery capacity.

**3. box_size=10**

Determines the number of pixels used for each QR code module.

A larger box size produces a larger image.

**4. border=4**

Defines the width of the quiet zone around the QR code.

The value 4 represents four modules of border space.

## 11.3 Adding Data to the QR Code

```python
qr.add_data("https://github.com/palaksharma032")
```

The `add_data()` method adds the information that needs to be encoded.

In this project, the information is a GitHub profile URL.

When someone scans the generated QR code, the encoded URL can be decoded and opened.

## 11.4 Generating the QR Code

```python
qr.make(fit=True)
```

The `make()` method generates the QR code structure.

**What does `fit=True` mean?**

It allows the library to automatically select a suitable QR code version based on the amount of data.

This is useful when the data does not fit within the initially specified version.

## 11.5 Creating a Customized Image

```python
img = qr.make_image(
    fill_color="blue",
    back_color="beige"
)
```

The `make_image()` method converts the generated QR code into an image.

Two important parameters are used:

| Parameter | Meaning |
|---|---|
| `fill_color` | Determines the color of the QR code modules. |
| `back_color` | Determines the background color. |

In this implementation:

- QR modules are blue.
- Background is beige.

This makes the generated QR code visually customized rather than using the default black-and-white appearance.

## 11.6 Saving the Generated Image

```python
img.save("Palak Sharma Github Profile.png")
```

The `save()` method exports the generated image to the specified file.

The output is saved in PNG format.

The generated image can then be opened, shared, or scanned.

## 11.7 Complete Code

```python
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://github.com/palaksharma032")
qr.make(fit=True)

img = qr.make_image(
    fill_color="blue",
    back_color="beige"
)

img.save("Palak Sharma Github Profile.png")
```

---

# ⚙️ 12. Installation and Setup

Follow these steps to run the project locally.

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### Step 3: Navigate to the Project

```bash
cd QR-Code-Generator
```

### Step 4: Install Dependencies

```bash
pip install qrcode[pil]
```

### Step 5: Verify Installation

```bash
python -c "import qrcode; print('QR Code library installed successfully')"
```

---

# ▶️ 13. Execution Guide

### Run the Simple Generator

```bash
python simple_qr.py
```

### Run the Advanced Generator

```bash
python advanced_qr.py
```

After successful execution, the advanced implementation generates:

```text
Palak Sharma Github Profile.png
```

The generated image is saved in the current working directory.

---

# 🔄 14. System Workflow

The overall workflow of the project:

```text
          START
            |
            v
     Import Libraries
            |
            v
      Select Generator
            |
       +----+----+
       |         |
       v         v
     Simple   Advanced
       |         |
       v         v
  Provide Data  Configure QR
       |         |
       +----+----+
            |
            v
      Encode Data
            |
            v
     Generate QR Code
            |
            v
      Create Image
            |
            v
       Save as PNG
            |
            v
           END
```

---

# 🧪 15. Testing and Validation

Testing ensures that the generated QR code behaves as expected.

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-01 | Execute the simple generator | QR code should be generated. |
| TC-02 | Execute the advanced generator | Customized QR code should be generated. |
| TC-03 | Use a valid GitHub URL | URL should be encoded. |
| TC-04 | Use high error correction | QR code should use Level H. |
| TC-05 | Configure custom colors | Generated image should use the selected colors. |
| TC-06 | Save generated image | PNG file should be created. |
| TC-07 | Scan generated QR code | Encoded information should be readable. |

### Manual Validation

To verify the generated QR code:

1. Execute `advanced_qr.py`.
2. Open the generated PNG image.
3. Scan it using a smartphone camera or QR scanner.
4. Verify that it redirects to the intended GitHub profile.

---

# 🐛 16. Common Errors and Troubleshooting

| Error | Possible Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'qrcode'` | QR code library is missing. | Run `pip install qrcode[pil]`. |
| `ModuleNotFoundError: No module named 'PIL'` | Pillow is missing. | Run `pip install Pillow`. |
| Image not found | Incorrect file path or working directory. | Check the output location. |
| QR code not scanning | Poor image quality or insufficient contrast. | Use appropriate colors and a clear image. |
| Permission error | Insufficient file permissions. | Save the image in a writable directory. |

### Important Note

A QR code's visual customization should not compromise readability. Always maintain sufficient contrast between the foreground and background.

---

# 🧠 17. Core Concepts Learned

This project introduces several useful programming concepts.

| Concept | Application |
|---|---|
| Modules | Importing external Python libraries. |
| Objects | Creating a QRCode object. |
| Methods | Using `add_data()`, `make()`, and `make_image()`. |
| Arguments | Passing configuration parameters. |
| Constants | Selecting error correction levels. |
| Boolean Values | Using `fit=True`. |
| File Handling | Saving generated images. |
| Image Processing | Customizing image appearance. |

### Important Distinction: Function vs Method

A **function** is a reusable block of code that performs a particular task.

A **method** is a function associated with an object or class.

For example:

```python
qr.add_data("Hello")
```

Here, `add_data()` is a method associated with the `qr` object.

---

# 🎓 18. Interview Questions and Answers

### Q1. What is a QR code?

A QR code is a two-dimensional barcode that stores information in a machine-readable pattern. It can encode URLs, text, and other supported data.

### Q2. What does QR stand for?

QR stands for Quick Response.

### Q3. Which Python library is used in this project?

The `qrcode` library is used to generate QR codes.

### Q4. What is Pillow?

Pillow is a Python imaging library used for opening, manipulating, and saving image files.

### Q5. What is the purpose of `QRCode()`?

It creates a QR code object that allows us to configure QR properties and add data.

### Q6. What is the purpose of `add_data()`?

It adds the information that needs to be encoded into the QR code.

### Q7. What does `make(fit=True)` do?

It generates the QR code and automatically adjusts its version when necessary to accommodate the provided data.

### Q8. What is error correction in QR codes?

Error correction allows QR codes to recover encoded information even if portions of the code are damaged or obscured.

### Q9. What are the four QR error correction levels?

- L – Low
- M – Medium
- Q – Quartile
- H – High

### Q10. Why is Level H used in this project?

Level H provides approximately 30% error correction capacity, making the QR code more resilient to certain types of damage.

### Q11. What does `box_size=10` mean?

It means each QR code module is rendered using a 10 × 10 pixel block.

### Q12. What is the purpose of `border=4`?

It creates a quiet zone of four modules around the QR code, helping scanners distinguish the code from its surroundings.

### Q13. What is the difference between `fill_color` and `back_color`?

`fill_color` determines the color of QR modules, while `back_color` determines the background color.

### Q14. What does the `save()` method do?

It saves the generated image to a specified file path.

### Q15. Why use PNG format?

PNG is a lossless image format, making it suitable for preserving the sharp edges and module patterns of QR codes.

### Q16. Can a QR code store only URLs?

No. QR codes can store different types of information, including text and other supported data.

### Q17. What happens when the QR code version increases?

The number of modules increases, allowing the QR code to accommodate more information, subject to the encoding mode and error correction level.

### Q18. Why is contrast important in QR codes?

Scanners need to distinguish the QR modules from the background. Insufficient contrast can make scanning difficult or unsuccessful.

### Q19. What is the difference between a one-dimensional and two-dimensional barcode?

A one-dimensional barcode stores information using patterns along one dimension, while a two-dimensional barcode stores information in both horizontal and vertical directions.

### Q20. What improvements can be made to this project?

The project can be extended with user input, GUI support, custom colors, logo integration, batch generation, and downloadable QR code formats.

---

# ⚠️ 19. Limitations

- The advanced implementation currently uses a predefined GitHub profile URL.
- There is no graphical user interface.
- Users cannot currently select custom URLs through an interactive interface.
- The current implementation saves the output in a predefined PNG file.
- The project does not currently include QR code scanning functionality.

---

# 🚀 20. Future Enhancements

Possible improvements include:

- [ ] Add interactive URL and text input.
- [ ] Implement a menu to select simple or advanced generation.
- [ ] Add dynamic foreground and background color selection.
- [ ] Allow users to configure error correction levels.
- [ ] Support different QR code image formats.
- [ ] Add logo integration.
- [ ] Implement batch QR code generation.
- [ ] Develop a graphical user interface using Tkinter.
- [ ] Build a web-based QR code generator using Flask or FastAPI.
- [ ] Add QR code scanning and decoding functionality.

---

# 👩‍💻 21. Author

**Palak Sharma**

B.Tech Computer Science Engineering Student | Python Developer

- GitHub: [@palaksharma032](https://github.com/palaksharma032)

---

<p align="center">
  <b>Built with Python 💙</b>
  <br/>
  
⭐ If you find this project useful, consider giving it a star!
