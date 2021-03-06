from tkinter import *
import random
root = Tk()
root.geometry('800x600')
root.title('Burst the ball')
root.resizable(False,False)

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1) 

colors = ['red','orange','yellow','green','blue']

def new_ball():
    global x,y,r,ball
    canv.delete(ball)
    x = random.randrange(100,700)
    y = random.randrange(100,500)
    r = random.randrange(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = random.choice(colors), width=1)
    root.after(1000,new_ball) #время в миллисекундах и функцию, которую надо выполнить через указанное время
    
def click(event):
    global points, x, text
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = -1000
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(20,20,text=str(points), font = 'Arial 25')
 

ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(20,20,text=0,font = 'Arial 25')
points = 0
new_ball()
canv.bind('<Button-1>', click)
mainloop()
