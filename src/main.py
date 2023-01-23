import tkinter as tk
from tkinter import ttk
import timeCalc

# Constants
MAX_ENTRY_LENGTH = 10


class TimeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.resizable(False, False)
        self.title("Time Calculator")

        # Bind keyboard shortcuts
        self.bind('<Key>', self.key_pressed)

        # Containers
        self.entry_frame = None
        self.buttons_frame = None

        # Entry fields
        self.sum_label = None

        self.hour_entry = None
        self.hour_text = None
        self.minute_entry = None
        self.minute_text = None
        self.second_entry = None
        self.second_text = None

        self.current_focus = None
        self.current_text = None

        # Numerical buttons
        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.button_4 = None
        self.button_5 = None
        self.button_6 = None
        self.button_7 = None
        self.button_8 = None
        self.button_9 = None
        self.button_0 = None

        # Operator buttons
        self.button_subtract = None
        self.button_add = None
        self.button_multiply = None
        self.button_divide = None
        self.button_equals = None

        # Other buttons
        self.button_colon = None
        self.button_clear = None
        self.button_delete = None

        # Store values
        self.values = []
        # Store last operator
        self.last_operator = ""

        self.create_gui()

    def create_gui(self) -> None:
        # Set style
        # style = tk.ttk.Style()
        # self.tk.call("lappend", "auto_path", "breeze-dark")
        # self.tk.call("package", "require", "ttk::theme::breeze-dark")
        # style.theme_use("breeze-dark")

        # Containers
        self.entry_frame = tk.Frame(self, padx=10, pady=10)
        self.buttons_frame = tk.Frame(self, padx=10, pady=10)

        # Entry fields
        self.sum_label = tk.Label(self.entry_frame, justify="right")

        self.hour_text = tk.StringVar(value="0")
        self.hour_entry = ttk.Entry(self.entry_frame, textvariable=self.hour_text, width=MAX_ENTRY_LENGTH,
                                    justify="right", validate="key")

        self.minute_text = tk.StringVar(value="0")
        self.minute_entry = ttk.Entry(self.entry_frame, textvariable=self.minute_text, width=MAX_ENTRY_LENGTH,
                                      justify="right", validate="key")

        self.second_text = tk.StringVar(value="0")
        self.second_entry = ttk.Entry(self.entry_frame, textvariable=self.second_text, width=MAX_ENTRY_LENGTH,
                                      justify="right", validate="key")

        # Numerical buttons
        self.button_1 = ttk.Button(self.buttons_frame, text="1", command=lambda: self.write_to_field(1), takefocus=0)
        self.button_2 = ttk.Button(self.buttons_frame, text="2", command=lambda: self.write_to_field(2), takefocus=0)
        self.button_3 = ttk.Button(self.buttons_frame, text="3", command=lambda: self.write_to_field(3), takefocus=0)
        self.button_4 = ttk.Button(self.buttons_frame, text="4", command=lambda: self.write_to_field(4), takefocus=0)
        self.button_5 = ttk.Button(self.buttons_frame, text="5", command=lambda: self.write_to_field(5), takefocus=0)
        self.button_6 = ttk.Button(self.buttons_frame, text="6", command=lambda: self.write_to_field(6), takefocus=0)
        self.button_7 = ttk.Button(self.buttons_frame, text="7", command=lambda: self.write_to_field(7), takefocus=0)
        self.button_8 = ttk.Button(self.buttons_frame, text="8", command=lambda: self.write_to_field(8), takefocus=0)
        self.button_9 = ttk.Button(self.buttons_frame, text="9", command=lambda: self.write_to_field(9), takefocus=0)
        self.button_0 = ttk.Button(self.buttons_frame, text="0", command=lambda: self.write_to_field(0), takefocus=0)

        # Operator buttons
        self.button_divide = ttk.Button(self.buttons_frame, text="÷", command=lambda: self.operator("÷"), takefocus=0)
        self.button_multiply = ttk.Button(self.buttons_frame, text="×", command=lambda: self.operator("×"), takefocus=0)
        self.button_subtract = ttk.Button(self.buttons_frame, text="-", command=lambda: self.operator("-"), takefocus=0)
        self.button_add = ttk.Button(self.buttons_frame, text="+", command=lambda: self.operator("+"), takefocus=0)
        self.button_equals = ttk.Button(self.buttons_frame, text="=", command=self.equate, takefocus=0)

        # Other buttons
        self.button_colon = ttk.Button(self.buttons_frame, text=":", command=self.shift_focus, takefocus=0)
        self.button_clear = ttk.Button(self.buttons_frame, text="C", command=lambda: self.clear(True), takefocus=0)
        self.button_delete = ttk.Button(self.buttons_frame, text="<", command=self.backspace, takefocus=0)

        # Pack entry frame
        self.entry_frame.grid(column=0, row=0)
        self.sum_label.grid(column=0, row=0, columnspan=5)
        self.hour_entry.grid(column=0, row=1)
        tk.Label(self.entry_frame, text="h :").grid(column=1, row=1)
        self.minute_entry.grid(column=2, row=1)
        tk.Label(self.entry_frame, text="m :").grid(column=3, row=1)
        self.second_entry.grid(column=4, row=1)
        tk.Label(self.entry_frame, text="s").grid(column=5, row=1)

        # Pack buttons frame
        self.buttons_frame.grid(column=0, row=1)

        self.button_clear.grid(column=0, row=0, columnspan=2)
        self.button_delete.grid(column=2, row=0, columnspan=2)

        self.button_7.grid(column=0, row=1)
        self.button_8.grid(column=1, row=1)
        self.button_9.grid(column=2, row=1)
        self.button_divide.grid(column=3, row=1)

        self.button_4.grid(column=0, row=2)
        self.button_5.grid(column=1, row=2)
        self.button_6.grid(column=2, row=2)
        self.button_multiply.grid(column=3, row=2)

        self.button_1.grid(column=0, row=3)
        self.button_2.grid(column=1, row=3)
        self.button_3.grid(column=2, row=3)
        self.button_subtract.grid(column=3, row=3)

        self.button_colon.grid(column=0, row=4)
        self.button_0.grid(column=1, row=4)
        self.button_equals.grid(column=2, row=4)
        self.button_add.grid(column=3, row=4)

        # Set focus on seconds entry field
        self.shift_focus(self.second_entry, self.second_text)

    def write_to_field(self, value: int) -> None:
        # Add value to the right of the current number
        current_value = int(self.current_text.get()) * 10 + value
        self.current_text.set(current_value)

        # Shift caret to end of entry
        self.current_focus.icursor(len(str(self.current_text.get())))

    def backspace(self) -> None:
        current_value = int(int(self.current_text.get()) / 10)
        self.current_text.set(current_value)

    def equate(self) -> None:
        # Store value
        self.values.append(
            timeCalc.get_time_in_seconds(int(self.hour_text.get()),
                                         int(self.minute_text.get()),
                                         int(self.second_text.get())))

        # Perform calculation
        if len(self.values) == 2 and 0 not in self.values:
            calculated_time = self.calculate_values()
        else:
            calculated_time = timeCalc.simplify_time(0, 0, self.values[0])

        # Clear fields
        self.clear(True)

        # Update fields
        self.hour_text.set(calculated_time[0])
        self.minute_text.set(calculated_time[1])
        self.second_text.set(calculated_time[2])

        # Shift caret to end of entry
        self.current_focus.icursor(len(self.current_text.get()))

    def shift_focus(self, field: ttk.Entry = None, string_var: tk.StringVar = None) -> None:
        if field is not None:
            # Focus on set field
            self.current_focus = field
            self.current_text = string_var
            self.current_focus.focus_set()
        else:
            # Shift values
            if self.hour_text.get() == "0":
                self.hour_text.set(self.minute_text.get())
                self.minute_text.set(self.second_text.get())
                self.second_text.set("0")

        # Shift caret to end of entry
        print(self.current_text.get())
        self.current_focus.icursor(len(self.current_text.get()))

    def operator(self, operator: str) -> None:
        # Set focus field (used when tab is pressed or mouse is clicked on different entry field)
        # self.shift_focus(self.focus_get(), self.focus_get().cget("textvariable"))

        # Get simplified time
        time = timeCalc.simplify_time(int(self.hour_text.get()),
                                      int(self.minute_text.get()),
                                      int(self.second_text.get()))

        # Store value
        self.values.append(timeCalc.get_time_in_seconds(time[0], time[1], time[2]))

        if self.values[-1] == 0:
            # Remove 0 value
            self.values.pop(-1)
        elif len(self.values) == 2:
            # Perform calculation of 2 values
            self.calculate_values()

        # Clear all fields
        self.hour_text.set("0")
        self.minute_text.set("0")
        self.second_text.set("0")

        # Write to label
        self.write_value(operator)

        # Focus on second entry
        self.shift_focus(self.second_entry, self.second_text)

        # Update last operator
        self.last_operator = operator

    def clear(self, event, clear_everything: bool = False) -> None:
        # Clear entry fields
        self.hour_text.set("0")
        self.minute_text.set("0")
        self.second_text.set("0")

        # Clear label
        self.sum_label.config(text="")

        # Clear values (optional)
        if clear_everything:
            self.values.clear()

        # Reset focus to second entry field
        self.shift_focus(self.second_entry, self.second_text)

    def clear_all(self, *args) -> None:
        # Clear entry fields
        self.hour_text.set("0")
        self.minute_text.set("0")
        self.second_text.set("0")

        # Clear label
        self.sum_label.config(text="")

        # Clear values (optional)
        self.values.clear()

        # Reset focus to second entry field
        self.shift_focus(self.second_entry, self.second_text)

    def calculate_values(self) -> list:
        # Perform calculation
        total_seconds = 0
        if self.last_operator == "+":
            total_seconds = timeCalc.add_time(self.values[0], "s", self.values[1], "s", "s")
        elif self.last_operator == "-":
            total_seconds = timeCalc.subtract_time(self.values[0], "s", self.values[1], "s", "s")
        elif self.last_operator == "×":
            total_seconds = timeCalc.multiply_time(self.values[0], "s", self.values[1], "s", "s")
        elif self.last_operator == "÷":
            total_seconds = timeCalc.divide_time(self.values[0], "s", self.values[1], "s", "s")

        # Store new value
        self.values.pop(1)
        self.values.pop(0)
        self.values.append(total_seconds)

        # Return formatted time
        return timeCalc.simplify_time(0, 0, total_seconds)

    def write_value(self, operator: str) -> None:
        time = timeCalc.simplify_time(0, 0, self.values[0])

        new_text = ""
        # Check for 0 values
        if time[0] != 0:
            new_text += f"{time[0]}h"
        if time[1] != 0:
            new_text += f"{time[1]}m"
        if time[2] != 0:
            new_text += f"{time[2]}s"

        # Add operator
        new_text += f" {operator} "

        # Write to label
        self.sum_label.config(text=new_text)

    def key_pressed(self, event) -> None:
        print(type(self))
        # Get key pressed
        char = event.char
        print(event)
        # Get text of current focused field
        text = self.current_text.get()

        # Check for digits
        if char.isdigit() and text.isdigit():
            # Remove 0 in front of number
            self.current_text.set(int(text))

        # Check for backspace
        elif char == "\x08":
            # Replace blank text with a 0
            if text == "":
                self.current_text.set("0")
                # Shift caret to end of entry
                self.current_focus.icursor(len(self.current_text.get()))

        # Check for shift shortcuts
        elif char == ":" or char == ".":
            # Remove characters from entry field
            text = text.replace(char, "")
            self.current_text.set(text)
            # Shift values
            self.shift_focus()

        # Check for equal shortcuts
        elif char == "\r":
            self.equate()

        # Check for operator shortcuts
        elif char == "+" or char == "-" or char == "*" or char == "/":
            # Remove characters from entry field
            text = text.replace(char, "")
            self.current_text.set(text)
            # Perform operator function
            self.operator(char)

        # Check for equate shortcuts
        elif char == "=":
            # Remove characters from entry field
            text = text.replace(char, "")
            self.current_text.set(text)
            # Perform equate function
            self.equate()

        # Check for shift focus
        elif char == "\t":
            # Focus on next widget
            if self.focus_get() == self.hour_entry:
                self.current_focus = self.minute_entry
                self.current_text = self.minute_text
            elif self.focus_get() == self.minute_entry:
                self.current_focus = self.second_entry
                self.current_text = self.second_text
            elif self.focus_get() == self.second_entry:
                self.current_focus = self.hour_entry
                self.current_text = self.hour_text
            # Shift caret to end of entry
            self.current_focus.selection_clear()
            self.current_focus.icursor(len(str(self.current_text.get())))

    def mouse_clicked(self, event) -> None:
        pass


if __name__ == '__main__':
    TimeCalculator().mainloop()
