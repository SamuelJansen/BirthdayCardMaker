import pygame as pg

WHITE = (255, 255, 255, 1)
GREEN = (0, 255, 0, 1)
BLUE = (0, 0, 128, 1)
RED = (200, 0, 0, 1)
TRANSPARENT = (0, 0, 0, 0)

pg.init()
pg.font.init()
pg.display.init()
screen = pg.display.set_mode([1920,1080])

pg.display.set_caption('Show Text')
font = pg.font.Font('TextFonts/good_times_rg.ttf', 12)

text = []
textRect = []
cardText = open('CardText/CardText.txt', "r", encoding='utf-8')
linesCardText = cardText.readlines()
for line,l in zip(linesCardText,range(len(linesCardText))) :
    line = line.rstrip()
    if len(line)!=0 :
        if line.startswith('*') :
            text.append(font.render(line[2:], True, RED, WHITE))
        else :
            text.append(font.render(line, True, RED, WHITE))
        textRect.append(text[-1].get_rect())
        if line.startswith('*') :
            textRect[-1].center = (1500,100+22*l)
        else:
            textRect[-1] = (1200,100+22*l)
cardText.close()

#a = pg.image.load("bola01.png")
fundo = pg.image.load("Images/win2.png")
card = pg.image.load("Images/card001-samuel.png")
cardRect = card.get_rect()
cardRect.center = (1500,520)
### pg.transform.smoothscale("card001.png",(200,200))

end = False
while not end:
    for event in pg.event.get() :
        if event.type == pg.QUIT : end = True
    screen.blit(fundo,[0,0])
    screen.blit(card,cardRect)
    for i in range(len(text)) :
        screen.blit(text[i],textRect[i])
    ### pg.font.Font.render(texto)

    pg.image.save(screen, "card1.png")
    ### pg.display.update()
    end = True
quit()
