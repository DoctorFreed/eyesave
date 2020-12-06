import time
import tkinter
import tkinter.messagebox


def messagebox(title, text):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(title, text)
    root.destroy()


def timer_start(session=20, pause=5):
    session_sec = session * 60
    pause_sec = pause * 60
    while True:
        messagebox('EyeSave', 'Your {0} minutes of computer use have started'.format(session))
        time.sleep(session_sec)
        messagebox('EyeSave', 'A break of {0} minutes!'.format(pause))
        time.sleep(pause_sec)
        messagebox('EyeSave', 'Break is over! Starting a {0}-minute session?'.format(session))


if __name__ == '__main__':
    timer_start()
