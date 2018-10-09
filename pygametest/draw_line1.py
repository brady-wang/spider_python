# *_*coding:utf-8 *_*


#@小五义 http://www.cnblogs.com/xiaowuyi
import pygame,sys
def lineleft(): #画马路左边界
    plotpoints=[]
    for x in range(0,640):
        y=-5*x+1000
        plotpoints.append([x,y])
    pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
    pygame.display.flip()
def lineright():#画马路右边界
    plotpoints=[]
    for x in range(0,640):
        y=5*x-2000
        plotpoints.append([x,y])
    pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
    pygame.display.flip()
def linemiddle():#画马路中间虚线
    plotpoints=[]
    x=300
    for y in range(0,480,20):
        plotpoints.append([x,y])
        if len(plotpoints)==2:
            pygame.draw.lines(screen,[0,0,0],False,plotpoints,5)
            plotpoints=[]
    pygame.display.flip()

def loadcar(): #载入car图像
    my_car=pygame.image.load('ok1.jpg') #当前文件夹下的ok1.jpg文件
    screen.blit(my_car,[320,320])
    pygame.display.flip()

pygame.init()
screen=pygame.display.set_caption('hello world!')
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
lineleft()
lineright()
linemiddle()
loadcar()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()