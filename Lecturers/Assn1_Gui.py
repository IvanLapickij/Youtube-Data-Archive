

from tkinter import *

from Assign_Team import Team

window = Tk()
window.geometry("300x470")
window.title("Welcome")

#============================================================
# Event Handling Methods

def addTeamsFromFile(teamlist):

    infile = open('teamsFile.txt', "r")
    for line in infile:
        line =line.rstrip()
        list = line.split(':')
        team = list[0]
        nationality = list[1]
        premier=True
        if (list[2]=='False'):
            premier=False
        points=int(list[3])
        played = int(list[4])
        wins=int(list[5])
        goals = int(list[6])

        new_team=Team(team,nationality,premier,points,played,wins,goals)
        teamlist.append(new_team)
        
def archiveCmd():
    outfile = open('teamsFile.txt', "w")
    print("Here")
    for el in teamlist:
        print(el.getName()+':',end='')
        print(el.getName()+':',file=outfile, end='')
        print(el.getNationality()+ ':',file=outfile, end='')
        print(el.getPremierLeague()+':',file=outfile, end='')
        print(str(el.getPoints())+ ':',file=outfile, end='')
        print(str(el.getPlayed())+ ':',file=outfile, end='')
        print(str(el.getWins())+ ':',file=outfile, end='')
        print(el.getGoals(),file=outfile)



def display(index):
    global current
    global team
    team = teamlist[index]
    current=index
    entry2.delete(0, END)
    entry2.insert(END, team.getName())
    entry3.delete(0, END)
    entry3.insert(END, team.getNationality())
    entry4.delete(0, END)
    entry4.insert(END, team.getPoints())
    entry5.delete(0, END)
    entry5.insert(END, team.getPlayed())
    entry6.delete(0, END)
    entry6.insert(END, team.getWins())
    entry6b.delete(0, END)
    entry6b.insert(END, team.getGoals())


    premierleague=team.getPremierLeague()
    if (premierleague==True):
        var_cb1.set(1)
    else:
        var_cb1.set(0)

def quitCmd():
    quit()

def markWin():
    team.markWin()
    display(current)


def markDraw():
    team.markDraw()
    display(current)

def markLoss():
    #days = int(excusedVar.get())
    team.markLoss()
    display(current)

def goalsCmd():
    goals = int(goalsVar.get())
    team.addGoals(goals)
    display(current)

def percentAttended():
    result = team.getPercentWins()
    entry7.delete(0, END)
    entry7.insert(END, (str(result) + " %"))

def nextCmd():
    global current
    if (current<(len(teamlist) - 1)):
        current += 1
        display(current)

def resetCmd():
    global current
    team.resetAll()
    display(current)


def prevCmd():
    global current
    if (current>0):
        current -= 1
        display(current)

def firstCmd():
    display(0)

def lastCmd():
    display(len(teamlist) - 1)


def clearData():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry6b.delete(0, END)
    var_cb1.set(0)
    entry4.insert(END, 0)
    entry5.insert(END, 0)
    entry6.insert(END, 0)
    entry6b.insert(END,0)

def insertNewStudent():
    name=entry2.get()
    Nationality=entry3.get()
    PremierLeague=False
    if (var_cb1.get()==1):
        PremierLeague=True
    newTeam=team(name, Nationality, PremierLeague,0,0,0,0)
    teamlist.append(newTeam)

# End of Method Declarations
#========================================================================



# Definitions
#=====================================================================
#team1 = Team("Manchester Utd", "English", True)
#team2 = Team("PSV", "French", True)
#team3 = Team("Preston N.E", "English", False)
#team4 = Team("Queens Park", "Scottish", False)
#Team5 = Team("Roma", "Italian", True)

teamlist=[]

addTeamsFromFile(teamlist)
global current     # current student
global team
team = teamlist[0]  # initialize to first student

#========= End of Definitions ============================

#=======================================================
# Menu to Add New Student
menu1 = Menu(window) #MenuBar
window.config(menu=menu1)
subm1=Menu(menu1)  #Menu
menu1.add_cascade(label="Add_Team_Options", menu=subm1)
subm1.add_command(label="clearData",  font=("arial", 12, "bold"),command = clearData)   # menu item
subm1.add_command(label="Insert Team", font=("arial", 12, "bold"), command = insertNewStudent)

#======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10,y=80)






label1 = Label(window, text="Football Team example", fg="blue",bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Name", fg="blue",width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Nationality", fg="blue",width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

label4 = Label(frame, text="Points", fg="blue",width=15, font=("arial", 10, "bold"))   #
label4.grid(row=2, column=0, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W+E)


label5 = Label(frame, text="Played", fg="blue",width=15, font=("arial", 10, "bold"))   #
label5.grid(row=3, column=0, sticky=W+E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=3, column=1, sticky=W+E)

label6 = Label(frame, text="Wins", fg="blue",width=15, font=("arial", 10, "bold"))   #
label6.grid(row=4, column=0, sticky=W+E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=4, column=1, sticky=W+E)

label6b = Label(frame, text="Goals", fg="blue",width=15, font=("arial", 10, "bold"))   #
label6b.grid(row=5, column=0, sticky=W+E)

entry6b = Entry(frame)
entry6b.insert(END, '0')
entry6b.grid(row=5, column=1, sticky=W+E)




var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Premier League", variable=var_cb1)
cb1.grid(row=6,column=0,columnspan=2)

button1 = Button(frame, text="record Win", fg="black", font=("arial", 10, "bold"), command=markWin)
button1.grid(row=7, column=0, sticky=W+E)

button2 = Button(frame, text="record Draw", fg="black", font=("arial", 10, "bold"), command=markDraw)
button2.grid(row=7, column=1, sticky=W+E)

button3 = Button(frame, text="mark Loss", fg="black", font=("arial", 10, "bold"), command=markLoss)
button3.grid(row=8, column=0, sticky=W+E)

button3b = Button(frame, text="reset data", fg="black", font=("arial", 10, "bold"), command=resetCmd)
button3b.grid(row=8, column=1, sticky=W+E)

button4a = Button(frame, text="add Goals", fg="black", font=("arial", 10, "bold"), command=goalsCmd)
button4a.grid(row=9, column=0, sticky=W+E)

list1=['1','2','3','4','5','6','7','8','9']
goalsVar = StringVar()
combo1= OptionMenu(frame,goalsVar, *list1)
goalsVar.set("1")
combo1.grid(row=9,column=1, sticky=W+E)

button4 = Button(frame, text="% Wins", fg="black", font=("arial", 10, "bold"), command=percentAttended)
button4.grid(row=10, column=0, sticky=W+E)

entry7 = Entry(frame)
entry7.insert(END, '')
entry7.grid(row=10, column=1, sticky=W+E)

labelBlank = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=11, column=0, columnspan=2,sticky=W+E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=12, column=0, sticky=W+E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=12, column=1, sticky=W+E)

button7 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button7.grid(row=13, column=0, sticky=W+E)

button8 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button8.grid(row=13, column=1, sticky=W+E)

button9 = Button(frame, text="Archive", fg="black", font=("arial", 10, "bold"), command=archiveCmd)
button9.grid(row=14, column=0, sticky=W+E)

button10 = Button(frame, text="Quit", fg="black", font=("arial", 10, "bold"), command=quitCmd)
button10.grid(row=14, column=1, sticky=W+E)
display(0)









mainloop()




