import tkinter as tk

# Function to draw the letter "C" with 20% of the circle removed from both ends
def draw_C(canvas):
    # Draw the upper curve (red)
    canvas.create_line(90, 110, 220, 60, fill="blue", width=5)
    canvas.create_arc(50, 50, 150, 150, start=216, extent=160, outline="blue", width=5, style="arc")
    canvas.create_arc(50, 50, 150, 150, start=160, extent=120, outline="green", width=5, style="arc")
    canvas.create_arc(50, 50, 150, 150, start=90, extent=120, outline="yellow", width=5, style="arc")
    
    # Draw the bottom curve (blue)
    canvas.create_arc(50, 50, 150, 150, start=36, extent=108, outline="red", width=5, style="arc")
    
    

# Create a tkinter window
root = tk.Tk()
root.title("Letter C")

# Create a canvas
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Draw the letter "C"
draw_C(canvas)

# Start the tkinter event loop
root.mainloop()
