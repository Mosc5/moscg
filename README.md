# moscg
**Mo**vie **sc**reen **g**rabber takes screenshots from a film representing its color spectrum

## Installation
To run this program you need a python environment. Necessary packages are listed in the requirements.txt.  
`opencv-python` might have to be installed via pip

## Run
Running `gui.py` creates a GUI to input options.  
`moscg.py` allows running the simulation directly from the command line or IDE.

A command line call could look like this:  
`moscg movie.mkv --num 6 --skip 499`  
The path of the movie is a required parameter, the amount of frames and skipped frames use default values if not set (num=4, skip=99).