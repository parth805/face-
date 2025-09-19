import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import os
import cv2
import mysql.connector
import numpy as np


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.running = False
        self.cap = None
        
        # ================== Top Title and Back Button Frame ==================
        top_frame = tk.Frame(self.root, bg="#0f0f23", height=45)
        top_frame.place(x=0, y=0, relwidth=1)

        title_lbl = tk.Label(top_frame, text="FACE RECOGNITION",
                             font=("times new roman", 25, "bold"),
                             bg="#0f0f23", fg="#00e5ff")
        title_lbl.pack(pady=5)
        
        # Back button
        back_btn = tk.Button(self.root, text="Back", command=self.close_window,
                             font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", relief=tk.FLAT)
        back_btn.place(x=20, y=20)
        
        def on_enter_back(e):
            e.widget['background'] = '#c0392b'
        def on_leave_back(e):
            e.widget['background'] = '#e74c3c'
            
        back_btn.bind("<Enter>", on_enter_back)
        back_btn.bind("<Leave>", on_leave_back)

        # ================== Main Container ==================
        main_container = tk.Frame(self.root, bg="#0f0f23")
        main_container.place(x=0, y=45, relwidth=1, relheight=1)

        # ================== Video Feed Frame ==================
        video_frame = tk.Frame(main_container, bg="#1c1c30", bd=2, relief=tk.RAISED)
        video_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER, width=700, height=500)
        
        self.video_label = tk.Label(video_frame, bg="white")
        self.video_label.pack(fill=tk.BOTH, expand=1)

        # ================== Button and Status Frame ==================
        control_frame = tk.Frame(main_container, bg="#0f0f23")
        control_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Progress Bar and Status Label (Optional but good practice)
        self.progress_bar = ttk.Progressbar(control_frame, orient=tk.HORIZONTAL, length=400, mode='indeterminate')
        
        self.status_label = tk.Label(control_frame, text="", font=("Arial", 12), bg="#0f0f23", fg="white")
        self.status_label.pack(pady=10)

        # Face Detector Button
        face_det_btn = tk.Button(control_frame, text="Face Detector", command=self.start_detection,
                                 font=("Arial", 16, "bold"), bg="#00e5ff", fg="#0f0f23", bd=0, relief=tk.GROOVE,
                                 activebackground="#2980b9", activeforeground="white")
        face_det_btn.pack(ipadx=20, ipady=10, pady=10)

        def on_enter_btn(e):
            e.widget['background'] = "#2980b9"
        def on_leave_btn(e):
            e.widget['background'] = "#00e5ff"

        face_det_btn.bind("<Enter>", on_enter_btn)
        face_det_btn.bind("<Leave>", on_leave_btn)

    def start_detection(self):
        if not self.running:
            self.status_label.config(text="Detection has started...")
            self.running = True
            
            try:
                self.clf = cv2.face.LBPHFaceRecognizer_create()
                self.clf.read("classifier.xml")
                self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            except cv2.error as e:
                messagebox.showerror("Error", f"OpenCV Error: {e}")
                self.status_label.config(text="Detection stopped.")
                self.running = False
                return
            
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Could not open webcam.")
                self.status_label.config(text="Detection stopped.")
                self.running = False
                return
            
            self.update_frame()

    def update_frame(self):
        if not self.running:
            return

        ret, img = self.cap.read()
        if not ret:
            self.status_label.config(text="Detection stopped.")
            self.running = False
            return

        img = self.recognize(img, self.faceCascade, self.clf)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)
        
        self.root.after(10, self.update_frame)


    def close_window(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
        self.root.destroy()

    def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        
        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int(100 * (1 - predict / 300))
            
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="##11Pappii", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)
                
                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
            
            except mysql.connector.Error:
                cv2.putText(img, "DB Error", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                
            coord = [x, y, w, h]
        
        return coord

    def recognize(self, img, faceCascade, clf):
        coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img

if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognition(root)
    root.mainloop()
