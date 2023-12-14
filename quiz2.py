import json
import tkinter
from tkinter import *
import random

root = tkinter.Tk()
root.title("Python Quiz")
root.geometry("700x780")
root.config(background="#ffffff")
root.resizable(0,0)


# questions = [                    #storing the questions
#     "What is output for this program ?\nx = 10 ,y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoifh\noewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoifhoe\nwirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoif\nhoewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoifh\noewirhirioajlkrhilaehrira",
#     "What is output for this program ?\nx = 10, y = x\nprint(y+x+1)hhhffjjjjueueuwrhehjsdhfkhdsikhoi\nfhoewirhirioajlkrhilaehrira",
# ]

# answers_choice =[        #options list for questions
#     ["20","11","21","10",],
#     ["Akeke","input","gets","D",],
#     ["Aehwwkhk","B","C","D",],
#     ["Turbo C","Py Interpreter","C","D",],
#     ["Ahakakqwn","B","C","D",],
#     ["Akqwhjjqrk","B","C","D",],
#     ["Akknwknk","B","C","D",],
#     ["Akqwkkwrnkkkr","B","C","D",],
#     ["Ajwrjjb","B","C","D",],
#     ["Akkwrkhu","B","C","global",],
# ]

# load questions and answer choices from json file instead of the file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,1,1,1,3,1,0,1,3,3]    #storing the answers for result
user_answer=[]     #for storing the ans of user and then finally calc score of user

indexes=[]     #funtion for questions that asked to user using a gen function
def genRandomQues():     # function for generating random questions for user and store it into the indexes list
    global indexes
    while(len(indexes)<5):
        x = random.randint(0,9)
        if x in indexes:
            continue      #this is for we dont want to repeat the ques. hence we skip duplicate ques. and store only unique ques.
        else:
            indexes.append(x)

print(indexes)

def calcScore():
    # lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    global indexes,user_answer,answers
    x=0
    global score
    score=0
    for i in indexes:
        if user_answer[x]==answers[i]:
            score+=1
            x += 1
    print(score)
    scor=str(score)
    lblQuestion.config(width=25,height=4,text="Your final Score is: "+scor ,font=("Arial Rounded MT Bold",20),)
    showResult(score)
    
def showResult(score):
    global End
    End = Button(
        frame,
        text="End",
        width=10,
        font=("Arial Rounded MT Bold",20),
        background="#ffffff",
        fg='blue',
        command=quizEnd,
        )
    End.place(x=250,y=700)

   
    
def quizEnd():
    End.destroy()
    lblQuestion.destroy()
    frame.destroy()
    labelimage=Label(
        root,
        width=500,
        height=300,
        background="#ffffff"
    )
    labelimage.place(x=105,y=150)

    labelresulttext = Label(
        root,
        font=("Arial Rounded MT Bold",20),
        background="#ffffff",
        fg='blue'
        )
    labelresulttext.place(x=80,y=450)


    if score>=9:
        img = PhotoImage(file="images/great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are excellent!!!")
    elif (score>4 and score<9):
        img = PhotoImage(file="images/better.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="   You are good but You can do better!!!")
    else:
        img = PhotoImage(file="images/bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should to learn more about Python!!!")

ques=1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    global indexes,user_answer,answers
    x = radiovar.get()
    user_answer.append(x)
    print(user_answer)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])   #upfate the ques.
        r1['text']=answers_choice[indexes[ques]][0]
        r2['text']=answers_choice[indexes[ques]][1]
        r3['text']=answers_choice[indexes[ques]][2]
        r4['text']=answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calcScore()

    
def startIspressed():          #when start button is pressed then we will disappear all content 
    backgroundimage.configure(file="images/quiz1.png")
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    genRandomQues()
    startQuiz()

def startQuiz():         #start the quiz
    global lblQuestion,r1,r2,r3,r4   #global beacuse we change questions outside function
    lblQuestion=Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas",15,"bold"),
        background="#ff7f27",
        width=40,
        height=5,
        wraplength = 400,
        # relief="flat",
        # justify="center" ,
        # wraplength=300,   #5because Ques length is different then when there is que.more that width 400 it will come on next line
    )
    lblQuestion.place(x=125,y=90)

#RADIO BUTTONS 
    global radiovar  
    radiovar = IntVar()
    radiovar.set(-1)  #-1 because no button is checked by default


    r1 = Radiobutton(
        frame,
        text=answers_choice[indexes[0]][0],     #00002f
        width=14,
        height=1,
        background="#00002f",
        foreground="#04c9fc",
        font=("Arial Rounded MT Bold",14),
        value=0,
        variable=radiovar,
        command=selected,
    )
    r1.place(x=158,y=279)

    r2 = Radiobutton(
        frame,
        text=answers_choice[indexes[0]][1],     #00002f
        width=14,
        height=1,
        background="#00002f",
        foreground="#04c9fc",
        font=("Arial Rounded MT Bold",14),
        value=1,
        variable=radiovar,
        command=selected,
    )
    r2.place(x=158,y=356)

    r3 = Radiobutton(
        frame,
        text=answers_choice[indexes[0]][2],     #00002f
        width=14,
        height=1,
        background="#00002f",
        foreground="#04c9fc",
        font=("Arial Rounded MT Bold",14),
        value=2,
        variable=radiovar,
        command=selected,
    )
    r3.place(x=158,y=435)

    r4 = Radiobutton(
        frame,
        text=answers_choice[indexes[0]][3],     #00002f
        width=14,
        height=1,
        background="#00002f",
        foreground="#04c9fc",
        font=("Arial Rounded MT Bold",14),
        value=3,
        variable=radiovar,
        command=selected,
    )
    r4.place(x=158,y=517)



# ------------------------------------------------------------------------
global frame
frame = Frame(root,bg="blue")
frame.pack(fill=X)

backgroundimage=PhotoImage(file="images/ready.png")
Label(frame,image=backgroundimage).pack()




img2 =PhotoImage(file="images/startButton.png")

btnStart=Button(
    frame,
    image = img2,
    relief='flat',
    background='#0c1524',
    command=startIspressed
)
btnStart.place(x=240,y=460)

lblInstruction = Label(
    root,
    width=100,
    text="Read the rules and Click Start once you are ready",
    background="#ee0ff2",
    font=("Consolas",14),
    foreground="#000000",
)
lblInstruction.place(x=-155,y=640)

lblRules = Label(
    root,
    text="This Quiz contains 10 questions.\nOnce you select a option that will be a final choice\nHence think carefully before you select!!!",
    width=100,
    height=5,
    font=("Times",14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.place(x=-170,y=670)






root.mainloop()