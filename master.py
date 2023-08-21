from tkinter import *
import tkinter.messagebox as tm

class MainPage(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_main = Label(self, text="Welcome to the Main Page",font=('calibri',20))
        self.label_main.pack(pady=150)
        self.pack()

    @staticmethod
    def loading():
        root = Tk()
        MainPage(root)
        root.title('Contact Book')

        root.attributes('-topmost', 1)
        #=============================== Window - Center=========================
        window_width = 400
        window_height = 400
        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.mainloop()




