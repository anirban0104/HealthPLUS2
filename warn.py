from tkinter import *       # do pip install 
from tkinter import messagebox

root=Tk()
def popup():
    response =messagebox.askyesno("YOU HAVE BEEN WARNED", "This App is intended for common issues only, please refer to a physical doctor for severe issues. Press YES to proceed or NO to exit.")
    Label(root, text=response).pack()
    if response==1:
        exec(open("main.py").read())
    if response==0:
        #destroyAllWindows()
        Button(root, text="QUIT", command=root.destroy).pack()



Button(root, text="OK", command=popup).pack()
mainloop()