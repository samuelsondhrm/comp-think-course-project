# Vending Machine Simulation $-$ WI1102 Computational Thinking Project

This repository contains an implementation for **Project I of WI1102 $-$
Computational Thinking** (Semester 1, 2024/2025).\
The project focuses on analyzing how a real-world system functions and
building a **functional simulation** based on computational thinking
principles and foundational Python programming concepts.

The selected system for the simulation is a **Vending Machine**,
emphasizing user interaction flow, product management, and transaction
processing.

## 📌 Project Description

The assignment requires examining a real-world system using the core
pillars of computational thinking:

-   **Decomposition** $-$ breaking the system into functional components
-   **Abstraction** $-$ identifying essential elements necessary for simulation
-   **Pattern Recognition** $-$ detecting recurring logic within system behavior
-   **Algorithm Design** $-$ constructing sequential, conditional, and iterative processes

The resulting design is implemented in Python to reflect the behavior of
the chosen system.

The vending machine simulation includes:

-   Product management
-   Admin authentication using QR codes
-   Customer transaction flow
-   Stock updates
-   QR code generation for payment

## 🚀 Features

### **Admin Mode**

-   Authentication via **QR Code + password**
-   Validation of registered admin QR codes
-   Ability to add products with:
    -   Name
    -   Price
    -   Stock quantity
-   Auto-saving to `produk.json`

### **Customer Mode**
-   Display of available items
-   Product selection
-   Generation of **terminal-rendered QR Code** for payment
-   Automatic stock reduction after each transaction

### **Technical Highlights**

-   QR scanning with **OpenCV**
-   QR creation using the `qrcode` library
-   Data persistence with JSON
-   Use of foundational programming structures:
    -   Conditional statements
    -   Loops
    -   Arrays/dictionaries
    -   Modular functions

## 📂 Repository Structure
```
    .
    ├── Vending Machine I Think.py     # Main program
    ├── produk.json                    # Auto-generated product storage
    └── README.md                      # Project documentation
```

## 🧩 System Workflow

### **1. Admin Authentication**

Admins authenticate through: 
1. QR code scanning (camera required)
2. Password verification corresponding to the scanned QR code

Admin QR codes are predefined within the program.

### **2. Product Management**

Admins may input: - Product name
- Price
- Stock amount

Each product receives an auto-incremented identifier.

### **3. Customer Purchase Flow**

1.  User selects a role

2.  Product list is shown

3.  A product is chosen

4.  A **QR Code** containing:

        Produk: <name>
        Harga: Rp<price>

    is generated for payment

5.  Stock decreases automatically after QR display

## 🛠 Requirements

Install the required dependencies:

``` bash
pip install opencv-python
pip install qrcode
```

Recommended Python version: **3.10+**

A functional camera is needed for the QR scanning feature.

## ▶️ Running the Program

Execute the script with:

``` bash
python "Vending Machine I Think.py"
```

Available roles:
- `"admin"` for managing products
- `"pembeli"` for simulating a purchase
- `"exit"` to close the program

## 📹 Deliverables (Based on Course Guidelines)

-   Final written report
-   Progress presentation
-   Source code
-   Final presentation video (external link included in course submission)

## 📝 Notes

The project demonstrates introductory computational thinking concepts
and basic Python programming.
The system is designed to highlight core principles rather than provide
full production-level reliability.

## 📜 License

This project is intended for academic and educational reference.
