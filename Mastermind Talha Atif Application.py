import os
from pygame import *
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 50) #Puts screen in top right corner, 50 pixels down

import pygame #Imports everything needed   
import math 
import random   
BLUE=       (0, 0, 255) #Sets all colour values
RED=        (255 ,0 ,0)
GREEN=        (0,255,0)
YELLOW=   (255, 255, 0)
SELECT= (130, 159, 255)
ORANGE=   (255, 165, 0)
GRAY=      (68, 68, 68)
LBlue=    (0, 102, 204)
DBlue=     (0, 82, 165)
GRAY=      (40, 40, 40)
LGray=     (65, 65, 65)
WHITE=  (255, 255, 255)
BLACK=        (0, 0, 0)
pygame.init()
SIZE =       (1000, 700) #Sets screen size
screen = pygame.display.set_mode(SIZE) #Sets screen variable
fontHello = font.SysFont("Times New Roman", 25) #Sets font and font sizes for fontHello and fontStart
fontStart = font.SysFont("Times New Roman", 50)
textOG= "MASTERMIND" #Sets text for intro scene

colourChoice= [BLUE,RED,GREEN,YELLOW,WHITE,ORANGE] #List of colours in actuall RGB code form (for drawing on screen)
colourNames= ['BLUE','RED','GREEN','YELLOW','WHITE','ORANGE'] #List of colours (in same order) in string form (for determining code to guess)

running = True #Sets boolean that keeps while loop running

def Restart(gameStatus): #Function that runs restart screen
    global running #Brings global variable running and code 
    global code
    run = True
    mClick= 0 #Amount of times the mouse clicks on the screen
    while run == True: #This is true as long as the mouse doesnt click on either of the buttons
        draw.rect(screen, GRAY, (0,0,1000,700)) #Draws backround
        draw.circle(screen, (70,200,70), (300, 350), 75) #Draws restart circle
        draw.circle(screen, RED, (700, 350), 75) #Draws quit circle
        xCord1=0 #Sets value of xCord1
        for codeCol in code: #Draws whats the code was
            xCord1+=1
            draw.circle(screen, codeCol, (xCord1*90+260, 600),40) #Draws circle for each colour in code
        textOG= ["<>","Yes", "No","The correct code was:"] #List of text to blit
        for cir in range (0,4): #Loop blits each text in List above (textOG) to different location on screen, this only uses one text centering program, keeping things neat 
            if cir == 0:
                xCord= 425 #Puts top text at these cords
                yCord= 150
                if gameStatus == "right":
                    textOG[0] = "You won! Would you like to play again?" #What the prgram displays on top
                elif gameStatus == "wrong": 
                    textOG[0] = "So close! Would you like to play again?"
            elif cir == 3: #Displays "the correct code was" at these cords
                xCord= 425
                yCord= 480
                    
            else:
                yCord= 305 #Restart and Quit buttons
                xCord= (cir*400-175)
            thisFont = font.SysFont("Times New Roman", 55) #Sets font size for all text on restart screen
            text = textOG[cir]
            renderedText = thisFont.render(text , 1, LBlue)#MR VAN ROOYEN TEXT CENTERING CODE
            fontSize = thisFont.size(text) 
            rectangle = (xCord,yCord,150,90) #Location of text + rectange dimentions
            startX = (rectangle[2] - fontSize[0])//2 + rectangle[0] 
            startY = (rectangle[3] - fontSize[1])//2 + rectangle[1]
            centeredRect = (startX, startY, fontSize[0], fontSize[1])
            screen.blit(renderedText, centeredRect)
        display.flip()        #Displats on screen
        for evnt in pygame.event.get(): #Checks for mouse click
            if evnt.type == MOUSEBUTTONDOWN:
                MouseX, MouseY = evnt.pos            
                button = evnt.button #Depending on mouse location, will either restart or end game
                if MouseX > 225 and MouseX< 375: 
                    running = True
                    mClick+=1
                    break
                elif MouseX > 625 and MouseX < 775:
                    running = False
                    mClick+=1
                    break
        if mClick > 0:
            run = False
            return running #returns True and False, which will restart or end code
                    
def Start():
    global text #text is "MASTERMIND"
    pygame.draw.rect(screen, GRAY, (0, 0, 1000, 700))
    for introMove in range (0, 50): #Makes intro scene by drawing many small rectanges in a pattern that goes up and gets longer each time the loop goes through
        for intro in range (0,introMove*5):
            draw.rect(screen, (0,0,255), (980,0,20,20))
            draw.rect(screen, (0,0,255), (0,680,20,20))
            pygame.draw.rect(screen, (intro,0,(255-intro)), ((introMove*10), (700-(intro*3)), 10, 4))
            pygame.draw.rect(screen, (intro,0,(255-intro)), ((990-(introMove*10)), (intro*3), 10, 4))        
            pygame.draw.rect(screen, (intro,0,(255-intro)), ((intro*4), (690-(introMove*10)), 4, 10))        
            pygame.draw.rect(screen, (intro,0,(255-intro)), ((1000-(intro*4)), (introMove*10), 4, 10))
        time.wait(20)
        pygame.display.flip() #Only displays 49 times, to avoid lag 
            
    for cir in range (0,10): #Writes mastermind inside of 8 circles, all centered
        pygame.draw.circle(screen, SELECT,((cir*100+50),350),45) #Draws cirlces
        rectange= (((cir*100+5),305,90,90),5)
        
        thisFont = font.SysFont("Times New Roman", 75) 
        text = textOG[cir]
        renderedText = thisFont.render(text , 1, LBlue) #MR VAN ROOYEN TEXT CENTERING CODE
        fontSize = thisFont.size(text)      
        rectangle = ((cir*100+5),305,90,90)
        startX = (rectangle[2] - fontSize[0])//2 + rectangle[0] #centering the text over the width
        startY = (rectangle[3] - fontSize[1])//2 + rectangle[1]
        centeredRect = (startX, startY, fontSize[0], fontSize[1])
        screen.blit(renderedText, centeredRect) #Writes each letter of mastermind
        pygame.time.wait(120)
        display.flip()
       
    pygame.display.flip()
    pygame.time.wait(1600)
def CalcDistance(CalcX, CalcY, Px, Py): #Finds distance between 2 points 
    VertexDis= (math.sqrt(((CalcX-Px)*(CalcX-Px))+((CalcY-Py)*(CalcY-Py))))  
    return VertexDis
def DrawBoard(): #Draws game board 
    pygame.draw.rect(screen, GRAY, (0, 0, 1000, 700)) #Draws backround
    
    pygame.draw.rect(screen, LBlue, (250, 50, 300, 600)) #Draws board (1 rectange and 2 ellipses)
    pygame.draw.ellipse(screen, LBlue, (200, 50, 100, 600))
    pygame.draw.ellipse(screen, LBlue, (500, 50, 100, 600))  
    
    for e in range (0,8): #Draws rectangles around each turn
        Y= (50+(75*e))
        pygame.draw.rect(screen, DBlue, (250, Y,300,75),5) 
        
    for d in range (1,9): #Draws all the circles (8 turns)
        d= ((d*75)+12.5)
        for z in range (1,5): #Circle template drawing (4 circles per turn)
            z= ((z*75)+212.5)
            pygame.draw.circle(screen, LGray, (z, d),30)
    pygame.display.flip()
   

def ColourChoice(): #Draws colour selecting part
    
    text = "Press enter to" #Displays "Press enter to submit your guess" text, centered
    renderedText = fontHello.render(text , 1, LBlue)
    fontSize = fontHello.size(text) 
    
    rectangle = (727, 600, 140, 20)
    startX = (rectangle[2] - fontSize[0])//2 + rectangle[0]   #MR VAN ROOYEN TEXT CENTERING CODE
    startY = (rectangle[3] - fontSize[1])//2 + rectangle[1]  #Centers font horizontaly and Verticaly by using a rectanlge as the area for the font to be placed in      
    centeredRect = (startX, startY, fontSize[0], fontSize[1])        
    screen.blit(renderedText, centeredRect)
    
    text = "sumbit your guess"
    renderedText = fontHello.render(text , 1, LBlue)
    fontSize = fontHello.size(text) 
    
    rectangle = (727, 620, 140, 20)    
    startX = (rectangle[2] - fontSize[0])//2 + rectangle[0]   #MR VAN ROOYEN TEXT CENTERING CODE
    startY = (rectangle[3] - fontSize[1])//2 + rectangle[1]    #Centers font horizontaly and Verticaly by using a rectanlge as the area for the font to be placed in    
    centeredRect = (startX, startY, fontSize[0], fontSize[1])        
    screen.blit(renderedText, centeredRect)
    
    pygame.draw.rect(screen, LGray, (727, 110, 140, 480)) #Draws rectangle again
        
    for w in range (2,8): #Draws circles for all the colours again, alligned with the board circles
        col= w
        w= ((w*75)+12.5)    
        draw.circle(screen, colourChoice[col-2], (800,w), 30) #Colour is based on which cirlce is being drawn (1st circle is 1st colour in the list etc.)
                
    pygame.display.flip()    
    
def SelectSpot(MouseX,MouseY, AttemptV, Col, turnList): #Function that selects spot on game board, also updates what the current guess is
    AttY= (50+(75*(AttemptV-1))) #Calcules Y cord of cirlces (based on turn)
    for e in range (0,8): #Draws rectangle to highlight current turn
        Y= (50+(75*e))
        pygame.draw.rect(screen, DBlue, (250, Y,300,75),5)
    pygame.draw.rect(screen, (70, 200, 70), (250, AttY,300,75),5)
    PrevDis= 1000
    for d in range (AttemptV,(AttemptV+1)):
        d= ((d*75)+12.5)
        for z in range (1,5): #Calculates which cirlce the mouse was closest to
            z= ((z*75)+212.5)
            VertexDis= CalcDistance(z,d,MouseX, MouseY)
            if PrevDis > VertexDis: #Calculates distance from circle to mouse, finds shortest distance
                Z= z
                D= d
                PrevDis= VertexDis
            
    ColourChoice() #Re-draws color choice board
    pygame.draw.circle(screen, BLACK, (800, colSel),32, 5) #Shows current selected colour by drawing black outline around it
    Z= int((Z- 212.5)/75)
    Before= turnList[Z-1] #Saves value of circle being selected
    turnList[Z-1]= colourNames[currentCol]
    colVal= [0,0,0,0,0,0,0]
    for y in turnList: #If the colour being used is not already in the code, the circle will change to that colour
        if y != 0:
            spot = colourNames.index(y)
            colVal[spot]+=1
    for c in colVal:
        if colVal[currentCol] <= 1:
            Z= ((Z*75)+212.5)            
            pygame.draw.circle(screen, colourChoice[currentCol], (Z, D),30)  
            break
        else:
            pygame.draw.circle(screen,GRAY, (Z,D), 30) #If the colour is already in the code, nothing will change, no circle will be drawn
            turnList[Z-1]= Before            
            break
    pygame.display.flip()
    return turnList
                
def SelectColour(MouseX, MouseY): #Draws circle around colour currently selected and sends current colour back
    PrevDis= 1000
    for d in range (2,8): #Finds which circle is closest to mouse pointer 
        Num = d
        d= ((d*75)+12.5)
        VertexDis= CalcDistance(800,d,MouseX, MouseY)
        if PrevDis > VertexDis:
            D= d
            PrevDis= VertexDis
            currentCol= Num
    ColourChoice() #Re-draws colour picking panel
    pygame.draw.circle(screen, BLACK, (800, D),32, 5) #Draws black circle outline over current selected colour    
    pygame.display.flip() #Displays 
    return D, (currentCol-2) #Returns Y cord for center of selected circle

myClock = pygame.time.Clock() #60 fps (Mr. Van Rooyen Code)
Start() #Displays start screen
start= "Y" #Sets start, the variable that activates the code selected program, to true
while running == True: #while loop that determines if game is running or not
    while start == "Y":
        currentCol= 20 #Sets currentCol to random value that is out of range for colourChoice list
        Attempt= 0 #Sets attempt to 0, goes to 7 once attempt = 8 (which is technically the 9th attempt) the game ends and shows restart screen
        turnList= [0, 0, 0, 0] #Current colours in guess, all set to 0 at begining of each game and each turn
        DrawBoard() #Draws board 
        ColourChoice() #Draws colour choices
        colours= ['BLUE','RED','GREEN','YELLOW','WHITE','ORANGE'] #This loop selects for the Letter colour code
        code= [] 
        for codeColour in range (1,5): #Creats code using random int to pick a random colour in the code
            colour= random.randint(0,len(colours))
            code.append(colours[colour-1]) 
            del colours[colour-1] #This removes 4 random colours from the colours, then adds them to the "code" list
        start = "N" #Turns of while loop that picks code, only picking new one once the user chooses to play again
        #If you put print(code) here, it will print the current answer
        
    for evnt in pygame.event.get(): #Check if left click was pressed or if enter was pressed
        if evnt.type == MOUSEBUTTONDOWN: #If mouse is clicked, any mouse button works
            
            MouseX, MouseY = evnt.pos #Finds location of mouse            
            button = evnt.button 
            if MouseX > 727 and MouseX<867: #If mouse is on the colour selecter, will run colour picking funtion
                colSel, currentCol= SelectColour(MouseX, MouseY) #Sends mouse X and Y cords, receives selected colour and location in colours list
            if MouseX > 240 and MouseX<560 and currentCol != 20 and MouseY < ((((8-Attempt)*75)+12.5)+30) and MouseY > ((((8-Attempt)*75)+12.5)-30): #if mouse is on board AND a colour is selected
                turnList=SelectSpot(MouseX, MouseY,(8-Attempt), colourChoice[currentCol], turnList) #Sends in current colour, mouse cords, attempt number and current turnList which is a list of the colours currently selected for the turn / guess
        if evnt.type == pygame.QUIT: #If X is pressed, game will immediatly end
            running = False
        if evnt.type == KEYDOWN: #If key is pressed
            keyPress = key.get_pressed() 
            if keyPress[K_RETURN]: #If the key pressed is enter:
                count= 0
                eCount= 0
                for e in turnList: #If any colour in the guess is empty, the program will not check the guess (for example if the 3rd colour in the guess still shows as 0, that means no colour is there. Therefore the program will not check how many colours are right and wrong in the code
                    if e == 0:
                        break
                    else:
                        eCount+=1
                if eCount== 4: #If all the items in turnList have a colour, the program will check the guess
                    Attempt+=1 #Attempt goes up once it gets to this part
                    AttY= (50+(75*(7-Attempt))) #Sets Y value in relation to attempt number
                    pygame.draw.rect(screen, DBlue, (250, (AttY+75),300,75),5) #Draws a blue rectanlge over the previous turns green rectangle                        
                    pygame.draw.rect(screen, (70, 200, 70), (250, AttY,300,75),5) #Draws a green rectangle over the current turn
                    display.flip() 
                    guess= [] #Since im using a list of strings to check the code, I can use my exact same guess checking from my thinking section
                    correctSpot= 0
                    wrongSpot= 0
                    k=0
                    for j in turnList: #Checks for right spot
                        guess.append(turnList[k])
                        if j == code[k]:
                            correctSpot+=1
                            k+=1
                        else: #Checks for wrong spot
                            k+=1                                
                            for h in code:
                                if j == h:
                                    wrongSpot+=1   
                    turnList= [0, 0, 0, 0] #resets turnlist
                    if guess == code or Attempt==8: #when the attempt is 8 or the code is right
                        if guess == code: #If the code is right, I will call function Restart and send in "right" which will display "you won" on the restart screen. The reason I put this if statement before the Attempt == 8 statement is that if the guess is correct on the 8th turn, it will still show "you won"
                            running= Restart("right")
                        elif Attempt == 8: #If on the 8th attempt the code is still wrong, it will show "nice try" on the restart screen
                            running= Restart("wrong")
                        if running == True: #Restart will send back a value for running, True or False, if running is true and the game continues, the variable that starts the code selecting loop will become "Y" again, in this case "Y" acts like True 
                            start = "Y"
                                         
                    else: #If the attempt is not 8 and the code is not right, it display how many colours are right and wrong
                        fontCheck= font.SysFont("Times New Roman", 25) #Sets reasonable font size
                        text = (("%s Right %s Wrong") %(correctSpot,wrongSpot)) #Font is set, displaying how many are right and wrong, which was calculated in the loop above
                        renderedText = fontCheck.render(text , 1, WHITE) #Sets font
                        fontSize = fontCheck.size(text) #MR VAN ROOYEN TEXT CENTERING CODE
                        
                        checkText= (((8-Attempt)*75)+50)   
                        rectangle = (10, checkText, 200, 75)
                        startX = (rectangle[2] - fontSize[0])//2 + rectangle[0]   #Centers font horizontaly and Verticaly by using a rectanlge as the area for the font to be placed in
                        startY = (rectangle[3] - fontSize[1])//2 + rectangle[1]        
                        centeredRect = (startX, startY, fontSize[0], fontSize[1])      
                        screen.blit(renderedText, centeredRect) #Displays text
                        
                        display.flip() #Displays font
                    break
    myClock.tick(60)
pygame.quit()

