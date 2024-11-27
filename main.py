import customtkinter as ctk
import os
import sys

from src.ui_elements import *

class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(" YoutubeDownloader ")
        self.geometry("600x300")
        self.resizable(False, False)

        self.draw_title()

    def draw_title(self):
        self.title_frame = DrawFrame(
            self,
            width = 100,
            height = 100,
            fg_color = "#ff0000"
        )
        self.title_frame.grid(row = 0, column = 0)

if __name__ == '__main__':
    try:
        app = main()
        app.mainloop()
    except KeyboardInterrupt:
        print("exiting...")
        sys.exit()