Image Manipulator

This is a image manipulation program ran through the command line that allows the user to apply these visual transformations: flip, mirror, invert, and a kaleidoscope effect to any jpg|jpeg|png|JPG|JPEG|PNG| image.

This project combines C++ and Python to work with user input, process and render the images.

Features:
- Cross-platformer with Windows, Mac, and Linux
- Can choose from these four options: flip, mirror, invert, or kaleidoscope
- Compares the original image with the manipulated result side-by-side
- Command-line interface input validation
- Displays and saves the kaleidoscope image output

Languages Used:
C++ : User input and control logic 
Python : image manipulation and display 

File Descriptions
main.cpp : Handles the user input, menu display, and passes arguments to Python file below
render.py : Receives the image and manipulation type from C++, processes it

How to Run
- Use command mkdir build to create a build folder
- cd build to go into the build folder
- g++ -std=c++17 -o manipulator ../main.cpp to compile
  either ./manipulator (Mac/Linux) or manipulator (Windows) to run.
(If you get a Python import error: use pip in the command line to install the package: pip3 install opencv-python.)
- Find your valid image file (jpg|jpeg|png|JPG|JPEG|PNG|), put it in your project folder, add it to Git, and run it through the image manipulator.

Resources:
I do not own the framework of this code, it belongs to Lisa Dion. All code in the To-Dos are mine. 


