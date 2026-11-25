# Restaurant Order Management System

A Python 3 console application for managing restaurant orders by table.
A waiter can select a table, add one or more menu items, view the
running order, and generate a final bill with service charge and GST.

## Project Details

-   **Project Serial Number:** 36
-   **Project Title:** Restaurant Order Management System
-   **Language:** Python 3
-   **Concepts:** Lists, Dictionaries, Loops, and Billing

## Problem Statement

Create a console application where a waiter selects a table, takes
orders from the menu, views the running order, and generates the final
bill with service charge and GST.

## Menu and Pricing

  Menu Item     Price
  ----------- -------
  Burger         ₹100
  Pizza          ₹200
  Coffee          ₹50

-   **Tables:** Numbered from 1 to 20
-   **Service charge:** 10%
-   **GST:** 5%

## Required Features

1.  Store menu items and their prices in a dictionary.
2.  Keep the ordered items for each table in a list.
3.  Allow multiple items to be added to one table's order.
4.  Display the running order.
5.  Calculate the subtotal, service charge, GST, and final total.
6.  Validate the table number, menu item, and quantity before adding an
    order.
7.  Generate and display the final bill.

## Billing Formula

The examples in the project brief calculate both charges on the
subtotal:

``` text
Subtotal       = Sum of item prices × quantities
Service charge = Subtotal × 10 / 100
GST            = Subtotal × 5 / 100
Final total    = Subtotal + Service charge + GST
```

## Sample Test Cases

### Test Case 1: Normal Input

**Input** - Table: 5 - Order item: Burger - Quantity: 2

**Expected output**

``` text
Burger x2 added to Table 5
Amount: ₹200
```

### Test Case 2: Boundary / Minimum Input

**Input** - Table: 1 - Order item: Coffee - Quantity: 1 - Generate bill

**Expected bill**

``` text
Subtotal: ₹50
Service charge (10%): ₹5.00
GST (5%): ₹2.50
Total: ₹57.50
```

### Test Case 3: Invalid Input

The application should handle these cases:

  -----------------------------------------------------------------------
  Input                               Expected message
  ----------------------------------- -----------------------------------
  Order item: Pasta                   Item not on the menu. Available:
                                      Burger, Pizza, Coffee

  Quantity: `abc`                     Invalid quantity. Enter a whole
                                      number.

  Table: 0                            Invalid table number. Enter a
                                      number between 1 and 20.
  -----------------------------------------------------------------------

### Test Case 4: Different Valid Scenario

**Input** - Table: 3 - Burger × 2 - Pizza × 1 - Coffee × 4 - Generate
bill

**Expected bill**

``` text
Burger x2 = ₹200
Pizza x1  = ₹200
Coffee x4 = ₹200
Subtotal: ₹600
Service charge (10%): ₹60.00
GST (5%): ₹30.00
Total: ₹690.00
```

## Requirements

-   Python 3 installed on your computer.
-   A code editor or terminal to run the Python file.

## How to Run

1.  Save the program in a file named `restaurant_order.py`.
2.  Open a terminal in the folder containing the file.
3.  Run:

``` bash
python restaurant_order.py
```

On some systems, use:

``` bash
python3 restaurant_order.py
```

## Suggested Project Structure

``` text
Restaurant-Order-Management-System/
│
├── restaurant_order.py
└── README.md
```

## Validation Rules

-   Accept only table numbers from **1 to 20**.
-   Accept only menu items listed in the menu.
-   Accept a positive whole-number quantity.
-   Do not add an order when its input is invalid.

## Project Learning Outcomes

By completing this project, students can practise:

-   Python dictionaries for menu and price storage.
-   Python lists for maintaining orders.
-   Loops for accepting multiple order items.
-   Conditional statements for input validation.
-   Arithmetic operations for bill calculation.
-   Functions and clear console output.

------------------------------------------------------------------------

**Note:** This README is based on the project brief and its sample test
cases. The actual Python implementation should be added in
`restaurant_order.py`.
