# /usr/bin/env python
# Importing tkinter for the GUI
from tkinter import *
import random, csv, time
from tkinter import messagebox
# Function to lead in data from text files
def loadfile(detailslist,file,d):
    # Opens the file with every new line being when there is a space
    with open(file, newline='') as csvfile:
        # Reads each piece of data as one thing until there is a space
        userdata = csv.reader(csvfile, delimiter=d)
        # Looping through each row in the file
        for row in userdata:
            # Adds each row from the file to the list
            detailslist.append(row)
# Creating a class for buttons to be added to the screen
class button():
    # Initiating the varibales for the buttons
    def __init__(self,canvas,xpos,ypos,bgcolour,number,height,width,position,command,id,row,column,cube,type):
        self.type = type
        # Setting row so it can be called by itself
        self.row = row
        # Setting column so it can be called by itself
        self.column = column
        # Setting cube so it can be called by itself
        self.cube = cube
        # Setting id so it can be called by itself
        self.id = id
        # Setting command so it can be called by itself
        self.command = command
        # Setting canvas so it can be called by itself
        self.canvas = canvas
        # Setting position so it can be called by itself
        self.position = position
        # Setting height so it can be called by itself
        self.height = height
        # Setting wdith so it can be called by itself
        self. width = width
        # Setting xpos so it can be called by itself
        self.xpos = xpos
        # Setting ypos so it can be called by itself
        self.ypos = ypos
        # Setting bgcolour so it can be called by itself
        self.bgcolour = bgcolour
        # Setting row so it can be called by itself
        self.number  = number
        # Creates a button based on details given
        self.button = Button(self.canvas,text=self.number,bg=self.bgcolour,command=self.buttonpressed,font=('Arial',15))
        # Places the button onto the canvas using predetermined x and y positions
        self.button.place(x=self.xpos,y=self.ypos,height=self.height,width=self.width)
    # Representing the objects as strings for debugging
    def __repr__(self):
        return '<%s %s %s %s %s %s %s %s %s %s %s %s %s>' % (self.canvas,self.xpos,self.ypos,self.bgcolour,self.number,self.height,self.width,self.position,self.command,self.id,self.row,self.column,self.cube)
    # Function to be called when a button on the sudoku grid is pressed
    def buttonpressed(self):
        # If a button on the grid has been pressed it will run the following code
        if self.command == 'grid':
            # Setting all logic to true in a list
            numbers = [True,True,True,True,True,True,True,True,True]
            # Starting a for loop which will run through every object the button class has created
            for i in grid:
                # Checking if the position of all buttons are in the same grid, coloumn or cube as the button the user wants to add a value to
                if i.cube == self.cube or i.column == self.column or i.row == self.row:
                    # Looping for a range of  9  starting from 1
                    for a in range(1,10):
                        # Checking if the button has a value of 1,2,3,4,5,6,7,8 or 9
                        if i.number == a:
                            # If there is a button that already has that value it will tell the system by setting that position in the numbers list to false
                            numbers[a-1] = False
            # Making options a global variable so it can be used throughout the code
            global options
            # Creating a new canvas ontop of the old one so it can allow the user to select the number they wish to add to the puzzle
            options = Frame(canvas,bg=bgcolour,highlightthickness=0) ; options.place(x=0,y=0,width=500,height=600)
            # Setting x position
            xpos = 62.5
            # Setting y position
            ypos = 137.5
            # Looping 9 times sud
            for i in range(1,10):
                # Amending x position each time the loop runs
                xpos +=75
                # Check if the xpos is at the max value the grid wants it to be
                if xpos == 362.5:
                    # Amending y position so that the grid is symmetrical
                    ypos +=75
                    # Resetting x position back to the first value
                    xpos = 137.5
                # Creating buttons to allow the user to select a number to add to the system
                button_to_edit = button(options,xpos,ypos,bgcolour,i,75,75,None,'choice',self,None,None,None,None)
                # Checking which numbers cannot be added to the intended position because there is already a number in that row, column or cube
                if numbers[i-1] == False:
                    # Turning the numbers that cannot be added to the new button to red and disabling them to show the user they cannot be used
                    button_to_edit.button.config(bg='#B55252',state='disabled')
            # Creating a button using the button class to add a blank button to the sudoku grid
            button(options,137.5,362.5,bgcolour,'',75,225,None,'choice',self,None,None,None,None)
        # If a button on the options canvas is pressed it will run the code below
        if self.command == 'choice':
            # Setting the number of the button to the number the user wants it to be
            self.id.number = self.number
            # Chagning the value of the button on them sudoku grid
            self.id.button.config(text=self.number)
            # Closes the window once the user has chosen a number to add ot the button they clicked on
            options.destroy()
            # If the button is clicked while in the game mode it will excute this code
            if self.id.type == 'game':
                # Setting variavle test to true
                test = True
                # Looping through list of objects
                for i in grid:
                    # If the object is blank it will set test to false
                    if i.number == '':
                        # Setting variable test to false
                        test = False
                    else:
                        # If the number is 0 which means blank it will also set test to false
                        if int(i.number) == 0:
                            # Setting variable test to false
                            test = False
                # If the test is true it means the game has ended
                if test:
                    # Stopping timer
                    stop()
                    # Chagning time to a green colour
                    lb.config(fg='green')
                    # Creating a button to allow the user to start a new game
                    newgame = Button(canvas,text='New game',bg=bgcolour,font=('Arial',15),command=lambda:creategame(None,'random')) ; newgame.place(x=20,y=495,height=40,width=150)
                    temp.destroy()
                    # Creating a button to allow the user to add their score to the scoreboard
                    scorebutton = Button(canvas,text='Add to scoreboard',bg=bgcolour,font=('Arial',15),command=addscore) ; scorebutton.place(x=175,y=495,height=90,width=145)

# Creating a class to manage scores
class scoreboards():
    def __init__(self,name,time,puzzle,difficulty):
        self.difficulty = difficulty
        # Setting name so it can be called by itself
        self.name = name
        # Setting time so it can be called by itself
        self.time = time
        # Setting puzzle so it can be called by itself
        self.puzzle = puzzle
    def __repr__(self):
        # Making string format for objects in the class
        return '{},{},{},{}'.format(self.name,self.time,self.puzzle,self.difficulty)
# Function to add a score to the scoreboard
def addscore():
    def appendscore():
        # validating that the time is more than 00:00:00
        if str(t.get()) == '00:00:00':
            scoreframe.destroy()
            messagebox.showwarning('Warning','Time to solve puzzle cannot be less than 00:00:01')
        # Setting check to true
        check = True
        # Looping through each letter in name entry to see if there is a space
        for i in nameentry.get():
            if i == ' ':
                # Setting check to false if a space is found
                check = False
        # Checking that something has been entered and thay it is not longer than 25 characters
        if len(nameentry.get()) > 0 and len(nameentry.get()) < 25 and check:
            test = True
            for i in scoreboardlist:
                if i.name == str(nameentry.get()) and i.time == str(t.get()) and i.puzzle == puzzlecode and i.difficulty == difficultycheck:
                    test = False
                    break
            if test == True:
                # Appending new score to the list of scores
                scoreboardlist.append(scoreboards(str(nameentry.get()),str(t.get()),puzzlecode,difficultycheck))
                # Destroying the frame once a score has been added
                scoreframe.destroy()
                # Opening file where the scores are to be saved
                file = open('scoreboard.txt', 'w')
                # Looping through each score in the list of scores
                for i in scoreboardlist:
                    # Appending the scores to the file scoreboard.txt
                    file.write(str(i))
                    # Adding a new line every time a score has been added to the file
                    file.write('\n')
                # Closing the file of scores
                file.close()
            else:
                scoreframe.destroy()

        else:
            # Label displaying an error if one has occured
            Label(scoreframe,text='Name must be between 1 and 25 characters \n and cannot contain spaces',font=("Courier 40 bold",10),bg=bgcolour,fg='darkred').place(x=125,y=330)
    # Creating a frame for the name of the user to be entered
    scoreframe = Frame(canvas,bg=bgcolour,highlightthickness=0) ; scoreframe.place(x=0,y=0,width=windowwidth,height=windowheight)
    global nameentry
    nameentry = Entry(scoreframe,bg=bgcolour,font=('Arial',20),) ; nameentry.place(x=154,y=200,height=50,width=200)
    # Adding a button so the user can submit there name to the system
    nameentrybutton = Button(scoreframe,text='Enter name',bg=bgcolour,font=('Arial',15),command=appendscore) ; nameentrybutton.place(x=154,y=275,height=40,width=200)
    # Creates the button to allow the user to go back to the previous page
    backbutton = Button(scoreframe,text='Back',bg=bgcolour,font=('Arial',15),command=lambda:scoreframe.destroy()) ; backbutton.place(x=20,y=545,height=40,width=150)

# Creates the background for all the widgets
def background():
    global canvas
    # Creating a canvas for widgets to be appended to
    canvas = Canvas(window,bg=bgcolour,highlightthickness=0) ; canvas.place(x=0,y=0,width=windowwidth,height=windowheight)
# Creating empty list for easy sudoku puzzles to be stored
easy = []
# Calls function so the file easy_puzzles can be read into "easy" list
loadfile(easy,'easy_puzzles.txt',' ')

hard = []
# Calls function so the file easy_puzzles can be read into "easy" list
loadfile(hard,'hard_puzzles.txt',' ')

# Function create a back button that goes back to the preious page
def back(place,phrase):
    # Function to go back to previous page
    def goback(place):
        # Deletes the old canvas
        canvas.destroy()
        if phrase == None:
            place()
        else:
            # Starts function to create the new canvas
            place(phrase)
    # Creates the button to allow the user to go back to the previous page
    backbutton = Button(canvas,text='Back',bg=bgcolour,font=('Arial',15),command=lambda:goback(place)) ; backbutton.place(x=20,y=545,height=40,width=150)

# Creating a funciton to check the cube position of a number
def cube_position(num):
    # Setting varibale to 0
    no = 0
    # Setting variable to 0
    pos = 0
    # Starting loop from 0 to the length of array which holds the numbers of positions each cube in the sudoku grid
    for x in range(0,len(array)):
        # Checking if the position is equal to the index of the number entered
        try:
            pos = array[x].index(num)
            break
        # If there is an exception it will pass to the next lines in the code
        except:
            pass
    # Setting variable to x
    no = x
    # Returning variable no
    return no

# Function to solve sudoku puzzle
def solve_puzzle():
    # Creating an empty list for the numbers in the grid to go
    g = []
    # Looping through each object in the grid list
    for i in grid:
        if i.number == '':
            g.append(0)
        else:
            # Appending the number of the buttons to the list g
            g.append(i.number)
    # Setting variable i to 0
    d = 0
    # Making board global so it can be used throughut the code
    global board
    # Defining board as a empty list
    board=[]
    # Looping unitl it reaches the end of the list
    while d < len(g):
      # Making a nested loop every 9 numbers so the grid is easier to calculate
      board.append(g[d:d+9])
      # Increasing the variable i by 9 each pass
      d+=9

    def valid(bo, num, pos):
      # Check row
      for i in range(len(bo[0])):
          if bo[pos[0]][i] == num and pos[1] != i:
              return False
      # Check column
      for i in range(len(bo)):
          if bo[i][pos[1]] == num and pos[0] != i:
              return False
      # Check box
      box_x = pos[1] // 3
      box_y = pos[0] // 3
      for i in range(box_y*3, box_y*3 + 3):
          for j in range(box_x * 3, box_x*3 + 3):
              if bo[i][j] == num and (i,j) != pos:
                  return False
      return True
    # Checks if the button is empty or has a number in it
    def find_empty(bo):
        for i in range(len(bo)):
           for j in range(len(bo[0])):
               if bo[i][j] == 0:
                   return (i, j)  # row, col
        return None

    # Function to solve sudoku
    def solved(bo):
      # Checking for empty spaces
      find = find_empty(bo)
      if not find:
          return True
      else:
          row, col = find
      # Looping 9 times starting from 1
      for i in range(1,10):
          # Checking if move is valid
          if valid(bo, i, (row, col)):
              bo[row][col] = i
              if solved(bo):
                  return True
              bo[row][col] = 0
      return False
    solved(board)
    # Putting the nested list back into a single array so it can be displayed on the GUI
    newarray = [j for i in board for j in i]
    # Looping through each button on the grid and appending their new value to show the solved sudoku grid
    for i in range(0,len(grid)):
        # Setting the value of the button to it's solved value
        grid[i].number = newarray[i]
        if newarray[i] == 0:
            newarray[i] = ''
        # Setting the test of each button to their solved number
        grid[i].button.config(text=newarray[i])
# Creating a fucntion to clear the sudoku grid of all numbers
def clear():
    # Looping through evrey object in the buttons class
    for i in grid:
        # Setting all buttons on the sudoku grid to blank
        i.button.config(text='')
        # Setting the number of the button to 0 which tells the code its an empty space
        i.number = 0
# Creating a function to make the sudoku grid
def table(type):
    background()
    # Frame to create a border around the buttons to make it look like a sudoku puzzle
    frame = Frame(canvas,bg='black',width=467,height=467.5) ; frame.place(x=20,y=20)
    # Setting x position to -25 because the first loop will make it start at 25
    xpos = -25
    # Setting y position to 25
    ypos = 25
    checklist = [27,54,81]
    # Looping 81 times som that all buttons in the grid cann be added
    for i in range(0,81):
        # Check if the button position is divisble by 3 which means that there needs to be an increased gap toi allow the border behind to be shown
        if i != 0 and i%3==0:
            # Amending x position
            xpos+=54
        else:
            # Amending x position
            xpos +=50
        # Checking if x position is at it's max so it can be reset
        if xpos == 487:
            # This checks if the button is in a position where the next position of the next button needs to be a little further away so it can show the black background behind to make the sudoku borders
            if i in checklist:
                # Amending y position
                ypos +=54
            else:
                # Amending y position
                ypos +=50
            # reseting x position
            xpos = 25
        # Creating buttons for the sudoku grid
        a = button(canvas,xpos,ypos,'white','',50,50,i,'grid',None,i//9,i%9,cube_position(i),type)
        clear()
        # Appending the objects created to a list so they can be used as pointers to each button
        grid.append(a)
    # Returns to prvious page
    back(home,None)
# Timer for the sudko game
# setting time to = 0
global count
# Setting count to 0
count = 0
# Function to reset the timer
def reset():
    global count
    count=1
    t.set('00:00:00')
# Funciton to start the timer
def start():
    global count
    count=0
    # Start the timer
    start_timer()
# Function to actually start the timer
def start_timer():
    global count
    timer()
# Function to stop the timer
def stop():
    global count
    count=1
# Function to create the timer
def timer():
    global count
    if(count==0):
        d = str(t.get())
        h,m,s = map(int,d.split(":"))
        h = int(h)
        m=int(m)
        s= int(s)
        if(s<59):
            s+=1
        elif(s==59):
            s=0
            if(m<59):
                m+=1
            elif(m==59):
                h+=1
        if(h<10):
            h = str(0)+str(h)
        else:
            h= str(h)
        if(m<10):
            m = str(0)+str(m)
        else:
            m = str(m)
        if(s<10):
            s=str(0)+str(s)
        else:
            s=str(s)
        d=h+":"+m+":"+s
        t.set(d)
        if(count==0):
            canvas.after(930,start_timer)

def endgame(diff):
    # Stops the timer
    stop()
    lb.config(fg='darkred')
    # Button to solve the sudoku puzzle
    newgame = Button(canvas,text='New game',bg=bgcolour,font=('Arial',15),command=lambda:creategame(diff,None,'random')) ; newgame.place(x=20,y=495,height=40,width=150)
    # Solves the puzzle that is displayed on the sudko board
    solve_puzzle()

def difficulty():
    background()
    canvas.create_text(250,75,text='Difficulty',fill='yellow',font=('copperplate gothic bold',50))
    easybutton = Button(canvas,text='Easy',bg=bgcolour,font=('Arial',15),command=lambda:game('easy','random'),fg=fgcolour) ; easybutton.place(x=154,y=250,height=40,width=200)
    hardbutton = Button(canvas,text='Hard',bg=bgcolour,font=('Arial',15),command=lambda:game('hard','random'),fg=fgcolour) ; hardbutton.place(x=154,y=300,height=40,width=200)
    back(home,None)
# A function to create a new random game of sudoku
def creategame(diff,puzz,type):
    global temp
    temp = Frame(canvas,bg=bgcolour,highlightthickness=0) ; temp.place(x=175,y=495,height=50,width=150)
    # Creating a button to end the game
    endgamebutton = Button(canvas,text='End game',bg=bgcolour,font=('Arial',15),command=lambda:endgame(diff)) ; endgamebutton.place(x=20,y=495,height=40,width=150)
    # Globaling the time variable so it can be used elsewhere in the code
    global t
    # Variable for setting the time
    t = StringVar()
    # Setting the time to 0
    t.set("00:00:00")
    # Globaling timer label so it can be used elsewhere
    global lb
    # Adding timer to screen
    lb = Label(canvas,textvariable=t,font=("Courier 40 bold",30),bg=bgcolour) ; lb.place(x=320,y=490)
    # Starting timer
    start()
    global difficultycheck
    difficultycheck = diff
    if diff == 'easy':
        diffarray = easy
    elif diff == 'hard':
        diffarray = hard
    if type == 'random':
        # Picks a random sudoku puzzle from the list
        randomgame = random.choice(diffarray)
        # Turns the sudoku puzzle into a readable list for the next stage of the code
        a = list(randomgame[0])
        # Finding the index of randomgame to be able to display the puzzle number
        global puzzlecode
        puzzlecode = diffarray.index(randomgame)
    # If the user searched for a game it will show the searched puzzle number instead of a random one
    elif type == 'searched':
        # Making variable a the searched puzzle
        a = puzz
        # Finding the puzzle number and assigning it to variavle "id"
        puzzlecode = diffarray.index([''.join(a)])
    # Displaying the puzzle number on the canvas
    puzzlenumber = Label(text='Puzzle {}'.format(puzzlecode),font=("Courier 40 bold",25),bg=bgcolour) ; puzzlenumber.place(x=320,y=540)
    # Looping for the length of the puzzle
    for i in range(0,len(a)):
        # If the puzzle has a 0 it converts it into a blank space so it is clear on the sudoku grid
        if a[i] == '0':
            # Setting the value to a blank space
            a[i] = ''
    # Looping 81 times starting from 0
    for i in range(0,81):
        # Amending the value of the button on the sudoku grid
        grid[i].button.config(text=a[i],state='active',activebackground='white')
        # Goes to next line if the grid contains a blank
        if a[i] == '':
            # Changes the blanks to 0 so it can be assigned to the object
            a[i] = 0
        # Setting the value of the button for validation
        grid[i].number = int(a[i])
        # Looping through objects in the grid list
        for i in grid:
            # If the number is not a blank then it will disable the button becuase it will be the starting point of the puzzle
            if i.number != 0:
                # The set number are set to disabled state as changing them would ruin the puzzle starting point
                i.button.config(state='disabled',disabledforeground='black')
    # When in use the code below will fill all but one square of the grid so I can test what happens when it gets solved more qucikly
    '''z = [9,4,2,7,6,1,8,5,3,3,8,7,5,9,2,6,4,1,6,1,5,8,3,4,2,9,7,2,6,3,1,4,7,5,8,9,8,7,1,9,2,5,3,6,4,4,5,9,3,8,6,1,7,2,7,9,6,2,1,8,4,3,5,5,2,8,4,7,3,9,1,6,1,3,4,6,5,9,7,2,'']
    for i in range(0,81):
        grid[i].button.config(text=z[i])
        grid[i].number = z[i]'''
# Function to create the scoreboard for the sudoku puzzles
def scoreboard(diff):
    def puzzlescoreboard():
        if diff == 'easy':
            array = easy
        elif diff == 'hard':
            array = hard
        # Setting variable check to true
        check = True
        # Checking if entry is a integer
        if not scoresearch.get().isdigit():
            # Setting variable check to false
            check = False
        # Checking if the entry widget it empty
        elif len(scoresearch.get()) < 1 or int(scoresearch.get()) > len(array):
            # Setting variable check to falose
            check = False
        else:
            # Looping through each chatacter in the entry
            for i in scoresearch.get():
                # If there is a space it will set the check to false
                if i == ' ':
                    # Setting variable check to false
                    check = False
        # If all checks have passed it will start the game with the valid puzzle number entered
        if check:
            # Creating background canvas
            background()
            # Adding the scoreboard title to the canvas
            canvas.create_text(250,25,text='Scoreboard',fill='Yellow',font=('copperplate gothic bold',40))
            # Adding the textbox for the names to displayed in
            namescores = Text(canvas,bg=bgcolour) ; namescores.place(x=22,y=58,height=454,width=466)
            # Adding the text box for the times to be displayed in
            timescores = Text(canvas,bg=bgcolour,borderwidth=0) ; timescores.place(x=254,y=60,height=450,width=232)
            # Inserting the text 'Name:' into the top of the scoreboard where the names will be displayed
            namescores.insert(END, 'Name:')
            # Inserting the text "Time:" into the top of the scoreboard where the times will be displayed
            timescores.insert(END, 'Time:')
            objects = []
            # Looping through the list of scores
            for i in scoreboardlist:
                # Checking if the scores are for the same puzzle the user wants to view the scoreboard for
                if int(i.puzzle) == int(scoresearch.get()) and i.difficulty == diff:
                    # Appending objects with the search puzzle number to list
                    objects.append(i)
            # Setting answer to true
            answer = True
            # Setting counter to check if a swap has been made at least once
            count = 1
            # Checking if count is still 1 (at least one swap was made)
            while count == 1:
                # Setting count to 0 so loop will break if no swaps are preformed while sorting the list
                count = 0
                # Looping through list of objetcs with the puzzle numbers that the user searched for
                for i in range(len(objects)-1):
                    # Checking if times are different
                    if objects[i].time != objects[i+1].time:
                        # Checking if the hours in both times are diffferent
                        if objects[i].time[0:2] != objects[i+1].time[0:2]:
                            # Checking if the first time is greater than the second
                            if objects[i].time[0:2] > objects[i+1].time[0:2]:
                                # If the first time is greater it will set answer to true
                                answer = True
                            else:
                                answer = False
                        # Checking if the minutes in both times are diffferent
                        elif objects[i].time[3:5] != objects[i+1].time[3:5]:
                            if objects[i].time[3:5] > objects[i+1].time[3:5]:
                                # If the first time is greater it will set answer to true
                                answer = True
                            else:
                                answer = False
                        # Checking if the seconds in both times are diffferent
                        elif objects[i].time[6:8] != objects[i+1].time[6:8]:
                            # Checking if the first time is greater the next time in the list of times
                            if objects[i].time[6:8] > objects[i+1].time[6:8]:
                                # If the first time is greater it will set answer to true
                                answer = True
                            else:
                                answer = False
                    else:
                        check +=1
                        if check == len(objects)-1:
                            break
                    # If the first time is greater then it will swap positions in the list so that overall the fastest times are at the start
                    if answer == True:
                        # Swapping the position of objects in the list
                        objects[i], objects[i+1] = objects[i+1], objects[i]
                        # Setting count to one to carry on the recursive loop
                        count = 1
            for i in objects:
                # Checking if the scores are for the same puzzle the user wants to view the scoreboard for
                if int(i.puzzle) == int(scoresearch.get()):
                    # Inserting new line
                    namescores.insert(END,'\n')
                    # Inseritng new line
                    timescores.insert(END,'\n')
                    # Inseritng the names into the scoreboard
                    namescores.insert(END, i.name)
                    # Inserting the times into the scoreboard
                    timescores.insert(END, i.time)
            # Disabling the textbox so it cannot be changed
            namescores.config(state='disabled')
            # Disabling the textbox so it cannot be changed
            timescores.config(state='disabled')
            # Adding a label to show the puzzle number of the scoreboard shown
            Label(text='Puzzle {}'.format(scoresearch.get()),font=("Courier 40 bold",25),bg=bgcolour).place(x=300,y=540)
            # Creating a function to disable the mousewheel so the user has to use the scroll bar provided
            def scrollwheel(event):
                return 'break'
            # Creating a function to move both text box with the same scroll wheel
            def multiple_yview(*args):
                timescores.yview(*args)
                namescores.yview(*args)
            # Making a scrollbar for the textbox
            scrollb = Scrollbar(timescores,orient=VERTICAL,command=multiple_yview)
            # Setting the scrollbar to control the textboxs
            timescores.configure(yscrollcommand=scrollb.set)
            namescores.configure(yscrollcommand=scrollb.set)
            # Adding the scrollbar to the textbox7
            scrollb.pack(side=RIGHT,fill=Y)
            # Binding the mousewheel to the fucntion which disables it
            namescores.bind('<MouseWheel>', scrollwheel)
            timescores.bind('<MouseWheel>', scrollwheel)
            # Creating a back button to go to the previous page
            back(scoreboard,diff)
        else:
            Label(canvas,text='Puzzle number is invalid',font=("Courier 40 bold",10),bg=bgcolour,fg='darkred').place(x=125,y=330)
    background()
    canvas.create_text(250,75,text='Enter puzzle number\n  to find scoreboard',fill='yellow',font=('copperplate gothic bold',20))
    scoresearch = Entry(canvas,bg=bgcolour,font=('Arial',20),) ; scoresearch.place(x=154,y=200,height=50,width=200)
    scoresearchbutton = Button(canvas,text='Find scoreboard',bg=bgcolour,font=('Arial',15),command=puzzlescoreboard) ; scoresearchbutton.place(x=154,y=275,height=40,width=200)
    back(scoreboardcheck,None)

def scoreboardcheck():
    background()
    canvas.create_text(250,75,text='    Puzzle\nDifficulty?',fill='yellow',font=('copperplate gothic bold',50))
    easybutton = Button(canvas,text='Easy',bg=bgcolour,font=('Arial',15),command=lambda:scoreboard('easy'),fg=fgcolour) ; easybutton.place(x=154,y=250,height=40,width=200)
    hardbutton = Button(canvas,text='Hard',bg=bgcolour,font=('Arial',15),command=lambda:scoreboard('hard'),fg=fgcolour) ; hardbutton.place(x=154,y=300,height=40,width=200)
    back(home,None)
# Starts the sudoku game
def game(diff,type):
    # Emptys the grid list so it can be repopulated with the latest data
    grid.clear()
    # Calling the table function so it draws the sudoku grid on the GUI
    table('game')
    # Button to solve the sudoku puzzle
    newgame = Button(canvas,text='New game',bg=bgcolour,font=('Arial',15),command=lambda:creategame(diff,'game',type)) ; newgame.place(x=20,y=495,height=40,width=150)
def puzzle_search(diff):
    # Function to start the puzzle game that was searched
    def searchpuzzleno():
        if diff == 'easy':
            array = easy
        elif diff == 'hard':
            array = hard
        # Setting variable check to true
        check = True
        # Checking if the entry widget it empty
        if len(searchentry.get()) < 1 or int(searchentry.get()) > len(array)-1:
            # Setting variable check to false
            check = False
        # Checking if entry is a integer
        elif not searchentry.get().isdigit():
            # Setting variable check to false
            check = False
        else:
            # Looping through each chatacter in the entry
            for i in searchentry.get():
                # If there is a space it will set the check to false
                if i == ' ':
                    # Setting variable check to false
                    check = False
        # If all checks have passed it will start the game with the valid puzzle number entered
        if check:
            # Creating the sudoku game format
            game(diff,'searched')
            # Appending the seached puzzle to the sudoku board
            creategame(diff,list(array[int(searchentry.get())][0]),'searched')
        else:
            Label(canvas,text='Puzzle not found',bg=bgcolour,fg='darkred',font=('Arial',15)).place(x=170,y=540,height=40,width=150)
    # Emptys the grid list so it can be repopulated with current data
    grid.clear()
    # Creating sudoku table for looks while the search is going on
    table('game')
    # Creating a entry widget so users can search for specific puzzles
    searchentry = Entry(canvas,font=('Arial',20),bg=bgcolour) ; searchentry.place(x=20,y=495,height=40,width=150)
    # Creating a button to click when the user wants to submit a search for a certain puzzle
    searchbutton = Button(canvas,text='Search',bg=bgcolour,font=('Arial',15),command=searchpuzzleno) ; searchbutton.place(x=180,y=495,height=40,width=150)

def checkdiff():
    background()
    canvas.create_text(250,75,text='Difficulty',fill='yellow',font=('copperplate gothic bold',50))
    easybutton = Button(canvas,text='Easy',bg=bgcolour,font=('Arial',15),command=lambda:puzzle_search('easy'),fg=fgcolour) ; easybutton.place(x=154,y=250,height=40,width=200)
    hardbutton = Button(canvas,text='Hard',bg=bgcolour,font=('Arial',15),command=lambda:puzzle_search('hard'),fg=fgcolour) ; hardbutton.place(x=154,y=300,height=40,width=200)
    back(home,None)
# Function to create the suduko solver screen
def calc():
    # Clearing the grid so it can be populated with the latest data
    grid.clear()
    # Calling the table function so it draws the sudoku grid on the GUI
    table('')
    # Globaling solve and remove so they can be destroyed in other functions
    global solve, remove
    # Button to solve the sudoku puzzle
    solve = Button(canvas,text='Solve',bg=bgcolour,font=('Arial',15),command=solve_puzzle) ; solve.place(x=20,y=495,height=40,width=150)
    # Button to clear the sudoku grid
    remove = Button(canvas,text='Clear',bg=bgcolour,font=('Arial',15), command=clear) ; remove.place(x=195,y=495,height=40,width=150)
# Function to create the main menu
def home():
    # Creating a background canvas
    background()
    # Creeating label for homescreen
    canvas.create_text(250,75,text='Sudoku',fill='yellow',font=('copperplate gothic bold',50))
    # Creating a button to play a sudoku game
    play = Button(canvas,text='Random Game',bg=bgcolour,font=('Arial',15),command=difficulty,fg=fgcolour) ; play.place(x=154,y=200,height=40,width=200)
    # Creating a button to search for specific puzzles
    search = Button(canvas,text='Puzzle Search',bg=bgcolour,font=('Arial',15),command=checkdiff,fg=fgcolour) ; search.place(x=154,y=250,height=40,width=200)
    # Creating a button to solve a sudoku puzzle
    ans = Button(canvas,text='Solver',bg=bgcolour,font=('Arial',15),command=calc,fg=fgcolour) ; ans.place(x=154,y=300,height=40,width=200)
    # Creating a button to close the window
    score = Button(canvas,text='Scoreboard',bg=bgcolour,font=('Arial',15),command=scoreboardcheck,fg=fgcolour) ; score.place(x=154,y=350,height=40,width=200)
    # Creating a button to close the window
    close = Button(canvas,text='Close',bg=bgcolour,font=('Arial',15),command=lambda: window.destroy(),fg=fgcolour) ; close.place(x=154,y=400,height=40,width=200)
# Empty list which will be populated with objects from the class of buttons
grid = []
# Creating an array of number of which the sudoku is split into cubes so I can calcuate which cube each button is in
array = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],
        [27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],
        [54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
# Creating tkinter window for sudoku GUI
window = Tk()
# Setting title of window
window.title('Sudoku')
# Setting the window width
windowwidth = 508
# Setting the window height
windowheight = 600
# Setting the background colour
bgcolour = '#7D8FA5'
# Setting the foreground colour
fgcolour = 'yellow'
# Setting size of window to '500x600'
window.geometry('{}x{}'.format(windowwidth,windowheight))
# Setting the window so it cannot be resized
window.resizable(height=False,width=False)
# Gloabling scoreboardlist so it can be used throughout the code
global scoreboardlist
# Creating an empty list for scoreboard data to go
scoreboardlist= []
# Loading data into the scoreboardlist list
with open('scoreboard.txt', newline='') as csvfile:
    # Reads each piece of data as one thing until there is a space
    userdata = csv.reader(csvfile, delimiter=',')
    # Looping through each row in the file
    for row in userdata:
        # Adds each row from the file to the list
        scoreboardlist.append(scoreboards(row[0],row[1],row[2],row[3]))
# Initiating the tkiner window so it automatically opens when the code it run
home()
# Allows the window to start when the code is run
if __name__ == "__main__":
    window.mainloop()
