from tkinter import *

window = Tk()
window.geometry("700x400+30+40")
window.title("How to play SMILEY")

btn = Button(window, text="play", bg='blue')
btn.place(x=350, y=120)

lbl = Label(window, text="Click play, if you want to start me", fg="black", font="Times, 10")
lbl.place(x=270, y=90)

txtfld = Entry(window, bd=5)
txtfld.place(x=300, y=60)

window.mainloop()
