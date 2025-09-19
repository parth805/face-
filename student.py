import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import cv2
import mysql.connector
import numpy as np


class Student1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # =================== Variables ===================
        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_std_id = tk.StringVar()
        self.var_std_name = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_radio1 = tk.StringVar()
        
        # Variables for Search
        self.var_search_by = tk.StringVar()
        self.var_search_txt = tk.StringVar()


        # --- UI Elements and Images ---
        header_frame = tk.Frame(self.root, bg="lightgrey")
        header_frame.place(x=0, y=0, width=1530, height=130)

        try:
            img_header1 = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\4.jpeg")
            img_header1 = img_header1.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg_header1 = ImageTk.PhotoImage(img_header1)
            tk.Label(header_frame, image=self.photoimg_header1).place(x=0, y=0, width=500, height=130)

            img_header2 = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\6.jpeg")
            img_header2 = img_header2.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg_header2 = ImageTk.PhotoImage(img_header2)
            tk.Label(header_frame, image=self.photoimg_header2).place(x=500, y=0, width=500, height=130)

            img_header3 = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\5.jpeg")
            img_header3 = img_header3.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg_header3 = ImageTk.PhotoImage(img_header3)
            tk.Label(header_frame, image=self.photoimg_header3).place(x=1000, y=0, width=550, height=130)
        except FileNotFoundError:
            tk.Label(header_frame, text="Header Images Not Found", font=("arial", 16, "bold"), bg="lightgrey", fg="red").pack(expand=True)

        bg_frame = tk.Frame(self.root)
        bg_frame.place(x=0, y=130, width=1530, height=710)
        try:
            img_bg = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\3.jpeg")
            img_bg = img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
            self.photobg_img = ImageTk.PhotoImage(img_bg)
            tk.Label(bg_frame, image=self.photobg_img).place(x=0, y=0, width=1530, height=710)
        except FileNotFoundError:
            bg_frame.config(bg="#E0E0E0")
            tk.Label(bg_frame, text="Background Image Not Found", font=("arial", 20, "bold"), bg="#E0E0E0", fg="red").pack(pady=20)


        title_lbl = tk.Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        main_frame = tk.Frame(bg_frame, bd=2, relief=tk.RIDGE, bg="white")
        main_frame.place(x=15, y=45, width=1500, height=600)

        Left_frame = tk.LabelFrame(main_frame, bd=2, relief=tk.RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        try:
            img_left = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\7.jpeg")
            img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            tk.Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)
        except FileNotFoundError:
            left_img_placeholder = tk.Frame(Left_frame, bg="lightgrey")
            left_img_placeholder.place(x=5, y=0, width=720, height=130)
            tk.Label(left_img_placeholder, text="Image Not Found", font=("arial", 12), bg="lightgrey").pack(expand=True)

        current_course_frame = tk.LabelFrame(Left_frame, bd=2, relief=tk.RIDGE, text="Current course information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=120)

        dep_label = tk.Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=tk.W)
        self.dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.dep_combo["values"] = ("Select Department", "Computer", "IT", "Electronics", "Civil", "Mechanical")
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=tk.W)

        course_label = tk.Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=tk.W)
        self.course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.course_combo["values"] = ("Select Course", "B.tech", "BCA", "MCA", "LAW")
        self.course_combo.current(0)
        self.course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=tk.W)

        year_label = tk.Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=tk.W)
        self.year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.year_combo["values"] = ("Select Year", "2022-23", "2023-24", "2024-25", "2025-26")
        self.year_combo.current(0)
        self.year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=tk.W)

        semester_label = tk.Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=tk.W)
        self.semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        self.semester_combo.current(0)
        self.semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=tk.W)

        class_student_frame = tk.LabelFrame(Left_frame, bd=2, relief=tk.RIDGE, text="Class Student information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=720, height=280)

        studentID_label = tk.Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"))
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        self.studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        studentName_label = tk.Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        self.studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        self.studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        gender_label = tk.Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"))
        gender_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        dob_label = tk.Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        
        # Date of Birth Dropdowns
        self.var_dob_day = tk.StringVar()
        self.var_dob_month = tk.StringVar()
        self.var_dob_year = tk.StringVar()

        dob_frame = tk.Frame(class_student_frame)
        dob_frame.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

        day_combo = ttk.Combobox(dob_frame, textvariable=self.var_dob_day, font=("times new roman", 12, "bold"), state="readonly", width=5)
        day_combo['values'] = ["Day"] + [str(i) for i in range(1, 32)]
        day_combo.current(0)
        day_combo.pack(side=tk.LEFT, padx=2)

        month_combo = ttk.Combobox(dob_frame, textvariable=self.var_dob_month, font=("times new roman", 12, "bold"), state="readonly", width=7)
        month_combo['values'] = ["Month"] + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_combo.current(0)
        month_combo.pack(side=tk.LEFT, padx=2)
        
        year_combo = ttk.Combobox(dob_frame, textvariable=self.var_dob_year, font=("times new roman", 12, "bold"), state="readonly", width=6)
        year_combo['values'] = ["Year"] + [str(i) for i in range(1990, 2026)]
        year_combo.current(0)
        year_combo.pack(side=tk.LEFT, padx=2)


        email_label = tk.Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        phone_label = tk.Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"))
        phone_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        btn_frame = tk.Frame(class_student_frame, bd=2, relief=tk.RIDGE)
        btn_frame.place(x=0, y=160, width=715, height=35)

        save_btn = tk.Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = tk.Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        photo_btn_frame = tk.Frame(class_student_frame, bd=2, relief=tk.RIDGE)
        photo_btn_frame.place(x=0, y=200, width=715, height=35)

        take_photo_btn = tk.Button(photo_btn_frame, text="Take Photo Sample", command=self.generate_dataset, width=35, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=2)
        
        update_photo_btn = tk.Button(photo_btn_frame, text="Update Photo Sample", command=self.generate_dataset, width=35, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=2)


        Right_frame = tk.LabelFrame(main_frame, bd=2, relief=tk.RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=740, height=580)
        
        # =================== SEARCH SYSTEM ===================
        search_frame = tk.LabelFrame(Right_frame, bd=2, relief=tk.RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=5, width=730, height=70)
        
        search_label = tk.Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Student_id", "Name", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=tk.W)
        
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_txt, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        
        search_btn = tk.Button(search_frame, text="Search", command=self.search_data, width=14, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = tk.Button(search_frame, text="Show All", command=self.fetch_data, width=14, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)


        # =================== TABLE FRAME ===================
        table_frame = tk.Frame(Right_frame, bd=2, relief=tk.RIDGE)
        table_frame.place(x=5, y=80, width=730, height=470)

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL, width=20) # Made the scrollbar thicker

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "gender", "dob", "email", "phone", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=120)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=80)
        self.student_table.column("id", width=80)
        self.student_table.column("name", width=120)
        self.student_table.column("gender", width=80)
        self.student_table.column("dob", width=80)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("photo", width=120)

        self.student_table.pack(fill=tk.BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    # =================== Function Definitions ===================
    def add_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "Department, Student ID, and Name are required fields.", parent=self.root)
        elif self.var_dob_day.get() == "Day" or self.var_dob_month.get() == "Month" or self.var_dob_year.get() == "Year":
            messagebox.showerror("Error", "Please select a valid Date of Birth.", parent=self.root)
        else:
            try:
                dob = f"{self.var_dob_day.get()}-{self.var_dob_month.get()}-{self.var_dob_year.get()}"
                self.var_dob.set(dob)

                conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.var_std_id.get(), self.var_std_name.get(), self.var_gender.get(), self.var_dob.get(),
                    self.var_email.get(), self.var_phone.get(), self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added Successfully", parent=self.root)
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    messagebox.showerror("Error", f"Student ID {self.var_std_id.get()} already exists.", parent=self.root)
                else:
                    messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            self.student_table.delete(*self.student_table.get_children())
            if len(data) != 0:
                for i in data:
                    self.student_table.insert("", tk.END, values=i)
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Could not connect to database: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred while fetching data: {str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        try:
            cursor_focus = self.student_table.focus()
            if not cursor_focus: return
            content = self.student_table.item(cursor_focus)
            if content and "values" in content and content["values"]:
                data = content["values"]
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_semester.set(data[3])
                self.var_std_id.set(data[4])
                self.var_std_name.set(data[5])
                self.var_gender.set(data[6])
                
                dob_str = data[7]
                if dob_str:
                    try:
                        day, month, year = dob_str.split('-')
                        self.var_dob_day.set(day)
                        self.var_dob_month.set(month)
                        self.var_dob_year.set(year)
                    except ValueError:
                        self.reset_dob_fields() # Reset if format is wrong
                else:
                    self.reset_dob_fields()

                self.var_email.set(data[8])
                self.var_phone.set(data[9])
                self.var_radio1.set(data[10])
        except IndexError:
            messagebox.showwarning("Data Mismatch", "Could not read the selected row.", parent=self.root)


    def update_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "Department, Student ID, and Name are required fields.", parent=self.root)
        elif self.var_dob_day.get() == "Day" or self.var_dob_month.get() == "Month" or self.var_dob_year.get() == "Year":
            messagebox.showerror("Error", "Please select a valid Date of Birth.", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if Update:
                    dob = f"{self.var_dob_day.get()}-{self.var_dob_month.get()}-{self.var_dob_year.get()}"
                    self.var_dob.set(dob)
                    
                    conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,PhotoSample=%s where Student_id=%s",
                        (
                            self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                            self.var_std_name.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(),
                            self.var_phone.get(), self.var_radio1.get(), self.var_std_id.get()
                        ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete.", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student", "Do you want to delete this student?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Successfully deleted student details.", parent=self.root)
                    self.reset_data()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)

    def reset_dob_fields(self):
        self.var_dob_day.set("Day")
        self.var_dob_month.set("Month")
        self.var_dob_year.set("Year")
        self.var_dob.set("")

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_gender.set("")
        self.reset_dob_fields()
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")
        self.var_search_by.set("Select")
        self.var_search_txt.set("")

    # =================== Generate Photo Samples (with Live Feedback) ===================
    def generate_dataset(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "Student ID and Name are required to generate photo samples.", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student where Student_id=%s", (self.var_std_id.get(),))
            if my_cursor.fetchone() is None:
                messagebox.showerror("Error", "This student is not in the database. Please save their details first.", parent=self.root)
                conn.close()
                return
            
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                messagebox.showerror("Error", "Could not open webcam.", parent=self.root)
                return
                
            img_id = 0
            if not os.path.exists("data"):
                os.makedirs("data")

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture image from webcam.", parent=self.root)
                    break
                
                gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                
                for (x,y,w,h) in faces:
                    # Draw rectangle on the main frame
                    cv2.rectangle(my_frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
                    
                    # Increment counter only when a face is detected
                    img_id += 1
                    
                    # Crop the face from the original frame
                    face = my_frame[y:y+h, x:x+w]
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    
                    # Save the cropped face
                    file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    
                    # Put text on the main frame
                    cv2.putText(my_frame, f"Samples: {img_id}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                
                # Show the main frame with feedback
                cv2.imshow("Taking Samples", my_frame)

                if cv2.waitKey(1) == 13 or int(img_id) >= 100:
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            my_cursor.execute("update student set PhotoSample=%s where Student_id=%s", ("Yes", self.var_std_id.get()))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Result", "Generating data sets completed!", parent=self.root)

        except cv2.error:
            messagebox.showerror("Error", "OpenCV Error: Make sure 'haarcascade_frontalface_default.xml' is in the script's folder.", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)
            
    # =================== Search Data ===================
    def search_data(self):
        if self.var_search_by.get() == "Select" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter text.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="##11Pappii", database="face_recognizer")
                my_cursor = conn.cursor()
                query = f"select * from student where {self.var_search_by.get()} LIKE '%{self.var_search_txt.get()}%'"
                my_cursor.execute(query)
                data = my_cursor.fetchall()

                self.student_table.delete(*self.student_table.get_children())
                if len(data) != 0:
                    for i in data:
                        self.student_table.insert("", tk.END, values=i)
                else:
                    messagebox.showinfo("Information", "No records found matching your search.", parent=self.root)

                conn.commit()
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Student1(root)
    root.mainloop()
