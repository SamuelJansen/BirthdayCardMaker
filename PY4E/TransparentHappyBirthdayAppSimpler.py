import HBLibrary as hb
from PIL import ImageTk,Image
import time as now

def __run__(initialTime,size,xy,image) :
    hb.Music("Sounds/HappyBirthdayToYou.mp3")

    windowSize = "400x600"

    time = now.time()
    while (now.time()-time<9.4) : #1) :#
        pass

    time = now.time()

    status=0
    #window = hb.TransparentCard("1920x1080",status)###.mainloop()
    window = hb.TransparentCard(windowSize,status)
    window.update()

    while (now.time()-initialTime<40*(1.1)+.5) : #10) :#
        window.update()

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
