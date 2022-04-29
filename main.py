import tkinter as tk
import os
import random
from pygame import mixer

class Game:
    playing = True
    btn_clicks = 0
    tries = 0
    correct = 0
    click = 0
    last_two_img_path = []
    last_two_btn_click = []

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="#A55B53")
        self.frame.pack()
        self.buttons()
        self.leagueboard()

    def buttons(self):
        self.all_images = ["resized_images/"+path for _ in range(2) for path in os.listdir("resized_images")]
        random.shuffle(self.all_images)
      
        self.btn1 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", command=lambda: self.images(self.btn1, 0), activebackground="#DEB887")
        self.btn2 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn2, 1))
        self.btn3 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn3 ,2))
        self.btn4 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn4, 3))

        self.btn5 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn5, 4))
        self.btn6 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn6 ,5))
        self.btn7 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn7, 6))
        self.btn8 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn8, 7))

        self.btn9 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn9, 8))
        self.btn10 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn10, 9))
        self.btn11 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn11, 10))
        self.btn12 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn12, 11))

        self.btn13 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn13, 12))
        self.btn14 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn14, 13))
        self.btn15 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn15, 14))
        self.btn16 = tk.Button(self.frame, height=4, width=8, bg="#DEB887", activebackground="#DEB887", command=lambda: self.images(self.btn16, 15))

        self.btn1.grid(row=0, column=0, padx=10, pady=10)
        self.btn2.grid(row=0, column=1, padx=10, pady=10)
        self.btn3.grid(row=0, column=2, padx=10, pady=10)
        self.btn4.grid(row=0, column=3, padx=10, pady=10)

        self.btn5.grid(row=1, column=0, padx=10, pady=10)
        self.btn6.grid(row=1, column=1, padx=10, pady=10)
        self.btn7.grid(row=1, column=2, padx=10, pady=10)
        self.btn8.grid(row=1, column=3, padx=10, pady=10)

        self.btn9.grid(row=2, column=0, padx=10, pady=10)
        self.btn10.grid(row=2, column=1, padx=10, pady=10)
        self.btn11.grid(row=2, column=2, padx=10, pady=10)
        self.btn12.grid(row=2, column=3, padx=10, pady=10)

        self.btn13.grid(row=3, column=0, padx=10, pady=10)
        self.btn14.grid(row=3, column=1, padx=10, pady=10)
        self.btn15.grid(row=3, column=2, padx=10, pady=10)
        self.btn16.grid(row=3, column=3, padx=10, pady=10)

    def images(self, btn, im_pos):
        if self.playing:
            self.btn = btn
            self.im_pos = im_pos

            if self.btn["image"] == "":
                img = tk.PhotoImage(file=self.all_images[self.im_pos])
                self.btn.config(image = img, height=0, width=0)
                self.btn.image = img
                self.frame.after(150, self.player)

    def player(self):
        self.click += 1
        self.last_two_img_path.append(self.all_images[self.im_pos])
        self.last_two_btn_click.append(self.btn)

        if self.click % 2 == 0:
            self.tries += 1
            self.lbl_tries["text"] = f"Tries: {self.tries}"

            mixer.init()
            
            if self.last_two_img_path[0] == self.last_two_img_path[1]:
                self.btn_clicks += 1
             
                for btn in self.last_two_btn_click:
                    btn.config(relief=tk.RAISED, borderwidth=5)
                self.correct += 1
                self.lbl_correct["text"] = f"Correct: {self.correct}"
                mixer.music.load("sound effects\\tile_matched.wav")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                self.game_ends()
            
            else:
                self.not_same_tile()
                mixer.music.load("sound effects\\tile_didn't_matched.mp3")
                mixer.music.play()
                
            self.lbl_accurcy["text"] = f"Accuracy: {round(self.correct/self.tries * 100)}%"

            self.last_two_img_path = []
            self.click = 0
            self.last_two_btn_click = []

    def not_same_tile(self):
        for btn in self.last_two_btn_click:
            btn.config(image="", height=4, width=8)

    def leagueboard(self):
        self.lb_frame = tk.Frame(self.master, bg="#A55B53", relief=tk.SUNKEN, borderwidth=5)

        self.lbl = tk.Label(self.lb_frame, text="Leagueboard", fg="#DEB887", bg="#A55B53", font=12)
        self.lbl_tries = tk.Label(self.lb_frame, text="Tries: ", fg="#DEB887", bg="#A55B53", font=8)
        self.lbl_correct = tk.Label(self.lb_frame, text="Correct: ", fg="#DEB887", bg="#A55B53", font=8)
        self.lbl_accurcy = tk.Label(self.lb_frame, text="Accuracy: ", fg="#DEB887", bg="#A55B53", font=8)

        self.lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.lbl_tries.grid(row=1, column=0, padx=10, pady=3, sticky="w")
        self.lbl_correct.grid(row=2, column=0, padx=10, pady=3, sticky="w")
        self.lbl_accurcy.grid(row=3, column=0, padx=10, pady=3, sticky="w")

        self.lb_frame.pack(fill=tk.BOTH)

    def game_ends(self):
        if self.btn_clicks == 8:
            for btn in self.frame.winfo_children():
                btn.config(image="", height=4, width=8, borderwidth=3)
            
            # variable are based on the image name and alphabet letter
            g = tk.PhotoImage(file="resized_alphabets/g.png")
            self.btn5.config(image=g, height=0, width=0, bg="white")
            self.btn5.image = g

            a = tk.PhotoImage(file="resized_alphabets/a.png")
            self.btn6.config(image=a, height=0, width=0, bg="white")
            self.btn6.image = a

            m = tk.PhotoImage(file="resized_alphabets/m.png")
            self.btn7.config(image=m, height=0, width=0, bg="white")
            self.btn7.image = m

            e = tk.PhotoImage(file="resized_alphabets/e.png")
            self.btn8.config(image=e, height=0, width=0, bg="white")
            self.btn8.image = m

            o = tk.PhotoImage(file="resized_alphabets/o.png")
            self.btn9.config(image=o, height=0, width=0, bg="white")
            self.btn9.image = o

            v = tk.PhotoImage(file="resized_alphabets/v.png")
            self.btn10.config(image=v, height=0, width=0, bg="white")
            self.btn10.image = v

            self.btn11.config(image=e, height=0, width=0, bg="white")
            self.btn11.image = e

            r = tk.PhotoImage(file="resized_alphabets/r.png")
            self.btn12.config(image=r, height=0, width=0, bg="white")
            self.btn12.image = r
            
            for btn in self.frame.winfo_children():
                if btn["image"] == "":
                    btn.config(state=tk.DISABLED)

            self.playing = False


            self.btn_new_game = tk.Button(self.lb_frame,  bg="#A55B53", text="New Game", width=16, height=2, borderwidth=0, fg="#DEB887", font=12, command=self.new_game, activebackground="#DEB887")
            self.btn_new_game.grid(row=4, column=0, pady=20, padx=10, sticky="w")

            self.btn_end_game = tk.Button(self.lb_frame,  bg="#A55B53", text="End Game", width=16, height=2, borderwidth=0, fg="#DEB887", font=12, command=self.master.destroy, activebackground="#DEB887")
            self.btn_end_game.grid(row=4, column=1, pady=20, padx=10, sticky="w")


    def new_game(self):

            for btn in self.frame.winfo_children():
                if btn["image"] != "": btn.config(image = "", height=4, width=8, bg="#DEB887")
                
                else: btn.config(state=tk.NORMAL, height=4, width=8)
            
            self.playing = True
            self.btn_clicks = 0
            self.tries = 0
            self.correct = 0
            self.click = 0
            self.last_two_img_path = []
            self.last_two_btn_click = []

            self.lb_frame.destroy()
            self.leagueboard()
            random.shuffle(self.all_images)
    
if __name__ == "__main__":
    win = tk.Tk()
    win.resizable(width=False, height=False)
    win.title("Memory Puzzle Game")
    win.iconbitmap(r"owl.ico")
    Game(win) 
    win.mainloop()
