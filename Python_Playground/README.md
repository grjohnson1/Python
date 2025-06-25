# Python_Playground

## Description
This covers projects from the ***Python Playground (Second Edition)*** by Mahesh Venkitachalam.

# Preparing
Go to main Python_Arena ReadMe file for steps on how to instill the information required to run the projects.

# Python Scripts

## drawTriangle.py
Simple drawing of a Triangle where I personally added a color for each line.

## koch.py
This is the Koch Snowflake being drawn.

## spiro.py
Draw various spirographs using simple calculation. Default will draw 4 random spirographs and once fully drawn it will start a new set over and over again. But you can pass parameters in to generate a specific design.

Default: `py spiro.py`

Passing parameters examples:
`py spiro.py -- 300 100 0.9`
`py spiro.py -- 300 200 0.6`
`py spiro.py -- 300 200 0.2`


## conway.py
Conway's game of life is a cellular automation game that has a set of rule on how the cells will expand/grow.

## ks.py
Karplus String algorithm is used to generate musical notes in a pentatonic scale. Creates a WAV file for each musical note. Will check if musical note is created before writing file. The minor pentatonic notes are used as they sound relatively nice when randomly combined with the other minor notes.

`py ks.py` - will write the WAV files. C4 Eb, F, G, and Bb.

`py ks.py --display` - will play the notes and display a plot of the waves the musical note plays.

`py ks.py --play` - will randomly play the muciscal notes. Will need to `CTRL+C` to stop running the program.


