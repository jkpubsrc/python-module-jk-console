#!/usr/bin/python3

import sys
import _curses
import curses

# https://docs.python.org/3/howto/curses.html
# https://docs.python.org/3/library/curses.html
# https://www.devdungeon.com/content/curses-windows-python
# https://stackoverflow.com/questions/8677627/getting-mouse-presses-on-a-console-window-for-python




def main(screen):
	curses.noecho() 
	screen.keypad(True)
	curses.cbreak() 

	screen.addstr("This is a Sample Curses Script\n")
	if curses.has_colors():
		screen.addstr("Screen supports colors.\n")
	else:
		screen.addstr("Screen does not support colors.\n")
	if curses.can_change_color():
		screen.addstr("Screen supports RGB.\n")
	else:
		screen.addstr("Screen does not support RGB.\n")

	curses.start_color()
	curses.use_default_colors()

	curses.curs_set(0)		# turn off cursor
	curses.mousemask(curses.ALL_MOUSE_EVENTS)


	lastY, lastX = screen.getmaxyx()
	while True:
		key = screen.getch() 
		#screen.erase()

		if key == 27:
			screen.erase()
			break

		if key == curses.KEY_MOUSE:
			_, mx, my, _, _ = curses.getmouse()
			y, x = screen.getyx()
			#screen.addstr('mx, my = %i,%i                \r'%(mx,my))
			sys.__stdout__.write("\x1b[32;40mMOUSE: %i:%i\n\r" % (mx,my))

		y, x = screen.getmaxyx()
		if (lastY != y) or (lastX != x):
			sys.__stdout__.write("\x1b[31;40mScreen size: " + str(x) + ":" + str(y) + "\n\r")
			#sys.__stdout__.flush()
			lastY == y
			lastX == x

		sys.__stdout__.write("\x1b[33;40m" + repr(key) + "\n\r")
		screen.refresh()




curses.wrapper(main)

