from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import numpy as np
import cv2
from tkinter import messagebox
from student_data_page import Student_data
from face_detect_page import Face_Detect
from attendance_page import Student_attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recogonition Attendance System")

        img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\main_page.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=800)


        title_lb1 = Label(bg_img,text="Face Recognition Attendance System",font=("verdana",30,"bold"),bg="white",fg="Black")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        img1=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\iitj.jpg")
        img1=img1.resize((60,60),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=2,y=2,width=60,height=60)

        img2=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\iitj.jpg")
        img2=img2.resize((60,60),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root,image=self.photoimg2)
        f_lb2.place(x=1470,y=2,width=60,height=60)

        std_img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\student.jpg")
        std_img=std_img.resize((225,225),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img)

        std_b1 = Button(bg_img,image=self.std_img1,command=self.std_data,cursor="hand2")
        std_b1.place(x=250,y=100,width=225,height=225)

        std_b1_text = Button(bg_img,text="Student Data",command=self.std_data,cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="Black")
        std_b1_text.place(x=250,y=325,width=225,height=45)

        face_img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\face_detector.jpg")
        face_img=face_img.resize((225,225),Image.ANTIALIAS)
        self.face_img1=ImageTk.PhotoImage(face_img)

        face_b1 = Button(bg_img,command=self.face_data,image=self.face_img1,cursor="hand2")
        face_b1.place(x=600,y=100,width=225,height=225)

        face_b1_text = Button(bg_img,command=self.face_data,text="Face Detector",cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="Black")
        face_b1_text.place(x=600,y=325,width=225,height=45)

        train_img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\training_data.jpg")
        train_img=train_img.resize((225,225),Image.ANTIALIAS)
        self.train_img1=ImageTk.PhotoImage(train_img)

        train_b1 = Button(bg_img,command = self.train_classifier,image=self.train_img1,cursor="hand2")
        train_b1.place(x=250,y=425,width=225,height=225)

        train_b1_text = Button(bg_img,command = self.train_classifier,text="Training Data",cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="Black")
        train_b1_text.place(x=250,y=650,width=225,height=45)

        attendance_img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\Attendance_data.jpg")
        attendance_img=attendance_img.resize((225,225),Image.ANTIALIAS)
        self.attendance_img1=ImageTk.PhotoImage(attendance_img)

        attendance_b1 = Button(bg_img,command = self.attend_data,image=self.attendance_img1,cursor="hand2")
        attendance_b1.place(x=600,y=425,width=225,height=225)

        attendance_b1_text = Button(bg_img,command = self.attend_data,text="Attendance Data",cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="Black")
        attendance_b1_text.place(x=600,y=650,width=225,height=45)

        exi_b1_1 = Button(bg_img,command = self.Close,text="Exit",cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="Black")
        exi_b1_1.place(x=425,y=722.5,width=225,height=45)


    def std_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_data(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detect(self.new_window)

    def attend_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_attendance(self.new_window)

    def Close(self):
        root.destroy()

    def train_classifier(self):
        data_dir=("std_photos")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('-')[0])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()