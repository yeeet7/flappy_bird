
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui, time, random

gap_size = 350
is_alive: bool = True
root = tk.Tk()

def main():
    game = Game()
    game.run()

class Bird:
     
    _bird: tk.Toplevel = tk.Toplevel(master=root, background="#3cc8c8")
    velocity = 0
    gravity = 9.8
    y_pos = 400

    def __init__(self):
        self._bird.geometry("120x120+180+400")
        self._bird.title("bird")
        _img = Image.open("C:\\Users\\Viktor\\Desktop\\hry\\nie hry\\vscode\\bird.png")
        _img = _img.resize((150, 150))
        _photo_img = ImageTk.PhotoImage(_img)
        _img_label = tk.Label(self._bird, image=_photo_img)
        _img_label.image = _photo_img
        _img_label.pack()
        self._bird.bind("<space>", self.flap)

    def flap(self, e):
        self.velocity = -20
    
    # def run(self):
    #     global is_alive
    #     while is_alive:
    #         try:
    #             time.sleep(0.017)
    #             self.velocity += self.gravity * 1/9
    #             self.y_pos += self.velocity * 0.5
    #             self._bird.geometry(f"+180+{int(self.y_pos)}")
    #             self._bird.update()
    #         except:
    #             is_alive = False

class PipePair:

    _top_pipe: tk.Toplevel
    _bottom_pipe: tk.Toplevel
    gap_height: int
    x_pos: int

    def __init__(self, gap_height, x_pos):
        self.gap_height = gap_height
        self.x_pos = x_pos

        self._top_pipe = tk.Toplevel(master=root, background="#3cc8c8")
        self._bottom_pipe = tk.Toplevel(master=root, background="#3cc8c8")
        
        self._top_pipe.geometry(f"180x{self.gap_height}+{int(self.x_pos)}+0")
        self._top_pipe.title('pipe top')
        self._bottom_pipe.geometry(f"180x{(pyautogui.size()[1] - self.gap_height - gap_size)}+{int(self.x_pos)}+{gap_height+gap_size}")
        self._bottom_pipe.title('pipe bottom')

        _img = Image.open("C:\\Users\\Viktor\\Desktop\\hry\\nie hry\\vscode\\pipe_end.png")
        _img2 = Image.open("C:\\Users\\Viktor\\Desktop\\hry\\nie hry\\vscode\\pipe.png")
        _img = _img.resize((180, 180))
        _img = _img.rotate(180)
        _img2 = _img.resize((155, 155))
        _img2 = _img.rotate(180)
        _photo_img = ImageTk.PhotoImage(_img)
        _photo_img2 = ImageTk.PhotoImage(_img2)
        _img_label = tk.Label(self._top_pipe, image=_photo_img)
        _img_label2 = tk.Label(self._top_pipe, image=_photo_img2)
        _img_label22 = tk.Label(self._top_pipe, image=_photo_img2)
        _img_label23 = tk.Label(self._top_pipe, image=_photo_img2)
        _img_label24 = tk.Label(self._top_pipe, image=_photo_img2)
        _img_label.image = _photo_img
        _img_label2.image = _photo_img2
        _img_label22.image = _photo_img2
        _img_label23.image = _photo_img2
        _img_label24.image = _photo_img2
        _img_label.pack(side="bottom")
        _img_label2.pack(side="bottom")
        _img_label22.pack(side="bottom")
        _img_label23.pack(side="bottom")
        _img_label24.pack(side="bottom")

        _img3 = Image.open("C:\\Users\\Viktor\\Desktop\\hry\\nie hry\\vscode\\pipe_end.png")
        _img4 = Image.open("C:\\Users\\Viktor\\Desktop\\hry\\nie hry\\vscode\\pipe.png")
        _img3 = _img3.resize((180, 180))
        _img4 = _img4.resize((155, 155))
        _photo_img3 = ImageTk.PhotoImage(_img3)
        _photo_img4 = ImageTk.PhotoImage(_img4)
        _img_label3 = tk.Label(self._bottom_pipe, image=_photo_img3)
        _img_label4 = tk.Label(self._bottom_pipe, image=_photo_img4)
        _img_label5 = tk.Label(self._bottom_pipe, image=_photo_img4)
        _img_label6 = tk.Label(self._bottom_pipe, image=_photo_img4)
        _img_label7 = tk.Label(self._bottom_pipe, image=_photo_img4)
        _img_label3.image = _photo_img3
        _img_label4.image = _photo_img4
        _img_label5.image = _photo_img4
        _img_label6.image = _photo_img4
        _img_label7.image = _photo_img4
        _img_label3.pack()
        _img_label4.pack()
        _img_label5.pack()
        _img_label6.pack()
        _img_label7.pack()

    # def run(self):
    #     global is_alive
    #     while is_alive:
    #         time.sleep(0.017)
    #         self.x_pos -= 1
    #         self._pipe_window.geometry(f"+{self.x_pos}+{self.y_pos}")

class Game:

    bird: Bird
    pipepairs: list[PipePair]

    def __init__(self):
        self.bird = Bird()
        _screen_width: int = pyautogui.size()[0]
        self.pipepairs = [
            PipePair(random.randint(10, pyautogui.size()[1] - 350), _screen_width),
            PipePair(random.randint(10, pyautogui.size()[1] - 350), int(_screen_width * 1.5)),
        ]

    def run(self):
        global is_alive
        while is_alive:
            try:
                time.sleep(0.017) # self.bird.run()
                self.bird.velocity += self.bird.gravity * 1/9
                self.bird.y_pos += self.bird.velocity * 0.5
                self.bird._bird.geometry(f"+180+{int(self.bird.y_pos)}")
                self.bird._bird.update()
                if self.bird.y_pos < 0 or self.bird.y_pos > pyautogui.size()[1]-120:
                    is_alive = False
                for pipepair in self.pipepairs:
                    pipepair.x_pos -= 10
                    pipepair._top_pipe.geometry(f"+{pipepair.x_pos}+0")
                    pipepair._bottom_pipe.geometry(f"+{pipepair.x_pos}+{pipepair.gap_height+gap_size}")
                    pipepair._top_pipe.update()
                    pipepair._bottom_pipe.update()
                    if pipepair.x_pos < -165:
                        pipepair._top_pipe.destroy()
                        pipepair._bottom_pipe.destroy()
                        pipepair._top_pipe.quit()
                        pipepair._bottom_pipe.quit()
                        self.pipepairs.pop(0)
                        self.pipepairs.append(PipePair(random.randint(10, pyautogui.size()[1] - 350), int(pyautogui.size()[0])))
                    if (pipepair.x_pos < 300 and pipepair.x_pos > 0) and (self.bird.y_pos < pipepair.gap_height or self.bird.y_pos > pipepair.gap_height+gap_size): # pipe collisions
                        is_alive = False
            except:
                is_alive = False

root.withdraw()

main()