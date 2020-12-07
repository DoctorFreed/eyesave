import time
import tkinter
import tkinter.messagebox
import argparse


def messagebox(title='EyeSave', text='None'):
    """
    Silent messagebox only

    :param title: Messagebox header text (default 'EyeSave')
    :param text: Messagebox main text (default 'None')
    :return: None
    """
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(title, text)
    root.destroy()


def timer_start(session=20, pause=5):
    """
    The main function of the timer

    :param session: The time you will work is specified in minutes (default 20)
    :param pause: The time you will rest is indicated in minutes (default 5)
    :return: None
    """
    session_sec = session * 60
    pause_sec = pause * 60
    while True:
        messagebox('EyeSave', 'Your {0} minutes of computer use have started'.format(session))
        time.sleep(session_sec)
        messagebox('EyeSave', 'A break of {0} minutes!'.format(pause))
        time.sleep(pause_sec)
        messagebox('EyeSave', 'Break is over! Starting a {0}-minute session?'.format(session))


def main():
    parser = argparse.ArgumentParser(
        description='EyeSave - script for eye safety'
    )
    parser.add_argument('--session', help='the time you will be working at the computer '
                                          '(in minutes)', type=int, default=20)
    parser.add_argument('--pause', help='time that you will rest (in minutes)', type=int, default=5)

    args = parser.parse_args()
    timer_start(session=args.session, pause=args.pause)


if __name__ == '__main__':
    main()
