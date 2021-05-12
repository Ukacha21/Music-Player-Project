
from tkinter import *
from tkinter import filedialog as filedialog
import pygame
#import keyboard
import time
import os



#from PIL import ImageTk, Image

root = Tk()

root.title("Calvin Player")

root.iconbitmap("Images/icon.ico")
root.geometry("480x600") #("480x720")
root.resizable(False,False)
root.overrideredirect(1)
#root["bg"] = "grMay"

pygame.mixer.init()

#Buttons

#def play():



#borderwidth = 2     to be used in buttons
#borderwidth, highlightthickness=4, highlightcolor="black", highlightbackground="black" 
#button modes: relief= "groove", "solid", "ridge", "sunken", "raised", "flat"

#playB = Button(text="play", borderwidth=0,  bg='#F0FFFF', fg='#FFFFFF', compound=LEFT, anchor="se", command=root.destroy)

playimg = PhotoImage(file="Images/x4x/unpause/unpause.png")
pauseimg = PhotoImage(file="Images/x4x/unpause/pause.png")
nextimg = PhotoImage(file="Images/nexp/next.png")
previmg = PhotoImage(file="Images/nexp/prev.png")
quitimg = PhotoImage(file="Images/Shutdown.png")

wallimg = PhotoImage(file="Images/capt.png")


def ask():
    global filep
    '''filep = filedialog.askopenfilename(initialdir="D:/Allupy/Welcome/Songs", title="Selec a music", filetypes=(("mp3 files", "*.mp3"),("m4a files", "*.m4a")))
    '''
    filep = filedialog.askdirectory()
    playlist = []
    musicNum = 0
    os.chdir(filep)
    for file in os.listdir(filep):
        if file.endswith('.mp3'):
            musicNum += 1
            playlist.append(file)
            pygame.mixer.music.load(playlist[0])
            pygame.mixer.music.play()
            if pygame.mixer.music.play() == False:
                playlist.append(file)
                for i in playlist:
                    pygame.mixer.music.load(playlist[i])
                    i += 1 
                    pygame.mixer.music.play(i)


    
    '''directory = filedialog.askdirectory()
    print("Loading files from directory:", directory)
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            print("PLaying file", file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            #wait for the music to play before exiting
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)
                if file == "Ela.mp3":
                    break'''
'''
    global found
    found = filep
    playlist.append(found)'''
    
    #loaded = Label(text=found, bg="#BA2667", font=("Sans", 11))
    #loaded.place(x=112, y=400) #anchor=CENTER
        
    #pygame.mixer_music.load(found)#mixer.music
    #pygame.mixer_music.play()#mixer.music
    #global playB

    #keep = True
    #while(keep):
    #        if pygame.K_SPACE:
    #            pygame.mixer_music.pause()
    #            if pygame.K_SPACE:
    #                pygame.mixer_music.unpause()
    #                keep = False'''
            

def play():

    pygame.mixer.music.unpause()
    '''if playB:
        pygame.mixer.music.play()
    elif playB:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()'''

def pause():
    pygame.mixer.music.pause()

wallLabel = Label(image=wallimg)

openB = Button(root,text="Open",borderwidth=0, bg="#CB2161", command=ask) 
openB.place(relx=0, rely=0, anchor=NW)

redB = PhotoImage(file="Images/close.png")
greenB = PhotoImage(file="Images/minim.png")

closeB = Button(image=redB, borderwidth=0, bg="#AB2B6C", command=root.destroy)
mimimB = Button(image=greenB, borderwidth=0, bg="#AB2B6C", command=root.iconify)

playB = Button(image=playimg, borderwidth=0, bg="#BA2667", command=play)
pauseB = Button(image=pauseimg, borderwidth=0, bg="#BA2667", command=pause)

#tryna make the same button play and pause

nextB = Button(image=nextimg, borderwidth=0, bg="#AB2B6C")
prevB = Button(image=previmg, borderwidth=0, bg="#CB2161")
quitB = Button(image=quitimg, borderwidth=0, bg="#A22D6F", command=root.destroy)

#keyboard.press()
'''if keyboard.press(hotkey="Space") == "Space":
    pygame.mixer.music.pause()
'''

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

title_bar = Frame(root, relief='flat',bg="#BA2667", bd=1,height=30, width=385)

title_text=Label(title_bar, text="Kinter Player", font=("Times new roman", 13), bg="#BA2667", anchor=CENTER)

music_icon = PhotoImage(file="images/icon.png")
music_Label = Label(image=music_icon, bg="#CB2161") #bg="#BA2667"

wallLabel.place(x=-2, y=-2)

title_bar.place(x=45, y=0)
title_text.place(x=150, y=2)
playB.place(x=220, y=430)
pauseB.place(x=220, y=430)
nextB.place(x=320, y=430)
prevB.place(x=90, y=430)
#quitB.place(x=360, y=480)

closeB.place(x=440, y=0)
#mimimB.place(x=400, y=0)

music_Label.place(y=240, anchor=CENTER, x=240)

root.geometry('480x600')

#window.place(x=45, y=0)

'''home = Menu(root,  bg="#BA2667")
home.add_cascade(label='Home', command=root.destroy)
root.config(menu=home)'''

def hometop():
    top = Toplevel()
    top.title("Home")
    top.geometry("320x320")
    top.resizable(False, False)
    label = Label(top, text="Home", font=("Arial", 32))
    label.pack()

home = Button(text="home", bg="#BA2667", relief="flat", command=hometop)

home.place(x=45, y=15)

title_bar.bind('<B1-Motion>', move_window)
title_text.bind('<B1-Motion>', move_window)
wallLabel.bind('<B1-Motion>', move_window)
music_Label.bind('<B1-Motion>', move_window)
home.bind('<B1-Motion>', move_window)

#closeB.place(x=440, y=0)

def frame():
    setF = Frame(root, height=480, width=120, bg="black")
    setF.place(x=0, y=45)
    def forget():
        setF.destroy()
        closeB.place_forget()
        frameB.pack_forget()
    closeB = Button(setF, image=redB, borderwidth=0, bg="black", command=forget)
    
    global vol
    vol = 0 

    def Up():
        vol += 1 #0.4
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.get_volume(vol)


    volUp = Button(setF, text="Up", command=Up)
    volDwn = Button(setF, text="Down") 
    volUp.place(x=5, y=10)
    volDwn.place(x=3, y=40)
    closeB.place(x=85, y=0) #bg="#AB2B6C"

    setF.place_configure()
    
    
frameB = Button(root, text="frame",  relief="flat", bg="green", command=frame)
frameB.place(x=45, y=45)

mainloop()

