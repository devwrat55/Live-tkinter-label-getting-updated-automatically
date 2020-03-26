import tkinter as tk

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
root = tk.Tk()
root.title("Increasing count after 1000 milliseconds")
root.state('zoomed')
root.configure(background='white')

mycolorbg = '#%02x%02x%02x' % (0, 248, 0)
mycolorfg = '#%02x%02x%02x' % (0, 0, 0)
label = tk.Label(root, font = ('Consolas', 350, 'bold'), 
			background = mycolorbg, 
			foreground = mycolorfg) 
label.pack()

counter_label(label)

mycolorbg = '#%02x%02x%02x' % (255, 100, 0)
mycolor_buttonclick = '#%02x%02x%02x' % (160, 160, 160)
next1 = tk.Button(root,
                   text="STOP", bg = mycolorbg,activebackground = mycolor_buttonclick, bd = 1,
                   font = ("Consolas", 20, 'bold'), height = 1, width = 40, command=root.destroy)
next1.pack()

root.mainloop()