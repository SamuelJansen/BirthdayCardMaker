import tkinter as tk
#from tkinter import *
import re
import pygame as pg

message = """* Prepara deseja um feliz aniverrsário
* aos aniversariantes

NATHALIA PACHECO BARROS
ANARETE CRISTINA TRINDADE
ALINE CAROLINE DOS SANTOS PEREIRA
LARISSA SILVA
JULIA CÉ BRITZKE
GABRIEL SCHNEIDERS DE OLIVEIRA
VITÓRIA FERREIRA MENEZES
VITÓRIA LEMKE RODRIGUES
ADRIANA RIBEIRO DA SILVA
LUCAS FLORES MALAQUIAS
OSCAR CHERISMA
PETERSON SILVA DA SILVA
Camila Silveira Marques
Bruna Verônica Alencastro de Menezes Soares
Marta Pinto Damasio
ADRIANA SILVEIRA DA SILVA
JOÃO VITOR DE MATTOS REI
RAFAEL FABIANO CHAROPEM
TATIANA CUNHA
BIANCA SOUCEDO BARBOSA

:D É os guri"""

class TransparentWin(tk.Tk):
    """ Transparent Tkinter Window Class. """

    def __init__(self):

        tk.Tk.__init__(self)

        self.Drag = Drag(self)

        # Sets focus to the window.
        self.focus_force()

        # Removes the native window boarder.
        self.overrideredirect(True)

        # Disables resizing of the widget.
        self.resizable(False, False)

        # Places window above all other windows in the window stack.
        self.wm_attributes("-topmost", True)

        # This changes the alpha value (How transparent the window should be).
        # It ranges from 0.0 (completely transparent) to 1.0 (completely opaque).
        self.attributes("-alpha", 0.7)

        # The windows overall position on the screen
        self.wm_geometry('+' + str(1000) + '+' + str(50))

        # Changes the window's color.
        # Check avaliable collors in Encycolorpedia:  https://encycolorpedia.com/html
        # For more specific search, use this: https://encycolorpedia.com/3e4134
        bg = '#eb0d00' #'#ee0028'

        self.config(bg=bg)

        self.Frame = tk.Frame(self, bg=bg)

        # Exits the application when the window is right clicked.
        self.Frame.bind('<Button-1>', self.exit)

        # Changes the window's size indirectly.
        self.Frame.configure(width=320, height=50)

        """
        top = Tk()
        text = Text(top)
        text.insert(INSERT, "Name.....")
        text.insert(END, "Salary.....")

        text.pack()

        text.tag_add("Write Here", "1.0", "1.4")
        text.tag_add("Click Here", "1.8", "1.13")

        text.tag_config("Write Here", background="yellow", foreground="black")
        text.tag_config("Click Here", background="black", foreground="white")

        top.mainloop()
        """

        ###- textBox = tk.Tk()
        text = tk.Text(self,{'bg':bg,'fg':'white','height':'2','width':'20'})#,'pady':'20'})#
        text.insert(tk.INSERT, message)
        #text.insert(tk.END, "Salary.....")

        text.pack()

        text.tag_add("Write Here", "1.8", "1.3")
        #text.tag_add("Click Here", "1.8", "4.13")

        text.tag_config("Write Here", background='white', foreground="white")
        #text.tag_config("Click Here", background="black", foreground="white")

        self.Frame.pack()

        Music("Sounds/HappyBirthdayToYou.mp3")



    def exit(self, event):
        self.destroy()

    def position(self):
        _filter = re.compile(r"(\d+)?x?(\d+)?([+-])(\d+)([+-])(\d+)")
        pos = self.winfo_geometry()
        filtered = _filter.search(pos)
        self.X = int(filtered.group(4))
        self.Y = int(filtered.group(6))

        return self.X, self.Y


class Drag:
    """ Makes a window dragable. """

    def __init__(self, par, dissable=None, releasecmd=None):
        self.Par        = par
        self.Dissable   = dissable
        self.ReleaseCMD = releasecmd

        self.Par.bind('<Button-3>', self.relative_position)
        self.Par.bind('<ButtonRelease-3>', self.drag_unbind)

    def relative_position(self, event):
        cx, cy = self.Par.winfo_pointerxy()
        x, y = self.Par.position()
        self.OriX = x
        self.OriY = y
        self.RelX = cx - x
        self.RelY = cy - y
        self.Par.bind('<Motion>', self.drag_wid)

    def drag_wid(self, event):
        cx, cy = self.Par.winfo_pointerxy()
        d = self.Dissable

        if d == 'x':
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y':
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY

        if x < 0:
            x = 0
        if y < 0:
            y = 0

        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind(self, event):
        self.Par.unbind('<Motion>')
        if self.ReleaseCMD != None:
            self.ReleaseCMD()

    def dissable(self):
        self.Par.unbind('<Button-3>')
        self.Par.unbind('<ButtonRelease-3>')
        self.Par.unbind('<Motion>')


class Music :
    """Makes a song playable"""

    def __init__(self,path):
        pg.mixer.init(44100)
        try:
            # create the sound instances
            pg.mixer.music.load(path)
            pg.mixer.music.play()
        except:
            print("Error: Sound file not found")


def __run__():
    TransparentWin().mainloop()

if __name__ == '__main__':
    __run__()
