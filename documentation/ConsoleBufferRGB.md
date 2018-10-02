ConsoleBufferRGB
================

Construction
------------

Example:

```python
buffer = ConsoleBufferRGB(
	width = 123,
	height = 45,
	bgColor = 255,
	bWithCaching = True
	)
```

Properties
----------

* `tuple<int,int> size`
	* *Description:* 
* `int width`
	* *Description:* 
* `int height`
	* *Description:* 

Methods
-------

### Core Methods

* `void bufferToBuffer(int ofsX, int ofsY, ConsoleBufferRGB other, bool bForceFullRepaint = false)`
	* *Description:* Pass on the data of this buffer to the buffer in variable `other`.
	* If `bForceFullRepaint` is set to `true` the full data is transferred, not only the cells in the buffer that have been changed.
* `void bufferToConsole(int ofsX, int ofsY, bool bForceFullRepaint = false)`
	* *Description:* Pass on the data of this buffer to the console.
	* If `bForceFullRepaint` is set to `true` the full data is transferred, not only the cells in the buffer that have been changed.
* `void clearInternalCache()`
* `void fullRepaint()`

### Drawing Methods

* `void clear()`
	* *Description:* Fill the whole buffer with the background color. Enforces full repaint.
* `void fill(int bgColor, int fgColor, char character)`
	* *Description:* Fill the whole buffer with data. Enforces full repaint.
	* *Arguments:*
		* `int bgColor` : 
		* `int fgColor` : 
		* `char character` : 
* `void fillRectangle(int x, int y, int w, int h, int bgColor, int fgColor, char character)`
	* *Description:* Fill part of the buffer with data.
	* *Arguments:*
		* `int x` : x-position where to begin filling
		* `int y` : y-position where to begin filling
		* `int w` : width of the area to fill
		* `int h` : height of the area to fill
		* `int bgColor` : background color to use or `None`
		* `int fgColor` : foreground color to use or `None`
		* `char character` : character to use in filling
* `void set(int x, int y, int bgColor, int fgColor, char character)`
	* *Description:* 
	* *Arguments:*
		* `int x` : x-position where set the data
		* `int y` : y-position where set the data
		* `int bgColor` : background color to use or `None`
		* `int fgColor` : foreground color to use or `None`
		* `char character` : character to use
* `void setSafe(int x, int y, int bgColor, int fgColor, char character)`
	* *Description:* 
	* *Arguments:*
		* `int x` : x-position where set the data
		* `int y` : y-position where set the data
		* `int bgColor` : background color to use or `None`
		* `int fgColor` : foreground color to use or `None`
		* `char character` : character to use
* `void printText(int x, int y, int bgColor, int fgColor, str text)`
	* *Description:* 
	* *Arguments:*
		* `int x` : x-position where set the text
		* `int y` : y-position where set the text
		* `int bgColor` : background color to use or `None`
		* `int fgColor` : foreground color to use or `None`
		* `str text` : the text to put at the specified position








