from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from ViewIssueStatus import *

mypass = "1873Ashutosh" 
mydatabase="db" #The database name

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here

cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library Management Software by Amratanshu")
root.minsize(width=400,height=400)
root.geometry("1920x1080")
root.iconbitmap("iconamra.ico")

same=True
n=1

#Adding Background Images
background_image =Image.open("lib31.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n)
#background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)


Canvas1 = Canvas(root)
Canvas1.create_image(570,540,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

logo_image = Image.open("iertlogo.png")
img1 = ImageTk.PhotoImage(logo_image)
logoFrame2 = Frame(root, bg = "White", bd = 0)
logoFrame2.place(relx = 0.01, rely = 0.01, relwidth=0.12, relheight=0.25)
logolabel = Label(logoFrame2,text = 'Amratanshu', image = img1, bg = "white")
logolabel.place(relx=0,rely=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \nLibrary Management Software", bg='black', fg='white', font=('Algerian',24))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook, font=('Lucida Sans', 22), bd= 4)
btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete, font=('Lucida Sans', 22), bd= 4)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View, font=('Lucida Sans', 22), bd= 4)
btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook, font=('Lucida Sans', 22), bd= 4)
btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook, font=('Lucida Sans', 22), bd= 4)
btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="Issued Book List",bg='black', fg='white', command = ViewIssueStatus, font=('Lucida Sans', 22), bd= 4)
btn6.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)

root.mainloop()