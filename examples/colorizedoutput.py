#!/usr/bin/env python3

#
# This example demonstrates how to write colored text to STDOUT.
#




from jk_console import Console




print(Console.ForeGround.CYAN + "Hello World!" + Console.RESET)

print(Console.BackGround.rgb256(128, 0, 0) + "Hello World!" + Console.RESET)








