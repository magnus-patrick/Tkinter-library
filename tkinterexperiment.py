import tkinter as tk

#Tkinter functions/widgets: Tk(), Label(), Text(), config(), pack(), title()
#bg changes background color, fg changes text color

window = tk.Tk()
window.geometry("700x400")
window.title("Tkinter Experiment")


widget = tk.Label(window, text = "Tkinter is awesome!", font = ("Courier", 20, "italic"))
widget.pack(padx = 20, pady = 50)

textbox = tk.Text(window, height = 2, font = ("Times New Roman", 16))
textbox.pack(padx = 10, pady = 10)

def click():
    widget.config(text = "You clicked the button!\n", bg = "black", fg = "white")
    window.config(bg = "black")


button = tk.Button(window, text = "Press/Click here!", command = click,
                   font = ("Times New Roman", 20, "bold"), bg = "red", fg = "white")
button.pack(padx = 10, pady = 10)


window.mainloop()