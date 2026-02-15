from src.logic import startup
from src.buttonFunctions import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Initialize checks
startup()

# Create window with a theme
app = ttk.Window(themename="superhero")  # Modern dark theme
app.title("Password Manager")
app.state('zoomed')
app.iconphoto(False, ttk.PhotoImage(file=r'C:\Users\riley\Desktop\Python project\images\icon.png'))


frame = ttk.Frame(app, padding=30)
frame.pack(expand=True)


storeBtn = ttk.Button(frame, text="Store a New Password", bootstyle=SUCCESS, command=lambda:storeButton(app, frame))
allPassBtn = ttk.Button(frame, text="Display All Passwords", bootstyle=INFO, command=lambda:allPassButton(app))
genPassBtn = ttk.Button(frame, text="Generate New Password", bootstyle=WARNING, command=lambda:genPass(app))
deletePassBtn = ttk.Button(frame, text="Delete Saved Password", bootstyle=DANGER, command=lambda:deletePass(app))
exitBtn = ttk.Button(frame, text="Exit", bootstyle=SECONDARY, command=app.destroy)


for btn in [storeBtn, allPassBtn, genPassBtn, deletePassBtn, exitBtn]:
    btn.pack(fill='x', pady=10, ipady=10)

app.mainloop()
