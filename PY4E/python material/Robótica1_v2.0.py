import SamuelJansenPrepara_v2 as sj
import sys
import os
import pygame as pg
import time as now
import numpy as np

###############################################################################
#- Initializing global paths, sizes, etc
###############################################################################
courseName = 'Robótica1'
path = 'C:/Users/Aula19'
screenSize = (620,380)
screenSize = (840,520)
#screenSize = (1200,780)
#screenSize = (1600,900)
fps = 64
sps = 100
colors =    {
            'black' : (0,0,0),
            'white' : (255,255,255)
            }
lessonNumber = 1
pageSize = screenSize # (620,380) #
pagePosition = (0,0)
animationFrames = 16

###############################################################################
#- Course(courseName,path,screenSize,workScreenSize,colors)
###############################################################################
c = sj.Course(courseName,path,screenSize,fps,sps,colors)

###############################################################################
#- Lesson(lessonNumber,lessonPages,pageSize,pagePosition,end,course)
###############################################################################
l = sj.Lesson(lessonNumber,pageSize,pagePosition,c)
ls = sj.LessonScript(l,c)

###############################################################################
#- Frame(animationFrames,course)
###############################################################################
f = sj.Frame(animationFrames,c)
m = sj.Mouse()

###############################################################################
#- The actual lesson
###############################################################################
while not l.end:
    ls.pageLessonScript(l)
    for event in pg.event.get() :
        if event.type == pg.QUIT : l.end = True
        else :
            m.events(event,ls,l)
    l.update(ls)
    f.update(now.time(),l,c)
quit()
#sys.exit()
