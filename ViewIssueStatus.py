from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "1873Ashutosh"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "issued_books" 
    
def ViewIssueStatus(): 
    
    root = Tk()
    root.title("Library Management Software by Amratanshu - VIEW ISSUE STATUS OF BOOKS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    root.maxsize(600,500)
    root.iconbitmap("iconamra.ico")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="cyan",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Status of Books", bg='black', fg='white', font=('Algerian',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-40s"%('BID','Issued To'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s"%(i[0],i[1]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()