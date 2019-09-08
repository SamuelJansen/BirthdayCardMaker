import sys
import os
import pygame as pg
import time as now
import numpy as np

page_library = {}
def getPageImage(path) :
    '''It picks the image contained in the path.
It works on mac and windows
--> getPageImage(path)'''
    global page_library
    page = page_library.get(path)
    if page==None :
        canonicalized_path = path.replace('/',os.sep).replace('\\',os.sep)
        page = pg.image.load(canonicalized_path)
    page_library[path] = page
    return page

class Course:
    '''It sets de course's characteristics'''
    def __init__(self,courseName,path,screenSize,fps,sps,colors):
        '''--> Course(courseName,path,screenSize,colors)
path/courseName
colors are a dictionary --> colors = {'black' : (0,0,0), 'white' : (255,255,255)}'''
        self.name = courseName
        self.path = path + '/' + self.name
        self.devScreenSize = (1600,900)
        self.screenSize = screenSize
        self.fps = fps
        self.sps = sps
        self.color = colors

    def newScreenSize(screenSize):
        self.screenSize = screenSize

class Lesson:
    '''It's a class to keep track of the lesson's
images, sounds and position

self.rect[0] = x_position
self.rect[1] = y_position
self.rect[2] = width
self.rect[3] = height

self.rect.left = x_position
self.rect.right = x_position + width
self.rect.top = y_position
self.rect.bottom = y_position + height'''
    def __init__(self,lessonNumber,pageSize,pagePosition,course,last_valid_path=None):
        '''--> Lesson(lessonNumber,pageSize,pagePosition,endLesson,course)'''
        self.pageList = []
        self.pages = 0
        self.page = 0
        self.oldPage = -1
        ### self.newPage = False

        self.size = pageSize
        self.resize = [course.devScreenSize[0]/self.size[0],course.devScreenSize[1]/self.size[1]]
        print(f'course.devScreenSize = {course.devScreenSize}, lesson.resize = {self.resize}')

        self.position = pagePosition

        self.name = 'Aula'+str(lessonNumber)
        self.path = course.path+'/'+self.name
        self.pagePath = self.path+'/'+'Images'
        self.soundPath = self.path+'/'+'Sounds'
        print(self.pagePath)
        done = False
        while not done :
            path = self.pagePath+'/'+str(self.pages)+'.png'
            try :
                self.pageList.append(pg.transform.smoothscale(getPageImage(path),self.size))
                #self.pageList.append(getPageImage(path))
                self.pages += 1
            except :
                print(f'This lesson has {self.pages} pages')
                done = True

        self.rect = pg.Rect(pagePosition[0],pagePosition[1], pageSize[0], pageSize[1])
        self.end = False

    def newPageSize(pageSize):
        self.screenSize = pageSize
        self.resize = [course.devScreenSize[0]/self.size[0],course.devScreenSize[1]/self.size[1]]
        print(f'course.devScreenSize = {course.devScreenSize}, lesson.resize = {self.resize}')

    def update(self,lessonScript):
        if lessonScript.backward :
            pg.mixer.music.stop() #- for safety
            lessonScript.pageSoundPlaying = False
            lessonScript.pageSoundPlayed = False
            self.page -= 1
        elif lessonScript.foward :
            if not lessonScript.script[self.page].done :
                lessonScript.script[self.page].done = True
            else :
                pg.mixer.music.stop() #- for safety
                lessonScript.pageSoundPlaying = False
                lessonScript.pageSoundPlayed = False
            self.page += 1
        if self.page<0 or self.page>=self.pages :
            self.error = True
            self.page = self.pages - 1

    def pageBlit(self,f):
        '''This function blits the page lesson into the display
--> pageBlit(f)'''
        if (self.oldPage==self.page-1 or self.oldPage==self.page or self.oldPage==self.page+1) and self.page<=self.pages-1 and self.page>=0 :
            f.screen.blit(self.pageList[self.page],self.rect)
            self.oldPage = self.page
        else :
            print(f"Error - page indice is not correct. lesson.pageIndice = {self.page}")
            f.screen.blit(self.pageList[-1],self.rect)

class Page():
    def __init__(self,lineScript):
        self.lineScript = lineScript
        self.done = False
    pass

class LessonScript():
    def __init__(self,lesson,course):
        self.pageSoundPlaying = False
        self.pageSoundPlayed = False

        self.foward = False
        self.fowardPosition = [-10,-10]
        self.fowardSize = [0,0]

        self.backward = False
        self.backwardPosition = [-10,-10]
        self.backwardSize = [0,0]

        self.script = []
        try :
            lessonScript = open(lesson.path+'/'+lesson.name+'.txt', "r")
        except :
            lessonScript = open(course.path+'/'+'dev'+'.txt', "r")
        scriptLines = lessonScript.readlines()
        for line in scriptLines :
            if line.startswith('*') :
                self.script.append(Page(line.rstrip()[2:]))
        lessonScript.close()
        if len(self.script)>0 :
            print(f'The page script has {len(self.script)} lines')
        else :
            print("The page script wasn't read")

        self.pageScriptList = []

    def pageLessonScript(self,lesson):
        '''lstrip() Returns a left trim version of the string
rstrip() Returns a right trim version of the string
split() Splits the string at the specified separator, and returns a list'''
        self.backwardPosition = [-10,-10]
        self.backwardSize = [0,0]
        self.fowardPosition = [-10,-10]
        self.fowardSize = [0,0]

        self.pageScriptList = self.script[lesson.page].lineScript.split()
        ### print(self.pageScriptList)
        for goal in self.pageScriptList :

            if 'tgls' not in self.pageScriptList :
                self.pageSoundPlayed = True

            if goal[:2]=='tg' :
                if goal[2:4]=='ls' and (not pg.mixer.music.get_busy()) and (not self.pageSoundPlayed) and (not self.pageSoundPlaying) : #self.triggerSoundOver :
                    pg.mixer.music.load(lesson.path+'/Sounds/'+str(lesson.page)+'.mp3')
                    pg.mixer.music.play()
                if pg.mixer.music.get_busy() :
                    self.pageSoundPlaying = True
                if self.pageSoundPlaying and not pg.mixer.music.get_busy() :
                    self.pageSoundPlayed = True
                    self.pageSoundPlaying = False

            self.backward = False
            if goal[:2]=='bb' : # and self.pageSoundPlayed : #
                firstPoint = goal.split('(')[1]
                firstPoint = firstPoint.split(')')[0]
                firstPoint = firstPoint.split(',')
                secondPoint = goal.split('[')[1]
                secondPoint = secondPoint.split(']')[0]
                secondPoint = secondPoint.split(',')
                self.backwardPosition[0] = (int(secondPoint[0])+int(firstPoint[0]))/2
                self.backwardPosition[1] = (int(secondPoint[1])+int(firstPoint[1]))/2
                self.backwardSize[0] = (int(secondPoint[0])-int(firstPoint[0]))
                self.backwardSize[1] = (int(secondPoint[1])-int(firstPoint[1]))

            self.foward = False
            if goal[:2]=='bf' and (self.pageSoundPlayed or self.script[lesson.page].done) :
                firstPoint = goal.split('(')[1]
                firstPoint = firstPoint.split(')')[0]
                firstPoint = firstPoint.split(',')
                secondPoint = goal.split('[')[1]
                secondPoint = secondPoint.split(']')[0]
                secondPoint = secondPoint.split(',')
                self.fowardPosition[0] = (int(secondPoint[0])+int(firstPoint[0]))/2
                self.fowardPosition[1] = (int(secondPoint[1])+int(firstPoint[1]))/2
                self.fowardSize[0] = (int(secondPoint[0])-int(firstPoint[0]))
                self.fowardSize[1] = (int(secondPoint[1])-int(firstPoint[1]))


class TimeErrors:
    '''It calculates unexpected time errors'''
    def __init__(self,timeNow) :
        '''--> TimeErrors(timeNow)'''
        self.now = timeNow
        self.before = timeNow
    def checkErrors(self,f,timeNow):
        '''It checks any time erros once each f.fps frames
--> checkErrors(f,timeNow)'''
        f.timeOtherErrors = 0
        if f.newSecond :
            self.before = self.now
            self.now = timeNow
            f.timeOtherErrors = self.now - self.before - 1
            f.spsTimeError += .2 * ((f.sps - f.spsCounter) * 1/f.sps**2 - f.spsTimeError)
            """
            print(f'''      Main loop -- It should be 1: {self.now-self.before}
            tick = {f.tick}, tack = {f.tack}
            timeError = {f.timeError}, timeOtherErrors = {f.timeOtherErrors}
            spsCounter = {f.spsCounter}
            f.spsTimeError = {f.spsTimeError}
            1/f.sps = {1/f.sps}
            f.lastInnerLoops = {f.lastInnerLoops}''')
            #"""
            f.spsCounter = 1

class Frame:
    '''It's just a class to keep track of the
animation frames'''
    def __init__(self,animationFrames,course):
        '''--> Frame(animation_frames,course)'''
        pg.init()
        ### pg.mixer.init()
        if pg.mixer.get_init() :
            print('Sound module initialized')
        else :
            print('Sound module not initialized')

        self.screen = pg.display.set_mode(course.screenSize) # Display
        pg.display.set_caption(course.name)
        self.screenSize = course.screenSize #- for while
        self.innerLoops = 0
        self.lastInnerLoops = 0

        self.fps = course.fps
        self.animationFrames = animationFrames
        self.width = self.fps // self.animationFrames

        self.tick = now.time()
        self.tack = self.tick + 1/self.fps

        self.frame = 0
        self.newFrame = True
        self.newSecond = True

        self.sps = course.sps
        self.spsTick = self.tick
        self.spsTack = self.tick + 1/self.sps
        self.spsNew = False
        self.spsTimeError = 0
        self.spsCounter = 0

        self.before = self.tick
        self.timeError = 0
        self.timeOtherErrors = 0
        self.correctionFactor = .8 #- a value between 0 and 1

        self.frameCorrection = TimeErrors(self.tick)

    def update(self,timeNow,lesson,course):#,OveralError):
        '''It updates the display background and lesson once per frame
It also aims to mantain the frame rate constant
--> update(lesson,timeNow,course)'''
        #- Sampling old overal time's error
        self.frameBefore = self.frame
        #- dealling with frame control
        self.newFrame = False
        self.newSecond = False
        if self.timeError>0 :
            timeError = self.timeError
        else :
            timeError = 0
        if timeNow>self.tack-timeError :
            self.newFrame = True
            self.timeError += (1/self.fps)*( (timeNow - self.tick - 1/self.fps) - self.timeError )
            self.tick = timeNow
            if self.frame<self.fps-1 :
                self.frame += 1
            else :
                self.newSecond = True
                self.frame = 0
                self.lastInnerLoops = self.innerLoops
                self.innerLoops = 0
            self.tack = self.tick + 1/self.fps
            #- Should be diplay.update before or after blit images?
            pg.display.update() #- pg.display.flip() #-
            self.screen.fill(course.color['white'])
            lesson.pageBlit(self)
            ### pg.display.update() #- pg.display.flip() #-

        #- Dealling with sps time erros
        self.spsTick = now.time()#self.frameCorrection.now
        if self.spsNew :
            self.spsCounter += 1
        if self.spsTick>self.spsTack :
            self.spsNew = True
            self.spsTack = self.spsTick + 1/self.sps - self.spsTimeError
        else :
            self.spsNew = False

        #- Dealling with time erros
        self.frameCorrection.checkErrors(self,now.time())

        #- Amount of inner loops
        self.innerLoops += 1

        #- Quit rotine
        if lesson.end :
            pg.mixer.quit()
            pg.quit()

class Mouse():
    def __init__(self):
        '''self.foward and self.backwards are already
pondered by course.resize'''
        self.position = [0,0]

    def getPosition(self,position,lessonScript,lesson):
        self.position = list(position)
        self.position[0] = int((self.position[0]*lesson.resize[0])//1)
        self.position[1] = int((self.position[1]*lesson.resize[1])//1)

    def events(self,event,lessonScript,lesson):
        '''It checks for mouse events and deal with it'''
        if event.type == pg.MOUSEBUTTONDOWN :
            self.getPosition(pg.mouse.get_pos(),lessonScript,lesson)
            print(f'\nself.position = ({self.position[0]},{self.position[1]})',end='')
            if abs(lessonScript.backwardPosition[0]-self.position[0])<lessonScript.backwardSize[0]/2 and abs(lessonScript.backwardPosition[1]-self.position[1])<lessonScript.backwardSize[1]/2 :
                lessonScript.backward = True
                ### print('lessonScript.backward')
            elif abs(lessonScript.fowardPosition[0]-self.position[0])<lessonScript.fowardSize[0]/2 and abs(lessonScript.fowardPosition[1]-self.position[1])<lessonScript.fowardSize[1]/2 :
                lessonScript.foward = True
                ### print('lessonScript.foward')
            if (lessonScript.backward or lessonScript.foward) and lessonScript.pageSoundPlayed :
                lessonScript.pageSoundPlayed = False
        if event.type == pg.MOUSEBUTTONUP :
            self.getPosition(pg.mouse.get_pos(),lessonScript,lesson)
            print(f'[{self.position[0]},{self.position[1]}]\n       lesson.page = {lesson.page}, lessonScript.script[lesson.page].lineScript = {lessonScript.script[lesson.page].lineScript}')
            print(f'       pageSoundPlaying = {lessonScript.pageSoundPlaying}, pageSoundPlayed = {lessonScript.pageSoundPlayed}')

class Arrows:
    '''It stores any current event until it's over'''
    def __init__(self):
        '''--> Arrows()'''
        self.key = [0,0]
    def events(self,event):
        '''This function is responsible for the
horizontal and vertical arrows events
--> events(event)'''
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_LEFT :
                self.key[0] = -1
            elif event.key==pg.K_RIGHT :
                self.key[0] = 1
            if event.key==pg.K_UP :
                self.key[1] = -1
            elif event.key==pg.K_DOWN :
                self.key[1] = 1
        if event.type==pg.KEYUP  :
            if pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.key[0] = -1
            elif pg.key.get_pressed()[pg.K_RIGHT] and not pg.key.get_pressed()[pg.K_LEFT] :
                self.key[0] = 1
            elif not pg.key.get_pressed()[pg.K_LEFT] and not pg.key.get_pressed()[pg.K_RIGHT] :
                self.key[0] = 0
            if pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.key[1] = -1
            elif pg.key.get_pressed()[pg.K_DOWN] and not pg.key.get_pressed()[pg.K_UP] :
                self.key[1] = 1
            elif not pg.key.get_pressed()[pg.K_UP] and not pg.key.get_pressed()[pg.K_DOWN] :
                self.key[1] = 0
