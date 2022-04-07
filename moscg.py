import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import main
from pathlib import Path


class GUI(tk.Tk):
    filename = ''

    def __init__(self):
        super().__init__()
        self.title("moscg")
        self.clusters = tk.IntVar(value=4)
        self.skip_frames = tk.IntVar(value=99)
        self.desc = tk.StringVar()

        self.draw()

    def select_file(self):
        self.filename = askopenfilename(
            title='Open a file',
            initialdir='.')

    def run(self):
        if self.filename == '':
            showinfo("Error", "Select a video file!")
        else:
            main.run_light(Path(self.filename), self.clusters.get(), self.skip_frames.get())

    def draw(self):
        self.desc.set("Movie screen grabber. Choose a movie file to proceed.")
        lbl_desc = tk.Label(textvariable=self.desc)
        lbl_cluster = tk.Label(text="Number of screenshots:")
        lbl_skip = tk.Label(text="Number of skipped frames:")

        ent_cluster = tk.Entry(textvariable=self.clusters)
        ent_skip = tk.Entry(textvariable=self.skip_frames)

        btn_file = tk.Button(text="Select movie file", command=self.select_file)
        btn_run = tk.Button(text="Run", command=self.run)

        lbl_desc.grid(row=0, column=0, padx=5, pady=5)
        lbl_cluster.grid(row=1, column=0, padx=5, pady=5)
        ent_cluster.grid(row=1, column=1, padx=5, pady=5)
        lbl_skip.grid(row=2, column=0, padx=5, pady=5)
        ent_skip.grid(row=2, column=1, padx=5, pady=5)
        btn_file.grid(row=3, column=0, padx=5, pady=5)
        btn_run.grid(row=3, column=1, padx=5, pady=5)


def main_fct():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main_fct()
