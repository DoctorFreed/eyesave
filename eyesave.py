import time
import argparse
import sys
from playsound import playsound


def parse_args():
    """
    The parsing of the passed arguments

    :return: args. An object that contains all passed arguments.
    """
    parser = argparse.ArgumentParser(
        description='EyeSave - script for eye safety'
    )
    parser.add_argument('-s', '--session', help='the time you will be working at the computer '
                                                '(in minutes)', type=int, default=20)
    parser.add_argument('-p', '--pause', help='time that you will rest (in minutes)', type=int, default=5)
    parser.add_argument('-c', '--count', help='the number of sessions that the program will run, one session is one '
                                              'cycle of work and rest.', type=int, default=9000)
    args = parser.parse_args()
    return args


def countdown(interval):
    interval -= 1
    for i in range(interval, -1, -1):
        for j in range(59, -1, -1):
            sys.stdout.write('\rDuration: \
            Minutes {0} Seconds {1} to go'.format(i, j))
            time.sleep(1)
            sys.stdout.flush()


def timer_start(session=20, pause=5, session_count=9000):
    for i in range(session_count):
        playsound(r'c:\windows\media\alarm02.wav')
        countdown(session)
        playsound(r'c:\windows\media\alarm02.wav')
        print('\nBreak time!')
        countdown(pause)
        print('\nsession number: ', i)


def main():
    args = parse_args()
    timer_start(session=args.session, pause=args.pause, session_count=args.count)


if __name__ == '__main__':
    main()
