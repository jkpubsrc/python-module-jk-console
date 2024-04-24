Console
=======

### Common Constants

* `str RESET`
* `str RESET_TOPLEFT`
* `str BOLD`
* `str UNDERLINE`
* `str STRIKETHROUGH`

### Common Methods

* `tuple<int,int> getSize()`
* `int width()`
* `int height()`
* `tuple<int,int> getCursorPosition()`
* `void printAt(int x, int y, str text, bool bFlush = true)`
* `int getTextWidth(str text)`
* `str stripESCSequences(str text)`
* `void moveCursorTo(int x, int y, bool bFlush = true)`
* `void clear()`
* `void flush()`

Input
-----

### Keys

`<TODO>`

### List of Key Constants

* `dict<str,str> ALL_KEYS_TO_KEY_NAME`

Each tuple has two elements:

* The key code
* The name of the constant

* `dict<str,str> ALL_KEY_NAMES_TO_KEY`

Each tuple has two elements:

* The name of the constant
* The key code

* `set<str> ALL_SPECIAL_KEYS`

### Methods

* `bool isSpecialKey(str key)`
* `str readKey()`
* `str readKeyWithTimeout(int timeoutSeconds)`


### Color Constants

ForeGround
----------

### Color Constants

* `str BLACK`
* `str DARK_GRAY`
* `str GRAY`
* `str LIGHT_GRAY`
* `str WHITE`

* `str RED`
* `str ORANGE`
* `str YELLOW`
* `str YELLOWGREEN`
* `str GREEN`
* `str GREENCYAN`
* `str CYAN`
* `str CYANBLUE`
* `str BLUE`
* `str BLUEVIOLET`
* `str VIOLET`
* `str VIOLETRED`

* `str DARK_RED`
* `str DARK_ORANGE`
* `str DARK_YELLOW`
* `str DARK_YELLOWGREEN`
* `str DARK_GREEN`
* `str DARK_GREENCYAN`
* `str DARK_CYAN`
* `str DARK_CYANBLUE`
* `str DARK_BLUE`
* `str DARK_BLUEVIOLET`
* `str DARK_VIOLET`
* `str DARK_VIOLETRED`

* `str LIGHT_RED`
* `str LIGHT_ORANGE`
* `str LIGHT_YELLOW`
* `str LIGHT_YELLOWGREEN`
* `str LIGHT_GREEN`
* `str LIGHT_GREENCYAN`
* `str LIGHT_CYAN`
* `str LIGHT_CYANBLUE`
* `str LIGHT_BLUE`
* `str LIGHT_BLUEVIOLET`
* `str LIGHT_VIOLET`
* `str LIGHT_VIOLETRED`

* `str STD_BLACK`
* `str STD_BLUE`
* `str STD_GREEN`
* `str STD_CYAN`
* `str STD_RED`
* `str STD_PURPLE`
* `str STD_DARKYELLOW`
* `str STD_LIGHTGRAY`
* `str STD_DARKGRAY`
* `str STD_LIGHTBLUE`
* `str STD_LIGHTGREEN`
* `str STD_LIGHTCYAN`
* `str STD_LIGHTRED`
* `str STD_LIGHTPURPLE`
* `str STD_YELLOW`
* `str STD_WHITE`

### List of Color Constants

* `tuple<str,str>[] ALL_STD_COLORS`

Each tuple has two elements:

* The color code
* The name of the constant

### Methods

* `str getByName(str name)`
* `str rgb256(int r, int g, int b)`
* `str rgb1(float r, float g, float b)`
* `str hsl1(float h, float s, float l)`

BackGround
----------

### Color Constants

* `str BLACK`
* `str DARK_GRAY`
* `str GRAY`
* `str LIGHT_GRAY`
* `str WHITE`

* `str RED`
* `str ORANGE`
* `str YELLOW`
* `str YELLOWGREEN`
* `str GREEN`
* `str GREENCYAN`
* `str CYAN`
* `str CYANBLUE`
* `str BLUE`
* `str BLUEVIOLET`
* `str VIOLET`
* `str VIOLETRED`

* `str DARK_RED`
* `str DARK_ORANGE`
* `str DARK_YELLOW`
* `str DARK_YELLOWGREEN`
* `str DARK_GREEN`
* `str DARK_GREENCYAN`
* `str DARK_CYAN`
* `str DARK_CYANBLUE`
* `str DARK_BLUE`
* `str DARK_BLUEVIOLET`
* `str DARK_VIOLET`
* `str DARK_VIOLETRED`

* `str LIGHT_RED`
* `str LIGHT_ORANGE`
* `str LIGHT_YELLOW`
* `str LIGHT_YELLOWGREEN`
* `str LIGHT_GREEN`
* `str LIGHT_GREENCYAN`
* `str LIGHT_CYAN`
* `str LIGHT_CYANBLUE`
* `str LIGHT_BLUE`
* `str LIGHT_BLUEVIOLET`
* `str LIGHT_VIOLET`
* `str LIGHT_VIOLETRED`

* `str STD_BLACK`
* `str STD_BLUE`
* `str STD_GREEN`
* `str STD_CYAN`
* `str STD_RED`
* `str STD_PURPLE`
* `str STD_DARKYELLOW`
* `str STD_LIGHTGRAY`

### List of Color Constants

* `tuple<str,str>[] ALL_STD_COLORS`

Each tuple has two elements:

* The color code
* The name of the constant

### Methods

* `str getByName(str name)`
* `str rgb256(int r, int g, int b)`
* `str rgb1(float r, float g, float b)`
* `str hsl1(float h, float s, float l)`

































