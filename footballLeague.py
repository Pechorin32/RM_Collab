"""
Football League

This script automates the process of logging football match scores and assigning points to teams based on the match result.

"""

league = {"Celtic": 3, "Rangers": 0, "Aberdeen": 0} #create dict object to store football league teams and their points. 

homePoints = 0 # create variable to store home points as an integer. Set to zero at point of object creation.
awayPoints = 0 # create variable to store away points as an integer. Set to zero at point of object creation.

while True: #start infinite loop - this is useful where continuous operations are required that are broken or interupted only when certain input is provided.
    homeTeam = input("Please enter the home team: ") #homeTeam variable stores user input. Syntax suggests Python 3. Is that right?
    if homeTeam == "quit": #if user types the string "quit" 
        break #interupt the infinite loop
    if homeTeam in league: #see if user input string matches an entry in the league dict.
        #SUGGESTION from MR: for reference to league dict in line 17, be explicit about the fact it's the dict KEYS your looking in for a match with homeTeam variable. Use league.keys() 
        existingHomePoints = league.get(homeTeam) # get the value associated with the key in the dict that matches the homeTeam variable.
        print("{} currently has {} points".format(homeTeam, existingHomePoints)) # print some facts for the user. Modern formatting syntax employed.
    else:
        print("We don't have a team called " + homeTeam) #some simple error handling to deal with user entering a team that isn't in the league.

 ### DM TO CONTINUE COMMENTING CODE FROM HERE###

    awayTeam = input("Please enter the away team: ")
    if awayTeam == "quit":
        break
    if awayTeam in league:
        existingAwayPoints = league.get(awayTeam)
        print("{} currently has {} points".format(awayTeam, existingAwayPoints))
    else:
        print("We don't have a team called " + awayTeam)

    homeScore = input("Please enter number of goals scored by {}: ".format(homeTeam))
    awayScore = input("Please enter number of goals scored by {}: ".format(awayTeam))

    if homeScore > awayScore:
        homePoints += 3
    elif homeScore == awayScore:
        homePoints += 1
        awayPoints += 1
    elif homeScore < awayScore:
        awayPoints += 3

    print()
    print("{} gets: {} points".format(homeTeam, homePoints))
    print("{} gets: {} points".format(awayTeam, awayPoints))
    print()

    totalHomePoints = int(existingHomePoints) +int(homePoints)
    print("{} now has a total of {} points in the league".format(homeTeam, totalHomePoints))

    totalAwayPoints = int(existingAwayPoints) +int(awayPoints)
    print("{} now has a total of {} points in the league".format(awayTeam, totalAwayPoints))


# league[homeTeam] = points + homePoints
# league[awayTeam] = points + awayPoints


