from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main_page import Face_Recognition_System
from registration_page import Registration

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recogonition Attendance System")
        # self.root.wm_iconbitmap("face.ico")

        show_icon = Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\view.png")
        show_icon=show_icon.resize((20,20),Image.ANTIALIAS)
        self.photoshow_icon=ImageTk.PhotoImage(show_icon)

        hide_icon = Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\hide.png")
        hide_icon=hide_icon.resize((20,20),Image.ANTIALIAS)
        self.photohide_icon=ImageTk.PhotoImage(hide_icon)

        img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\login_page.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=800)

        frame1= Frame(self.root,bg="White")
        frame1.place(x=300,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\login_icon.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(self.root,image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=420,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",30,"bold"),fg="navyblue",bg="White")
        get_str.place(x=120,y=110)

        img1=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\username.jpg")
        img1=img1.resize((32,32),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.img1)
        f_lb1.place(x=310,y=360,width=32,height=32)

        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=190,width=270)

        img2=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\password.jpg")
        img2=img2.resize((32,32),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root,image=self.img2)
        f_lb2.place(x=310,y=410,width=32,height=32)

        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"),show='*')
        self.txtpwd.place(x=50,y=240,width=270)

        self.hide_icon_btn = Button(frame1,image = self.photoshow_icon, bd=0)
        self.hide_icon_btn.place(x=320,y=245)

        self.show_icon_btn = Button(frame1,image = self.photohide_icon, bd=0, command =self.show)
        self.show_icon_btn.place(x=320,y=245)

        loginbtn=Button(frame1,command = self.login,text="Login",font=("times new roman",15,"bold"),cursor="hand2",bd=0,relief=RIDGE,fg="White",bg="navyblue",activeforeground="navyblue",activebackground="white")
        loginbtn.place(x=50,y=300,width=270,height=35)


        registerbtn=Button(frame1,command=self.regis,text="Register",font=("times new roman",15,"bold"),cursor="hand2",bd=0,relief=RIDGE,fg="White",bg="Black",activeforeground="Black",activebackground="White")
        registerbtn.place(x=50,y=350,width=270,height=35)


        # pwdbtn=Button(frame1,text="Forget Password",font=("times new roman",13,"bold"),cursor="hand2",bd=0,relief=RIDGE,fg="Black",bg="White",activeforeground="white",activebackground="navyblue")
        # pwdbtn.place(x=170,y=370,width=135,height=20)

    def show(self):
        if self.txtpwd['show'] == '':
            self.show_icon_btn.config(image = self.photohide_icon)
            self.txtpwd.config(show = '*')

        else :
            self.show_icon_btn.config(image = self.photoshow_icon)
            self.txtpwd.config(show = '')

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!",parent=self.root)
        elif(self.txtuser.get()=="ayush" and self.txtpwd.get()=="ayush007"):
            open_min=1
            if open_min>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
            else:
                if not open_min:
                    return
        else:
            # messagebox.showerror("Error","Please Check Username or Password !",parent=self.root)
            conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            mycursor.execute("select * from registered where Username=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            print(self.txtuser.get())
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!",parent=self.root)
            else:
                open_min=1
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()

    def regis(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)

    

if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()