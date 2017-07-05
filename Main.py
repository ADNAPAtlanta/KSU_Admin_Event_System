
import pyrebase
from firebase import firebase
import os
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3

try:
    # for Python2
    from Tkinter import *
    from tkinter import filedialog
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import filedialog

categories = ["fun","academic","greek","networking","ncaa","cultural","athletics","service"]

config = {
  "apiKey": " AIzaSyCkLEL05gnfbuGaWYVlOmXbkZWb_95CYBE",
  "authDomain": "school-events-3b62e.firebaseapp.com",
  "databaseURL": "https://school-events-3b62e.firebaseio.com",
  "storageBucket": "school-events-3b62e.appspot.com",

}
firebasepyre = pyrebase.initialize_app(config)
database = firebasepyre.database()
storage = firebasepyre.storage()
Firebase = firebase.FirebaseApplication("https://school-events-3b62e.firebaseio.com/", None)

pmAMList = ["PM","AM"]


class eventEntry:
    def __init__(self,master):
        master.title("KSU Event System (Admin ver.)")
        master.minsize(width=300, height=300)

        self.name = StringVar()
        self.organization = StringVar()
        self.category = StringVar()
        self.category.set("networking")
        self.date = StringVar()
        self.dateNum = IntVar()
        self.time = StringVar()
        self.startTime = StringVar()
        self.endTime = StringVar()
        self.pmAM = StringVar()
        self.pmAMEnding = StringVar()
        self.pmAMEnding.set("PM")
        self.pmAM.set("AM")
        self.description = StringVar()
        self.shareMessage = StringVar()
        self.address = StringVar()
        self.food = StringVar()
        self.food.set("No")
        self.music = StringVar()
        self.music.set("No")
        self.merchandise = StringVar()
        self.merchandise.set("No")
        self.lat = StringVar()
        self.longitude = StringVar()
        self.locationName = StringVar()
        self.category = StringVar()
        self.picture = StringVar()
        self.colorPicture = StringVar()
        self.pictureName = StringVar()
   

        self.nameLabel = Label(master, text="name of Event",underline=0)
        self.nameLabel.grid(column=1)
        self.nameEntry = Entry(master,textvariable=self.name,bd=3)
        self.nameEntry.grid(column=1)
        self.organizationLabel = Label(master, text="Name of organization", underline=0)
        self.organizationLabel.grid(column=1)
        self.organizationEntry = Entry(master, textvariable=self.organization, bd=3)
        self.organizationEntry.grid(column=1)
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
        self.shareMessageLabel = Label(master, text="Enter share message", underline=0)
        self.shareMessageLabel.grid(column=1)
        self.shareMessageEntry = Entry(master, textvariable=self.shareMessage, bd=3)
        self.shareMessageEntry.grid(column=1)

        self.locationNameLabel = Label(master, text="Enter location name.", underline=0)
        self.locationNameLabel.grid(column=2, row=6)
        self.locationNameEntry = Entry(master, textvariable=self.locationName, bd=3)
        self.locationNameEntry.grid(column=2, row=7)
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
        self.attachButton = Button(master, text="search", command=self.attachPicture)
        self.attachButton.grid(column=1)
        self.submitButton = Button(master, text="Submit", command=self.post)
        self.submitButton.grid(column=1)

        self.foodChoiceLabel = Label(master, text="Is food available?",underline=0)
        self.foodChoiceLabel.grid(column=2, row=1)
        self.foodChoiceYes = Radiobutton(master, text="Yes", variable=self.food, value="Yes")
        self.foodChoiceYes.grid(column=2,row=2)
        self.foodChoiceNo = Radiobutton(master,text="No",variable=self.food,value="No")

        self.foodChoiceNo.grid(column=2, row=3)

        self.musicChoiceLabel = Label(master,text= "Will there be music?")
        self.musicChoiceLabel.grid(column=3, row=1)
        self.musicChoiceYes = Radiobutton(master,text="Yes",variable=self.music,value="Yes")
        self.musicChoiceYes.grid(column=3, row=2)
        self.musicChoiceNo = Radiobutton(master,text="No",variable=self.music,value="No")
        self.musicChoiceNo.grid(column=3, row=3)

        self.merchandiseChoiceLabel = Label(master,text= "Will there be merchandise?")
        self.merchandiseChoiceLabel.grid(column=4, row=1)
        self.merchandiseChoiceYes = Radiobutton(master,text="Yes",variable=self.merchandise,value="Yes")
        self.merchandiseChoiceYes.grid(column=4, row=2)
        self.merchandiseChoiceNo = Radiobutton(master,text="No",variable=self.merchandise,value="No")
        self.merchandiseChoiceNo.grid(column=4, row=3)

        self.foodChoiceNo.grid(column=2,row=3)

        self.alcoholChoiceLabel = Label(master,text= "Will there be music?")
        self.alcoholChoiceLabel.grid(column=3,row=1)
        self.alcoholChoiceYes = Radiobutton(master,text="Yes",variable=self.music,value="Yes")
        self.alcoholChoiceYes.grid(column=3,row=2)
        self.alcoholChoiceNo = Radiobutton(master,text="No",variable=self.music,value="No")
        self.alcoholChoiceNo.grid(column=3,row=3)

        self.merchandiseChoiceLabel = Label(master,text= "Will there be merchandise?")
        self.merchandiseChoiceLabel.grid(column=4,row=1)
        self.merchandiseChoiceYes = Radiobutton(master,text="Yes",variable=self.merchandise,value="Yes")
        self.merchandiseChoiceYes.grid(column=4,row=2)
        self.merchandiseChoiceNo = Radiobutton(master,text="No",variable=self.merchandise,value="No")
        self.merchandiseChoiceNo.grid(column=4,row=3)

        self.pmAMLabel = Label(master, text="PM/AM", underline=0)
        self.pmAMLabel.grid(column=2, row=4)
        self.pmAMOption = OptionMenu(master,self.pmAM,*pmAMList)
        self.pmAMOption.grid(column=2,row=5)

        self.pmAMEndingLabel = Label(master,text="ending AM/PM.", underline=0)
        self.pmAMEndingLabel.grid(column=3,row=4)
        self.pmAMEndingOption = OptionMenu(master,self.pmAMEnding,*pmAMList)
        self.pmAMEndingOption.grid(column=3,row=5)

        self.startTimeLabel = Label(master,text= "Enter start time.")
        self.startTimeLabel.grid(column=4,row=4)
        self.startTimeEntry = Entry(master,textvariable=self.startTime, bd=3)
        self.startTimeEntry.grid(column=4,row=5)

        self.endTimeLabel = Label(master, text= "Enter ending time.")
        self.endTimeLabel.grid(column=5, row=4)
        self.endTimeEntry = Entry(master, textvariable=self.endTime, bd=3)
        self.endTimeEntry.grid(column=5, row=5)
        #


    def post(self):
        name = self.name.get()
        organization = self.organization.get()
        category = self.category.get()
        date = self.date.get()
        dateNum = self.dateNum.get()
        endTime = self.endTime.get()
        startTime = self.startTime.get()
        pmAM = self.pmAM.get()
        pmAMEnding = self.pmAMEnding.get()
        description = self.description.get()
        shareMessage = self.shareMessage.get()
        address = self.address.get()
        food = self.food.get()
        music = self.music.get()
        merchandise = self.merchandise.get()
        lat = self.lat.get()
        longitude = self.longitude.get()
        locationName = self.locationName.get()
        picture = self.pictureName.get()
       

        Firebase.patch("/" + category + "/" + name,{"name":name})
        Firebase.patch("/"+category+ "/" + name,{"organization":organization})
        Firebase.patch("/"+category+ "/" + name,{"category":category})
        Firebase.patch("/"+category+ "/" + name,{"date": date})
        Firebase.patch("/" +category+ "/" + name,{"dateNum": dateNum})
        Firebase.patch("/"+category+ "/" + name,{"endTime": endTime})
        Firebase.patch("/"+category+ "/" + name,{"startTime": startTime})
        Firebase.patch("/"+category+ "/" + name,{"pmAMEnding": pmAMEnding})
        Firebase.patch("/"+category+ "/" + name,{"pmAM": pmAM})
        Firebase.patch("/" +category+ "/" + name,{"description": description})
        Firebase.patch("/" +category+ "/" + name,{"shareMessage": shareMessage})
        Firebase.patch("/" +category+ "/" + name,{"address":address})
        Firebase.patch("/" +category+ "/" + name,{"food": food})
        Firebase.patch("/" +category+ "/" + name,{"music": music})
        Firebase.patch("/" +category+ "/" + name,{"merchandise": merchandise})
        Firebase.patch("/" +category+ "/" + name,{"location name": locationName})
        Firebase.patch("/" +category+ "/" + name,{"lat": r"" +lat + r""})
        Firebase.patch("/" +category+ "/" + name,{"longitude": r"" +longitude + r""})
        Firebase.patch("/" +category+ "/" + name,{"picture": picture})
        Firebase.patch("/" +category+ "/" + name,{"votes":0})
        Firebase.patch("/" +category+ "/"+ name+"/"+"voters",{"placeholder":"voted"})

        Firebase.patch("/Events/" + name,{"name":name})
        Firebase.patch("/Events/" + name,{"organization":organization})
        Firebase.patch("/Events/" + name,{"category":category})
        Firebase.patch("/Events/" + name,{"date": date})
        Firebase.patch("/Events/" + name,{"dateNum": dateNum})
        Firebase.patch("/Events/" + name,{"endTime": endTime})
        Firebase.patch("/Events/" + name,{"startTime": startTime})
        Firebase.patch("/Events/" + name,{"pmAM": pmAM})
        Firebase.patch("/Events/" + name,{"pmAMEnding": pmAMEnding})
        Firebase.patch("/Events/" + name,{"description": description})
        Firebase.patch("/Events/" + name,{"shareMessage": shareMessage})
        Firebase.patch("/Events/" + name,{"address":address})
        Firebase.patch("/Events/" + name,{"food": food})
        Firebase.patch("/Events/" + name,{"music": music})
        Firebase.patch("/Events/" + name,{"merchandise": merchandise})
        Firebase.patch("/Events/" + name,{"location name": locationName})
        Firebase.patch("/Events/" + name,{"lat": r"" +lat + r""})
        Firebase.patch("/Events/" + name,{"longitude": r"" +longitude + r""})
        Firebase.patch("/Events/" + name,{"picture": picture})
        Firebase.patch("/Events/" + name,{"votes":0})
        Firebase.patch("/Events/"+ name+"/"+"voters",{"placeholder":"voted"})
        storage.child(category + "/" + self.pictureName.get()).put(self.picture.get())
        self.pictureEntry.insert(0,root.filename)
        self.nameEntry.delete(0, END)
        self.dateEntry.delete(0, END)
        self.descriptionEntry.delete(0, END)
        self.shareMessageEntry.delete(0,END)
        self.addressEntry.delete(0, END)
        self.latEntry.delete(0, END)
        self.longitudeEntry.delete(0, END)
        self.pictureEntry.delete(0, END)
        self.colorPictureEntry.delete(0, END)
        self.dateNumEntry.delete(0, END)
    def attachPicture(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.pictureName.set(os.path.basename(root.filename))
        self.pictureEntry.insert(0,root.filename)
        print(self.picture.get())
    def attachColorPicture(self):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.colorPictureName.set(os.path.basename(root.filename))
        self.colorPictureEntry.insert(0,root.filename)
        print(self.colorPictureName.get())



if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    GUI = eventEntry(root)
    root.mainloop()

