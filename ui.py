import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import main
from pathlib import Path


class GUI:
    filename = ''

    def __init__(self):
        self.draw()

    def select_file(self):
        self.filename = askopenfilename(
            title='Open a file',
            initialdir='.')

    def run(self):
        if self.filename == '':
            showinfo("Error", "Select a video file!")
        else:
            main.run_light(Path(self.filename), 4, 59)

    def draw(self):
        window = tk.Tk()
        text = tk.Label(text="Movie screen grabber. Choose a movie file to proceed.")
        text.pack()
        btn_file = tk.Button(text="Select movie file", command=self.select_file)
        btn_file.pack()
        btn_run = tk.Button(text="Run", command=self.run)
        btn_run.pack()

        window.mainloop()


if __name__ == '__main__':
    GUI()
