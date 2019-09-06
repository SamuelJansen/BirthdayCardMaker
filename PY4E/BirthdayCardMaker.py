

import pygame as pg
"""
cd PY4E
BirthdayCardMaker.py
"""

texto = """NATHALIA PACHECO BARROS
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
BIANCA SOUCEDO BARBOSA"""

pg.init()

pg.font.init()

pg.display.init()

screen = pg.display.set_mode([1920,1080])

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
    ### pg.font.Font.render(texto)

    pg.image.save(screen, "card1.png")
    pg.display.update()
    pg.image.save()
    end = True
quit()
