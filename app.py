import pygame 
import time 
import math

pygame.init()

screen=pygame.display.set_mode((500,600))#màng hình to
pygame.display.set_caption("Countdown")

RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

running=True

total=0
mins=0
secs=0
start=False
pre_total=0
stop=0
k=0 

clock=pygame.time.Clock()
font=pygame.font.SysFont('sans',50)
text_1=font.render('+',True,BLACK)
text_2=font.render('-',True,BLACK)
text_3=font.render('+',True,BLACK)
text_4=font.render('-',True,BLACK)
text_5=font.render('Start',True,BLACK)
text_6=font.render('Reset',True,BLACK)
text_7=font.render('Stop',True,BLACK)

while running:
	screen.fill(RED)
	clock.tick(60)
	mouse_x,mouse_y=pygame.mouse.get_pos()# x trước y sau
	
	pygame.draw.rect(screen, WHITE,(100,50,50,50))
	pygame.draw.rect(screen, WHITE,(100,200,50,50))
	pygame.draw.rect(screen, WHITE,(200,50,50,50))
	pygame.draw.rect(screen, WHITE,(200,200,50,50))
	pygame.draw.rect(screen, WHITE,(300,50,150,50))
	pygame.draw.rect(screen, WHITE,(300,150,150,50))
	pygame.draw.rect(screen, WHITE,(300,250,150,50))

	pygame.draw.rect(screen, BLACK,(50,520,400,50))
	pygame.draw.rect(screen, WHITE,(60,530,380,30))
	#CÁI SAU ĐÈ LÊN CÁI TRƯỚC

	pygame.draw.circle(screen, BLACK,(250,400),100)
	#100 LÀ RADIUS
	pygame.draw.circle(screen, WHITE,(250,400),95)
	pygame.draw.circle(screen, BLACK,(250,400),5)

	
	screen.blit(text_1,(100,50))
	screen.blit(text_2,(100,200))
	screen.blit(text_3,(200,50))
	screen.blit(text_4,(200,200))
	screen.blit(text_5,(300,50))
	screen.blit(text_6,(300,150))
	screen.blit(text_7,(300,250))
	#WHITE màu hình chữ nhật


	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running =False
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				if mouse_x>=100 and mouse_x<=150 and mouse_y>=50 and mouse_y<=100:
					total=total+1
					k=total
					pre_total=total
				if mouse_x>=100 and mouse_x<=150 and mouse_y>=200 and mouse_y<=250:
					total=total-1
					k=total
					pre_total=total
				if mouse_x>=200 and mouse_x<=250 and mouse_y>=50 and mouse_y<=100:
					total=total+60
					k=total
					pre_total=total
				if mouse_x>=200 and mouse_x<=250 and mouse_y>=200 and mouse_y<=250:
					total=total-60
					k=total
					pre_total=total
				if mouse_x>=300 and mouse_x<=450 and mouse_y>=50 and mouse_y<=100:
					pre_total=total
					k=total
					total=total-1
					
					start=True
				if mouse_x>=300 and mouse_x<=450 and mouse_y>=150 and mouse_y<=200:
					total=0
					pre_total=total
					k=total
				if mouse_x>=300 and mouse_x<=450 and mouse_y>=250 and mouse_y<=300:
					start=False

	mins=int(total/60)
	secs=total-mins*60
	#print(time)
	
	#lệnh cho start
	if start:
		if total>=0:
			total-=1
			k-=1
			time.sleep(1)
		else:
			total+=1
			start=False
		
	
	text_time=font.render(str(mins)+ " : " + str(secs),True,BLACK)
	screen.blit(text_time,(120,120))
	
	#Vẽ kim giây
	x_sec=250+90*math.sin(6*secs*math.pi/180)
	y_sec=400-90*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,400),(x_sec,y_sec))
	#Vẽ kim phút
	x_min=250+50*math.sin(6*mins*math.pi/180)
	y_min=400-50*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,400),(x_min,y_min))
	#Vẽ hình chữ nhật đỏ
	if k!=0:
		pygame.draw.rect(screen, BLACK,(60,530,380*(k/pre_total),30))	
	pygame.display.flip()

pygame.quit()