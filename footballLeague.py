"""
Football League

This script automates the process of logging football match scores and assigning points to teams based on the match result.

"""

league = {"CELTIC": 3, "RANGERS": 0, "ABERDEEN": 0}
# create dict object to store football league teams and their points.

while True: #start infinite loop - this is useful where continuous operations are required that are broken or interupted only when certain input is provided.
    homeTeam = input("Please enter the home team: ").upper() #homeTeam variable stores user input. Syntax suggests Python 3. Is that right?
    if homeTeam == "quit": #if user types the string "quit"
        break #interupt the infinite loop
    if homeTeam in league: #see if user input string matches an entry in the league dict.
        #SUGGESTION from MR: for reference to league dict in line 17, be explicit about the fact it's the dict KEYS your looking in for a match with homeTeam variable. Use league.keys()
        existingHomePoints = league.get(homeTeam) # get the value associated with the key in the dict that matches the homeTeam variable.
        print("{} currently has {} points".format(homeTeam, existingHomePoints)) # print some facts for the user. Modern formatting syntax employed.
    else:
        print("We don't have a team called " + homeTeam) #some simple error handling to deal with user entering a team that isn't in the league.

    awayTeam = input("Please enter the away team: ").upper()
    if awayTeam == "quit":
        break
    if awayTeam in league:
        existingAwayPoints = league.get(awayTeam)
        print("{} currently has {} points".format(awayTeam, existingAwayPoints))
    else:
        print("We don't have a team called " + awayTeam)

    homeScore = input("Please enter number of goals scored by {}: ".format(homeTeam)) # homeScore variable stores user input
    awayScore = input("Please enter number of goals scored by {}: ".format(awayTeam)) # awayScore variable stores user input

    homePoints = 0  # create variable to store home points as an integer. Set to zero at point of object creation.
    awayPoints = 0  # create variable to store away points as an integer. Set to zero at point of object creation.
    postGameHomePoints = 0
    postGameAwayPoints = 0

    if homeScore > awayScore: # compares variables
        postGameHomePoints = homePoints + 3  # when above condition is met adds three points to the existing number of points held by the home team
        postGameAwayPoints = awayPoints + 0
    elif homeScore == awayScore:  # compares variables
        postGameHomePoints = homePoints + 1  # when above condition is met adds one point to the existing number of points held by the home team
        postGameAwayPoints = awayPoints + 1  # when above condition is met adds one point to the existing number of points held by the away team
    elif homeScore < awayScore:  # compares variables
        postGameAwayPoints = awayPoints + 3  # when above condition is met adds three points to the existing number of points held by the away team
        ostGameHomePoints = homePoints + 0

    print()
    print("{} gets: {} points".format(homeTeam, postGameHomePoints))
    print("{} gets: {} points".format(awayTeam, postGameAwayPoints))
    print()
    # prints number of points for user to view.

    totalHomePoints = int(existingHomePoints) +int(postGameHomePoints) # calculates the number of points the home team now has in the league
    print("{} now has a total of {} points in the league".format(homeTeam, totalHomePoints))

    totalAwayPoints = int(existingAwayPoints) +int(postGameAwayPoints) # calculates the number of points the home team now has in the league
    print("{} now has a total of {} points in the league".format(awayTeam, totalAwayPoints))

    league[homeTeam] = totalHomePoints # updates the dict object with the number of points
    league[awayTeam] = totalAwayPoints

    print(league)


