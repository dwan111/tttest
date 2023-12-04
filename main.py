import js as p5
font = p5.loadFont('telugu-mn.ttf')
print('Assignment #8 (Final Project Part B)')
#music = p5.loadSound('music.wav')
program_state  = 'RESTART'
key = 'SPACEBAR'
timeLimit = 60 
timer = p5.random(1000,5000)
countdown = 60
food_ate = 0
press_released_time = 0
press_start_time = 0
chair_img = p5.loadImage('chair.png')
x_list = [71,69,88,95,57]
y_list = [76,96,120,100,150]
size_listw = [10,10,10,10,10]
size_listh = [5,5,5,5,5]
bell_sound = p5.loadSound('classbell.mp3')
yay_sound = p5.loadSound('yay.mp3')




class Student:
  
  def __init__(self, x =50,y=40):# x , y is location coordinates
    self.img1 = p5.loadImage('sittingstudent.png')
    self.img2 = p5.loadImage( 'eatingstudent.png')
    self.img10 = p5.loadImage('food.png')
    self.x = x
    self.y = y 

  def draw(self):
    global time
    #p5.image(self.img1,self.x,self.y, 300,300)
    if (program_state == 'RESTART'):
       p5.image(self.img1,self.x,self.y, 300,300)
    if (program_state == 'INTRO'):
      p5.image(self.img1,self.x,self.y, 300,300)
    if (program_state == 'PLAY'):
      if(p5.keyIsPressed == False):
        p5.image(self.img1,self.x,self.y, 300,300)
      if(p5.keyIsPressed == True):
        if(p5.keyCode == p5.UP_ARROW):
          p5.image(self.img2,150,40,290,290)
          p5.image(self.img10,150,101,150,150)

      else:
        p5.image(self.img1,self.x,self.y, 300,300)
      
       
  def update(self):
      pass 
  
student = Student()


class Teacher(Student):
  
  def __init__(self, x =30, y= 20 ):
    self.x = x
    self.y = y
    self.img3 = p5.loadImage('teacherinitial.png')
    self.img4 = p5.loadImage('turnaround.png')
    self.img_current = self.img3
    
  
  def draw(self):
    global timer,countdown
    if(self.img_current == self.img3 and p5.millis() > timer + 9000): #CHANGED to 9sec
      self.img_current = self.img4
      timer = p5.millis()
    elif (self.img_current == self.img4 and p5.millis() > timer + 2000):
      self.img_current = self.img3
      timer = p5.millis()
    p5.image(self.img_current, 50,30,200,203)
    if (self.img_current == self.img4 and p5.keyIsPressed == True and p5.keyCode == p5.UP_ARROW):
      p5.textSize(15)
      p5.fill(0)
      p5.text('Press mouse to restart', 45,170)
      countdown = 0
      countdown = countdown

    
    
  
    #for i  in range (5):
      #s=p5.random(110, 120)
      #p5.image(self.img3, self.x,self.y, s, s)
    
    #if (p5.millis()% 1000 < 500): 
      #p5.image(self.img3, 100,100,100,100)
    
    #else:
      #p5.image(self.img4, 100, 100,100,100)
  
  def update(self):
    pass
    #teachers = [self.img3, self.img4];
    #teacher = p5.random(teachers);
    #p5.text(teacher, 50, 50);
    
    #p5.image(self.img4, self.x,self.y, 300,200)
    #turnteacher = p5.image(self.img4, self.x,self.y, 300,200)
    #turn_around = p5.random(p5.millis(0,10000))
    
    #if(turn_around +p5.millis() > 5000):
      #p5.image(self.img3, self.x,self.y, 300,200)
    #else:
      #p5.image(self.img4, self.x,self.y, 300,200)

teacher = Teacher()

class Clock(Student):
  def draw(self):
    p5.stroke(1)
    p5.fill(255)
    p5.ellipse(self.x, self.y, 20, 20)#inheritance & polymorphism
    p5.fill(139,20,111)
    p5.ellipse(self.x ,self.y,5,5)

clock = Clock()

def setup():
  p5.createCanvas(300, 300)  


def draw():
  global countdown, countdown_timer, food_ate, press_released_time, press_start_time, program_state
  p5.background(255)   
  p5.fill(0)
  p5.stroke(0)
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  p5.textSize(10)
  p5.text(cursor_xy, 10, 20)  # cursor (x, y) 
  p5.fill(255)
  p5.textSize(10)
  p5.fill(102,0,204,50)

  #p5.text('Food ate: ' + str(food_ate), 209,10)
  #msec = p5.millis()
  #sec = int(msec / 1000)  
  #p5.text('milliseconds: ' + str(int(msec)), 10, 42)
  #p5.text('seconds: ' + str(sec), 10, 55)
  
#dark brown bg
  p5.noStroke()
  p5.fill(222,184,135)
  p5.rect(130,0,210,130)
#light brown bg
  p5.fill(245,222,179)
  p5.triangle(0,300,130,130,0,0)
  p5.triangle(0,0,130,0,130,130)
#whiteboard
  p5.fill(255)
  p5.triangle(20,100,109,30,20,150)
  p5.triangle(20,150,109,115,109,30)
  p5.triangle(20,150,20,220,109,115)
  p5.stroke(0)
  p5.strokeWeight(1)
  p5.line(20,220,109,115)
  p5.line(20,100,20,220)
#floor
  p5.noStroke()
  p5.fill(169,169,169)
  p5.triangle(130,130,300,130,0,300)
  p5.triangle(0,300,300,300,300,130)
#window
  p5.fill(0,204,204)
  p5.rect(225,32,50,20)
  p5.rect(290,32,30,20)
#cursor on top
  p5.fill(0)
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  p5.text(cursor_xy, 10, 20)  # cursor (x, y) 
#chair
  p5.image(chair_img, 65,40,300,300)
#table
  p5.fill(102,51,0)
  p5.triangle(186,210,222,210,214,180)
  p5.triangle(212,182,227,182,222,210)
  p5.rect(188,210,10,35)
  
  
  
  student.draw()
  student.update()
  teacher.draw()
  teacher.update()
  clock.draw()

  p5.fill(102,0,0,50)
  p5.rect(197,0,110,30)
  p5.fill(255)
  p5.textSize(15)
  p5.noStroke()
  p5.text('Food ate: ' + str(food_ate), 210, 17)
  if (program_state =='PLAY'):
    draw_countdown()

    if(food_ate == 3):
      p5.text('You Win',150,150)
      yay_sound.play()
      p5.text('Press mouse to play again',32,170)
      
    if(countdown == 0 and food_ate< 3):
      p5.fill(255, 0, 0)
      p5.textSize(18)
      p5.text('YOU LOOSE!', 90, 150)
      
  if (program_state =='RESTART'):
    countdown = 60
    food_ate =0

  
  if (program_state == 'RESTART'):
    p5.textFont(font)
    p5.textSize(25)
    p5.strokeWeight(2)
    p5.stroke(255,128,0)
    p5.fill(255,128,0)
    p5.text('NOM NOM',90, 120)
    p5.noStroke()
    p5.fill(51,0,102)
    p5.textSize(20)
    p5.strokeWeight(1)
    p5.text('Press to Start Game',60,150)
    p5.textSize(13)
    p5.noStroke()
    p5.fill(51,0,102)
    p5.text('Original Artworks by Amanda Wan', 50, 280)
    
  if (program_state== 'INTRO'):
    p5.textFont(font)
    p5.textSize(10)
    p5.noStroke()
    p5.fill(204,153,225)
    p5.rect(80,75,150,70)
    p5.strokeWeight(1)
    p5.fill(255,255,255)
    p5.text('*Read the description below', 87, 113)

  if (program_state== 'PLAY'):
    global size_listh, size_listw, x_list, y_list
    
   

    
      #p5.text('Food ate:', food_ate, 211,10)
    # if (p5.millis()== 5000 and p5.keyIsPressed):#FOOD ATE COUNTING
    #   print(p5.millis())
    #   food_ate = 1
    #   food_ate = food_ate
    #   p5.fill(124,22,220)
    #   p5.text('Food ate=', 215, 16)
    #   p5.text('Food ate:', food_ate, 50,10)
    # if (p5.keyIsPressed == p5.UP_ARROW):
    #   p5.stroke(0)
    #   msec = p5.millis()
    #   sec = int(msec / 1000) 
    #   if (msec + p5.millis() >= 5000):
    #     p5.fill(0)
    #     p5.stroke(0)
    #     p5.text('seconds: ' + str(sec),260,15)
    #     msec = p5.millis()
  #countdown from 60 seconds
    #currentTime = int(p5.millis()/1000)
    #countdown = timeLimit - currentTime
    #if(countdown < 0):
      #countdown = 0
    #p5.textSize(14)
   # p5.fill(0,102,153)
    #p5.stroke(0)
    #p5.text('Time:',currentTime,30,380)
   # p5.text('CountDown Timer:', countdown , 100,20)
   # if(countdown < 0):
      #countdown = 0
    
    for i in range(len(x_list)): #decor on whiteboard traverse, loop, and list
      p5.push()
      p5.fill(102, 204, 0)
      p5.strokeWeight(0.5)
      size_listw[i] = 10 + p5.random(0, 2)
      p5.rotate(p5.mouseX/10000) #rotate using mouse X motion
      p5.rect(x_list[i], y_list[i], size_listw[i], size_listh[i])
      p5.pop()

  #global countdown
  #p5.text(countdown, p5.width/2, p5.height/2);
  #if (frameCount % 60 == 0 and countdown > 0): 
    #countdown = 0
# countdown countdown and countdown timer variables:
countdown = 60
countdown_timer = 0 


def draw_countdown():
  global countdown, countdown_timer

  p5.fill(204,0,102)
  p5.textSize(15)
  p5.noStroke()
  p5.text('Countdown: ' + str(countdown), 13, 290)

  if(countdown > 0):
    if(p5.millis() > countdown_timer + 1000):
      countdown -= 1
      countdown_timer = p5.millis()
    if (program_state =='PLAY'): #should PAUSE the time
      countdown = countdown
    if(countdown == 0):
        p5.fill(255, 0, 0)
        p5.textSize(18)
        p5.text('YOU LOSE!', 90, 75)

# event function below need to be included,
# even if they don't do anything

def keyPressed(event):
  global press_start_time 
  if (p5.keyCode == p5.UP_ARROW):
    press_start_time = p5.millis()
    print('start time:', press_start_time)
  #print('keyPressed.. ' + str(p5.key))
  #if (key =='SPACEBAR'):
      #p5.image(eat, 150,150, 30,40)

def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  global press_released_time, food_ate
  if(p5.keyCode == p5.UP_ARROW):
    press_released_time = p5.millis()
    print('release time:', press_released_time)
    if(press_released_time - press_start_time >= 5000):
      food_ate += 1
      print('food count:', food_ate)
      p5.stroke(1)
      p5.fill(0)
      p5.textSize(15)
      p5.text('Food ate:', food_ate, 210,17)
      
  #print('keyReleased.. ' + str(p5.key))

def mousePressed(event):
  #print('mousePressed..')
  global program_state
  if (program_state == 'RESTART'): #when pressed, the 
    program_state = 'INTRO'
    print('Eat in class without letting the teacher notice. Press UP ARROW to eat and release to hide the food..Each food takes 5 secs to consume. YOUR GOAL is to eat 3 foods within 1 min. Tap to start. GOOD LUCK! + Original Art by Amanda Wan')
    print('program state = ', program_state)
  elif (program_state == 'INTRO'):
    program_state = 'PLAY'
    bell_sound.play()
    print('program state = ', program_state)
  elif (program_state == 'PLAY'):
    program_state = 'RESTART'
    print('program state = ', program_state)

def mouseReleased(event):
  #print('mouseReleased..')
  pass
