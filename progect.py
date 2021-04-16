from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(width,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<win_height-80:
            self.rect.y+=self.speed
        if keys[K_a] and self.rect.x>0:
            self.rect.x-=self.speed
        if keys[K_d] and self.rect.x<250:
            self.rect.x+=self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<win_height-80:
            self.rect.y+=self.speed 
        if keys[K_LEFT] and self.rect.x>250:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x<500:
            self.rect.x+=self.speed
win_height=500
win_width=600
window=display.set_mode((win_width,win_height))
background=transform.scale(image.load('pole.png'),(win_width,win_height))
score_l=0
score_r=0
mixer.init()
mixer.music.load('mus.mp3')
mixer.music.play()
game=True
finish=False
clock=time.Clock()
FPS=60
bit1=Player('bit.png',30,200,4,100,150)
bit2=Player('bit.png',520,200,4,100,150)
shaiba=GameSprite('shaiba.png',200,200,4,50,50)
font.init()
font=font.SysFont('Areal',35)
lose1=font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2=font.render('PLAYER 2 LOSE!',True,(180,0,0))
speed_x=3
speed_y=3
plathorm1=GameSprite('rea.png',0,0,0,50,200)
plathorm2=GameSprite('rea.png',0,325,0,50,200)
plathorm3=GameSprite('rea.png',550,0,0,50,200)
plathorm4=GameSprite('rea.png',550,325,0,50,200)
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish != True:
        window.blit(background,(0,0))
        bit1.update_l()
        bit2.update_r() 
        plathorm1.reset()
        plathorm2.reset()
        plathorm3.reset()
        text_l=font.render('счёт:'+str(score_l),1,(255,255,255))
        window.blit(text_l,(10,20))
        text_r=font.render('счёт:'+str(score_r),1,(255,255,255))
        window.blit(text_r,(500,20))
        plathorm4.reset()
        shaiba.rect.x+=speed_x
        shaiba.rect.y+=speed_y
        if score_l or score_r ==3:
            finish=True
        if sprite.collide_rect(plathorm1,shaiba):
            speed_x*=-1
            speed_y*=1
        if sprite.collide_rect(plathorm2,shaiba):
            speed_x*=-1
            speed_y*=1
        if sprite.collide_rect(plathorm3,shaiba):
            speed_x*=-1
            speed_y*=1
        if sprite.collide_rect(plathorm4,shaiba):
            speed_x*=-1
            speed_y*=1
        if sprite.collide_rect(bit1,shaiba) or sprite.collide_rect(bit2,shaiba):
            speed_x*=-1
            speed_y*=1
        if shaiba.rect.y>win_height-50 or shaiba.rect.y<0:
            speed_y*=-1
        if shaiba.rect.x<20:
            score_r=score_r+1
            bit1=Player('bit.png',30,200,4,100,150)
            bit2=Player('bit.png',520,200,4,100,150)
            shaiba=GameSprite('shaiba.png',200,200,4,50,50)
            finish=False
            game=True
        if shaiba.rect.x>570:
            score_l=score_l+1
            bit1=Player('bit.png',30,200,4,100,150)
            bit2=Player('bit.png',520,200,4,100,150)
            shaiba=GameSprite('shaiba.png',200,200,4,50,50)
            finish=False
            game=True

        bit1.reset()
        bit2.reset()
        shaiba.reset()
        display.update()
    else:
        finish=False
        game=True
        score_l=0
        score_r=0
    clock.tick(FPS)