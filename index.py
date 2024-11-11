import tkinter as tk

def animate():
    global step
    if step < 200:
        canvas.move(square1, -1, -1)
        canvas.move(square2, 1, -1)
        canvas.move(square3, -1, 1)
        canvas.move(square4, 1, 1)
        step += 1
        root.after(10, animate)
    else:
        reset_animation()

def reset_animation():
    global step
    step = 0
    canvas.coords(square1, 190, 190, 210, 210)
    canvas.coords(square2, 210, 190, 230, 210)
    canvas.coords(square3, 190, 210, 210, 230)
    canvas.coords(square4, 210, 210, 230, 230)
    animate()

step = 0

root = tk.Tk()
root.title("Beskonačna animacija kvadrata")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Kreiranje kvadrata
square1 = canvas.create_rectangle(190, 190, 210, 210, fill="red")
square2 = canvas.create_rectangle(210, 190, 230, 210, fill="green")
square3 = canvas.create_rectangle(190, 210, 210, 230, fill="blue")
square4 = canvas.create_rectangle(210, 210, 230, 230, fill="orange")

# Pokretanje animacije
animate()

root.mainloop()
