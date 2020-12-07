import time
import tkinter
import tkinter.messagebox
import argparse

# Some global variables
DEBUG = False


def log_print(msg):
    """
    #TODO сделать описание
    :param msg:
    :return: None
    """
    if DEBUG:
        print(msg)


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
        log_print('Your {0} minutes of computer use have started'.format(session))
        messagebox('EyeSave', 'Your {0} minutes of computer use have started'.format(session))
        time.sleep(session_sec)
        log_print('A break of {0} minutes!'.format(pause))
        messagebox('EyeSave', 'A break of {0} minutes!'.format(pause))
        time.sleep(pause_sec)
        log_print('Break is over! Starting a {0}-minute session?'.format(session))
        messagebox('EyeSave', 'Break is over! Starting a {0}-minute session?'.format(session))


def main():
    parser = argparse.ArgumentParser(
        description='EyeSave - script for eye safety'
    )
    parser.add_argument('-s', '--session', help='the time you will be working at the computer '
                                                '(in minutes)', type=int, default=20)
    parser.add_argument('-p', '--pause', help='time that you will rest (in minutes)', type=int, default=5)
    parser.add_argument('-l', '--log', help='enable messages in the console', action='store_true', default=False)
    parser.add_argument('-d', '--disable', help='disabling the GUI and messagebox', action='store_true', default=False)

    args = parser.parse_args()

    if args.log:
        global DEBUG
        DEBUG = True
    timer_start(session=args.session, pause=args.pause)


if __name__ == '__main__':
    main()
