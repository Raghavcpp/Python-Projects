from unicodedata import name
import pyautogui 
import time
import tkinter as tk

def screenshot():
    root.withdraw()
    time.sleep(0.5)
    img = pyautogui.screenshot()
    img.save("screenshots/SS"+str(time.time())+".png")
    img.show()
    root.deiconify()

# screenshot()

#---------------GUI-----------------#
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Close", command=quit)
close.pack(side=tk.LEFT)

root.mainloop()