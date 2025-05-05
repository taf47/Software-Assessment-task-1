import tkinter as tk
from PIL import Image, ImageTk

class TriangleFunApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Shapes Fun App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        self.is_dark = False
        self.colors = {
            'light': {
                'bg': "#f0f8ff",
                'text': "navy",
                'button1': "#4CAF50",
                'button2': "#2196F3",
                'content_bg': "white",
                'frame_bg': "#f9f9f9",
                'symbol_fg': "black"
            },
            'dark': {
                'bg': "#2d2d2d",
                'text': "#add8e6",
                'button1': "#ff66b2",
                'button2': "#bb86fc",
                'content_bg': "#424242",
                'frame_bg': "#535353",
                'symbol_fg': "white"
            }
        }

        try:
            self.bg_pic = Image.open("triangle_bg.png")
            self.bg_pic = self.bg_pic.resize((800, 600), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_pic)
        except:
            self.bg_photo = None

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg=self.colors['light']['bg'])
        self.canvas.pack(fill="both", expand=True)

        if self.bg_photo:
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        else:
            self.title_id = self.canvas.create_text(400, 50, text="Types of Triangles",
                                    font=("Arial", 24, "bold"), fill=self.colors['light']['text'])
            self.name_id = self.canvas.create_text(400, 550, text="TAFHEEM MUHAMMAD",
                                    font=("Arial", 12), fill=self.colors['light']['text'])

        btn_style = {
            "font": ("Arial", 16, "bold"),
            "width": 12,
            "height": 1,
            "borderwidth": 2,
            "relief": "raised",
            "activebackground": "#555555"
        }

        self.quiz_btn = tk.Button(self.root, text="QUIZ", command=self.show_quiz,
                                  bg=self.colors['light']['button1'], fg="white", **btn_style)
        self.canvas.create_window(200, 400, anchor="center", window=self.quiz_btn)

        self.tut_btn = tk.Button(self.root, text="TUTORIAL", command=self.show_tutorial,
                                 bg=self.colors['light']['button2'], fg="white", **btn_style)
        self.canvas.create_window(600, 400, anchor="center", window=self.tut_btn)

        self.moon_btn = tk.Button(self.root, text="☀️🌙", command=self.flip_mode,
                                 font=("Arial", 12), bd=0, bg=self.colors['light']['bg'],
                                 fg=self.colors['light']['symbol_fg'], activeforeground=self.colors['light']['symbol_fg'])
        self.canvas.create_window(750, 30, anchor="center", window=self.moon_btn)

        self.fun_area = None
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def flip_mode(self):
        self.is_dark = not self.is_dark
        mode = 'dark' if self.is_dark else 'light'
        
        self.canvas.config(bg=self.colors[mode]['bg'])
        self.moon_btn.config(text="😴" if self.is_dark else "👻", 
                            bg=self.colors[mode]['bg'],
                            fg=self.colors[mode]['symbol_fg'],
                            activeforeground=self.colors[mode]['symbol_fg'])
        
        self.quiz_btn.config(bg=self.colors[mode]['button1'])
        self.tut_btn.config(bg=self.colors[mode]['button2'])

        if self.fun_area:
            if hasattr(self, 'q_label'): 
                self.q_label.config(bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text'])
                self.score_label.config(bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text'])
                for btn in self.option_buttons:
                    btn.config(bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text'])
            self.fun_area.config(bg=self.colors[mode]['content_bg'])

        if self.bg_photo is None:
            self.canvas.itemconfig(self.title_id, fill=self.colors[mode]['text'])
            self.canvas.itemconfig(self.name_id, fill=self.colors[mode]['text'])

    def bye_fun_area(self):
        if self.fun_area:
            self.fun_area.destroy()
            self.fun_area = None

    def show_quiz(self):
        self.bye_fun_area()
        mode = 'dark' if self.is_dark else 'light'
        
        self.fun_area = tk.Frame(self.root, bg=self.colors[mode]['content_bg'], bd=2)
        self.fun_area.place(x=0, y=0, width=800, height=600)

        tk.Label(self.fun_area, text="Triangles Quiz", font=("Arial", 20, "bold"),
                 fg=self.colors[mode]['text'], bg=self.colors[mode]['content_bg']).pack(pady=10)

        self.questions = [
            {"question": "What type of triangle has all sides equal?",
             "options": ["Equilateral", "Isosceles", "Scalene", "Right"], "answer": "Equilateral"},
            {"question": "Which triangle has one 90° angle?",
             "options": ["Acute", "Obtuse", "Right", "Equilateral"], "answer": "Right"},
            {"question": "How many equal sides does an isosceles triangle have?",
             "options": ["0", "1", "2", "3"], "answer": "2"},
            {"question": "What is true about a scalene triangle?",
             "options": ["All sides equal", "Two equal sides", "All sides different", "One 90° angle"], "answer": "All sides different"},
            {"question": "Which triangle has one angle bigger than 90°?",
             "options": ["Right", "Acute", "Equilateral", "Obtuse"], "answer": "Obtuse"}
        ]
        self.now_q = 0
        self.points = 0

        self.q_label = tk.Label(self.fun_area, text="", font=("Arial", 14),
                                wraplength=600, bg=self.colors[mode]['content_bg'], 
                                fg=self.colors[mode]['text'], justify="center")
        self.q_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.fun_area, font=("Arial", 12), width=30,
                           bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text'])
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.score_label = tk.Label(self.fun_area, text=f"Score: 0/{len(self.questions)}",
                                    font=("Arial", 12), bg=self.colors[mode]['content_bg'],
                                    fg=self.colors[mode]['text'])
        self.score_label.pack(pady=10)

        tk.Button(self.fun_area, text="Back", command=self.bye_fun_area,
                 bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text']).pack(pady=10)

        self.next_question()

    def next_question(self):
        q = self.questions[self.now_q]
        self.q_label.config(text=q["question"])
        for i in range(4):
            self.option_buttons[i].config(
                text=q["options"][i],
                command=lambda idx=i: self.check_answer(q["options"][idx], q["answer"])
            )

    def check_answer(self, picked, correct):
        if picked == correct:
            self.points += 1
        self.score_label.config(text=f"Score: {self.points}/{len(self.questions)}")
        self.now_q += 1
        if self.now_q < len(self.questions):
            self.next_question()
        else:
            for thing in self.fun_area.winfo_children():
                thing.destroy()
            mode = 'dark' if self.is_dark else 'light'
            tk.Label(self.fun_area, text=f"Nice! All Done\nFinal Score: {self.points}/{len(self.questions)}",
                     font=("Arial", 16), bg=self.colors[mode]['content_bg'],
                     fg=self.colors[mode]['text']).pack(pady=50)
            tk.Button(self.fun_area, text="Back", command=self.bye_fun_area,
                     bg=self.colors[mode]['content_bg'], fg=self.colors[mode]['text']).pack()

    def show_tutorial(self):
        self.bye_fun_area()
        mode = 'dark' if self.is_dark else 'light'
        
        self.fun_area = tk.Frame(self.root, bg=self.colors[mode]['content_bg'])
        self.fun_area.place(x=0, y=0, width=800, height=600)

        canvas = tk.Canvas(self.fun_area, bg=self.colors[mode]['content_bg'], highlightthickness=0)
        scroll = tk.Scrollbar(self.fun_area, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)

        scroll.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        scroll_frame = tk.Frame(canvas, bg=self.colors[mode]['content_bg'])
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        def zoomy(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", zoomy)
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units")) 

        tk.Label(scroll_frame, text="Triangle Fun Tutorial", font=("Arial", 24, "bold"),
                 fg=self.colors[mode]['text'], bg=self.colors[mode]['content_bg']).grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        lessons = [
            ("Equilateral Triangle", "All three sides same\nAll three angles 60°"),
            ("Isosceles Triangle", "Two sides same\nTwo angles same"),
            ("Scalene Triangle", "All sides different\nAll angles different"),
            ("Right Triangle", "One angle 90°\nFollows Pythagorean thingy"),
            ("Acute Triangle", "All angles less than 90°"),
            ("Obtuse Triangle", "One angle bigger than 90°")
        ]

        for i, (name, about) in enumerate(lessons, start=1):
            frame = tk.Frame(scroll_frame, bg=self.colors[mode]['frame_bg'], bd=2, relief="groove", padx=15, pady=10)
            frame.grid(row=i, column=0, padx=30, pady=10, sticky="we")
            tk.Label(frame, text=name, font=("Arial", 18, "bold"),
                     fg=self.colors[mode]['text'], bg=self.colors[mode]['frame_bg']).pack(anchor="w")
            tk.Label(frame, text=about, font=("Arial", 14),
                     fg=self.colors[mode]['text'], bg=self.colors[mode]['frame_bg'], justify="left", wraplength=500).pack(anchor="w")

        try:
            tri_pic = Image.open("classification.of.triangles.png")
            tri_pic = tri_pic.resize((360, 500), Image.LANCZOS)
            tri_photo = ImageTk.PhotoImage(tri_pic)
            img_label = tk.Label(scroll_frame, image=tri_photo, bg=self.colors[mode]['content_bg'])
            img_label.image = tri_photo 
            img_label.grid(row=1, column=1, rowspan=6, padx=20, pady=20, sticky="n")
        except Exception as e:
            print("Picure didn’t load:", e)

        back_btn = tk.Button(scroll_frame, text="Back", command=self.bye_fun_area,
                             font=("Arial", 14, "bold"), width=12,
                             bg=self.colors[mode]['button1'], fg="white", bd=2, relief="raised",
                             activebackground="#555555")
        back_btn.grid(row=7, column=0, pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleFunApp(root)

    if app.bg_photo is None:
        print("\nHi! If you wanna see a background pic:")
        print("1. Save a pic as 'triangle_bg.png'")
        print("2. Put it next to this file\n")

    root.mainloop()