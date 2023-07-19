 #? Python Scripts to Display Georgia Institute Of Technology Football Data

def all_time_record(opponent): ## Choose an Opponent Team to Display Wins/Losses/Ties 
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    wins = 0
    losses = 0
    ties = 0
    
    itemlist = []
    
    for line in alllines:
        itemlist = line.split(",")
        if opponent in itemlist:

            if int(itemlist[3]) > int(itemlist[4]):
                wins +=1
            if int(itemlist[3]) < int(itemlist[4]):
                losses +=1
            if int(itemlist[3]) == int(itemlist[4]):
                ties += 1
            
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def first_team_played(): ## First Team GA Tech Ever Played
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    dates = []
    for line in alllines:
        itemlist = line.split(",")
        dates.append(itemlist[0])
    
    sorteddates = sorted(dates, key= lambda x: x)
    for line in alllines:
        itemlist = line.split(",")
        if sorteddates[0] in itemlist:
            return itemlist[1]
    
def all_time_points(opponent): ## Total Points GA Tech Has Scored
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    points = 0
    
    
    itemlist = []
    
    for line in alllines:
        itemlist = line.split(",")
        if opponent in itemlist:
            points += int(itemlist[3])
    return points
      
def GAall_time_HomeGame_Record(): ## All Wins/Losses/Ties on Home Field
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    wins = 0
    losses = 0
    ties = 0
    
    itemlist = []
    
    for line in alllines:
        itemlist = line.split(",")
        if itemlist[2] == "Home":

            if int(itemlist[3]) > int(itemlist[4]):
                wins +=1
            if int(itemlist[3]) < int(itemlist[4]):
                losses +=1
            if int(itemlist[3]) == int(itemlist[4]):
                ties += 1
            
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def year_all_time_record(year): ## Wins/Losses/Ties of Specified Year
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    wins = 0
    losses = 0
    ties = 0
    
    itemlist = []
    
    for line in alllines:
        itemlist = line.split(",")
        if year in itemlist[0]:
            print(itemlist[0])

            if int(itemlist[3]) > int(itemlist[4]):
                wins +=1
            if int(itemlist[3]) < int(itemlist[4]):
                losses +=1
            if int(itemlist[3]) == int(itemlist[4]):
                ties += 1
            
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def month_all_time_record(month): ## Wins/Losses?Ties of Specified Month
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    wins = 0
    losses = 0
    ties = 0
    
    itemlist = []
    
    for line in alllines:
        itemlist = line.split(",")
        if month in itemlist[0]:
            print(itemlist[0])

            if int(itemlist[3]) > int(itemlist[4]):
                wins +=1
            if int(itemlist[3]) < int(itemlist[4]):
                losses +=1
            if int(itemlist[3]) == int(itemlist[4]):
                ties += 1
            
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def between_years_all_time_record(startyear, endyear): ## W/L/Ts Within a Span of Years
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    wins = 0
    losses = 0
    ties = 0

    for line in alllines:
        start = startyear
        end = endyear

        while start <= end:
            if str(start) in line:
                print(line)

                itemlist = line.split(",")

                if int(itemlist[3]) > int(itemlist[4]):
                    wins += 1
                elif int(itemlist[3]) < int(itemlist[4]):
                    losses += 1
                else:
                    ties += 1
            start += 1

    record_file.close()
    return str(wins) + "-" + str(losses) + "-" + str(ties)

def most_scored_on_team(): ## Team GA Tech Has Scored the Most Points On
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    teamdict= {}
    
    for line in alllines:
        itemlist = line.split(",")
        
        if itemlist[1] not in teamdict:
            try:
                teamdict[itemlist[1]] = int(itemlist[3])
            except ValueError:
                pass
        else:
            teamdict[itemlist[1]] += int(itemlist[3])

    highest_score_team = max(teamdict, key=teamdict.get)
    return highest_score_team
        
def GA_Never_Scored_On_This_Team(): ## Teams GA Tech Has Never Scored On Ever
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    nopoints = []
    for line in alllines:
        itemlist = line.split(",")
        if itemlist[3] == "0":
            name = itemlist[1]
            nopoints.append(name)
        
    for line in alllines:
        itemlist = line.split(",")
        for name in nopoints:
            if name in itemlist:
                if itemlist[3] != "0":
                    nopoints.remove(name)
                    
    return nopoints  
    
def Team_Never_Scored_On_GA(): ## Teams That Have Never Scored on GA Tech Ever
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()
    nopoints = []
    
    for line in alllines:
        itemlist = line.split(",")
        if itemlist[4] == "0" or itemlist[4] == "0\n":
            nopoints.append(itemlist[1])
    nopoints = list(set(nopoints))
    
    haspoints = []
    for line in alllines:
        itemlist = line.split(",")
        for name in nopoints:
            if name in itemlist:
                
                if itemlist[4] == "0" or itemlist[4] == "0\n":
                    continue
                else:
                    haspoints.append(name)
    
    for name in haspoints:
        if name in nopoints:
            nopoints.remove(name)
            
    return len(nopoints)

def highest_point_differential(): ## Team that GA Tech Has the Highest Point Differential On
    record_file = open('georgia_tech_football.csv', 'r')
    alllines = record_file.readlines()

    teamstats = {}
    total_games = {}
    ga_scored = {}
    op_team_scored = {}
    overall_diff = {}

    for line in alllines:
        itemlist = line.split(",")
        team_name = itemlist[1].strip()  

        if team_name not in teamstats:
            try:
                total_games[team_name] = 1
                ga_scored[team_name] = int(itemlist[3])
                op_team_scored[team_name] = int(itemlist[4])

                teamstats[team_name] = {
                    'games_played': total_games[team_name],
                    'GA_scored': ga_scored[team_name],
                    'Op_Team_Scored': op_team_scored[team_name],
                }
            except ValueError:
                pass
        else:
            total_games[team_name] += 1
            ga_scored[team_name] += int(itemlist[3])
            op_team_scored[team_name] += int(itemlist[4])

            teamstats[team_name] = {
                'games_played': total_games[team_name],
                'GA_scored': ga_scored[team_name],
                'Op_Team_Scored': op_team_scored[team_name],
            }

    for team, stats in teamstats.items():
        
        if 'games_played' in stats and stats['games_played'] >= 5:
            overall_diff[team] = (stats['GA_scored'] - stats['Op_Team_Scored']) / stats['games_played']

    highest_diff_team = max(overall_diff, key=overall_diff.get)
    highest_diff_value = overall_diff[highest_diff_team]

    return highest_diff_team, highest_diff_value


