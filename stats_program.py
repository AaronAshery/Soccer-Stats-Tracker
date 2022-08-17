#Aaron Ashery

#Use boxScore() to start program


from graphics import *
import math

def display(time):       #takes the time and converts it to minutes and seconds so that it can be read easier
    minutes = int(time // 1)
    seconds = int(time % 1 * 60)
    return minutes,seconds

class Timer:    #this class creates a timer object that can be started, paused, and reset

    def __init__(self,setTime):
        self.setTime = setTime
        self.timeLeft = setTime
        self.now = time.time()
        self.started = False


    def __str__(self):
        s = "Timer set for {:d} minutes".format(setTime)
        return s
        
    def start(self):
        if self.started == True:
            return "already going"
        else:
            self.started = True
            self.now = time.time()
            print("Timer started")

    def pause(self):
        if self.started == True:
            self.timeLeft = self.timeLeft - ((time.time() - self.now) / 60)
            m, s = display(self.timeLeft)
            print("{:d}:{:d}".format(m,s))
            self.started = False
            
        else:
            return "Already paused"

    def inquiry(self):
        if self.started == False:
            m,s = display(self.timeLeft)
            print("{:d}:{:d}".format(m,s))
            return self.timeLeft
        else:
            m,s = display(self.timeLeft-((time.time()-self.now)/60))
            print("{:d}:{:d}".format(m,s))
            return self.timeLeft-((time.time()-self.now)/60)

    def reset(self,setTime):
        self.timeLeft = setTime
        
        
t = Timer(.5)       
        
#----------------------------------------------------------------------
class SquareButton:   #code from class that makes a square button object
                    #originally I had buttons but now it is used as a label for the scoreboard display
                    
    def __init__(self, win, centerX, centerY, size, color, label, textSize):
        leftX = centerX - size/2
        rightX = centerX + size/2
        topY = centerY - size/2
        bottomY = centerY + size/2
        rect = Rectangle(Point(leftX, bottomY), Point(rightX, topY))
        rect.setFill(color)
        rect.draw(win)
        centerPoint = Point(centerX, centerY)
        text = Text(centerPoint, label)
        text.draw(win)
        text.setSize(textSize)
        # information we need to remember about this object:
        self.x1 = leftX
        self.x2 = rightX
        self.y1 = topY
        self.y2 = bottomY
        self.graphicsObject = rect
        self.color = color
        

    def contains(self, point):
        pointX = point.getX()
        pointY = point.getY()
        if (pointX >= self.x1 and pointX <= self.x2 and
            pointY >= self.y1 and pointY <= self.y2):
            return True
        else:
            return False

    def press(self):
        self.graphicsObject.setFill("gray")
        time.sleep(0.2)
        self.graphicsObject.setFill(self.color)


#----------------------------------------------------------------------
def players():          #players creates dictionaries of each teams players and numbers, as well as their goalkeeper
    print("First thing to do is set up the game!")
    print("Please select which team you would like to set up first, home(h) or away(a), then enter the number of the goalkeeper")
    print("After that begin entering the name of the players followed by their number")
    team = input("h/a:")
    if team == "h" or team == "home":
        
        gkH = input("What # is the gk? ")
        players = eval(input("How many players? "))

        homeNumbers = {}
        homeNames = []
        hNumsList = []
        for _ in range(players):

            name = input("Name: ")
            num = input("#: ")
            homeNumbers[name] = num

            homeNames.append(name)
            hNumsList.append(num)
        for keys, values in homeNumbers.items():
            key = keys
            value = values
            print(key , value)     
    elif team == "a" or team == "away":
        
        gkA = input("What # is the gk? ")
        players = eval(input("How many players? "))
        awayNumbers = {}
        awayNames = []
        aNumsList = []
        for _ in range(players):

            name = input("Name: ")
            num = input("#: ")
            awayNumbers[name] = num

            awayNames.append(name)
            aNumsList.append(num)
        for keys, values in awayNumbers.items():
            key = keys
            value = values
            print(key , value)
    print("Now do the same for the opposing team")
    
    if team == "a" or team == "away":
        
        gkH = input("What # is the gk? ")
        players = eval(input("How many players? "))

        homeNumbers = {}
        homeNames = []
        hNumsList = []
        for _ in range(players):

            name = input("Name: ")
            num = input("#: ")
            homeNumbers[name] = num

            homeNames.append(name)
            hNumsList.append(num)
        for keys, values in homeNumbers.items():
            key = keys
            value = values
            print(key , value)
    elif team == "h" or team == "home":

        gkA = input("What # is the gk? ")
        players = eval(input("How many players? "))

        awayNumbers = {}
        awayNames = []
        aNumsList = []
        for _ in range(players):

            name = input("Name: ")
            num = input("#: ")
            awayNumbers[name] = num

            awayNames.append(name)
            aNumsList.append(num)
        for keys, values in awayNumbers.items():
            key = keys
            value = values
            print(key , value)
    return (gkH,gkA,homeNumbers, homeNames,hNumsList,
            awayNumbers, awayNames,aNumsList)

def eventChain():   #the eventchain asks the user for an event and then prompts them what to enter next
                    #depending on what is entered a dictionary is updated to record which player recorded which stat
                    #also the score is updated and tracked
    (gkH,gkA,homeNumbers, homeNames,
     hNumsList, awayNumbers, awayNames,aNumsList) = players()
    win = GraphWin("Second Screen", 100,100)
    hScore = SquareButton(win,25,25,50,"green",0,16)
    aScore = SquareButton(win,75,25,50,"red",0,16)
    homeLabel = Text(Point(25,75), "H")
    homeLabel.draw(win)
    awayLabel = Text(Point(75,75), "A")
    awayLabel.draw(win)
    hGoals = 0
    aGoals = 0
    hCorners = 0
    aCorners = 0
    homeShots = {}
    homeSog = {}
    homeFouls = {}
    homeOffsides = {}
    homeSaves = {}
    homeGoals = {}
    homeAssists = {}
    homeCards = {}
    homeGoalsAgainst = {}
    awayShots = {}
    awaySog = {}
    awayFouls = {}
    awayOffsides = {}
    awaySaves = {}
    awayGoals = {}
    awayAssists = {}
    awayCards = {}
    awayGoalsAgainst = {}
    for num in hNumsList:
        homeAssists[num] = 0
        homeShots[num] = 0
        homeSaves[num] = 0
        homeGoals[num] = 0
        homeSog[num] = 0
        homeOffsides[num] = 0
        homeFouls[num] = 0
        homeCards[num] = "none"
        homeGoalsAgainst[num] = 0
    homeCards["Team"] = "none"
    for num in aNumsList:
        awayAssists[num] = 0
        awayShots[num] = 0
        awaySaves[num] = 0
        awayGoals[num] = 0
        awaySog[num] = 0
        awayOffsides[num] = 0
        awayFouls[num] = 0
        awayCards[num] = "none"
        awayGoalsAgainst[num] = 0
    awayCards["Team"] = "none"

    time = eval(input("How much time do you want on the clock in minutes? "))
    t.reset(time)

    print("To enter an event start by stating if it is for the home team(h) or away team(a)")
    print("Then choose an event: shot(s), foul(f), offsides(o), yellow card(y), red card(r), or corner(c)")
    print("Depending on the event you will either be asked to enter the player's number or the event is over and play is continued")
    print("If it is a shot then the result is either a goal(g), save(s), miss(m), or blocked(b)")
    print("Type pause(p) to stop the clock (you can still enter events), unpause(u) to unpause, or quit(q) to end the program")
    begin = input("Press enter to begin the game")
    t.start()
    while t.inquiry() > 0: 
        possesion = input("Team: ") # h, a
        if possesion == "h" or possesion == "home":
            start = input("Enter event: ") # s, f, o, y, r, c, p(pause)
            if start == "s" or start == "shot":
                num = input("What number? ")
                if num not in hNumsList:
                    print("???")
                else:
                    sResult = input("Result? ") #g, s, m, b
                    if sResult == "g" or sResult == "goal":
                        hGoals += 1
                        hScore = SquareButton(win,25,25,50,"green",hGoals,16)
                        homeGoals[num] += 1
                        homeShots[num] += 1
                        homeSog[num] += 1
                        awayGoalsAgainst[gkA] += 1
                        assisted = input("Who assisted? (Leave blank for no assist)")
                        if assisted == "":
                            pass
                        elif assisted not in hNumsList:
                            print("???")
                        else:
                            homeAssists[assisted] += 1
                    elif sResult == "s" or sResult == "save":
                        awaySaves[gkA] += 1
                        homeSog[num] += 1
                        homeShots[num] += 1
                    elif sResult == "m" or sResult == "miss":
                        homeShots[num] += 1
                    elif sResult == "b" or sResult == "block":
                        homeShots[num] += 1
                    else:
                        pass
            elif start == "f" or start == "foul":
                num = input("What number penalized? ")
                if num not in hNumsList:
                    print("???")
                else:
                    homeFouls[num] += 1
            elif start == "o" or start == "offsides":
                num = input("What number? ")
                if num not in hNumsList:
                    print("???")
                else:
                    homeOffsides[num] += 1
            elif start == "y" or start == "yellow":
                num = input("What number? ")
                if num not in hNumsList:
                    print("???")
                else:
                    homeCards[num] = "yellow"
            elif start == "r" or start == "red":
                num = input("What number? ")
                if num not in hNumsList:
                    print("???")
                else:
                    homeCards[num] = "red"
            elif start == "c" or start == "corner":
                hCorners += 1
            else:
                pass
        elif possesion == "a" or possesion == "away":
            start = input("Enter event: ") # s, f, o, y, r, c
            if start == "s" or start == "shot":
                num = input("What number? ")
                if num not in aNumsList:
                    print("???")
                else:
                    sResult = input("Result? ") #g, s, m, b
                    if sResult == "g" or sResult == "goal":
                        aGoals += 1
                        aScore = SquareButton(win,75,25,50,"red",aGoals,16)
                        awayGoals[num] += 1
                        awayShots[num] += 1
                        awaySog[num] += 1
                        homeGoalsAgainst[gkH] += 1
                        assisted = input("Who assisted? (Leave blank for no assist)")
                        if assisted == "":
                            pass
                        elif assisted not in aNumsList:
                            print("???")
                        else:
                            awayAssists[assisted] += 1
                    elif sResult == "s" or sResult == "save":
                        homeSaves[gkH] += 1
                        awaySog[num] += 1
                        awayShots[num] += 1
                    elif sResult == "m" or sResult == "miss":
                        awayShots[num] += 1
                    elif sResult == "b" or sResult == "block":
                        awayShots[num] += 1
                    else:
                        pass
            elif start == "f" or start == "foul":
                num = input("What number penalized? ")
                if num not in aNumsList:
                    print("???")
                else:
                    awayFouls[num] += 1
            elif start == "o" or start == "offsides":
                num = input("What number? ")
                if num not in aNumsList:
                    print("???")
                else:
                    awayOffsides[num] += 1
            elif start == "y" or start == "yellow":
                num = input("What number? ")
                if num not in aNumsList:
                    print("???")
                else:
                    awayCards[num] = "yellow"
            elif start == "r" or start == "red":
                num = input("What number? ")
                if num not in aNumsList:
                    print("???")
                else:
                    awayCards[num] = "red"
            elif start == "c" or start == "corner":
                aCorners += 1
            else:
                pass
        elif possesion == "quit" or possesion == "q":
            t.pause()
            return (hGoals,aGoals,hCorners,aCorners,homeNumbers,homeShots,
            homeSog,homeFouls,homeOffsides,homeSaves,homeGoals,homeAssists,
            homeCards,homeNames, homeGoalsAgainst,
            awayNumbers,awayShots,awaySog,awayFouls,awayOffsides,awaySaves,
            awayGoals, awayAssists,awayCards,awayNames,awayGoalsAgainst)
        elif possesion == "pause" or possesion == "p":
            t.pause()
        elif possesion == "unpause" or possesion == "u":
            t.start()
        else:
            print("?????")
    t.pause()
    return (hGoals,aGoals,hCorners,aCorners,homeNumbers,homeShots,
            homeSog,homeFouls,homeOffsides,homeSaves,homeGoals,homeAssists,
            homeCards,homeNames, homeGoalsAgainst,
            awayNumbers,awayShots,awaySog,awayFouls,awayOffsides,awaySaves,
            awayGoals, awayAssists,awayCards,awayNames,awayGoalsAgainst)
       
def boxScore():  #box score uses the dictionaries created by eventchain and turns it into an-
                #easy graphic to interpret all of the stats from the game
                #it also creates the more in depth stats

                #boxscore is not the most organized thing in the world and probably
                #could have been done in a better way, but it gets the job done
    (hGoals,aGoals,hCorners,aCorners,homeNumbers,homeShots,
            homeSog,homeFouls,homeOffsides,homeSaves,homeGoals,homeAssists,
            homeCards,homeNames, homeGoalsAgainst,
            awayNumbers,awayShots,awaySog,awayFouls,awayOffsides,awaySaves,
            awayGoals, awayAssists,awayCards,awayNames,awayGoalsAgainst) = eventChain()
    win = GraphWin("Box",1200,600)
    midLine = Line(Point(600,0),Point(600,600))
    midLine.setFill("red")
    midLine.draw(win)
    topLine = Line(Point(0,30),Point(1200, 30))
    topLine.draw(win)
    nameX = 90
    nameY = 40
    dx = 0
    dy = 25
    numX = 15
    numY = 40
    goalsY = 40
    assistsY = 40
    t = Text(Point(15,15), "#")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(90, 15), "Name")
    t.setSize(10)
    t.draw(win)
    for name, num in homeNumbers.items():
        person = Text(Point(nameX,nameY), "{:_<16}".format(name))
        person.setSize(10)
        person.draw(win)
        number = Text(Point(numX,numY), num)
        number.setSize(10)
        number.draw(win)
        nameY += dy
        numY += dy
    teamText = Text(Point(nameX,nameY),"{:_<16}".format("Team"))
    teamText.setSize(10)
    teamText.draw(win)
    for name, value in homeGoals.items():
        goals = Text(Point(175,goalsY),value)
        goals.setSize(10)
        goals.draw(win)
        goalsY += dy
    t = Text(Point(175, 15), "G")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(205, 15), "A")
    t.setSize(10)
    t.draw(win)
    tHomeAssists = 0   
    for name,value in homeAssists.items():
        assists = Text(Point(205, assistsY),value)
        assists.setSize(10)
        assists.draw(win)
        assistsY += dy
        tHomeAssists += value 
    tha = Text(Point(205,assistsY),tHomeAssists)
    tha.setSize(10)
    tha.draw(win)                
    shotsY = 40
    thg = Text(Point(175, assistsY),hGoals)
    thg.setSize(10)
    thg.draw(win)
    tHomeShots = 0
    for name,value in homeShots.items():
        shots = Text(Point(235,shotsY), value)
        shots.setSize(10)
        shots.draw(win)
        shotsY += dy
        tHomeShots += value

    sogY = 40
    tHomeSog = 0
    for name, value in homeSog.items():
        sog = Text(Point(265,sogY),value)
        sog.setSize(10)
        sog.draw(win)
        sogY += dy
        tHomeSog += value
    thSog = Text(Point(265,assistsY),tHomeSog)
    thSog.setSize(10)
    thSog.draw(win)
    foulY = 40
    tHomeFouls = 0
    for name, value in homeFouls.items():
        foul = Text(Point(295,foulY),value)
        foul.setSize(10)
        foul.draw(win)
        foulY += dy
        tHomeFouls += value
    thf = Text(Point(295,assistsY),tHomeFouls)
    thf.setSize(10)
    thf.draw(win)
    yelY1 = 25
    yelY2 = 5
    tHomeYellow = 0
    tHomeRed = 0
    for name, value in homeCards.items():
        yelY1 += dy
        yelY2 += dy
        if value == "yellow":
            yel = Rectangle(Point(317.5, yelY1), Point(332.5,yelY2))
            yel.setFill("yellow")
            yel.draw(win)
            tHomeYellow += 1
        elif value == "red":
            red = Rectangle(Point(347.5, yelY1), Point(362.5,yelY2))
            red.setFill("red")
            red.draw(win)
            tHomeRed += 1
        else:
            pass
    thy = Text(Point(325,assistsY),tHomeYellow)
    thy.setSize(10)
    thy.draw(win)
    thr = Text(Point(355,assistsY),tHomeRed)
    thr.setSize(10)
    thr.draw(win)
    saveY = 40
    tHomeSaves = 0
    for name, value in homeSaves.items():
        save = Text(Point(385,saveY),value)
        save.setSize(10)
        save.draw(win)
        saveY += dy
        tHomeSaves += value
    thSaves = Text(Point(385,assistsY),tHomeSaves)
    thSaves.setSize(10)
    thSaves.draw(win)
    offY = 40
    tHomeOffsides = 0
    for name, value in homeOffsides.items():
        off = Text(Point(475,offY),value)
        off.setSize(10)
        off.draw(win)
        offY += dy
        tHomeOffsides += value
    thOff = Text(Point(475,assistsY),tHomeOffsides)
    thOff.setSize(10)
    thOff.draw(win)

    
    

    t = Text(Point(235, 15,), "S")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(265, 15), "SOG")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(295, 15), "F")
    t.setSize(10)
    t.draw(win)
    y = Rectangle(Point(317.5, 25), Point(332.5,5))
    y.setFill("yellow")
    y.draw(win)
    r = Rectangle(Point(347.5, 25), Point(362.5,5))
    r.setFill("red")
    r.draw(win)
    t = Text(Point(385,15), "SV")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(415,15), "GA")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(445,15), "SF")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(520,15), "SV%")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(475,15), "OFF")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(575,15), "CK")
    t.setSize(10)
    t.draw(win)
    lineX = 160
    while lineX < 580:
        if lineX == 520 or lineX == 580:
            lineX += 30
            pass
        else:
            Line(Point(lineX,0),Point(lineX,600)).draw(win)
            lineX += 30
    lineX = 760
    while lineX < 1180:
        if lineX == 520+600 or lineX == 580+600:
            lineX += 30
        else:
            Line(Point(lineX,0),Point(lineX,600)).draw(win)
            lineX += 30



    thc = Text(Point(575, assistsY),hCorners) #
    thc.setSize(10)
    thc.draw(win)

    copyY = assistsY
            
######################Away side#######################################
    numX = 15+600
    numY = 40
    nameX = 90+600
    nameY = 40
    goalsY = 40
    assistsY = 40
    t = Text(Point(15+600,15), "#")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(90+600, 15), "Name")
    t.setSize(10)
    t.draw(win)
    for name, num in awayNumbers.items():
        person = Text(Point(nameX,nameY), "{:_<16}".format(name))
        person.setSize(10)
        person.draw(win)
        number = Text(Point(numX,numY), num)
        number.setSize(10)
        number.draw(win)
        nameY += dy
        numY += dy
    teamText = Text(Point(nameX,nameY),"{:_<16}".format("Team"))
    teamText.setSize(10)
    teamText.draw(win)
    for name, value in awayGoals.items():
        goals = Text(Point(175+600,goalsY),value)
        goals.setSize(10)
        goals.draw(win)
        goalsY += dy
    t = Text(Point(175+600, 15), "G")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(205+600, 15), "A")
    t.setSize(10)
    t.draw(win)
    
    taAssists = 0
    for name,value in awayAssists.items():
        assists = Text(Point(205+600, assistsY),value)
        assists.setSize(10)
        assists.draw(win)
        assistsY += dy
        taAssists += value
    shotsY = 40
    taShots = 0
    for name,value in awayShots.items():
        shots = Text(Point(235+600,shotsY), value)
        shots.setSize(10)
        shots.draw(win)
        shotsY += dy
        taShots += value
    taa = Text(Point(205+600,shotsY),taAssists)
    taa.setSize(10)
    taa.draw(win)
    
    tas = Text(Point(235+600,shotsY),taShots)
    tas.setSize(10)
    tas.draw(win)
    sogY = 40
    taSog = 0
    for name, value in awaySog.items():
        sog = Text(Point(265+600,sogY),value)
        sog.setSize(10)
        sog.draw(win)
        sogY += dy
        taSog += value
    tas = Text(Point(265+600,shotsY),taSog)
    tas.setSize(10)
    tas.draw(win)
    foulY = 40
    taFouls = 0
    for name, value in awayFouls.items():
        foul = Text(Point(295+600,foulY),value)
        foul.setSize(10)
        foul.draw(win)
        foulY += dy
        taFouls += value
    taf = Text(Point(295+600,shotsY),taFouls)
    taf.setSize(10)
    taf.draw(win)
    yelY1 = 25
    yelY2 = 5
    thy = 0
    thr = 0
    for name, value in awayCards.items():
        yelY1 += dy
        yelY2 += dy
        if value == "yellow":
            yel = Rectangle(Point(317.5+600, yelY1), Point(332.5+600,yelY2))
            yel.setFill("yellow")
            yel.draw(win)
            thy += 1
        elif value == "red":
            red = Rectangle(Point(347.5+600, yelY1), Point(362.5+600,yelY2))
            red.setFill("red")
            red.draw(win)
            thr += 1
        else:
            pass
    thg = Text(Point(175+600, shotsY),aGoals)
    thg.setSize(10)
    thg.draw(win)
    thY = Text(Point(325+600,shotsY),thy)
    thY.setSize(10)
    thY.draw(win)
    thR = Text(Point(355+600,shotsY),thr)
    thR.setSize(10)
    thR.draw(win)
    saveY = 40
    taSav = 0
    for name, value in awaySaves.items():
        save = Text(Point(385+600,saveY),value)
        save.setSize(10)
        save.draw(win)
        saveY += dy
        taSav += value
    tas = Text(Point(385+600,shotsY),taSav)
    tas.setSize(10)
    tas.draw(win)     
    offY = 40
    taOffsides = 0
    for name, value in awayOffsides.items():
        off = Text(Point(475+600,offY),value)
        off.setSize(10)
        off.draw(win)
        offY += dy
        taOffsides += value
    tao = Text(Point(475+600,shotsY),taOffsides)
    tao.setSize(10)
    tao.draw(win)
    gaY = 40
    aga = 0
    for name, value in awayGoalsAgainst.items(): 
        ga = Text(Point(415+600,gaY),value)
        ga.setSize(10)
        ga.draw(win)
        gaY += dy
        aga += value

    taga = Text(Point(415+600,shotsY),aga)
    taga.setSize(10)
    taga.draw(win)

    gaY = 40
    tHomeGoalsAgainst = 0
    for name, value in homeGoalsAgainst.items(): 
        ga = Text(Point(415,gaY),value)
        ga.setSize(10)
        ga.draw(win)
        gaY += dy
        tHomeGoalsAgainst += value
    
    t = Text(Point(235+600, 15,), "S")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(265+600, 15), "SOG")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(295+600, 15), "F")
    t.setSize(10)
    t.draw(win)
    y = Rectangle(Point(317.5+600, 25), Point(332.5+600,5))
    y.setFill("yellow")
    y.draw(win)
    r = Rectangle(Point(347.5+600, 25), Point(362.5+600,5))
    r.setFill("red")
    r.draw(win)
    t = Text(Point(385+600,15), "SV")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(415+600,15), "GA")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(445+600,15), "SF")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(520+600,15), "SV%")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(475+600,15), "OFF")
    t.setSize(10)
    t.draw(win)
    t = Text(Point(575+600,15), "CK")
    t.setSize(10)
    t.draw(win)
    lineX = 160
    while lineX < 580:
        if lineX == 520 or lineX == 580:
            lineX += 30
            pass
        else:
            Line(Point(lineX,0),Point(lineX,600)).draw(win)
            lineX += 30
    lineX = 760
    while lineX < 1180:
        if lineX == 520+600 or lineX == 580+600:
            lineX += 30
        else:
            Line(Point(lineX,0),Point(lineX,600)).draw(win)
            lineX += 30

    if tHomeSog != 0:
        awaySave = round(1 - (hGoals / tHomeSog),2)
    else:
        awaySave = "N/A"

    if taSog != 0:
        homeSave = round(1 - (aGoals / taSog),2)
    else:
        homeSave = "N/A"
    
    thsv = Text(Point(520,copyY), homeSave)
    thsv.setSize(10)
    thsv.draw(win)
    
    tasv = Text(Point(520+600,shotsY), awaySave)
    tasv.setSize(10)
    tasv.draw(win)

    tac = Text(Point(575+600, shotsY),aCorners)
    tac.setSize(10)
    tac.draw(win)
                
    tsfa = Text(Point(445+600,shotsY),tHomeShots)
    tsfa.setSize(10)
    tsfa.draw(win)

    thga = Text(Point(415,copyY),tHomeGoalsAgainst)
    thga.setSize(10)
    thga.draw(win)

    ths = Text(Point(235,copyY),tHomeShots)
    ths.setSize(10)
    ths.draw(win)

    tsfh = Text(Point(445,copyY),taShots)  #
    tsfh.setSize(10)
    tsfh.draw(win)
    
