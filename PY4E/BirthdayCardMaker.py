

import pygame as pg
"""
cd PY4E
BirthdayCardMaker.py
"""

content = """Prepara deseja um feliz aniverrsário
aos aniversariantes

NATHALIA PACHECO BARROS
ANARETE CRISTINA TRINDADE
ALINE CAROLINE DOS SANTOS PEREIRA
LARISSA SILVA
JULIA CÉ BRITZKE
GABRIEL SCHNEIDERS DE OLIVEIRA
VITÓRIA FERREIRA MENEZES
VITÓRIA LEMKE RODRIGUES
ADRIANA RIBEIRO DA SILVA
LUCAS FLORES MALAQUIAS
OSCAR CHERISMA
PETERSON SILVA DA SILVA
Camila Silveira Marques
Bruna Verônica Alencastro de Menezes Soares
Marta Pinto Damasio
ADRIANA SILVEIRA DA SILVA
JOÃO VITOR DE MATTOS REI
RAFAEL FABIANO CHAROPEM
TATIANA CUNHA
BIANCA SOUCEDO BARBOSA

:D É os guri"""

content = content.split("\n")
print(content)


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
font = pg.font.Font('good times rg.ttf', 12)
text = []
textRect = []
for i in range(len(content)) :
    text.append(font.render(content[i], True, RED, WHITE))
    textRect.append(text[i].get_rect())
    textRect[i].center = (1600,100+i*25)


#a = pg.image.load("bola01.png")
fundo = pg.image.load("win2.png")
card = pg.image.load("card001.png")
### pg.transform.smoothscale("card001.png",(200,200))

end = False
while not end:
    for event in pg.event.get() :
        if event.type == pg.QUIT : end = True
    screen.blit(fundo,[0,0])
    screen.blit(card,[1200,60])
    for i in range(len(text)) :
        screen.blit(text[i], textRect[i])
    ### pg.font.Font.render(texto)

    pg.image.save(screen, "card1.png")
    pg.display.update()
    pg.image.save()
    end = True
quit()
