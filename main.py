from cgitb import reset
from tkinter import *
from tkinter import messagebox

WIDTH = 600
HEIGHT = 420

root = Tk()
root.title('tictactoe')
root.geometry("600x450")

menuFrame = Frame(root, width=600, height=420)
menuFrame.grid_propagate(0)
menuFrame.pack()

gameFrame = Frame(root)

rstFrame = Frame(root, height=30, width = 90)

menuTxt = Label(menuFrame, text="TICTACTOE", fg='black', font=('Roboto',20))
playB = Button(menuFrame, text='PLAY', font=('Helvetica', 8), height=3, width=12, bg="silver", command=lambda:playB())
quitB = Button(menuFrame, text='QUIT', font=('Helvetica', 8), height=3, width=12, bg="silver", command=lambda:exit())

menuTxt.place(x= WIDTH/2-5, y = HEIGHT/4, anchor="center")
playB.place(x = WIDTH/2-53, y = HEIGHT/2)
quitB.place(x = WIDTH/2-53, y = HEIGHT/1.5)


b1 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b1))
b2 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b2))
b3 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b3))

b4 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b4))
b5 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b5))
b6 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b6))

b7 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b7))
b8 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b8))
b9 = Button(gameFrame, text=' ', font=('Helvetica', 20), height=3, width=6, bg="silver", command=lambda: b_click(b9))

restB = Button(rstFrame, text='RESTART', font=('Helvetica', 8), height=3, width=12, bg="silver", command=lambda:restartB())

restB.pack()

#Grid the buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#X starts so true
clicked = True
count = 0
buttons_l = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

def playB():
    global count, clicked
    clicked = True
    count = 0
    
    menuFrame.pack_forget()
    gameFrame.pack(pady=30)
    rstFrame.pack(anchor=S)
    
    for i in buttons_l:
        i.config(text=' ', state=NORMAL)

#Deactivate all buttons after a win or a draw
def disable_buttons():
    for i in buttons_l:
        i.config(state=DISABLED)

#Button clicked
def b_click(b):  # sourcery skip: extract-duplicate-method
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkwin(b)
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwin(b)
    else:
        messagebox.showerror("tictactoe", "Already selected\nPick another one")

#Check to see if someone won
def checkwin(b):  # sourcery skip: extract-duplicate-method
    global count
    
    #for i in buttons_l:
        #if i["text"] == (i+1)["text"] and (i+3)["text"]:
            #messagebox.showinfo('tictactoe', f'{i["text"]} a gagné !')
    
    if b1["text"] == b2["text"] == b3["text"] and (b1["text"] and b2["text"] and b3["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b1["text"]} a gagné !')
        #b1.configure(bg='#303596')
    elif b4["text"] == b5["text"] == b6["text"] and (b4["text"] and b5["text"] and b6["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b4["text"]} a gagné !')
    elif b1["text"] == b4["text"] == b7["text"] and (b1["text"] and b4["text"] and b7["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b1["text"]} a gagné !')
    elif b2["text"] == b5["text"] == b8["text"] and (b2["text"] and b5["text"] and b8["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b2["text"]} a gagné !')
    elif b3["text"] == b6["text"] == b9["text"] and (b3["text"] and b6["text"] and b9["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b3["text"]} a gagné !')
    elif b7["text"] == b8["text"] == b9["text"] and (b7["text"] and b8["text"] and b9["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b7["text"]} a gagné !')
    elif b1["text"] == b5["text"] == b9["text"] and (b1["text"] and b5["text"] and b9["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b1["text"]} a gagné !')
    elif b3["text"] == b5["text"] == b7["text"] and (b3["text"] and b5["text"] and b7["text"] != ' '):
        disable_buttons()
        messagebox.showinfo('tictactoe', f'{b3["text"]} a gagné !')
    elif count == 9:
        messagebox.showinfo("tictactoe", "Aucun gagnant")
        disable_buttons()

#Restart Button
def restartB():
    disable_buttons()
    gameFrame.pack_forget()
    rstFrame.pack_forget()
    menuFrame.pack()


root.mainloop()