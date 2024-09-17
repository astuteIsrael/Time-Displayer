# Simple Python Time Displayer

## Overview
The **Simple Python Time Displayer** is a Python project that shows the current time in a graphical window. It updates the time every second, using the `tkinter` library for the interface. The time is displayed in **Hour:Minute:Second** format along with an **AM/PM** indicator.

## Features
- Continuously updates and displays the current time.
- Displays time in **HH:MM:SS AM/PM** format.
- Customizable font and background color.
- Simple and easy-to-use interface.

## Requirements
- Python 3.x
- Tkinter (Comes pre-installed with Python)

## How to Run
1. Ensure that Python 3.x is installed on your machine.
2. Clone or download this repository.
3. Open a terminal (or command prompt) and navigate to the project folder.
4. Run the script by typing the following command:

    ```bash
    python time_displayer.py
    ```

5. A window will pop up displaying the current time, updating every second.

## Customization
You can customize the following in the `time_displayer.py` file:
- **Font**: Modify the font style and size in the `label` widget.
- **Background color**: Change the background color using the `background` argument in the `label` widget.
- **Text color**: Customize the text color using the `foreground` argument in the `label` widget.

For example:
```python
label = tk.Label(root, font=('Arial', 50, 'italic'), background='blue', foreground='yellow')

```python
label = tk.Label(root, font=('Arial', 50, 'italic'), background='blue', foreground='yellow')
