import tkinter as tk
from tkinter import scrolledtext

from beepThread import BeepThread

signs = {
    "A": (False, True),
    "B": (True, False, False, False),
    "C": (True, False, True, False),
    "D": (True, False, False),
    "E": (False,),
    "F": (False, False, True, False),
    "G": (True, True, False),
    "H": (False, False, False, False),
    "I": (False, False),
    "J": (False, True, True, True),
    "K": (True, False, True),
    "L": (False, True, False, False),
    "M": (True, True),
    "N": (True, False),
    "O": (True, True, True),
    "P": (False, True, True, False),
    "Q": (True, True, False, True),
    "R": (False, True, False),
    "S": (False, False, False),
    "T": (True,),
    "U": (False, False, True),
    "V": (False, False, False, True),
    "W": (False, True, True),
    "X": (True, False, True, False),
    "Y": (True, False, True, True),
    "Z": (True, True, False, False),
    "0": (True, True, True, True, True),
    "1": (False, True, True, True, True),
    "2": (False, False, True, True, True),
    "3": (False, False, False, True, True),
    "4": (False, False, False, False, True),
    "5": (False, False, False, False, False),
    "6": (True, False, False, False, False),
    "7": (True, True, False, False, False),
    "8": (True, True, True, False, False),
    "9": (True, True, True, True, False),
    ".": (False, True, False, True, False, True),
    ",": (True, True, False, False, True, True),
    "?": (False, False, True, True, False, False),
    "!": (True, False, True, False, True, True),
    "-": (True, False, False, False, False, True),
    "/": (True, False, False, True, False),
    ":": (True, True, True, False, False, False),
    "'": (False, True, True, True, True, False),
    ")": (True, False, True, True, False, True),
    ";": (True, False, True, False, True),
    "(": (True, False, True, True, False),
    "=": (True, False, False, False, True),
    "@": (False, True, True, False, True, False),
    "&": (False, True, False, False, False)
}


def setup_beep_thread(text_entry):
    message = text_entry.get()
    thread_beep = BeepThread(signs, message)
    thread_beep.start()


def output_to_label(text_entry):
    message = text_entry.get()
    output.configure(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.INSERT, create_morse_text(signs, message))
    output.configure(state="disabled")

def create_morse_text(morse_code, message):
    text = message.upper()
    string_output = ""
    letter_index = 0
    for letter in list(text):
        if letter == " ":
            string_output += "   "
        else:
            for beep in morse_code[letter]:
                if beep:
                    string_output += "-"
                else:
                    string_output += "."
            if letter_index < len(list(text)):
                string_output += " "
        letter_index += 1
    return string_output


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("660x440")
    root.resizable(False, False)
    root.configure(background='#E1C699')

    label = tk.Label(root, text="Input:")
    label.grid(row=0, column=0)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1)

    sound_button = tk.Button(root, text="Sound out morse", command=(lambda message=entry: setup_beep_thread(message)))
    sound_button.grid(row=1, column=0)

    text_button = tk.Button(root, text="Output as text", command=(lambda message=entry: output_to_label(message)))
    text_button.grid(row=1, column=1)

    output = scrolledtext.ScrolledText(root)
    output.grid(row=2, column=0, columnspan=2)
    output.configure(state="disabled")

    root.pack_slaves()
    root.mainloop()
