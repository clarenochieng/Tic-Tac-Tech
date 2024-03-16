from tkinter import *


def render_board(board):
    global display, button00, button01, button02, button10, button11, button12, button20, button21, button22

    display = Tk()
    display.title('Tic-Tac-Toe')
    display.resizable(False, False)

    button00 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button01 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button02 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)

    button10 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button11 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button12 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)

    button20 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button21 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)
    button22 = Button(display, text="", font=("Helvetica", 22), width=6, height=3)

    button00.grid(row=0, column=0)
    button01.grid(row=0, column=1)
    button02.grid(row=0, column=2)

    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)

    button20.grid(row=2, column=0)
    button21.grid(row=2, column=1)
    button22.grid(row=2, column=2)

    button00.config(text=board[0][0], bg="SystemButtonFace")
    button01.config(text=board[0][1], bg="SystemButtonFace")
    button02.config(text=board[0][2], bg="SystemButtonFace")

    button10.config(text=board[1][0], bg="SystemButtonFace")
    button11.config(text=board[1][1], bg="SystemButtonFace")
    button12.config(text=board[1][2], bg="SystemButtonFace")

    button20.config(text=board[2][0], bg="SystemButtonFace")
    button21.config(text=board[2][1], bg="SystemButtonFace")
    button22.config(text=board[2][2], bg="SystemButtonFace")

    display.mainloop()
