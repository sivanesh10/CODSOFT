from tkinter import *
from PIL import ImageTk,Image
import random 

def intro_window() :
    global intro
    intro = Tk()
    intro.geometry("500x300")
    intro.title('Intro')
    intro.configure(background="orange")
    # gui like button entry ext...for fist window!
    label_1 = Label(intro,text="Lets Play the Game!!",foreground="RED",font=('Algerian', 25),justify="center")
    label_1.place(x=70 ,y=100)
    button_1 = Button(intro,text="Ready",width=10,height=2,command=lambda:game_window())
    button_1.configure(background="pink",font=('Times', 10, 'bold'))
    button_1.place(x=290,y=170)
    button_2 = Button(intro,text="Exit",width=10,height=2,command=lambda: exit_window())
    button_2.configure(background="pink",font=('Times', 10, 'bold'))
    button_2.place(x=110,y=170)
    intro.mainloop()

def game_window():
    exit_window()
    global game
    game = Tk()
    game.geometry("800x800")
    game.title('Rock Paper Scissor')
    game.configure(background="pink")

    #importing image
    img_r = Image.open('rock.jpg')
    img_r2 = Image.open('rock_flip.jpg')
    img_d = Image.open('default.jpg')
    img_d2 = Image.open('default_flip.jpg')
    img_s = Image.open('scissor.jpg')
    img_s2 = Image.open('scissor_flip.jpg')
    img_sel = Image.open('selection.jpg')
    img_p = Image.open('paper.jpg')
    img_p2 = Image.open('paper_flip.jpg')

    #resize the image
    img_r = img_r.resize((300,300))
    img_p = img_p.resize((300,300))
    img_s = img_s.resize((300,300))
    img_d = img_d.resize((300,300))
    img_r2 = img_r2.resize((300,300))
    img_p2 = img_p2.resize((300,300))
    img_s2 = img_s2.resize((300,300))
    img_d2 = img_d2.resize((300,300))
    img_sel = img_sel.resize((562,132))


    #creating image for player
    global img_default_p, rock_p, paper_p, scissor_p
	
    img_default_p = ImageTk.PhotoImage(img_d)
    rock_p = ImageTk.PhotoImage(img_r)
    paper_p = ImageTk.PhotoImage(img_p)      
    scissor_p = ImageTk.PhotoImage(img_s)

    #creating image for computer
    global img_default_c,rock_c, paper_c , scissor_c
	
    img_default_c = ImageTk.PhotoImage(img_d2)
    rock_c = ImageTk.PhotoImage(img_r2)
    paper_c = ImageTk.PhotoImage(img_p2)
    scissor_c  = ImageTk.PhotoImage(img_s2)

    #image selection
    selection_img  = ImageTk.PhotoImage(img_sel)

    #label for player vs computer
    p_label = Label(game,text='PLAYER',font=('Algerian', 20),background="pink")
    c_label = Label(game,text='COMPUTER',font=('Algerian', 20),background="pink")
    p_label.place(x=140,y=30)
    c_label.place(x=580,y=30)


    #buttons
    button_1 = Button(game,text='Exit',foreground="red",width=10,height=2, font=('Times', 10, 'bold'),command=lambda:clear())
    button_1.place(x=360,y=300)
    button_2 = Button(game,text='Rock',foreground="red",width=7, font=('Times', 10, 'bold'),command=lambda :game_fun(1))
    button_3 = Button(game,text='Paper',foreground="red",width=7, font=('Times', 10, 'bold'),command=lambda:game_fun(2))
    button_4 = Button(game,text='Scissor',foreground="red",width=7, font=('Times', 10, 'bold'),command=lambda:game_fun(3))
    button_2.place(x=180,y=600)
    button_3.place(x=380,y=600)
    button_4.place(x=580,y=600)

    #label for selection
    label_default = Label(game,image=selection_img)
    label_default.place(x=131,y=450)



    #printing images
    label_p = Label(game,image=img_default_p)
    label_c = Label(game,image=img_default_c)
    label_p.place(x=20,y=90)
    label_c.place(x=475,y=90)
    game.mainloop()

def game_fun(player):
	
    select = [1, 2, 3]
    computer = random.choice(select)
    global res_frame
    if player == 1:
        label_r = Label(game, image=rock_p)
        label_r.place(x=20, y=90)
    elif player == 2:
        label_p = Label(game, image=paper_p)
        label_p.place(x=20, y=90)
    else:
        label_s = Label(game, image=scissor_p)
        label_s.place(x=20, y=90)

    if computer == 1:
        label_c = Label(game, image=rock_c)
        label_c.place(x=475, y=90)
    elif computer == 2:
        label_c = Label(game, image=paper_c)
        label_c.place(x=475, y=90)
    else:
        label_c = Label(game, image=scissor_c)
        label_c.place(x=475, y=90)

    if player == computer:
        res = '   Draw    '
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        res = 'You won!!!'
    else:
        res = 'Comp won!!'
    res_frame = Label(game,background='white',font=('Algerian', 20),justify='center')
    res_frame.place(x=260,y=650)
    res_frame.config(text= 'Result:- ' + res)
 
def clear():
    game.destroy()


def exit_window():
    intro.destroy()    




if __name__ == "__main__":
    intro_window()