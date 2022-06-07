import matplotlib
from matplotlib import pyplot as plt
from csv import DictReader
# allTeamsData={}
# for row in csvreader:
#     year = 2017
#     if year == 2017:
#         team1 = row['bowling_team']
#         team2 = row['batting team']
#         if team1 not in allTeamsData:
#             allTeamsData[team1]=1
#         else:
#             allTeamsData[team1]+=1
def by_teams():
    with open('matches.csv','r') as match:
        reader = DictReader(match)
        byTeam = list(reader)
        print(byTeam)
by_teams()
