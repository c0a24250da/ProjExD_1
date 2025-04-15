import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    k_img = pg.image.load("fig/3.png")
    k_img=pg.transform.flip(k_img,True,False)
    k_rct = k_img.get_rect()
    k_rct.center=300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        a=-1
        b=0
        if key_lst[pg.K_UP]:
            a=-1
            b=-1
        if key_lst[pg.K_DOWN]:
            a=-1
            b=1
        if key_lst[pg.K_LEFT]:
            a=-2
            b=0
        if key_lst[pg.K_RIGHT]:
            a=1
            b=0
        k_rct.move_ip(a,b)
        
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[-x+1500,0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(k_img,k_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()