import sys, pygame,random
#bb is player  n. 0   jl is  n.1

pygame.init()

size = width, height = 800, 600

black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball= pygame.image.load("balon.png")
ball=pygame.transform.scale(ball,(50,50))
bb= pygame.image.load("bb.png")
jl= pygame.image.load("jl.png")
jl=pygame.transform.scale(jl,(100,175))
bb=pygame.transform.scale(bb,(200,175))
ballrect = ball.get_rect()
bbrect = bb.get_rect()
jlrect = jl.get_rect()
whoHasTurn=""





btStartGame=pygame.Rect(375,0,50,50)
#resets game
def startGame():
    #jonah lomu initial position
    jlrect.x=600
    jlrect.y=0

    #beauden barrett initial position
    bbrect.x=0
    bbrect.y=0

    #ball initial position
    ballrect.x=400
    ballrect.y=300
    whoHasTurn=random.randint(0,1)
    print whoHasTurn

startGame()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:

                ballrect = ballrect.move([0,5])
            elif event.key==pygame.K_UP:
                ballrect = ballrect.move ([0,-5 ])
            elif event.key==pygame.K_RIGHT:
                ballrect = ballrect.move ([5,0 ])
            elif event.key==pygame.K_LEFT:
                ballrect = ballrect.move ([-5,0 ])
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if btStartGame.collidepoint(event.pos):
                startGame()
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(bb, bbrect)
    screen.blit(jl, jlrect)
    pygame.draw.rect(screen,[255,0,0 ],btStartGame)

    pygame.display.flip()
