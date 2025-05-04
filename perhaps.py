import tkinter as tk
from PIL import Image, ImageTk
class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Learning App")
        self.root.geometry("800x600")
        self.mode = "light"  # dark mode

        self.bg_color = "#f0f0f0"
        self.text_color = "#000000"

        self.make_main_menu()

    def toggle_mode(self):
        # light mode and dark mode
        if self.mode == "light":
            self.mode = "dark"
            self.bg_color = "#222222"
            self.text_color = "#ffffff"
        else:
            self.mode = "light"
            self.bg_color = "#f0f0f0"
            self.text_color = "#000000"
        self.make_main_menu()

    def make_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root, bg=self.bg_color, width=800, height=600)
        self.canvas.pack()

        try:
            # background
            self.bg_img = Image.open("triangle_bg.png")
            self.bg_img = self.bg_img.resize((800, 600))
            self.bg = ImageTk.PhotoImage(self.bg_img)
            self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        except:
            self.canvas.create_text(400, 50, text="TRIANGLES!", fill=self.text_color, font=("Arial", 30, "bold"))

        # buttons
        btn1 = tk.Button(self.root, text="Tutorial", command=self.show_tutorial)
        btn2 = tk.Button(self.root, text="Quiz", command=self.show_quiz)
        btn3 = tk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_mode)

        self.canvas.create_window(400, 200, window=btn1)
        self.canvas.create_window(400, 260, window=btn2)
        self.canvas.create_window(400, 320, window=btn3)

    def show_tutorial(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, bg=self.bg_color)
        scroll_y = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas, bg=self.bg_color)

        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        tk.Label(frame, text="Triangle Tutorial", font=("Arial", 18, "bold"), fg=self.text_color, bg=self.bg_color).pack(pady=10)

        lessons = [
            ("Equilateral", "All 3 sides and angles are equal"),
            ("Isosceles", "2 sides and 2 angles are equal"),
            ("Scalene", "All sides are different"),
            ("Right", "Has one 90° angle"),
            ("Acute", "All angles < 90°"),
            ("Obtuse", "One angle > 90°")
        ]

        for title, desc in lessons:
            box = tk.Frame(frame, bg=self.bg_color, pady=10)
            box.pack(fill="x", padx=20)
            tk.Label(box, text=title, font=("Arial", 14, "bold"), fg=self.text_color, bg=self.bg_color).pack(anchor="w")
            tk.Label(box, text=desc, fg=self.text_color, bg=self.bg_color).pack(anchor="w")

        tk.Button(frame, text="Back", command=self.make_main_menu).pack(pady=20)

    def show_quiz(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.quiz_frame = tk.Frame(self.root, bg=self.bg_color)
        self.quiz_frame.pack(fill="both", expand=True)

        self.questions = [
            {"q": "What triangle has all sides equal?", "options": ["Scalene", "Right", "Equilateral", "Isosceles"], "a": "Equilateral"},
            {"q": "Triangle with one 90° angle?", "options": ["Right", "Obtuse", "Acute", "Scalene"], "a": "Right"},
            {"q": "How many equal sides does isosceles have?", "options": ["1", "2", "3", "0"], "a": "2"},
            {"q": "Triangle with all angles < 90°?", "options": ["Right", "Obtuse", "Acute", "Equilateral"], "a": "Acute"}
        ]
        self.q_index = 0
        self.score = 0

        self.show_question()

    def show_question(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        q = self.questions[self.q_index]
        tk.Label(self.quiz_frame, text=q["q"], font=("Arial", 14), bg=self.bg_color, fg=self.text_color).pack(pady=20)

        for opt in q["options"]:
            tk.Button(self.quiz_frame, text=opt, width=20,
                      command=lambda opt=opt: self.check_answer(opt)).pack(pady=5)

        tk.Label(self.quiz_frame, text=f"Score: {self.score}/{len(self.questions)}",
                 bg=self.bg_color, fg=self.text_color).pack(pady=10)

    def check_answer(self, choice):
        correct = self.questions[self.q_index]["a"]
        if choice == correct:
            self.score += 1
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        tk.Label(self.quiz_frame, text=f"You're done!\nFinal Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 16), bg=self.bg_color, fg=self.text_color).pack(pady=50)
        tk.Button(self.quiz_frame, text="Back to Menu", command=self.make_main_menu).pack()

# run
if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()
