
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2022.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#

student_number = 10880623 # put your student number here as an integer
student_name   ='caitlinwenck' # put your name here as a character string

#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  BREAKOUT
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program runs it fills
#  a map with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client's briefings" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You may NOT change
# any of the code in this section except as indicated by the
# comments marked '*****'.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define the length of the sides of the cells. All other dimensions
# for the drawing canvas are calculated relative to this value.
# ***** If necessary you can change this value to alter the
# ***** overall size of the drawing canvas, but only do so
# ***** as a last resort. A better option is to change the
# ***** resolution of your computer's screen. Setting the value
# ***** below too small will limit the space available for drawing
# ***** symbols and making it too big may cause the canvas
# ***** to be too large for the marker's screen.
cell_side = 50 # pixels (default is 50)

# Derive constant values used in the main program that sets up
# the drawing canvas.  Do NOT change any of these values.
cell_width = cell_side + (2 * (cell_side * cos(radians(60)))) # some trigonometry!
cell_height = 2 * (cell_side * sin(radians(60))) # and some more!
x_margin = cell_width * 2.5 # the size of the margin left and right of the map
y_margin = cell_height // 1.5 # the size of the margin below and above the map
window_height = 8 * cell_height + y_margin * 2 # the drawing canvas' height
window_width = 8 * cell_width + x_margin * 2 # the drawing canvas' width
coord_font = ('Arial', cell_side // 3, 'normal') # text font for coords
label_font = ('Arial', cell_side // 2, 'normal') # text font for labels

# Validity check on dimensions - do not change this code
assert (40 <= cell_side <= 60), \
       'Cell sides must be between 40 and 60 pixels in length'

#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  Do
# NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('motion_data.py'):
    print('\nData module found ...')
    from motion_data import steps
    def movements(new_seed = randint(0, 999)):
        print('Using seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return steps() # return the random data set
else:
    print('\nNo data module available!\n')
    def movements(dummy_parameter = None):
        return [] # return an empty data set

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Map----------------------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_map(bg_colour = 'light grey',
               line_colour = 'slate grey',
               draw_map = True,
               add_text = True): # NO! DON'T CHANGE THIS CODE!
    
    # Set up the drawing canvas with enough space for the map and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the map
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the map
    left_edge = -(8.5 * cell_width) // 2 
    bottom_edge = -(7 * cell_height) // 2

    # Optionally draw the map
    if draw_map:

        # Mark the home coordinate
        home()
        dot(cell_side // 4)

        # Draw the cells row by row
        for rows in range(8):
            # Draw upper half of row
            goto(left_edge, bottom_edge + (rows * cell_height))
            pendown()
            setheading(0) # face east
            for angle in ([60, -60, -60, 60] * 6)[:-1]:
                left(angle)
                forward(cell_side)
            penup()
            # Draw lower half of row
            goto(left_edge, bottom_edge + (rows * cell_height))
            pendown()
            setheading(0) # face east
            for angle in ([-60, 60, 60, -60] * 6)[:-1]:
                left(angle)
                forward(cell_side)
            penup()

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_height // 1.2 # pixels
        for x_label in range(11):
            goto(left_edge - (cell_width // 4) + ((x_label + 1) * (cell_width // 1.32)),
                 bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = coord_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_side // 5, cell_height // 10 # pixels
        for y_label in range(15):
            goto(left_edge + (cell_width * 8.7), bottom_edge + (y_label * (cell_height // 2)) - y_offset)
            write(str(y_label + 1), align = 'left', font = coord_font)


    # Optionally mark the blank spaces ... HANDS OFF! YOU CAN'T CHANGE ANY OF THIS CODE!
    if add_text:
        # Write to the left of the map
        goto(-(4.4 * cell_width), -(cell_height // 2))
        write('Draw the\nfour levels of\nyour object or\nentity here', align = 'right', font = label_font)
        # Write to the right of the map
        goto(4.8 * cell_width, -cell_height)
        write('Your final\nmessage\n(if any) will\nappear\nhere', align = 'left', font = label_font)
        

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(False)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_map(hide_cursor = True):
    tracer(False) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Function to Write a Message------------------------------------#
#
# The function in this section writes a message to the screen.  You
# can use it to write your closing message at the end of the
# simulation.
#

def write_breakout_message(step_num):
    penup()
    color('firebrick')
    goto(cell_width * 4.8, -cell_height * 0.25)
    write('Breakout\nat Step ' + str(step_num) + '!',
          align = 'left', font = label_font)

#
#--------------------------------------------------------------------#



#-----Code to Create Drawing Canvas----------------------------------#
#
# This part of the main program sets up the canvas, ready for you to
# draw your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the map and other elements, by
# ***** providing arguments to this function call
create_map(add_text = False)


# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of the
# ***** object or entity shown in your solution
title("The Cloud Effect")

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.  ALL of your solution code
#  must appear in, or be called from, function "follow_path".  Do
#  NOT put any of your code in any other parts of the program and do
#  NOT change any of the provided code except as allowed in parts
#  of the main program marked '*****'.
#

# All of your code goes in, or is called from, this function

def follow_path(dataset, bool):

    def texttitle():
        #Add text title
        goto(-600,250)
        write('\nWeather', font = label_font)
    texttitle()
    
    def hexagon_cell():
        #Draw Hexagon Border
        for i in range(6):
            width(2)
            forward(cell_side)
            left(60)

    setheading(-90)
    forward(100)
    setheading(0)
    forward(20)
    setheading(0)
    def sun():
        setheading(0)
        #Filling in Hexagon with Colour, Fill etc.
        fillcolor('sky blue')
        pencolor('black')
        pendown()
        begin_fill()
        hexagon_cell()
        end_fill()
        penup()

        #Start Drawing of Sun
        width(2)
        forward(25)
        left(90)
        forward(40)
        pendown()
        speed('fastest')
        fillcolor('yellow')
        pencolor('orange')
        for i in range(20):
            right(70)
            forward(30)
            back(30)
            left(90)
        penup()
        #Circle
        fillcolor('yellow')
        setheading(0)
        forward(20)
        setheading(90)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
    sun()


    def text1():
        #Add text below hexagon
        goto(-590,110)
        pencolor('black')
        write('\nA.Clear', font = label_font)
    text1()
    
    setheading(-90)
    forward(100)
    setheading(0)
    forward(15)
    def cloudy():
        #Call Hexgon
        setheading(0)
        pencolor('black')
        fillcolor('sky blue')
        pendown()
        begin_fill()
        hexagon_cell()
        end_fill()
        penup()

        #Draw Sun
        width(2)
        setheading(90)
        forward(10)
        setheading(180)
        forward(5)
        setheading(0)
        forward(25)
        left(90)
        forward(40)
        pendown()
        speed('fastest')
        fillcolor('yellow')
        pencolor('orange')
        for i in range(20):
            right(70)
            forward(25)
            back(25)
            left(90)
        setheading(0)
        forward(15)
        setheading(90)
        fillcolor('yellow')
        begin_fill()
        circle(15)
        end_fill()
        penup()

        #Draw Cloud
        setheading(0)
        forward(15)
        setheading(90)
        back(25)
        setheading(0)
        pencolor('white')
        pendown()
        fillcolor('white')
        begin_fill()
        circle(8,180)
        right(100)
        circle(10,150)
        right(100)
        circle(15,180)
        right(100)
        circle(8,200)
        right(70)
        circle(18,50)
        right(70)
        circle(8,120)
        end_fill()
        penup()

    cloudy()

    def text2():
        #Add text below hexagon
        goto(-590,-30)
        pencolor('black')
        write('\nB.Cloudy', font = label_font)
    text2()

    setheading(-90)
    forward(100)
    setheading(0)
    forward(15)
    def raining():
        #Draw Hexagon
        setheading(0)
        pencolor('black')
        fillcolor('dark grey')
        pendown()
        begin_fill()
        hexagon_cell()
        end_fill()
        penup()

        #Draw Cloud
        setheading(0)
        forward(25)
        setheading(90)
        forward(50)
        setheading(0)
        width(1)
        pencolor('black')
        pendown()
        fillcolor('light grey')
        begin_fill()
        circle(6,180)
        right(100)
        circle(8,150)
        right(100)
        circle(12,180)
        right(100)
        circle(6,200)
        right(70)
        circle(16,50)
        right(70)
        circle(6,120)
        end_fill()
        penup()

        #Draw Another Cloud
        setheading(0)
        forward(25)
        setheading(-10)
        width(1)
        pencolor('black')
        pendown()
        fillcolor('light grey')
        begin_fill()
        circle(6,180)
        right(80)
        circle(8,120)
        right(80)
        circle(12,150)
        right(80)
        circle(6,200)
        right(70)
        circle(16,50)
        right(70)
        circle(6,120)
        end_fill()
        penup()

        #Rain Drops
        color("blue")
        speed("fastest")
        penup()
        left(-90)
        forward(10)
        setheading(0)
        back(20)
        setheading(0)
        dot(size=3)
        setheading(-70)
        forward(10)
        penup()
        setheading(0)
        back(20)
        setheading(0)
        dot(size=5)
        setheading(-70)
        forward(10)
        penup()
        setheading(0)
        back(20)
        setheading(0)
        dot(size=4)
        setheading(-70)
        forward(10)
        penup()
        setheading(0)
        forward(15)
        setheading(0)
        dot(size=6)
        setheading(-70)
        forward(15)
        setheading(0)
        forward(15)
        setheading(0)
        setheading(70)
        forward(15)
        dot(size=4)
        penup()
    raining()

    def text3():
        #Add text below hexagon
        goto(-590,-170)
        pencolor('black')
        write('\nC.Raining', font = label_font)
    text3()

    setheading(-90)
    forward(100)
    setheading(0)
    forward(15)
    def storming():
        #Draw Hexagon
        setheading(0)
        pencolor('black')
        fillcolor('dark blue')
        pendown()
        begin_fill()
        hexagon_cell()
        end_fill()
        penup()

        #Draw Cloud
        setheading(0)
        forward(25)
        setheading(90)
        forward(50)
        setheading(0)        
        width(1)
        pencolor('black')
        pendown()
        fillcolor('light grey')
        begin_fill()
        circle(6,180)
        right(100)
        circle(8,150)
        right(100)
        circle(12,180)
        right(100)
        circle(6,200)
        right(70)
        circle(16,50)
        right(70)
        circle(6,120)
        end_fill()
        penup()

        #Draw Another Cloud
        setheading(0)
        forward(25)
        setheading(-10) 
        width(1)
        pencolor('black')
        pendown()
        fillcolor('light grey')
        begin_fill()
        circle(6,180)
        right(80)
        circle(8,120)
        right(80)
        circle(12,150)
        right(80)
        circle(6,200)
        right(70)
        circle(16,50)
        right(70)
        circle(6,120)
        end_fill()
        penup()

        #Rain Drops
        color("blue")
        speed("fastest")
        pencolor('dark blue')
        penup()
        left(-90)
        forward(5)
        setheading(0)
        back(20)
        setheading(0)
        pendown()
        setheading(-70)
        forward(10)
        penup()
        setheading(0)
        back(20)
        setheading(0)
        pendown()
        setheading(-70)
        forward(10)
        penup()
        setheading(0)
        back(20)
        setheading(0)
        pendown()
        setheading(-70)
        forward(10)
        penup()

        #Lightning Bolt 1
        pencolor('black')
        setheading(90)
        forward(20)
        setheading(0)
        pendown()
        fillcolor('yellow')
        begin_fill()
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(15)
        setheading(0)
        right(-70)
        forward(9)
        setheading(180)
        forward(5)
        setheading(0)
        right(-55)
        forward(10)
        setheading(180)
        forward(5)
        setheading(0)
        right(-50)
        forward(14)
        end_fill()
        penup()

        #Lightning Bolt 2
        pencolor('black')
        setheading(0)
        forward(20)
        pendown()
        fillcolor('yellow')
        begin_fill()
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(15)
        setheading(0)
        right(-70)
        forward(9)
        setheading(180)
        forward(5)
        setheading(0)
        right(-55)
        forward(10)
        setheading(180)
        forward(5)
        setheading(0)
        right(-50)
        forward(14)
        end_fill()
        penup()

        #Draw Lightning Bolt 3
        pencolor('black')
        setheading(0)
        forward(20)
        pendown()
        fillcolor('yellow')
        begin_fill()
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(10)
        setheading(0)
        forward(5)
        right(130)
        forward(15)
        setheading(0)
        right(-70)
        forward(9)
        setheading(180)
        forward(5)
        setheading(0)
        right(-55)
        forward(10)
        setheading(180)
        forward(5)
        setheading(0) 
        right(-50)
        forward(14)
        end_fill()
        penup()

    storming()

    def text4():
        #Add text below hexagon
        goto(-590,-310)
        pencolor('black')
        write('\nD.Storming', font = label_font)
    text4()

    # Algorithm:
    # We first process the input dataset. The dataset is a list of lists. The content of the first list is different from the content of the rest of the list. We need to process the first list to get the correct starting setup.
    # We will use two trackers, one for tracking level progression, another one for the direction.
    # We process the rest of the list to get the moving sequence
    # And at the end we iterate the two lists simultaneously to draw out the movement.

    # first create the trackers
    lvltracker = []
    dirtracker = [0]
    
    # Process the first list of the input dataset. 
    # Create a function to process the first list.
    def process_first_list(first_Arg):
        # Go to the bottom right corner of the hexagon as the starting position
        pu()
        home()
        right(120)
        fd(50)
        seth(0)
        # record the location of the starting position
        posx = xcor()
        posy = ycor()

        # evaluate the 3rd element of the list which is the starting level
        if first_Arg[2] == 'Level A':
            sun()
            goto(posx,posy)
            lvltracker.append('sun()')
        elif first_Arg[2] == 'Level B':
            cloudy()
            goto(posx,posy)
            lvltracker.append('cloudy()')
        elif first_Arg[2] == 'Level C':
            raining()
            goto(posx,posy)
            lvltracker.append('raining()')
        elif first_Arg[2] == 'Level D':
            storming()
            goto(posx,posy)
            lvltracker.append('storming()')
        # write the step number 0 if the second argument of the function call follow_path() is True.
        if bool == True:
            color('black')
            write(0, font = label_font)
            goto(posx, posy)
            seth(0)

    process_first_list(dataset[0])
    
    # After we've processed the first list, we can process the rest of the list.
    for data in dataset[1::]:
        if data[2] == 'Decrease':
            if lvltracker[-1] == 'sun()':
                lvltracker.append('sun()')
            elif lvltracker[-1] == 'cloudy()':
                lvltracker.append('sun()')
            elif lvltracker[-1] == 'raining()':
                lvltracker.append('cloudy()')
            elif lvltracker[-1] == 'storming()':
                lvltracker.append('raining()')
        elif data[2] == 'Increase':
            if lvltracker[-1] == 'sun()':
                lvltracker.append('cloudy()')
            elif lvltracker[-1] == 'cloudy()':
                lvltracker.append('raining()')
            elif lvltracker[-1] == 'raining()':
                lvltracker.append('storming()')
            elif lvltracker[-1] == 'storming()':
                lvltracker.append('storming()')
        # when the level indicator is the same, we don't need to change the level.
        else:
            lvltracker.append(lvltracker[-1])
        # also add the direction into the direction tracker.
        dirtracker.append(data[1])


    # now we have two lists, one with the level progression, and one with the direction. We ca iterate them simultaneously to draw out the movement.
    for symbol, dir, step in zip(lvltracker[1::], dirtracker[1::], dataset[1::]):

        # create a function for writing out the steps
        def write_step(step):
            goto(posx, posy)
            color('black')
            write(step[0], font=label_font)
            goto(posx, posy)
            seth(0)

        if dir == 'N':
            # move to the starting position to draw the next step, which is the top left cornor of the hexagon.
            seth(120)
            fd(50)
            seth(60)
            fd(50)
            seth(0)
            # record the starting position so we can return to it once we finish drawing the step.
            posx = xcor()
            posy = ycor()
                   
            # if the starting postion is within the allowed range, we can draw the step.
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            # else we stop drawing and write the return message.
            else:
                write_breakout_message(step[0])
                return
        # repeat the same process for all other directions.
        elif dir == 'NE':
            fd(50)
            left(60)
            fd(50)
            seth(0)
            posx = xcor()
            posy = ycor()
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            else:
                write_breakout_message(step[0])
                return
        elif dir == 'SE':
            fd(50)
            right(60)
            fd(50)
            seth(0)
            posx = xcor()
            posy = ycor()
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            else:
                write_breakout_message(step[0])
                return
        elif dir == 'S':
            seth(300)
            fd(50)
            right(60)
            fd(50)
            seth(0)
            posx = xcor()
            posy = ycor()
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            else:
                write_breakout_message(step[0])
                return
        elif dir == 'SW':
            right(120)
            fd(50)
            right(60)
            fd(50)
            seth(0)
            posx = xcor()
            posy = ycor()
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            else:
                write_breakout_message(step[0])
                return
        elif dir == 'NW':
            left(120)
            fd(50)
            left(60)
            fd(50)
            seth(0)
            posx = xcor()
            posy = ycor()
            if -410 < posx < 360 and -350< posy <270:
                eval(symbol)
                if bool == True:
                    write_step(step)
            else:
                write_breakout_message(step[0])
                return
    

#
#--------------------------------------------------------------------#



#-----Main Program to Call Student's Solution------------------------#
#
# This part of the main program calls your code and provides the
# data set to be visualised.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "movements" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "movements()" as the first argument to
# ***** "follow_path", i.e., for any data set that can be
# ***** returned by calling function "movements" with no seed.
follow_path(movements(), True) # <-- no argument for "movements" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_map()

#
#--------------------------------------------------------------------#
