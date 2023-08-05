from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import numpy as np
from datetime import datetime
import cv2
import mysql.connector
import csv
from tkinter import messagebox

class Face_Detect:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recogonition Attendance System")

        img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\face_detect.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img_bt = Button(self.root,command=self.face_recog,image=self.photoimg,cursor="hand2")
        bg_img_bt.place(x=0,y=0,width=1530,height=800)

    def mark_attendance(self,r,n):
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString=now.strftime("%H:%M:%S")
            if "14:00:00"<=dtString < "15:00:00":
                f = open("Attendance_report/2-3.csv","r+",newline = '\n')
                read = csv.reader(f)
                nrec = []
                found = 0
                for rec in read:
                    if rec[0]==r and rec[4]=="Absent":
                        rec[2]=dtString
                        rec[3]=d1
                        rec[4]="Present"
                        found=1
                    nrec.append(rec)
                
                if found==1:
                    f = open("Attendance_report/2-3.csv","w+",newline='')
                    w = csv.writer(f)
                    w.writerows(nrec)
                    f.close()

                with open("Attendance_report/2-3n.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    name_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[0])

                    if((r not in name_list)) and ((n not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{r}, {n}, {dtString}, {d1}, Present")
            
            elif "9:00:00"<=dtString < "10:00:00":   
                f = open("Attendance_report/9-10.csv","r+",newline = '\n')
                read = csv.reader(f)
                nrec = []
                found = 0
                for rec in read:
                    if rec[0]==r and rec[4]=="Absent":
                        rec[2]=dtString
                        rec[3]=d1
                        rec[4]="Present"
                        found=1
                    nrec.append(rec)
                
                if found==1:
                    f = open("Attendance_report/9-10.csv","w+",newline='')
                    w = csv.writer(f)
                    w.writerows(nrec)
                    f.close()

                with open("Attendance_report/9-10n.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    name_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[0])

                    if((r not in name_list)) and ((n not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{r}, {n}, {dtString}, {d1}, Present")

            elif "10:00:00"<=dtString < "11:00:00":   
                f = open("Attendance_report/10-11.csv","r+",newline = '\n')
                read = csv.reader(f)
                nrec = []
                found = 0
                for rec in read:
                    if rec[0]==r and rec[4]=="Absent":
                        rec[2]=dtString
                        rec[3]=d1
                        rec[4]="Present"
                        found=1
                    nrec.append(rec)
                
                if found==1:
                    f = open("Attendance_report/10-11.csv","w+",newline='')
                    w = csv.writer(f)
                    w.writerows(nrec)
                    f.close()

                with open("Attendance_report/10-11n.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    name_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[0])

                    if((r not in name_list)) and ((n not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{r}, {n}, {dtString}, {d1}, Present")

            elif "11:00:00"<=dtString < "12:00:00":   
                f = open("Attendance_report/11-12.csv","r+",newline = '\n')
                read = csv.reader(f)
                nrec = []
                found = 0
                for rec in read:
                    if rec[0]==r and rec[4]=="Absent":
                        rec[2]=dtString
                        rec[3]=d1
                        rec[4]="Present"
                        found=1
                    nrec.append(rec)
                
                if found==1:
                    f = open("Attendance_report/11-12.csv","w+",newline='')
                    w = csv.writer(f)
                    w.writerows(nrec)
                    f.close()

                with open("Attendance_report/11-12n.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    name_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[0])

                    if((r not in name_list)) and ((n not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{r}, {n}, {dtString}, {d1}, Present")

            elif "15:00:00"<=dtString < "16:00:00":   
                f = open("Attendance_report/3-4.csv","r+",newline = '\n')
                read = csv.reader(f)
                nrec = []
                found = 0
                for rec in read:
                    if rec[0]==r and rec[4]=="Absent":
                        rec[2]=dtString
                        rec[3]=d1
                        rec[4]="Present"
                        found=1
                    nrec.append(rec)
                
                if found==1:
                    f = open("Attendance_report/3-4.csv","w+",newline='')
                    w = csv.writer(f)
                    w.writerows(nrec)
                    f.close()

                with open("Attendance_report/3-4n.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    name_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[0])

                    if((r not in name_list)) and ((n not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{r}, {n}, {dtString}, {d1}, Present")
                    
    def face_recog(self):
        

        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                id  = str(id)
                if id[2:3]=='1':
                    id = "B"+ id[0:2] + "CS" + id[3:6]
                elif id[2:3]=='2':
                    id = "B"+ id[0:2] + "AI" + id[3:6]
                elif id[2:3]=='3':
                    id = "B"+ id[0:2] + "EE" + id[3:6]
                elif id[2:3]=='4':
                    id = "B"+ id[0:2] + "ME" + id[3:6]
                elif id[2:3]=='5':
                    id = "B"+ id[0:2] + "CI" + id[3:6]
                elif id[2:3]=='6':
                    id = "B"+ id[0:2] + "CH" + id[3:6]
                elif id[2:3]=='7':
                    id = "B"+ id[0:2] + "MT" + id[3:6]
                elif id[2:3]=='8':
                    id = "B"+ id[0:2] + "BB" + id[3:6]

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
                cursor = conn.cursor()

                temp = id

                cursor.execute("SELECT Name FROM student_data WHERE Roll = %s",(temp,))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("SELECT Roll FROM student_data WHERE Roll = %s",(temp,))
                r=cursor.fetchone()
                r="+".join(r)

                if confidence > 70:
                    cv2.putText(img,f"Name : {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll No. : {r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    
                coord=[x,y,w,y]
            
            return coord    

        

        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root=Tk()
    obj=Face_Detect(root)
    root.mainloop()