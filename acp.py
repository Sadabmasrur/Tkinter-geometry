from tkinter import *

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x200")
root.configure(bg="#f0f4f7")

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(
            text=f"{inches} inches = {cm:.2f} cm",
            fg="#2e7d32"
        )
    except ValueError:
        result_label.config(
            text="Please enter a valid number.",
            fg="#c62828"
        )

instruction_label = Label(
    root, text="Enter length in inches:", font=("Arial", 12),
    bg="#f0f4f7", fg="#333333"
)
instruction_label.pack(pady=10)

entry = Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

convert_button = Button(
    root, text="Convert", command=convert_to_cm,
    bg="#4CAF50", fg="white", activebackground="#45a049",
    font=("Arial", 12), relief=FLAT, padx=10, pady=5
)
convert_button.pack(pady=10)

result_label = Label(
    root, text="", font=("Arial", 14),
    bg="#f0f4f7", fg="#333333"
)
result_label.pack(pady=10)

root.mainloop()
