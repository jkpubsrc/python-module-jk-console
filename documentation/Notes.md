Concepts
========

Rendering a CUI is based on ...

* a viewport object representing the full view port
* one ore more buffer objects representing part of the viewports

Viewport
--------

The viewport is an instance of `ConsoleViewPort` which covers the whole text area of a console window (except the last row).

A viewport consists of

* the default background color
* a set of buffers convering the viewport
* `Cell[,] _cells`: a set of cells (taken from the buffers) representing the whole screen
* various internal color tables

ScreenBuffer
------------

A screen buffer is representing a region of the viewport. It is registered at the viewport object so that the viewport knows the buffer(s).

Each buffer consists of the following fields:

* `int colBG`: a default background color value
* `int _dimmingFactor`: a dimming factor that modifies the colors of this buffer
* `Cell[,] cells`: a set of cells consisting of
	* `str c`: character to display
	* `int colBG`: background color value
	* `int colFG`: foreground color value
	* `str _cc` (private): combined color string
	* `int _oldC` (private): old character to display
	* `int _oldColBG` (private): old background color
	* `int _oldColFG` (private): old foreground color
* `int ofsX` (read only): a horizontal offset absolute to the top left corner of the viewport
* `int ofsY` (read only): a vertical offset absolute to the top left corner of the viewport
* `int zOrder` (read only): z-order of the buffer (lower is lower)
* `ConsoleViewPort viewPort` (read only): a reference to the viewport

The connection of viewports and screen buffers
-----------------------------------------------

The viewport represents the area of a console that can be filled with data.

A buffer contains fields of a limited screen area some CUI controls render into.

A screen buffer is created via the viewport. The viewport knows about all screen buffers, their size and their layering.

Each dialog window must use it's own screen buffer for rendering. Each control in a dialog must render into a screen buffer.

Whenever a buffer is ...

* created,
* destroyed,
* moved,
* resized or
* changed in z-order

... the viewport will collect all cells of the buffers again to suite the new layout.























