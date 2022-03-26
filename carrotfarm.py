from tkinter import *
import tkinter as tk
import threading

### 게임 화면

game = Tk()
game.title("Carrot Farm")
game.geometry("500x650")

### 중요 변수

poInt = int(0)
carrotRobot = int(0)

### 윗 프레임

frame = Frame(game, bd = 5, bg = 'white', height = 30)
frame.pack(fill = "both")

top_frame = Frame(game, bg = 'white')
top_frame.pack()

top_lbl = Label(top_frame, text="Carrot Farm",bg = 'white')
top_lbl.pack(side=LEFT)

### 가운데 사진, 당근 갯수

mid_frame= Frame(game, bg = 'light grey')
mid_frame.pack()

canvas = Canvas(mid_frame, width = 300, height = 200)
canvas.pack()
img = PhotoImage(file = "carrot.png")
canvas.create_image(0,0, anchor = NW, image = img)

carrot_lbl = Label(mid_frame, bd=5,bg = 'light grey', text= poInt)
carrot_lbl.pack()

### 당근 추가

def PlusOnePoint():    
    global poInt
    poInt = poInt +1
    carrot_lbl.config(text= str(poInt))

#game.bind('<space>',PlusOnePoint)

### 하단 프레임

down_frame = Frame(game, bd = 40, bg = 'light grey')

down_btn = Button(down_frame, text="Pick Carrot", command = lambda:PlusOnePoint())  
down_frame.pack(expand = True, fill = "both")   

down_btn.pack(ipadx = 10, ipady = 10)

### 당근 로봇 관련 프레임

robot_frame = Frame(down_frame, bd = 20)
robot_frame.pack()

robot_lbl = Label(robot_frame, text = "0 robots")
robot_lbl.pack()

robot_btn = Button(robot_frame, text = "Robot Price:10", command = lambda:PlusCarrotRobot())
robot_btn.pack(side = LEFT)

### 로봇 추가 


def PlusCarrotRobot():
    global poInt, carrotRobot
    if (poInt >=0): 
        if (carrotRobot ==0 and poInt >=10):
            carrotRobot +=1
            poInt = poInt - 10
            robot_lbl.config(text = str(carrotRobot))
            robot_btn.config(text = str("Robot Price:20"))
            carrot_lbl.config(text = str(poInt))
        elif( carrotRobot >= 1 and poInt >= 10 * (carrotRobot+1)):
            carrotRobot +=1
            poInt = poInt - (10*carrotRobot)
            robot_lbl.config(text = str(carrotRobot))
            carrot_lbl.config(text = str(poInt))
            robot_btn["text"] = 'Robot Price:' ,10*(carrotRobot+1)
        else:
            pass
    else:
        pass

#game.bind('<r>', PlusCarrotRobot)s

### 로봇 당근 뽑는 중

def robotWorking():
    global poInt
    poInt = poInt + carrotRobot * 5
    carrot_lbl.config(text = str(poInt))
    threading.Timer(3,robotWorking).start()

robotWorking()

###

game.mainloop() 




