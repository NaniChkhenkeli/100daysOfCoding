from tkinter import *

window = Tk()
window.title("gui program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="label", font=("Arial", 20, "bold"))
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="new text")

# button

def button_clicked():
    print("clicked")



button = Button(text="Click", command= button_clicked())
button.pack()



window.mainloop()