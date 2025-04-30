import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import os

class TriangleLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Types of Triangles Learning App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load the background image (replace with your image file)
        try:
            self.bg_image = Image.open("triangle_bg.png")  # Change to your image filename
            self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        except Exception as e:
            print(f"Error loading background image: {e}")
            # Fallback solid color background
            self.bg_photo = None
            self.canvas = tk.Canvas(root, bg="#f0f8ff", width=800, height=600)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_text(400, 50, text="Types of Triangles", 
                                 font=("Arial", 24, "bold"), fill="navy")
            self.canvas.create_text(400, 550, text="TAFHEEM MUHAMMAD", 
                                 font=("Arial", 12), fill="black")
        else:
            self.canvas = tk.Canvas(root, width=800, height=600)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Custom style for buttons
        button_style = {
            "font": ("Arial", 16, "bold"),
            "borderwidth": 2,
            "relief": "raised",
            "width": 12,
            "height": 1,
            "activebackground": "#555555"
        }
        
        # Create transparent buttons (position these based on your image)
        self.quiz_btn = tk.Button(root, text="QUIZ", 
                                 bg="#4CAF50", fg="white",
                                 command=self.open_quiz, **button_style)
        self.quiz_btn_window = self.canvas.create_window(200, 400, anchor="center", window=self.quiz_btn)
        
        self.tutorial_btn = tk.Button(root, text="TUTORIAL", 
                                    bg="#2196F3", fg="white",
                                    command=self.open_tutorial, **button_style)
        self.tutorial_btn_window = self.canvas.create_window(600, 400, anchor="center", window=self.tutorial_btn)
        
        # Bind escape key to close windows
        self.root.bind("<Escape>", lambda e: self.root.destroy())
    
    def open_quiz(self):
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Triangles Quiz")
        quiz_window.geometry("600x500")
        quiz_window.resizable(False, False)
        
        # Quiz frame
        quiz_frame = tk.Frame(quiz_window, padx=20, pady=20)
        quiz_frame.pack(fill="both", expand=True)
        
        # Quiz title
        tk.Label(quiz_frame, text="Triangles Quiz", 
                font=("Arial", 20, "bold"), fg="navy").pack(pady=10)
        
        # Quiz questions
        questions = [
            {
                "question": "What type of triangle has all sides equal?",
                "options": ["Equilateral", "Isosceles", "Scalene", "Right"],
                "answer": "Equilateral"
            },
            {
                "question": "Which triangle has one 90° angle?",
                "options": ["Acute", "Obtuse", "Right", "Equilateral"],
                "answer": "Right"
            },
            {
                "question": "How many equal sides does an isosceles triangle have?",
                "options": ["0", "1", "2", "3"],
                "answer": "2"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(quiz_frame, text=questions[self.current_question]["question"],
                                     font=("Arial", 14), wraplength=500, justify="center")
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(quiz_frame, text=questions[self.current_question]["options"][i],
                          font=("Arial", 12), width=20,
                          command=lambda idx=i: self.check_answer(questions[self.current_question]["options"][idx], 
                          questions[self.current_question]["answer"], quiz_window, questions))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.score_label = tk.Label(quiz_frame, text=f"Score: {self.score}/{len(questions)}",
                                 font=("Arial", 12))
        self.score_label.pack(pady=10)
    
    def check_answer(self, selected, correct, window, questions):
        if selected == correct:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/{len(questions)}")
        
        self.current_question += 1
        if self.current_question < len(questions):
            self.question_label.config(text=questions[self.current_question]["question"])
            for i in range(4):
                self.option_buttons[i].config(text=questions[self.current_question]["options"][i],
                                            command=lambda idx=i: self.check_answer(
                                                questions[self.current_question]["options"][idx],
                                                questions[self.current_question]["answer"],
                                                window, questions))
        else:
            result = f"Quiz Completed!\nFinal Score: {self.score}/{len(questions)}"
            for widget in window.winfo_children():
                widget.destroy()
            tk.Label(window, text=result, font=("Arial", 16)).pack(pady=50)
            tk.Button(window, text="Close", command=window.destroy).pack()
    
    def open_tutorial(self):
        tutorial_window = tk.Toplevel(self.root)
        tutorial_window.title("Triangles Tutorial")
        tutorial_window.geometry("700x600")
        tutorial_window.resizable(False, False)
        
        # Tutorial frame with scrollbar
        main_frame = tk.Frame(tutorial_window)
        main_frame.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(main_frame)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Tutorial content
        tk.Label(scrollable_frame, text="Types of Triangles Tutorial", 
                font=("Arial", 20, "bold"), fg="navy").pack(pady=20)
        
        content = [
            ("Equilateral Triangle", "All three sides are equal\nAll three angles are 60°"),
            ("Isosceles Triangle", "Two sides are equal\nTwo angles are equal"),
            ("Scalene Triangle", "All sides are different\nAll angles are different"),
            ("Right Triangle", "One angle is exactly 90°\nFollows Pythagorean theorem"),
            ("Acute Triangle", "All angles are less than 90°"),
            ("Obtuse Triangle", "One angle is greater than 90°")
        ]
        
        for title, description in content:
            frame = tk.Frame(scrollable_frame, bd=2, relief="groove", padx=10, pady=10)
            frame.pack(fill="x", padx=20, pady=10)
            
            tk.Label(frame, text=title, font=("Arial", 16, "bold"), fg="#333333").pack(anchor="w")
            tk.Label(frame, text=description, font=("Arial", 12), justify="left").pack(anchor="w", pady=5)
        
        tk.Button(scrollable_frame, text="Close Tutorial", command=tutorial_window.destroy,
                font=("Arial", 12), bg="#ff4444", fg="white").pack(pady=20)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleLearningApp(root)
    
    # Instructions if image not found
    if app.bg_photo is None:
        print("\nIMPORTANT: To use your custom background:")
        print("1. Convert the first page of your PDF to an image (PNG/JPEG)")
        print("2. Save it as 'triangle_bg.png' in the same folder as this script")
        print("3. Run the program again\n")
    
    root.mainloop()
