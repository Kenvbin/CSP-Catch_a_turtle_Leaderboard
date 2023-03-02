# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

spoco = ['pink','red' ,'green' ,'blue' ,'orange']
sposha = ["turtle","arrow" ,"circle" ,"square" ,"triangle"]
#-----game configuration----
score = 0
spot_size = 2
spot_color = random.choice(spoco)
spot_shape = random.choice(sposha)
spot_size =  random.randint(2,5)
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name: ")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.speed(0)

#-----countdown variables-----
font_setup = ("Ariel", 10, "bold")
timer = 30
spot_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------
def circlelelelel_click(x,y):
  global score, spot_size, spot_color, sposhaha, spot_shape, spot
  score = score + 1
  spot_size =  random.randint(2,5)
  spot_color = random.choice(spoco)
  spot_shape = random.choice(sposha)
  spot.shape(spot_shape)
  spot.shapesize(spot_size)
  spot.fillcolor(spot_color)
  wex = random.randint(-400,400)
  why = random.randint(-200,200)
  spot.penup()
  spot.setposition(wex, why)
  spot.pendown()

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

def countdown():
  global timer, timer_up
  spot.clear()
  if timer <= 0:
    spot.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    print("You clicked tracy the shapeshifter a total of",score,"times")
    print("Good job now run the program again!")
    spot.hideturtle()
  else:
    spot.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    spot.getscreen().ontimer(countdown, spot_interval) 

#-----events----------------
spot.onclick(circlelelelel_click)
wn = trtl.Screen()
wn.ontimer(countdown, spot_interval) 
wn.mainloop()