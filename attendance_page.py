from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Student_attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recogonition Attendance System")

        img=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\main_page.jpg")
        img=img.resize((1530,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=800)

        imgx=Image.open(r"C:\Users\USER\Documents\Face_recognition_system\Images\attendance_page_1.jpg")
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

        str_l = Label(left_frame,text="Student Attendance Details",font=("times new roman",30,"bold"),fg="navyblue",bg="White")
        str_l.place(x=140,y=10)

        str_r = Label(right_frame,text="Attendance Data",font=("times new roman",30,"bold"),fg="navyblue",bg="White")
        str_r.place(x=240,y=10)

        left_frame_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        left_frame_frame.place(x=10,y=70,width=725,height=395)

        right_frame_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        right_frame_frame.place(x=10,y=70,width=725,height=395)

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        roll_no_label = Label(left_frame_frame,text="Roll-No:",font=("verdana",16,"bold"),fg="Black",bg="white")
        roll_no_label.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        roll_no_entry = ttk.Entry(left_frame_frame,textvariable=self.var_roll,width=17,font=("verdana",16,"bold"))
        roll_no_entry.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_name_label = Label(left_frame_frame,text="Name:",font=("verdana",16,"bold"),fg="Black",bg="white")
        student_name_label.grid(row=2,column=1,padx=5,pady=15,sticky=W)

        student_name_entry = ttk.Entry(left_frame_frame,textvariable=self.var_name,width=17,font=("verdana",16,"bold"))
        student_name_entry.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        time_label = Label(left_frame_frame,text="Time:",font=("verdana",16,"bold"),fg="Black",bg="white")
        time_label.grid(row=7,column=1,padx=5,pady=15,sticky=W)

        time_entry = ttk.Entry(left_frame_frame,textvariable=self.var_time,width=17,font=("verdana",16,"bold"))
        time_entry.grid(row=7,column=2,padx=5,pady=5,sticky=W)

        date_label = Label(left_frame_frame,text="Date:",font=("verdana",16,"bold"),fg="Black",bg="white")
        date_label.grid(row=8,column=1,padx=5,pady=15,sticky=W)

        date_entry = ttk.Entry(left_frame_frame,textvariable=self.var_date,width=17,font=("verdana",16,"bold"))
        date_entry.grid(row=8,column=2,padx=5,pady=5,sticky=W)

        Attend_label=Label(left_frame_frame,text="Attend:",font=("verdana",16,"bold"),bg="white",fg="Black")
        Attend_label.grid(row=9,column=1,padx=5,pady=15,sticky=W)

        Attend_entry=ttk.Entry(left_frame_frame,textvariable=self.var_attend,width=17,font=("verdana",16,"bold"))
        Attend_entry.grid(row=9,column=2,padx=5,pady=5,sticky=W)

        btn_frame = Frame(left_frame_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.place(x=525,y=0,width=175,height=380)

        import_btn=Button(btn_frame,command = self.importcsv,text="Import CSV",cursor="hand2",width=11,font=("verdana",12,"bold"),fg="white",bg="Black")
        import_btn.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        export_btn=Button(btn_frame,text="Export CSV",command= self.exportCsv,width=11,cursor="hand2",font=("verdana",12,"bold"),fg="white",bg="Black")
        export_btn.grid(row=4,column=2,padx=15,pady=15,sticky=W)

        Reset_btn=Button(btn_frame,command = self.reset_data,text="Reset",cursor="hand2",width=11,font=("verdana",12,"bold"),fg="white",bg="Black")
        Reset_btn.grid(row=6,column=2,padx=15,pady=15,sticky=W)

        table_frame = Frame(right_frame,bg="white",relief=RIDGE)
        table_frame.place(x=19,y=78,width=705,height=380)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendance_table = ttk.Treeview(table_frame,column=("Roll","Name","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("Roll",text="Roll")
        self.attendance_table.heading("Name",text="Name")
        self.attendance_table.heading("Time",text="Time")
        self.attendance_table.heading("Date",text="Date")
        self.attendance_table.heading("Attendance",text="Attendance")
        self.attendance_table["show"]="headings"


        # Set Width of Colums 
        self.attendance_table.column("Roll",width=125)
        self.attendance_table.column("Name",width=150)
        self.attendance_table.column("Time",width=135)
        self.attendance_table.column("Date",width=125)
        self.attendance_table.column("Attendance",width=150)

        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
        

    def importcsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    def get_cursor(self,event=""):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content["values"]

        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_time.set(data[2]),
        self.var_date.set(data[3]),
        self.var_attend.set(data[4])

    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("")

    


if __name__ == "__main__":
    root=Tk()
    obj=Student_attendance(root)
    root.mainloop()