import csv



if __name__ == '__main__':
  
  exp = []
  inexp = []
  dragons = []
  sharks = []
  raptors = []
  
  with open('soccer_players.csv', newline = '') as csvfile:
    player_list = csv.reader(csvfile, delimiter = ',')
    rows = list(player_list)
    
  #divde players in 2 group inexperience and experience
  def divide_group():
    for row in rows[1:]:
      if row[2] == 'YES':
        exp.append(row)
      elif row[2] == 'NO':
        inexp.append(row)
      
  #group players in 3 teams equally
  def team_up():
    for player in exp:
      if len(dragons) < int(len(exp)/3):
        dragons.append(player)
      elif len(sharks) < int(len(exp)/3):
        sharks.append(player)
      elif len(raptors) < int(len(exp)/3):
        raptors.append(player)
    
    for player in inexp:
      if len(dragons) < int(((len(rows)-1))/3):
        dragons.append(player)
      elif len(sharks) < int(((len(rows)-1))/3):
        sharks.append(player)
      elif len(raptors) < int(((len(rows)-1))/3):
        raptors.append(player)
      
  #create teams file which stores information of three teams
  def generate_txt():
    txt_file = open('teams.txt', 'w')
    
    txt_file.write('Dragons:\n\n')
    for player in dragons:
      txt_file.write(', '.join(player))
      txt_file.write('\n')
    
    txt_file.write('\nSharks:\n\n')
    for player in sharks:
      txt_file.write(', '.join(player))
      txt_file.write('\n')
      
    txt_file.write('\nRaptors:\n\n')
    for player in raptors:
      txt_file.write(', '.join(player))
      txt_file.write('\n')
    
  #create 18 welcome letters
  def welcome_letter():
    for player in dragons:
      name = player[0].split()
      letter = open('{}_{}.txt'.format(name[0].lower(), name[1]).lower(), 'w')
      letter.write('Dear {},\n\n'.format(player[3]))
      letter.write('Player {} will be in the Dragons team, the first practice will start on 26 September 7 A.M.'.format(player[0]))
      
    for player in sharks:
      name = player[0].split()
      letter = open('{}_{}.txt'.format(name[0].lower(), name[1]).lower(), 'w')
      letter.write('Dear {},\n\n'.format(player[3]))
      letter.write('Player {} will be in the Sharks team, the first practice will start on 26 September 9 A.M.'.format(player[0]))
                                                                                                                               
    for player in raptors:
      name = player[0].split()
      letter = open('{}_{}.txt'.format(name[0].lower(), name[1]).lower(), 'w')
      letter.write('Dear {},\n\n'.format(player[3]))
      letter.write('Player {} will be in the Raptors team, the first practice will start on 26 September 3 P.M.'.format(player[0]))
      
  
  divide_group()    
  team_up()
  generate_txt()
  welcome_letter()