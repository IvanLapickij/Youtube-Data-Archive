import tkinter
import customtkinter
from tkinter import *
from tkinter import messagebox
from Video_classes import Video
from googleapiclient.discovery import build

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# window = Tk()
window = customtkinter.CTk()
window.geometry("800x800")
# creates title for the window
window.title('YouTube Video Downloader')
# makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)

# creates the canvas for containing all the widgets
canvas = Canvas(window, width=500, height=150, background=window["bg"])
canvas.pack()

# loading the logo
logo = PhotoImage(file='youtubelogo.png')
# creates dimensions of the logo
logo = logo.subsample(10, 10)
# adding the logo to the canvas
canvas.create_image(250, 80, image=logo)


# ============================================================
# Event Handling Methods


def addLinksFromFile(videolist):
    infile = open('links.txt', "r")
    for line in infile:
        line = line.rstrip()
        list = line.split(':')
        title = list[0]
        likes = list[1]
        views = list[2]
        link = list[3]
        new_video = Video(title, likes, views, link)
        videolist.append(new_video)


def archiveCmd():
    outfile = open('links.txt', "w")
    print("archived")
    for el in videolist:
        print(el.getTitle() + ':', end='')
        print(el.getTitle() + ':', file=outfile, end='')
        print(el.getLikes() + ':', file=outfile, end='')
        print(el.getViews() + ':', file=outfile, end='')
        print(str(el.getLink()), file=outfile)


def display(index):
    global current
    global title
    title = videolist[index]
    current = index
    # Title
    entry1.delete(0, END)
    entry1.insert(END, title.getTitle())
    # Likes
    entry2.delete(0, END)
    entry2.insert(END, title.getLikes())
    # Views
    entry3.delete(0, END)
    entry3.insert(END, title.getViews())

    entry4.delete(0, END)
    entry4.insert(END, title.getLink())


def quitCmd():
    quit()


def nextCmd():
    global current
    if current < (len(videolist) - 1):
        current += 1
        display(current)


def prevCmd():
    global current
    if current > 0:
        current -= 1
        display(current)


def clearData():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)


def insertNewVideo():
    title = entry1.get()
    likes = entry2.get()
    views = entry3.get()
    link = entry4.get()
    newVideo = Video(title, likes, views, link)
    videolist.append(newVideo)


# Get data from youtube function
def video_details():
    if "youtube" in video_url.get():
        video_id = video_url.get()[len("https://www.youtube.com/watch?v="):]
        # if input is empty catching index error + message for user
    elif IndexError:
        messagebox.showwarning(title="IndexError", message="Please insert your link before request")
        video_id = video_url.get()
    else:
        video_id = video_url.get()

    # creating YouTube resource object
    youtube = build('youtube', 'v3', developerKey='AIzaSyBvwWqA6z3by-dQGOWYzqkjpxjdcvuYOaA')
    # retrieve youtube video results
    video_request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id)
    video_response = video_request.execute()
    title = video_response['items'][0]['snippet']['title']
    likes = video_response['items'][0]['statistics']['likeCount']
    views = video_response['items'][0]['statistics']['viewCount']
    link = video_response['items'][0]['id']
    # inserting data in table
    entry1.delete(0, END)
    entry1.insert(END, title)
    entry2.delete(0, END)
    entry2.insert(END, likes)
    entry3.delete(0, END)
    entry3.insert(END, views)
    entry4.delete(0, END)
    entry4.insert(END, link)


# End of Method Declarations
# ========================================================================
videolist = []
addLinksFromFile(videolist)
global current  # current video
title = videolist[0]  # initialize to first video
# MENU TOPBAR
# =======================================================
optionmenu_var = customtkinter.StringVar(value="Menu")  # set initial value
# Menu to Add New Student
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)
subm1 = Menu(menu1)  # Menu
menu1.add_cascade(label="Add_Video_Options", menu=subm1)
subm1.add_command(label="clearData", font=("arial", 12, "bold"), command=clearData)  # menu item
subm1.add_command(label="Insert Video", font=("arial", 12, "bold"), command=insertNewVideo)

# ======= End of Menu Definition ============================
# Gui elements design
frame = Frame(window, width=200, height=200, background=window["bg"])
frame.place(x=100, y=400)
# ----
text_var = tkinter.StringVar(value="Title, Views, Likes of YouTube Video")

Label(window, text="Title, Views, Likes of YouTube Video", fg="grey",
      font="Helvetica 20 bold", relief="solid", bg=window["bg"]).pack(pady=10)

Label(window, text="Enter video URL or ID", font="10", fg="yellow", bg=window["bg"]).pack()

video_url = Entry(window, width=40, font="15")
video_url.pack(pady=10)

button0 = customtkinter.CTkButton(master=window, text="Get Details", command=video_details).pack()
# ------

# Table design definitions
label1 = Label(frame, text="Title", fg="white", background=window["bg"], width=15, font=("arial", 10, "bold"))  #
label1.grid(row=0, column=0, sticky=W + E)

entry1 = Entry(frame, fg="white", background=window["bg"], width=80)
entry1.insert(END, '0')
entry1.grid(row=0, column=1, sticky=W + E)

label2 = Label(frame, text="Likes", fg="white", background=window["bg"], width=15, font=("arial", 10, "bold"))  #
label2.grid(row=1, column=0, sticky=W + E)

entry2 = Entry(frame, background=window["bg"], fg="white")
entry2.insert(END, '0')
entry2.grid(row=1, column=1, sticky=W + E)

label3 = Label(frame, text="Views", fg="white", background=window["bg"], width=15, font=("arial", 10, "bold"))  #
label3.grid(row=2, column=0, sticky=W + E)

entry3 = Entry(frame, background=window["bg"], fg="white")
entry3.insert(END, '0')
entry3.grid(row=2, column=1, sticky=W + E)

label4 = Label(frame, text="Link", fg="white", background=window["bg"], width=15, font=("arial", 10, "bold"))  #
label4.grid(row=3, column=0, sticky=W + E)

entry4 = Entry(frame, background=window["bg"], fg="white")
entry4.insert(END, '0')
entry4.grid(row=3, column=1, sticky=W + E)

button5 = Button(frame, text="Next", fg="white", background=window["bg"], font=("arial", 10, "bold"), command=nextCmd,
                 activebackground="green")
button5.grid(row=12, column=1, sticky=W + E)

button6 = Button(frame, text="Prev", fg="white", background=window["bg"], font=("arial", 10, "bold"), command=prevCmd,
                 activebackground="yellow")
button6.grid(row=12, column=0, sticky=W + E)

button9 = Button(frame, text="Archive", fg="white", background=window["bg"], font=("arial", 10, "bold"),
                 command=archiveCmd, activebackground="pink")
button9.grid(row=14, column=0, sticky=W + E)

button10 = Button(frame, text="Quit", fg="white", background=window["bg"], font=("arial", 10, "bold"), command=quitCmd,
                  activebackground="orange")
button10.grid(row=14, column=1, sticky=W + E)
display(0)

window.mainloop()# End of code line 227, main loop starts