#import required libraries
import random 
from random import *
import pygame
import time 
from time import *
#initialize variables
intro = True
score = 0
text_count = 30
temp_variable = 0    
type = ""
key = 0
rotation = 0
dictionary_for_y_values = {
  570:0, 540:0, 510:0, 480:0, 450:0, 420:0, 390:0, 360:0, 330:0
, 300:0, 270:0, 240:0, 210:0, 180:0, 150:0, 120:0, 90:0, 60:0, 30:0, 0:0}
x1, y1, x2, y2, x3, y3, x4, y4 = 0, 0, 0, 0, 0, 0, 0, 0
active_positions = [[x1, y1],[x2, y2],[x3, y3],[x4,y4]]
inactive_positions = []
bag = []
count = 0
looper_count = 0
delay = 1
down_check = 0
#VariableMc_Shmariable_Fifty7 IS A VERY IMPORTANT VARIABLE THAT KEEPS TRACK OF WHEN I NEED A NEW BLOCK
#IT DOES NOT NEED TO BE NAMED THAT WAY BUT IT IS
VariableMc_Shmariable_Fifty7 = 0
#load tile images

square = pygame.image.load("Tiles/Square Piece tile.png")
square = pygame.transform.scale(square, (30, 30))

placed = pygame.image.load("Tiles/Placed tile.png")
placed = pygame.transform.scale(placed, (30, 30))

j_tile = pygame.image.load("Tiles/J Piece tile.png")
j_tile = pygame.transform.scale(j_tile, (30, 30))

l_tile = pygame.image.load("Tiles/L Piece tile.png")
l_tile = pygame.transform.scale(l_tile, (30, 30))

line_tile = pygame.image.load("Tiles/Line Piece tile.png")
line_tile = pygame.transform.scale(line_tile, (30, 30))

s_tile = pygame.image.load("Tiles/S Piece tile.png")
s_tile = pygame.transform.scale(s_tile, (30, 30))

t_tile = pygame.image.load("Tiles/T Piece tile.png")
t_tile = pygame.transform.scale(t_tile, (30, 30))

z_tile = pygame.image.load("Tiles/Z Piece tile.png")
z_tile = pygame.transform.scale(z_tile, (30, 30))

tile_set = [square, j_tile, l_tile, line_tile, s_tile, t_tile, z_tile]

end = pygame.image.load("game over screen.jpg")
end = pygame.transform.scale(end, (480, 600))
piece_set = ["t", "l", "square", "reverse l", "s", "reverse s", "line"]
screen_dimensions = (480, 600)
bg_colour = (255, 255, 255)
running = True
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()


#function to set the piece order each bag
def set_bag():
  pieces = ["T", "L", "Square", "J", "S", "Z", "Line"]
  count = 0
  random_number = 0
  bag = []
  new_pieces = pieces
  piece_add = ""
  while count < 7:
    random_number = randint(0, 6-count)
    piece_add = new_pieces[random_number]
    bag.append(piece_add)
    new_pieces.pop(random_number)
    count += 1
  return bag
#function to see if user has quit program
def quit_check():
  running = True
  x = pygame.event.get()
  for event in x:
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      running = False
  return running, x
#function to get user key input
def key_check(events):
  for event in events:
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
      return "left"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
      return "right"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
      return "up"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
      return "down"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
      return "1"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
      return "2"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
      return "3"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
      return "4"
      
difficulty = "unknown"

pygame.init()
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 20)
intro_text = pygame.font.Font.render(font, "Choose a difficulty by pressing the number:", False, (255, 255, 255))
easy_text = pygame.font.Font.render(font, "1. Easy", False, (255, 255, 255))
medium_text = pygame.font.Font.render(font, "2. Medium", False, (255, 255, 255))
hard_text = pygame.font.Font.render(font, "3. Hard", False, (255, 255, 255))
impossible_text = pygame.font.Font.render(font, "4. Impossible", False, (255, 255, 255))
list = [easy_text, medium_text, hard_text, impossible_text]
#difficulty select screen
while intro != "09":
  pygame.display.update()
  text_count = 30
  screen.blit(intro_text, [0, 0])
  for i in list:
    screen.blit(i, [30, text_count])
    text_count+=30
  difficulty = key_check(pygame.event.get())
  if difficulty != None:
    if difficulty in "1234":
      break
#main loop    
while running == True:
  pygame.draw.rect(screen, (125, 125, 125), [300, 0, 180, 600])
  score_text = pygame.font.Font.render(font, f"Score: {score}", False, (255, 255, 255))
  screen.blit(score_text, [300, 30]) 
  for i in dictionary_for_y_values:
    dictionary_for_y_values[i] = 0
  looper_count = 0
  down_check = 0
  left_check = 0
  right_check = 0
  if bag == []:
    bag = set_bag()
  #if a new piece is required
  if VariableMc_Shmariable_Fifty7 == 0:  
    if bag[0] == "Square":
      for i in active_positions:
        if i == active_positions[0]:
          i[0], i[1] = 120, 0
        if i == active_positions[1]:
          i[0], i[1] = 150, 0
        if i == active_positions[2]:
          i[0], i[1] = 120, 30
        if i == active_positions[3]:
          i[0], i[1] = 150, 30
          type = tile_set[0]
          VariableMc_Shmariable_Fifty7 = 1
      bag.remove("Square")
    elif bag[0] == "Line":
      for i in active_positions:
        if i == active_positions[0]:
          i[0], i[1] = 150, 0
        if i == active_positions[1]:
          i[0], i[1] = 150, 30
        if i == active_positions[2]:
          i[0], i[1] = 150, 60
        if i == active_positions[3]:
          i[0], i[1] = 150, 90
          type = tile_set[3]
          VariableMc_Shmariable_Fifty7 = 1
      bag.remove("Line")
    elif bag[0] == "T":
      rotation = randint(1, 4)
      if rotation == 1:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 180, 0
          if i == active_positions[2]:
            i[0], i[1] = 150, 0
          if i == active_positions[3]:
            i[0], i[1] = 150, 30
          
      elif rotation == 2:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 120, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 60
      elif rotation == 3:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 120, 30
          if i == active_positions[2]:
            i[0], i[1] = 90, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 60
      elif rotation == 4:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 90, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 30
        
      type = tile_set[5]
      VariableMc_Shmariable_Fifty7 = 1 
      bag.remove("T")
    elif bag[0] == "S":
      rotation = randint(1, 2)
      if rotation == 1:
        for i in active_positions:
          if i == active_positions[0]:
            i[0] = 150
          if i == active_positions[1]:
            i[0] = 180
          if i == active_positions[2]:
            i[0], i[1] = 150, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 30
      else:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 120, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 30
          if i == active_positions[3]:
            i[0], i[1] = 150, 60
      type = tile_set[4]
      VariableMc_Shmariable_Fifty7 = 1
      bag.remove("S")
    elif bag[0] == "J":
      rotation = randint(1, 4)
      if rotation == 1:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 150, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 60
          if i == active_positions[3]:
            i[0], i[1] = 120, 60
      elif rotation == 2:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 90, 0
          if i == active_positions[1]:
            i[0], i[1] = 90, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 30
      elif rotation == 3:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 150, 30
          if i == active_positions[2]:
            i[0], i[1] = 180, 0
          if i == active_positions[3]:
            i[0], i[1] = 150, 60
      elif rotation == 4:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 90, 0
          if i == active_positions[2]:
            i[0], i[1] = 150, 0
          if i == active_positions[3]:
            i[0], i[1] = 150, 30
      type = tile_set[1]
      VariableMc_Shmariable_Fifty7 = 1
      bag.remove("J")
    elif bag[0] == "L":
      rotation = randint(1, 4)
      if rotation == 1:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 150, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 60
          if i == active_positions[3]:
            i[0], i[1] = 180, 60
      elif rotation == 2:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 90, 0
          if i == active_positions[2]:
            i[0], i[1] = 120, 0
          if i == active_positions[3]:
            i[0], i[1] = 90, 30
      elif rotation == 3:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 150, 30
          if i == active_positions[2]:
            i[0], i[1] = 120, 0
          if i == active_positions[3]:
            i[0], i[1] = 150, 60
      elif rotation == 4:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 30
          if i == active_positions[1]:
            i[0], i[1] = 90, 30
          if i == active_positions[2]:
            i[0], i[1] = 150, 0
          if i == active_positions[3]:
            i[0], i[1] = 150, 30
      type = tile_set[2]
      VariableMc_Shmariable_Fifty7 = 1
      bag.remove("L")
    elif bag[0] == "Z":
      rotation = randint(1,2)
      if rotation == 1:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 120, 0
          if i == active_positions[1]:
            i[0], i[1] = 90, 0
          if i == active_positions[2]:
            i[0], i[1] = 120, 30
          if i == active_positions[3]:
            i[0], i[1] = 150, 30
      else:
        for i in active_positions:
          if i == active_positions[0]:
            i[0], i[1] = 150, 0
          if i == active_positions[1]:
            i[0], i[1] = 150, 30
          if i == active_positions[2]:
            i[0], i[1] = 120, 30
          if i == active_positions[3]:
            i[0], i[1] = 120, 60
      type = tile_set[6]
      VariableMc_Shmariable_Fifty7 = 1
      bag.remove("Z")
  #if the bag is empty, will generate a new bag
  if bag != []:
    #shows what block will come next
    next_text = pygame.font.Font.render(font, f"Up Next: {bag[0]}", False, (255, 255, 255))
    screen.blit(next_text, [300, 60])
  pygame.display.update()
  running, x = quit_check()
  screen.fill(bg_colour)
  key = key_check(x)
#does right movement
  if key == "right" and active_positions[3][0] < 240 and type == tile_set[5] and (rotation == 1 or rotation == 4) or key == "right" and active_positions[3][0] < 270 and type == tile_set[0] or key == "right" and active_positions[3][0] < 270 and type == tile_set[3] or key == "right" and active_positions[3][0] < 210 and type == tile_set[4] and rotation == 1 or key == "right" and active_positions[3][0] < 270 and type == tile_set[4] and rotation == 2 or key == "right" and active_positions[3][0] < 240 and type == tile_set[1] and (rotation == 1 or rotation == 2) or key == "right" and active_positions[3][0] < 270 and type == tile_set[2] and (rotation == 1 or rotation == 3 or rotation == 4) or key == "right" and active_positions[3][0] < 270 and type == tile_set[6] and rotation == 1 or key == "right" and active_positions[3][0] < 240 and type == tile_set[5] and rotation == 2 or key == "right" and active_positions[3][0] < 270 and type == tile_set[5] and rotation == 3 or key == "right" and active_positions[3][0] < 240 and type == tile_set[6] and rotation == 2 or key == "right" and active_positions[3][0] < 240 and type == tile_set[1] and rotation == 3 or key == "right" and active_positions[3][0] < 270 and type == tile_set[1] and rotation == 4 or key == "right" and active_positions[3][0] < 210 and type == tile_set[2] and rotation == 2 :
    #checks if any overlaps would occur
    for i in active_positions:
      for b in inactive_positions:
        if i[0] + 30 == b[0] and i[1] == b[1]:
          #records the overlap
          right_check += 1
    #if there is no overlap move the piece
    if right_check == 0:
      for i in active_positions:
        i[0] += 30
 
  elif key == "left" and (active_positions[3][0] > 30 and type == tile_set[0] or active_positions[3][0] > 0 and type == tile_set[3] or active_positions[3][0] > 30 and type == tile_set[5] and (rotation == 1 or rotation == 3 or rotation == 4) or active_positions[3][0] > 0 and type == tile_set[4] and rotation == 1 or active_positions[3][0] > 0 and (rotation == 1 or rotation == 3) and type == tile_set[1] or active_positions[3][0] > 30 and type == tile_set[2] and (rotation == 1 or rotation == 3) or active_positions[3][0] > 60 and type == tile_set[6] and rotation == 1 or active_positions[3][0] > 30 and type == tile_set[4] or active_positions[3][0] > 0 and type == tile_set[6] and rotation == 2 or rotation == 2 and active_positions[3][0] > 30 and type == tile_set[1] or active_positions[3][0] > 60 and type == tile_set[1] and rotation == 4 or active_positions[3][0] > 0 and type == tile_set[2] and rotation == 2 or active_positions[3][0] > 60 and type == tile_set[2] and rotation == 4 or active_positions[3][0] > 0 and type == tile_set[5] and rotation == 2):
    #checks if any overlaps would occur
    for i in active_positions:
      for b in inactive_positions:
        if i[0] - 30 == b[0] and i[1] == b[1]:
          #records the overlap
          left_check += 1
    #if there is no overlap move the piece
    if left_check == 0:
      for i in active_positions:
        i[0] -= 30
  for i in active_positions:
    screen.blit(type, i)
  for i in inactive_positions:
    screen.blit(placed, i)
  #checks if piece is at bottom of board
  if active_positions[3][1] >= 570 and delay <= 0:
    VariableMc_Shmariable_Fifty7 = 0
    for i in active_positions:
     inactive_positions.append(i)
    for item in active_positions:
        active_positions[looper_count] = [0, 0]
        looper_count += 1
    #resets delay between ticks (delay determines how fast blocks fall)
    if difficulty == "1":
      delay = 20
    elif difficulty == "2":
      delay = 15
    elif difficulty == "3":
      delay = 10
    elif difficulty == "thomas_langford":
      delay = 0
    else:
      delay = 5
  if delay <= 0 and active_positions[3][1] < 570 or key == "down" and active_positions[3][1] < 570:
    temp_variable = 0
    #checks if any overlaps would occur
    for i in active_positions:
      for b in inactive_positions:
        if i[1] + 30 == b[1] and i[0] == b[0]:
          #records the overlap
          down_check += 1
    #if there is no overlap
    if down_check == 0:
      for i in active_positions:
        i[1] += 30
    
    else:
        VariableMc_Shmariable_Fifty7 = 0
        for i in active_positions:
          inactive_positions.append(i)
        for item in active_positions:
          active_positions[looper_count] = [0, 0]
          looper_count += 1
    if difficulty == "1":
      delay = 20
    elif difficulty == "2":
      delay = 15
    elif difficulty == "3":
      delay = 10
    elif difficulty == "thomas_langford":
      delay = 0
    else:
      delay = 5
  else: 
    delay -=1+(0.00125*score)
  
  clock.tick(30)
  #used to check for cheaters
  langford_check = {1}
  langford_check.remove(1)
  for itemmmmm in inactive_positions:
    langford_check.add(tuple(itemmmmm))
  if len(langford_check) != len(inactive_positions):
    difficulty = "thomas_langford"
  #checks when a line needs to be cleared
  for i in inactive_positions:
    if i[1] == 0:
      running = False
    dictionary_for_y_values[i[1]] += 1
    for j in dictionary_for_y_values:
      if dictionary_for_y_values[j] >= 10:
        temp_variable += 1
        score += 100*temp_variable
        to_remove = [k for k in inactive_positions if k[1] == j]
        while to_remove:
          for p in inactive_positions:
            if p in to_remove:
              inactive_positions.remove(p)
              to_remove.remove(p)
        for p in inactive_positions:
          if p[1] < j:
            p[1] += 30
            
#game over screen
screen.blit(end, [0, 0])
screen.blit(score_text, [200, 30])
pygame.display.update()
sleep(5)   
pygame.quit()
