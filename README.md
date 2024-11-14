# AutoClicker v1.0

AutoClicker v1.0 is a simple and easy-to-use auto-clicking tool for both mouse and keyboard inputs. This application comes with a graphical user interface (GUI) to control the clicking frequency and toggle between mouse clicks and keyboard key presses.

## Features

- **Graphical User Interface (GUI)**: Intuitive GUI built using Tkinter.
- **Custom Click/Press Frequency**: Set your own frequency for mouse clicks or keyboard presses.
- **Mouse and Keyboard Support**: Toggle between mouse clicks and keyboard key presses.
- **Hotkey Support**: Toggle the auto-clicking/pressing using the `right shift` key.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/autoclicker.git
    ```
2. **Navigate to the Directory**:
    ```sh
    cd autoclicker
    ```
3. **Install the Required Dependencies**:
    ```sh
    pip install pyautogui keyboard tkinter
    ```

## Usage

To run the AutoClicker, simply execute the Python script:
```sh
python AutoClickerv1.0.py
```
FOR NO CONSOLE MODE 

```sh
python AutoClickerv1.0.pyw
```

### GUI Features

- **Version Label**: Display the current version of AutoClicker.
- **Click Frequency Input**: Set the frequency of mouse clicks or key presses. Insert `0` for default frequency.
- **Update Frequency Button**: Update the click frequency based on the input.
- **Toggle Button**: Start or stop the auto-clicking/pressing.
- **State Toggle Button**: Switch between mouse clicking and keyboard pressing. The default is mouse clicking.
- **Exit Button**: Exit the application.

### Hotkey

- **Right Shift**: Pressing the `right shift` key will toggle the auto-clicking/pressing on and off.

## Example

1. **Launch the Application**:
    ```sh
    python AutoClickerv1.0.py
    ```
2. **Set Click Frequency**:
    - Enter the desired frequency in the "Click Frequency" field.
    - Click "Update Frequency" to apply the changes.
3. **Toggle Pressing**:
    - Click the "Toggle" button or press the `right shift` key to start or stop the auto-clicking/pressing.
4. **Switch Between Mouse and Keyboard**:
    - Click the "Mouse" button to switch to keyboard pressing, or vice versa.

## Dependencies

- `pyautogui`: For performing mouse clicks.
- `keyboard`: For detecting and simulating keyboard key presses.
- `tkinter`: For creating the graphical user interface.

## Notes

- Default key for keyboard pressing is `e`.
- Default state is mouse clicking.
- Very high click frequencies may affect the performance of your system.


---

Thank you for using AutoClicker! We hope you find it useful.