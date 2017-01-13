
import pyrebase
from firebase import firebase
import os

try:
    # for Python2
    from Tkinter import *
    from tkinter import filedialog
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import filedialog

categories = ["fun","academic","greek","networking","football","cultural"]

config = {
  "apiKey": " AIzaSyCkLEL05gnfbuGaWYVlOmXbkZWb_95CYBE",
  "authDomain": "school-events-3b62e.firebaseapp.com",
  "databaseURL": "https://school-events-3b62e.firebaseio.com/",
  "storageBucket": "school-events-3b62e.appspot.com",

}
firebasepyre = pyrebase.initialize_app(config)
database = firebasepyre.database()
storage = firebasepyre.storage()
Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/Organizations")

class eventEntry:
    def __init__(self,master):
        master.title("KSU Event System (Admin ver.)")
        master.minsize(width=300, height=300)

        self.name = StringVar()
        self.category = StringVar()
        self.category.set("networking")
        self.date = StringVar()
        self.dateNum = IntVar()
        self.time = StringVar()
        self.description = StringVar()
        self.shareMessage = StringVar()
        self.address = StringVar()
        self.food = StringVar()
        self.food.set("No")
        self.alcohol = StringVar()
        self.alcohol.set("No")
        self.merchandise = StringVar()
        self.merchandise.set("No")
        self.lat = StringVar()
        self.longitude = StringVar()
        self.category = StringVar()
        self.picture = StringVar()
        self.colorPicture = StringVar()
        self.pictureName = StringVar()
        self.colorPictureName = StringVar()

        self.nameLabel = Label(master, text="name of Event",underline=0)
        self.nameLabel.grid(column=1)
        self.nameEntry = Entry(master,textvariable=self.name,bd=3)
        self.nameEntry.grid(column=1)
        self.categoryLabel = Label(master, text="Enter Category",underline=0)
        self.categoryLabel.grid(column=1)
        self.categoryOptions = OptionMenu(master,self.category,*categories)
        self.categoryOptions.grid(column=1)
        self.dateLabel = Label(master,text="Enter Date",underline=0)
        self.dateLabel.grid(column=1)
        self.dateEntry = Entry(master,textvariable=self.date,bd=3)
        self.dateEntry.grid(column=1)
        self.dateNumLabel = Label(master, text="Enter DateNum",underline=0)
        self.dateNumLabel.grid(column=1)
        self.dateNumEntry = Entry(master,textvariable=self.dateNum, bd=3)
        self.dateNumEntry.grid(column=1)
        self.descriptionLabel = Label(master,text="Enter Description", underline=0)
        self.descriptionLabel.grid(column=1)
        self.descriptionEntry = Entry(master, textvariable=self.description, bd=3)
        self.descriptionEntry.grid(column=1 , rowspan=2)
        self.shareMessageLabel = Label(master, textvariable=self.shareMessage, underline=0)
        self.shareMessageLabel.grid(column=1)
        self.shareMessageEntry = Entry(master, textvariable=self.shareMessage, bd=3)
        self.shareMessageEntry.grid(column=1)

        self.latLabel = Label(master, text="Enter Latitude", underline=0)
        self.latLabel.grid(column=1)
        self.latEntry = Entry(master, textvariable=self.lat, bd=3)
        self.latEntry.grid(column=1)
        self.longitudeLabel = Label(master, text="Enter Longitude", underline=0)
        self.longitudeLabel.grid(column=1)
        self.longitudeEntry = Entry(master, textvariable=self.longitude, bd=3)
        self.longitudeEntry.grid(column=1)

        self.addressLabel = Label(master,text="Enter Address", underline=0)
        self.addressLabel.grid(column=1)
        self.addressEntry = Entry(master, textvariable=self.address, bd=3)
        self.addressEntry.grid(column=1)

        self.pictureLabel = Label(master,text="Attach picture")
        self.pictureLabel.grid(column=1)

        self.pictureEntry = Entry(master,textvariable=self.picture,bd=3)
        self.pictureEntry.grid(column=1)
        self.colorPictureLabel = Label(master,text="Attach colored picture.")
        self.colorPictureLabel.grid(column=1)
        self.colorPictureEntry = Entry(master, textvariable=self.colorPicture, bd=3)
        self.colorPictureEntry.grid(column=1)
        self.attachButton = Button(master, text="search", command=self.attachPicture)
        self.attachButton.grid(column=1)
        self.colorAttach = Button(master, text="Attach color picture", command=self.attachColorPicture)
        self.colorAttach.grid(column=1)
        self.submitButton = Button(master, text="Submit", command=self.post)
        self.submitButton.grid(column=1)

        self.foodChoiceLabel = Label(master, text="Is food available?",underline=0)
        self.foodChoiceLabel.grid(column=2,row=1)
        self.foodChoiceYes = Radiobutton(master, text="Yes", variable=self.food, value="Yes")
        self.foodChoiceYes.grid(column=2,row=2)
        self.foodChoiceNo = Radiobutton(master,text="No",variable=self.food,value="No")
        self.foodChoiceNo.grid(column=2,row=3)

        self.alcoholChoiceLabel = Label(master,text= "Will there be alcohol?")
        self.alcoholChoiceLabel.grid(column=3,row=1)
        self.alcoholChoiceYes = Radiobutton(master,text="Yes",variable=self.alcohol,value="Yes")
        self.alcoholChoiceYes.grid(column=3,row=2)
        self.alcoholChoiceNo = Radiobutton(master,text="No",variable=self.alcohol,value="No")
        self.alcoholChoiceNo.grid(column=3,row=3)

        self.merchandiseChoiceLabel = Label(master,text= "Will there be merchandise?")
        self.merchandiseChoiceLabel.grid(column=4,row=1)
        self.merchandiseChoiceYes = Radiobutton(master,text="Yes",variable=self.merchandise,value="Yes")
        self.merchandiseChoiceYes.grid(column=4,row=2)
        self.merchandiseChoiceNo = Radiobutton(master,text="No",variable=self.merchandise,value="No")
        self.merchandiseChoiceNo.grid(column=4,row=3)

        self.timeLabel = Label(master,text= "Enter time-range")
        self.timeLabel.grid(column=2,row=4)
        self.timeEntry = Entry(master,textvariable=self.time, bd=3)
        self.timeEntry.grid(column=2,row=5)
        #





    def post(self):
        name = self.name.get()
        category = self.category.get()
        date = self.date.get()
        dateNum = self.dateNum.get()
        description = self.description.get()
        shareMessage = self.shareMessage.get()
        address = self.address.get()
        food = self.food.get()
        alcohol = self.alcohol.get()
        merchandise = self.merchandise.get()
        lat = self.lat.get()
        longitude = self.longitude.get()
        picture = self.picture.get()

        Firebase.patch(name,{"name":name})
        Firebase.patch(name,{"category":category})
        Firebase.patch(name,{"date": date})
        Firebase.patch(name,{"dateNum": dateNum})
        Firebase.patch(name,{"description": description})
        Firebase.patch(name,{"shareMessage": shareMessage})
        Firebase.patch(name,{"address":address})
        Firebase.patch(name,{"food": food})
        Firebase.patch(name,{"alcohol": alcohol})
        Firebase.patch(name,{"merchandise": merchandise})
        Firebase.patch(name,{"lat": lat})
        Firebase.patch(name,{"longitude": longitude})
        Firebase.patch(name,{"picture": picture})
        Firebase.patch(name,{"votes":0})
        Firebase.patch(name+"/"+"voters",{"placeholder":"voted"})
        storage.child(category+ "/"+"color"+ self.pictureName.get()).put(picture)
        self.pictureEntry.insert(0,root.filename)
        self.nameEntry.delete(0, END)
        self.dateEntry.delete(0, END)
        self.descriptionEntry.delete(0, END)
        self.shareMessageEntry.delete(0,END)
        self.addressEntry.delete(0, END)
        self.latEntry.delete(0, END)
        self.longitudeEntry.delete(0, END)
        self.pictureEntry.delete(0, END)
    def attachPicture(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.picture.set(os.path.basename(root.filename))
        print(self.picture.get())
    def attachColorPicture(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.colorPicture.set(os.path.basename(root.filename))
        print(self.picture.get())



if __name__ == "__main__":
    root = Tk()
    GUI = eventEntry(root)
    root.mainloop()

