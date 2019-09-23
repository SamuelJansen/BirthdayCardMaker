import HBLibrary as hb
from PIL import ImageTk,Image
import time as now

def __run__(initialTime,size,xy,image) :
    ### TransparentWin(time).mainloop()
    hb.Music("Sounds/HappyBirthdayToYou.mp3")

    time = now.time()
    while (now.time()-time<9.4) : #1) :#
        pass

    time = now.time()
    otherTime = time-.5

    status = 0

    #"""
    ballonLeft = hb.SideStuff(size,xy[0],image)
    ballonLeft.update()
    #"""

    """
    ballonRight = hb.SideStuff(size,xy[1],image)
    ballonRight.update()#"""

    window = hb.TransparentCard("1920x1080",status)
    window.update()

    while (now.time()-initialTime<40*(1.1)+.5) : #10) :#
        if (now.time()-time>1.1) : #4*1.1) :#
            #"""
            window.update()
            try:
                ballonRight.update()
            except :
                ballonLeft.update()
            #"""

            time = now.time()
            if status==0:
                status = 1
            else:
                status = 0

            try :
                xy[0][1] -= 120
                ballonRight.destroy()
                ballonLeft = hb.SideStuff(size,xy[0],image)
                ballonLeft.update()

                ###- x,y=window.Drag.Par.position()
                window.destroy()
                window = hb.TransparentCard("1920x1080",status) #,x,y)#.mainloop()
                window.update()

            except :
                done = True
                break

        elif (now.time()-otherTime>1.1) : #4*1.1) :#

            otherTime = now.time()
            try :
                xy[1][1] -= 120
                ballonLeft.destroy()
                ballonRight = hb.SideStuff(size,xy[1],image)
                ballonRight.update()

                window.destroy()
                window = hb.TransparentCard("1920x1080",status) #,x,y)#.mainloop()
                window.update()

            except :
                done = True
                break

    time = now.time()
    window.update()
    while (now.time()-time<11) : #1): #
        pass

    ###- quit()


if __name__ == '__main__' :
    time = now.time()
    size=626
    xy=[[0,0],[1920-size,int(-size+size/2)]] #[0,size],[0,size*2],[1920-size,int(size/2)],[1920-size,int(size+size/2)],
    ammount = len(xy) #1 #
    image = Image.open('Images/baloons.png')
    __run__(time,size,xy,image)
