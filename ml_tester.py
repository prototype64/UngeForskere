import tkinter as tk


lastx, lasty = 0, 0

#Takes the coordinates of the mouse when you click the mouse
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
 
# this makes the new starting point of the drawing
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y
 
root = tk.Tk()
root.geometry("1200x1000")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
 
canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
 
root.mainloop()


#class network: