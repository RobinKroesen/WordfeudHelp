woorden = open("Woorden.txt", "r")

woorden_lijst = woorden.read().split('\n')

import tkinter as tk


class bord(tk.Frame):
    """class die het Wordfeud bord actueel weergeeft"""

    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.grid()

        for row in range(15):
            for col in range(15):
                vak = tk.Entry(self, font=("Calibri", 14),width=2)
                vak.grid(row=row, column=col)
        plank_tekst = tk.Label(root, text="plank:", width=8)
        plank = tk.Entry(root, font=("Calibri", 16),width=7)
        plank_tekst.grid(row=16)
        plank.grid(row=17)



master = tk.Tk()
canvas = bord(root=master)
master.mainloop()







