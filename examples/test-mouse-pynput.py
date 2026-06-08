#!/usr/bin/python3

# sudo pip3 install pynput
# https://pypi.org/project/pynput/
# https://pynput.readthedocs.io/en/latest/
#
# Other:
#	https://www.devdungeon.com/content/colorize-terminal-output-python


import sys

try:
	from pynput.mouse import Listener
except:
	print("Running on X required.")
	sys.exit(0)





def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))



with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	listener.join()




















