from tkinter import *
from playsound import *
root = Tk()

def getvals():
    print("Logging In...")

    print(f"{'Welcome' ,namevalue.get()} ")
    


    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")
    # Destroy window after taking input
    root.destroy()
    #exec(open("main.py").read())
root.title("HealthPLUS Sign In")
photo = PhotoImage(file = "images\sign.png")




#root.geometry("644x344")



#Heading
Label(root, text="Join HealthPLUS Today!",justify="center", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone Number/ Email")
gender = Label(root, text="Password")


#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)


# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)


# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)


#Checkbox & Packing it
foodservice = Checkbutton(text="Receive Latest Health Updates?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Register/Sign In", command=getvals).grid(row=7, column=3)

root.mainloop()
