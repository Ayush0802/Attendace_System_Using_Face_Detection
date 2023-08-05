from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recogonition Attendance System")

        img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\main_page.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=800)

        imgx=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\student_data.jpg")
        imgx=imgx.resize((1530,292),Image.ANTIALIAS)
        self.photoimgx=ImageTk.PhotoImage(imgx)

        f_lb = Label(self.root,image=self.photoimgx)
        f_lb.place(x=0,y=0,width=1530,height=292)

        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=0,y=290,width=1530,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",15,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=750,height=480)

        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",15,"bold"),fg="navyblue")
        right_frame.place(x=770,y=10,width=750,height=480)

        str_l = Label(left_frame,text="Student Details",font=("times new roman",30,"bold"),fg="navyblue",bg="White")
        str_l.place(x=210,y=10)

        str_r = Label(right_frame,text="All Students Data",font=("times new roman",30,"bold"),fg="navyblue",bg="White")
        str_r.place(x=240,y=10)

        left_frame_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        left_frame_frame.place(x=10,y=70,width=725,height=395)

        right_frame_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        right_frame_frame.place(x=10,y=70,width=725,height=395)

        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_teacher=StringVar()
        self.var_dob=StringVar()

        roll_no_label = Label(left_frame_frame,text="Roll-No:",font=("verdana",16,"bold"),fg="Black",bg="white")
        roll_no_label.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(left_frame_frame,textvariable=self.var_roll,width=17,font=("verdana",16,"bold"))
        roll_no_entry.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_name_label = Label(left_frame_frame,text="Name:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_name_label.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame_frame,textvariable=self.var_std_name,width=17,font=("verdana",16,"bold"))
        student_name_entry.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_email_label = Label(left_frame_frame,text="Email:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_email_label.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(left_frame_frame,textvariable=self.var_email,width=17,font=("verdana",16,"bold"))
        student_email_entry.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        dep_label=Label(left_frame_frame,text="Branch:",font=("verdana",16,"bold"),bg="white",fg="Black")
        dep_label.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_frame_frame,textvariable=self.var_dep,width=16,font=("verdana",16,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CS","AI","EE","CH","CI","ME","BB","MT")
        dep_combo.current(0)
        dep_combo.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        year_label=Label(left_frame_frame,text="Year:",font=("verdana",16,"bold"),bg="white",fg="Black")
        year_label.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        year_combo=ttk.Combobox(left_frame_frame,textvariable=self.var_year,width=16,font=("verdana",16,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2019-23","2020-24","2021-25","2022-26")
        year_combo.current(0)
        year_combo.grid(row=5,column=2,padx=5,pady=5,sticky=W)

        student_gender_label = Label(left_frame_frame,text="Gender:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_gender_label.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(left_frame_frame,textvariable=self.var_gender,width=16,font=("verdana",16,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=6,column=2,padx=5,pady=5,sticky=W)

        student_dob_label = Label(left_frame_frame,text="DOB:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_dob_label.grid(row=7,column=1,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(left_frame_frame,textvariable=self.var_dob,width=17,font=("verdana",16,"bold"))
        student_dob_entry.grid(row=7,column=2,padx=5,pady=5,sticky=W)

        student_mob_label = Label(left_frame_frame,text="Mob-No:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_mob_label.grid(row=8,column=1,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(left_frame_frame,textvariable=self.var_mob,width=17,font=("verdana",16,"bold"))
        student_mob_entry.grid(row=8,column=2,padx=5,pady=5,sticky=W)

        faculty_label = Label(left_frame_frame,text="Faculty Advisor:",font=("verdana",16,"bold"),fg="Black",bg="white")
        faculty_label.grid(row=9,column=1,padx=5,pady=5,sticky=W)

        faculty_entry = ttk.Entry(left_frame_frame,textvariable=self.var_teacher,width=17,font=("verdana",16,"bold"))
        faculty_entry.grid(row=9,column=2,padx=5,pady=5,sticky=W)

        btn_frame = Frame(left_frame_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.place(x=525,y=0,width=175,height=380)

        save_btn=Button(btn_frame,command=self.save,text="Save Details",cursor="hand2",width=11,font=("verdana",12,"bold"),fg="white",bg="Black")
        save_btn.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=11,cursor="hand2",font=("verdana",12,"bold"),fg="white",bg="Black")
        reset_btn.grid(row=4,column=2,padx=15,pady=15,sticky=W)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete,width=11,cursor="hand2",font=("verdana",12,"bold"),fg="white",bg="Black")
        delete_btn.grid(row=5,column=2,padx=15,pady=15,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command = self.generate_dataset,text="Take Photos",cursor="hand2",width=11,font=("verdana",12,"bold"),fg="white",bg="Black")
        take_photo_btn.grid(row=6,column=2,padx=15,pady=15,sticky=W)

        search_frame = LabelFrame(right_frame_frame,bd=0,bg="white",relief=RIDGE,padx=5,text=" Search Student Details",font=("verdana",15,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Roll No:",font=("verdana",15,"bold"),fg="Black",bg="white")
        search_label.grid(row=0,column=0,padx=0,pady=5,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command = self.search,text="Search",cursor="hand2",width=9,font=("verdana",12,"bold"),fg="white",bg="Black")
        search_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command = self.fetch_data,text="Show All",cursor="hand2",width=9,font=("verdana",12,"bold"),fg="white",bg="Black")
        showAll_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        table_frame = Frame(right_frame_frame,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=695,height=295)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("Roll","Name","Email","Dep","Year","Gender","DOB","Mob-No","Teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Mob-No")
        self.student_table.heading("Teacher",text="Faculty Advisor")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def save(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_std_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port= 3307)
                mycursor = conn.cursor()
                mycursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_roll.get(),
                self.var_std_name.get(),
                self.var_email.get(),
                self.var_dep.get(),
                self.var_year.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_teacher.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
        mycursor = conn.cursor()

        mycursor.execute("select * from student_data")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_roll.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[3]),
        self.var_year.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_mob.set(data[7]),
        
        self.var_email.set(data[2]),
        self.var_teacher.set(data[8])

    def delete(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
                    mycursor = conn.cursor() 
                    sql="delete from student_data where Email=%s"
                    val=(self.var_email.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset(self):
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),

    
    # ===========================Search Data===================
    def search(self):
        if self.var_search.get()=="":
            messagebox.showerror("Error","Please Enter the Roll No.",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student_data where Roll= %s",(str(self.var_search.get()),))
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Year" or self.var_std_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            messagebox.showinfo("Ready","Please move your face right-left and Up-down for proper photo sample!",parent=self.root)
            try:
                    
                conn = mysql.connector.connect(username='root', password='ayush007',host='127.0.0.1',database='face_recognition',port=3307)
                mycursor = conn.cursor()
                id=self.var_roll.get()

                if id[3:5]=="CS":
                    id = id[1:3]+'1'+id[5:]
                elif id[3:5]=="AI":
                    id = id[1:3]+'2'+id[5:]
                elif id[3:5]=="EE":
                    id = id[1:3]+'3'+id[5:]
                elif id[3:5]=="ME":
                    id = id[1:3]+'4'+id[5:]
                elif id[3:5]=="CI":
                    id = id[1:3]+'5'+id[5:]
                elif id[3:5]=="CH":
                    id = id[1:3]+'6'+id[5:]
                elif id[3:5]=="MT":
                    id = id[1:3]+'7'+id[5:]
                elif id[3:5]=="BB":
                    id = id[1:3]+'8'+id[5:]
                
                
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(700,700))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="std_photos/"+str(id)+"-"+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(200,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Photo Samples taken Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student_data(root)
    root.mainloop()