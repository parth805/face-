from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # ================== Main Container Frame ==================
        main_container = Frame(self.root, bg="#f0f2f5")
        main_container.pack(fill=BOTH, expand=1)

        # ================== Title Label (TOP) ==================
        title_lbl = Label(main_container, text="TRAIN DATA SET",
                          font=("Helvetica", 35, "bold"),
                          bg="#333", fg="#fff")
        title_lbl.pack(pady=20, fill=X)

        # ================== Content Frame ==================
        content_frame = Frame(main_container, bg="#f0f2f5")
        content_frame.pack(expand=1, fill=BOTH, pady=20)

        # ================== Train Data Button ==================
        train_btn_frame = Frame(content_frame, bg="#f0f2f5")
        train_btn_frame.pack(expand=1)

        # Apply a modern button style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 18, "bold"), padding=10, relief="flat", background="#e74c3c", foreground="black")
        style.map("TButton", background=[('active', '#c0392b')], foreground=[('active', 'black')])

        train_btn = ttk.Button(train_btn_frame, text="TRAIN DATA", command=self.train_classifier)
        train_btn.pack(pady=50)
        
        # ================== Visuals Section (Simplified) ==================
        # This frame adds visual separation without using images
        visual_frame = Frame(content_frame, bg="#e9ecef", relief=RIDGE, bd=2)
        visual_frame.pack(pady=20, padx=50, fill=X)

        # Add some descriptive text to hint at the process
        Label(visual_frame, text="The system will now process the captured face data.",
              font=("Helvetica", 16), bg="#e9ecef").pack(pady=10)
        
        Label(visual_frame, text="This process may take a few moments...",
              font=("Helvetica", 14), bg="#e9ecef").pack(pady=5)


    # ================== Training Function ==================
    def train_classifier(self):
        data_dir = "data"
        # Check if the data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "The 'data' directory does not exist.")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        id_map = {}
        unique_id_counter = 0

        print("Starting training process...")

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Gray scale image
                imageNp = np.array(img, 'uint8')
                
                # Split the filename to get the alphanumeric ID
                parts = os.path.split(image)[1].split('.')
                student_id = parts[1]
                
                # Assign a unique integer ID to each unique alphanumeric ID
                if student_id not in id_map:
                    id_map[student_id] = unique_id_counter
                    unique_id_counter += 1
                
                current_id = id_map[student_id]

                faces.append(imageNp)
                ids.append(current_id)
                
            except (ValueError, IndexError) as e:
                print(f"Skipping file {image} due to error: {e}")
                continue
        
        print(f"Found {len(faces)} faces and {len(ids)} corresponding IDs.")
        print(f"Number of unique IDs found: {len(id_map)}")
        
        if not faces:
            messagebox.showinfo("Result", "No valid training data found. Please capture images first.", parent=self.root)
            return
            
        ids_np = np.array(ids)
        
        print("Training classifier...")
        # ================== Train the classifier And save ==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids_np)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!", parent=self.root)
        print("Training complete and classifier.xml saved.")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
