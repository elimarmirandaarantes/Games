import pygame 
import sys, os, time

def update_laser(laser_list,speed=300):
    for laserRec in laser_list:
        laserRec.y-=round(speed*dt) #type: ingnore
        if laserRec.midbottom[1]< 0:
             laser_list.remove(laserRec) 

def displayScore(display,font):
    score_text = str (f'S T A R - GAME {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True,(178,34,34))
    recText = texto.get_rect(midleft=(30,15))
    display.blit(texto,recText)

pygame.init()
largura,altura = 1200,650
display = pygame.display.set_mode((largura,altura))
fundo=pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
nave=pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf = pygame.transform.scale(lasersurf,(4,40))

navRec= nave.get_rect(center=(500,500))
laser_list =[]
#laserRec = lasersurf.get_rect(midbottom=navRec.midtop)

#carregando imagem de fundo
bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()

bgR1 = bg1.get_rect(center=((largura/2,(altura/2))))

font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(178,34,34))
recText = texto.get_rect(center=(70,10))

pygame.display.set_caption(("Space Combat"))
loop = True
pos_y = 300
relogio = pygame.time.Clock()

while loop:
    start = int(round(time.time()*1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            navRec.center = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Tiro {event.pos}")
        if event.type==pygame.MOUSEBUTTONDOWN:
            laserRec = lasersurf.get_rect(midbottom=navRec.midtop)
            laser_list.append(laserRec)
   
    display.blit(bg1, bgR1)

    display.blit(nave, navRec)
    displayScore(display=display,font=font)
     #Limitando os Frames
    dt = relogio.tick(120)/1000

    update_laser(laser_list)

    for laserRec in laser_list:
        display.blit(lasersurf,laserRec)
    #if navRec.y >=10:
       # navRec.y -=1
    
   # display.blit(nave, (200,pos_y))
   # pos_y-=1 
   # if pos_y < 0:
   #     pos_y =720
    pygame.display.update()

    #Limitando os Frames
    #dt = relogio.tick(120)/1000
    
    end = int(round(time.time()*1000))
    
    #print(f"{end-start} ms")
   
    display.blit(texto, recText)

    pygame.display.update()

pygame.quit()