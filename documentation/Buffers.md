Buffers
=======

For efficiently displaying text in a terminal window buffers can be used. Buffers store character and color values. They can be filled as needed with data. After filling it with data you can transfer this buffer to the console. During this transfer only the delta between the existing character and color data and the new data is calculated and sent to the terminal window.

Calculating this difference is computationally expensive to some extent. If very large regions of a terminal window needs to be updated, it might be better to update the full screen without these computations. Therefor there are these two modes:

* The default mode where the difference from last state and new state is calculated,
* the "force-full-update" mode where the entire display area will be updated.

You can choose between these different kind of buffer systems:

* `ConsoleBuffer`
	* *Description:* This buffer consists of cells that contain a character and string based color data where background and foreground is stored in the same color data field.
	* *Links:* [Class: ConsoleBuffer](ConsoleBuffer.md)
* `ConsoleBufferRGB`
	* *Description:* This buffer consists of cells that contain a character and integer based color data where background and foreground is stored in two different color data fields.
	* *Links:* [Class: ConsoleBufferRGB](ConsoleBufferRGB.md)













