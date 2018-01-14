league = {"Celtic": 3, "Rangers": 0, "Aberdeen": 0}

homePoints = 0
awayPoints = 0

while True:
    homeTeam = input("Please enter the home team: ")
    if homeTeam == "quit":
        break
    if homeTeam in league:
        existingHomePoints = league.get(homeTeam)
        print("{} currently has {} points".format(homeTeam, existingHomePoints))
    else:
        print("We don't have a team called " + homeTeam)

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


