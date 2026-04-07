import pygame as pg

pg.init()
tela = pg.display.set_mode((1280, 720))
fps = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    tela.fill("lightgreen")

    pg.display.flip()
    fps.tick(60)

pg.quit()