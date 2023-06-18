import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import moscg
from pathlib import Path


class GUI(tk.Tk):
    filename = ''

    def __init__(self):
        super().__init__()
        self.title("moscg")
        self.clusters = tk.IntVar(value=4)
        self.skip_frames = tk.IntVar(value=99)
        self.save_adj = tk.IntVar(value=0)
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
            foo = moscg.Moscg(Path(self.filename), self.clusters.get(), self.skip_frames.get(), self.save_adj.get())
            foo.run()
            self.create_finish_popup()

    def create_finish_popup(self):
        # pop = tk.Toplevel(self)
        # pop.geometry("750x250")
        # pop.title("Child Window")
        # tk.Label(pop, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)
        showinfo("Done!", "Frame analysis complete!")

    def draw(self):
        self.desc.set("Movie screen grabber. Choose a movie file to proceed.")
        lbl_desc = tk.Label(textvariable=self.desc)
        lbl_cluster = tk.Label(text="Number of screenshots:")
        lbl_skip = tk.Label(text="Number of skipped frames:")
        lbl_adj = tk.Label(text="Number of additional adjacent frames to save:")

        ent_cluster = tk.Entry(textvariable=self.clusters)
        ent_skip = tk.Entry(textvariable=self.skip_frames)
        ent_adj = tk.Entry(textvariable=self.save_adj)

        btn_file = tk.Button(text="Select movie file", command=self.select_file)
        btn_run = tk.Button(text="Run", command=self.run)

        lbl_desc.grid(row=0, column=0, padx=5, pady=5)
        lbl_cluster.grid(row=1, column=0, padx=5, pady=5)
        ent_cluster.grid(row=1, column=1, padx=5, pady=5)
        lbl_skip.grid(row=2, column=0, padx=5, pady=5)
        ent_skip.grid(row=2, column=1, padx=5, pady=5)
        lbl_adj.grid(row=3, column=0, padx=5, pady=5)
        ent_adj.grid(row=3, column=1, padx=5, pady=5)
        btn_file.grid(row=4, column=0, padx=5, pady=5)
        btn_run.grid(row=4, column=1, padx=5, pady=5)


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
