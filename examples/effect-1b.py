#!/usr/bin/env python3

#
# This example uses a console buffer implementation to perform fast rendering of text.
# Performance measurements are displayed.
# Performance might vary greatly from system to system.
#



import sys
import time
import datetime

from jk_console import *
from jk_console.demo import *









Console.clear()

#e = Effect1(width=Console.width()*3//4, height=Console.height()*3//4)
e = Effect1(2, 2, width=Console.width()*2//3, height=Console.height()*2//3)

e.runForever()


