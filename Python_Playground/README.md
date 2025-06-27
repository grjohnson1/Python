# Python_Playground

## Description
This covers projects from the ***Python Playground (Second Edition)*** by Mahesh Venkitachalam.

# Preparing
Go to main Python_Arena ReadMe file for steps on how to instill the information required to run the projects.

# Python Scripts

## drawTriangle.py
Simple drawing of a Triangle where I personally added a color for each line.

`py drawTriangle`
![image](https://github.com/user-attachments/assets/53ae2b36-9cab-4d86-b491-588fe7418997)

## koch.py
This is the Koch Snowflake being drawn.

`py koch.py`

## spiro.py
Draw various spirographs using simple calculation. Default will draw 4 random spirographs and once fully drawn it will start a new set over and over again. But you can pass parameters in to generate a specific design.

Default: `py spiro.py`
![Screenshot 2025-06-24 120601](https://github.com/user-attachments/assets/0ff6dcda-a755-4c0e-85c8-6aee897fb6c0)

Passing parameters examples:

`py spiro.py -- 300 100 0.9`

`py spiro.py -- 300 200 0.6`

`py spiro.py -- 300 200 0.2`

## conway.py
Conway's game of life is a cellular automation game that has a set of rule on how the cells will expand/grow.

`py conway.py`
![Screenshot 2025-06-24 122532](https://github.com/user-attachments/assets/dd6ea2ce-12a9-4851-81dc-246344ef1afe)

See Conway_Figure_1.png as example of saving the game down at a particular time which was close to the end where only block (2x4 square), loaf (surrounded/circular like), blinker (1x3 line), or glider (almost points in a direction) is left.

## ks.py
Karplus String algorithm is used to generate musical notes in a pentatonic scale. Creates a WAV file for each musical note. Will check if musical note is created before writing file. The minor pentatonic notes are used as they sound relatively nice when randomly combined with the other minor notes.

`py ks.py` - will write the WAV files. C4 Eb, F, G, and Bb.

`py ks.py --display` - will play the notes and display a plot of the waves the musical note plays.

`py ks.py --play` - will randomly play the musical notes. Will need to `CTRL+C` to stop running the program.

Note: this requires `pip install PyAudio`

## boids.py
This is a bird migration simulator. Boids is a how a New Yorker would pronounce bird. This works with the three core rules: Separation, Alignment, and Cohesion for each bird.

Doing a left mouse click will add a new bird to the flock. A right mouse click will scatter the birds similar as if they encountered an obstacle.

`py boids.py` - will render 100 in the center and they will move from there.

`py boid.py --num-boids #` - will render the number of birds entered. The default is 100.

Note: this requires `pip install scipy`

## ascii.py
This will take an image (png or jpg) and convert it into ASCII characters. You can choose the default of 10 characters or go with 70 characters. This take the value of the image as a grayscale and determines what level of gray it is at each section (row, column).

`py ascii.py --file [location/of/data/file.jpg]` - renders with 10 characters used

`py ascii.py --file [location/of/data/file.jpg] --morelevels` - renders with 70 characters used

Other parameters:
* `--scale [font_name]` - will change the font from Courier to value specified
* `--out [file_name]` - will change the output filename from the default of 'out'
* `--cols #` - will set the number of columns for the ASCII text
