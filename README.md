# Function-Plotter
Function Plotter

Overview
The Function Plotter is a simple Python application that allows you to plot the graph of a mathematical function of a single variable, represented by "x." It uses the Matplotlib library for plotting and PySide2 for creating the graphical user interface (GUI).
Requirements
To run the Function Plotter, you need the following:
* Python 3.x installed on your system.
* The following Python libraries: matplotlib, numpy, sympy, PySide2.
How to Use
1. Make sure you have all the required libraries installed.
2. Run the Python file using the command: python function_plotter.py or execute it in your preferred Python IDE.
Application Interface
The Function Plotter GUI consists of the following elements:
1. Enter the function of x: A text input field where you can enter your mathematical function of "x." For example, you can enter expressions like x*2, x^3, etc.
2. Enter the minimum value of x: A text input field where you should provide the minimum value of the x-axis range.
3. Enter the maximum value of x: A text input field where you should provide the maximum value of the x-axis range.
4. Plot Button: After entering the function and the range of x-values, click this button to plot the function.
5. Graph Area: The area where the graph of the function will be displayed using Matplotlib.
How to Plot a Function
1. Enter the mathematical function in the "Enter the function of x" field. Please ensure that you only use valid mathematical characters and supported functions (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, x, e, E, +, -, *, /, ^, (), ). 
2. Provide the minimum and maximum values for the x-axis in the "Enter the minimum value of x" and "Enter the maximum value of x" fields, respectively.
3. Click the "Plot" button. If the function is valid, the plot will be displayed in the graph area.
4. If there are any errors in the input, such as invalid characters in the function or incorrect minimum/maximum values, an error message will be shown.
Input Validation
The Function Plotter includes basic input validation to ensure that the user provides valid inputs for the function and the range of x-values. If any errors are encountered, the application will display a relevant error message.

Automated Testing
The Function Plotter comes with automated tests using pytest to ensure that the application functions correctly. The tests check the following aspects:
1. Function Plotting: The application plots the function correctly and displays the graph.
2. Valid Function Input: The application correctly validates a valid function input and does not raise any errors.
3. Invalid Function Input: The application raises a ValueError when an invalid function is entered.
4. Invalid Value of x: The application validates that the minimum value of x is not greater than the maximum value.
5. Invalid Character in Function: The application validates that only valid characters are used in the function input and displays an error message if invalid characters are detected.
To run the tests, save the provided test code in a Python file (e.g., test_function_plotter.py). Ensure that the Function Plotter application (function_plotter.py) and the required libraries are available in the Python environment.
To execute the tests, use the command: pytest test_function_plotter.py.

Troubleshooting
If you encounter any issues or errors while using the Function Plotter, check the following:
* Ensure you have installed all the required Python libraries: matplotlib, numpy, sympy, PySide2.
* Check the function you entered for any syntax errors or unsupported characters.
Acknowledgments
The Function Plotter was developed using Python and popular open-source libraries, including Matplotlib and PySide2. It demonstrates how to create a simple GUI application for plotting mathematical functions.

