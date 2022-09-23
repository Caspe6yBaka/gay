# Import the required libraries
from tkinter import *
from tkinter import font
import tkinter

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("1366x768")

# Create two frames in the window
Main_Menu = Frame(win, bg="#ec1c24")
Main_Menu.pack(fill='both', expand=1)
PlayerPicker = Frame(win, bg="#5f0000")

# Define a function for switching the frames
def change_to_Main_Menu():
   Main_Menu.pack(fill='both', expand=1)
   PlayerPicker.pack_forget()

def change_to_PlayerPicker():
   PlayerPicker.pack(fill='both', expand=1)
   Main_Menu.pack_forget()

# Fonts
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='22', weight='bold')

# Meny
Menu_Play_Button = PhotoImage(file = "Images\Play_menu.png")
Menu_Play_Button_New = Menu_Play_Button.subsample(2, 2)
Menu_Screen = PhotoImage(file = "Images\math_menu_new.png")

Menu_button = Button(Main_Menu, image=Menu_Play_Button_New, command=change_to_PlayerPicker, borderwidth=0, bg="#ec1c24", fg="#ec1c24")
Menu_Screen_bg = Label(Main_Menu, image=Menu_Screen, bg="#ec1c24")


Menu_button.place(x=454, y=500)
Menu_Screen_bg.place(x=439, y=80)


# Player Meny
# darker bgcolor = "#5f0000"
Menu_Play_Button_BG = PhotoImage(file = "Images\Play_menu_Dark.png")
Menu_Play_Button_New_BG = Menu_Play_Button_BG.subsample(2, 2)
Menu_Screen_BG = PhotoImage(file = "Images\math_menu_Dark.png")

Menu_button_BG = Button(PlayerPicker, image=Menu_Play_Button_New_BG, command=change_to_Main_Menu, borderwidth=0, bg="#5f0000", fg="#ec1c24")
Menu_Screen_bg_BG = Label(PlayerPicker, image=Menu_Screen_BG, bg="#5f0000")

Menu_button_BG.place(x=454, y=500)
Menu_Screen_bg_BG.place(x=439, y=80)

win.mainloop()