import tkinter as tk 


def fun():
	print("oops you clicked me !")

root = tk.Tk()

root.geometry("400x400")

label = tk.Label(root, text="this is some text")
label.grid(row=0)

button = tk.Button(root, text="button 1", command=fun)
button.grid(row=1)


root.mainloop()






