import tkinter as tk
import pyautogui as gui
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_app = tk.Button(self)
        self.start_app['text'] = "Start"
        self.start_app['command'] = self.go
        self.start_app['bg'] = "red"
        self.start_app['fg'] = "white"
        self.start_app['font'] = "bold"
        self.start_app.pack(side="top")

    def Fidge(self):
        time.sleep(0.5)
       #print('Up')
        gui.press('up')
        time.sleep(0.5)
        #print('Down')
        gui.press('down')
    
         

    def go(self):
        if self.start_app['text'] == "Start":
            time.sleep(3)
            position = gui.position()
            self.start_app['text'] = "Working ..."
            self.start_app['bg'] = "green"
            self.master.update()
            while True:
                self.Fidge()
                if position != gui.position():
                    break
            self.start_app['bg'] = "red"
            self.start_app["text"] = "Start"
            self.master.update()

root = tk.Tk()
root.title("Automating")
root.geometry("300x40")
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)

app = Application(master=root)

app.mainloop()
