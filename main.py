from tkinter import *


def converter():
    gram_results = float(two_label.get()) * 1000
    pound_results = float(two_label.get()) * 2.20462
    ounce_results = float(two_label.get()) * 35.247

    gram_text.delete("1.0", END)
    gram_text.insert(END, gram_results)

    pound_text.delete("1.0", END)
    pound_text.insert(END, pound_results)

    ounce_text.delete("1.0", END)
    ounce_text.insert(END, ounce_results)


window = Tk()
window.title("Weight Converter")
window.iconbitmap("icon.ico")
window.geometry("770x300")
window.config(padx=20, pady=20)

kg_label = Label(text="Input The Weight in KG", font=("Helvetica", 13, "bold"), fg="green")
kg_label.grid(row=0, column=0)

convert_button = Button(text=" Convert ", font=("Helvetica", "15"), fg="DarkBlue", command=converter)
convert_button.grid(row=0, column=2)

two_label = StringVar()

kg_entry = Entry(window, textvariable=two_label)
kg_entry.grid(row=0, column=1)

gram_label = Label(text="Gram", font=("Helvetica", "12"))
gram_label.grid(row=1, column=0)

pound_label = Label(text="Pound", font=("Helvetica", "12"))
pound_label.grid(row=1, column=1)

ounce_label = Label(text="Ounce", font=("Helvetica", "12"))
ounce_label.grid(row=1, column=2)

gram_text = Text(height=5, width=30)
gram_text.grid(row=2, column=0)

pound_text = Text(height=5, width=30)
pound_text.grid(row=2, column=1)

ounce_text = Text(height=5, width=30)
ounce_text.grid(row=2, column=2)

window.mainloop()