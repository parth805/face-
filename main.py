from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from train import Train
from face_recog import FaceRecognition
from student import Student1


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # ================== Title Label ==================
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="navy", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================== Main Frame ==================
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=700)

        # ================== Left Frame for Student Info ==================
        Left_Frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"), bg="white")
        Left_Frame.place(x=10, y=10, width=730, height=680)
        
        # --- Course Information Frame ---
        course_frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, text="Course Information",
                                   font=("times new roman", 12, "bold"), bg="white")
        course_frame.place(x=5, y=10, width=720, height=150)

        # Department
        dep_label = Label(course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18)
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Course
        course_label = Label(course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(course_frame, font=("times new roman", 12), state="readonly", width=18)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # --- Student Information Frame ---
        student_frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, text="Class Student Information",
                                   font=("times new roman", 12, "bold"), bg="white")
        student_frame.place(x=5, y=170, width=720, height=480)
        
        # Student ID
        studentId_label = Label(student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentId_entry = ttk.Entry(student_frame, width=20, font=("times new roman", 12))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(student_frame, width=20, font=("times new roman", 12))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # --- Button Frame ---
        btn_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=350, width=705, height=40)

        save_btn = Button(btn_frame, text="Save", width=17, font=("times new roman", 13, "bold"), bg="navy", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="navy", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17, font=("times new roman", 13, "bold"), bg="navy", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, font=("times new roman", 13, "bold"), bg="navy", fg="white")
        reset_btn.grid(row=0, column=3)


        # ================== Right Frame for Student Data Table ==================
        Right_Frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Data",
                                 font=("times new roman", 12, "bold"), bg="white")
        Right_Frame.place(x=750, y=10, width=730, height=680)

        # --- Table Frame ---
        table_frame = Frame(Right_Frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=10, width=720, height=640)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "id", "name"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Header Images
        img_header1 = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\2.png")
        img_header1 = img_header1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_header1 = ImageTk.PhotoImage(img_header1)
        Label(self.root, image=self.photoimg_header1).place(x=0, y=0, width=500, height=130)

        img_header2=Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\1.png")
        img_header2 = img_header2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_header2=ImageTk.PhotoImage(img_header2)
        Label(self.root,image=self.photoimg_header2).place(x=500,y=0,width=500,height=130)

        img_header3=Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\1.png")
        img_header3 = img_header3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_header3=ImageTk.PhotoImage(img_header3)
        Label(self.root,image=self.photoimg_header3).place(x=1000,y=0,width=550,height=130)
        
        # ================== Title Label (NEW) ==================
        title_lbl = Label(self.root, text="FACE RECOGNITION SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="darkblue")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        # Background Image (Adjusted y-position)
        img_bg=Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\2.png")
        img_bg=img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photobg_img=ImageTk.PhotoImage(img_bg)
        bg_img_label=Label(self.root, image=self.photobg_img)
        bg_img_label.place(x=0, y=175, width=1530, height=615) # Adjusted y and height

        # ================== Buttons ==================
        icon_size = (150, 150)
        button_width = 220
        button_height = 180
        font_style = ("times new roman", 15, "bold")

        # Load images for buttons
        img_std_icon = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\2.png")
        img_std_icon = img_std_icon.resize(icon_size, Image.Resampling.LANCZOS)
        self.photoimg_std_icon = ImageTk.PhotoImage(img_std_icon)

        img_other_icon = Image.open(r"C:\Users\REPUBLIC OF GAMERS\OneDrive\Desktop\image\1.png")
        img_other_icon = img_other_icon.resize(icon_size, Image.Resampling.LANCZOS)
        self.photoimg_other_icon = ImageTk.PhotoImage(img_other_icon)

        # --- Helper function for hover effect ---
        def on_enter(e):
            e.widget['background'] = 'orange'
            e.widget['foreground'] = 'black'
            e.widget['relief'] = FLAT

        def on_leave(e):
            e.widget['background'] = 'white'
            e.widget['foreground'] = 'navy'
            if e.widget.cget('text') == "Exit":
                e.widget['foreground'] = 'red'
            e.widget['relief'] = RAISED

        # --- Row 1 Buttons ---
        
        # Student Details Button
        student_btn = Button(bg_img_label, image=self.photoimg_std_icon, text="Student Details", font=font_style,
                              compound="top", cursor="hand2", command=self.student_details_window,
                              bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        student_btn.place(x=200, y=100, width=button_width, height=button_height)
        student_btn.bind("<Enter>", on_enter)
        student_btn.bind("<Leave>", on_leave)

        # Face Detector Button
        face_det_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Face Detector", font=font_style,
                              compound="top", cursor="hand2", command=self.face_recog,
                              bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        face_det_btn.place(x=450, y=100, width=button_width, height=button_height)
        face_det_btn.bind("<Enter>", on_enter)
        face_det_btn.bind("<Leave>", on_leave)

        # Attendance Button
        attendance_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Attendance", font=font_style,
                                 compound="top", cursor="hand2",
                                 bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        attendance_btn.place(x=700, y=100, width=button_width, height=button_height)
        attendance_btn.bind("<Enter>", on_enter)
        attendance_btn.bind("<Leave>", on_leave)
        
        # Help Desk Button
        help_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Help Desk", font=font_style,
                          compound="top", cursor="hand2",
                          bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        help_btn.place(x=950, y=100, width=button_width, height=button_height)
        help_btn.bind("<Enter>", on_enter)
        help_btn.bind("<Leave>", on_leave)


        # --- Row 2 Buttons ---

        # Train Data Button
        train_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Train Data", font=font_style,
                           compound="top", cursor="hand2", command=self.train_data,
                           bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        train_btn.place(x=325, y=350, width=button_width, height=button_height)
        train_btn.bind("<Enter>", on_enter)
        train_btn.bind("<Leave>", on_leave)

        # Photos Button
        photos_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Photos", font=font_style,
                            compound="top", cursor="hand2", command=self.open_photos_folder,
                            bg="white", fg="navy", relief=RAISED, bd=3, pady=5)
        photos_btn.place(x=575, y=350, width=button_width, height=button_height)
        photos_btn.bind("<Enter>", on_enter)
        photos_btn.bind("<Leave>", on_leave)
        
        # Exit Button
        exit_btn = Button(bg_img_label, image=self.photoimg_other_icon, text="Exit", font=font_style,
                          compound="top", cursor="hand2", command=self.root.destroy,
                          bg="white", fg="red", relief=RAISED, bd=3, pady=5)
        exit_btn.place(x=825, y=350, width=button_width, height=button_height)
        
        def on_enter_exit(e):
            e.widget['background'] = 'darkred'
            e.widget['foreground'] = 'white'
            e.widget['relief'] = FLAT
        def on_leave_exit(e):
            e.widget['background'] = 'white'
            e.widget['foreground'] = 'red'
            e.widget['relief'] = RAISED
        exit_btn.bind("<Enter>", on_enter_exit)
        exit_btn.bind("<Leave>", on_leave_exit)

    # ================== Function to open student window ==================
    def student_details_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Student1(self.new_window)

    # ================== Function to open photos folder ==================
    def open_photos_folder(self):
        try:
            os.startfile("data")
        except FileNotFoundError:
            messagebox.showerror("Error", "The 'data' folder was not found.")
    
    # ================== Function to open training window ==================
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recog(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
