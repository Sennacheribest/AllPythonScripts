# IMPORT MODULES
import time
import random
from tkinter import *

# PREPARING THE ENVIRNOMENT
tk = Tk()
tk.title("Bounce Game - by Abu Rayyan")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

# INITIALIZING THE CANVAS
canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0)
bg = PhotoImage(
    file="/home/sennacheribest/Documents/Projects/bounce_game/base.png")
canvas.create_image(0, 0, anchor=NW, image=bg)
canvas.pack()
tk.update()

# CREATE AND INITIALIZE THE BALL CLASS AND DRAW FUNCTION
class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 390, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

# CREATE AND INITIALIZE THE PADDLE CLASS AND DRAW FUNCTION
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 151, 10, fill=color)
        self.canvas.move(self.id, 325, 450)
        self.x = 0
        self.started = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def start_game(self, evt):
        self.started = True

# CREATE AND INITIALIZE THE SCORE CLASS AND ITS FUNCTION
class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.score = 0
        self.id = self.canvas.create_text(50, 30, text="Score: " + str(self.score), fill=color, font=("Times", 15))

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text="Score: " + str(self.score))

# CREATING A NEW OBJECTS TO REPRESENT BALL, PADDLE, AND SCORE
score = Score(canvas, 'black')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, 'red')
game_over_text = canvas.create_text(395, 100, text='Game Over!', state='hidden', font=("Times", 50))

# BUILDING THE MAIN LOOP
while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
