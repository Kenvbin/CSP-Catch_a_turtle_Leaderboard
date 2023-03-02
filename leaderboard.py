# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# return names in the leaderboard file
def get_names(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  global names
  names = []
  for line in leaderboard_file:
    leader_name = ""
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1
    print("leader name is:", leader_name)
    # TODO 2: add the player name to the names list
    names.append(leader_name)
  leaderboard_file.close()

  #  TODO 6: return the names list in place of the empty list
  return names

  
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  # be sure you have created this
  global scores
  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0

    # TODO 3: use a while loop to index beyond the comma, skipping the player's name
    while (line[index] != ","):
      index = index + 1
      # TODO 4: use a while loop to get the score
    while (line[index + 1] != "/"):
      index = index + 1
      leader_score =leader_score + line[index]
    # TODO 5: add the player score to the scores list
    scores.append(int(leader_score))
  leaderboard_file.close()

  # TODO 7: return the scores in place of the empty list
  return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):
  global scores, names
  index = 0
  # TODO 8: loop through all the scores in the existing leaderboard list

  while ():
    # TODO 9: check if this is the position to insert new score at
    if (player_score >= leader_scores[index]):
      break
    else:
      index = index + 1

  
  # TODO 10: insert new player and score
  scores.insert(index, player_score)
  names.insert(index, player_name)
  # TODO 11: keep both lists at 5 elements only (top 5 players)
  if (len(names) > 5): 
    names.pop(5)
    scores.pop(5)
  # TODO 12: store the latest leaderboard back in the file
  

  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
 
  index = 0
  # TODO 13 loop through all the leaderboard elements and write them to the the file
  while (index < len(leader_names)):
    leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "/ \n")
    index = index + 1
  leaderboard_file.close()

  

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()
  index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while (index < len(leader_names)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  # TODO 14: display message about player making/not making leaderboard
  if (high_scorer):
    turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)


  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal

  if (player_score >= bronze_score and player_score < silver_score):
    turtle_object.write("You earned a bronze medal!", font=font_setup)
  elif (player_score >= silver_score and player_score < gold_score):
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif (player_score >= gold_score):
        turtle_object.write("You earned a gold medal!", font=font_setup)