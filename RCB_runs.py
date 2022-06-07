from csv import DictReader
from matplotlib import pyplot as plt

def RCB():
    with open("deliveries.csv","r") as deliv:
        match_reader=DictReader(deliv)
        matchRuns = list(match_reader)
        batsmen={}
        for match in matchRuns:
            if match['batting_team']=='Royal Challengers Bangalore':
                batsmen[match['batsman']] = batsmen.get(match['batsman'],[]) + [int(match['total_runs'])]
        BatNames = []
        totalRunsCount = []
        for key in batsmen:
            BatNames.append(key)
            totalRunsCount.append(sum(batsmen[key]))
    BatRuns = dict(zip(BatNames,totalRunsCount))
    sortedBatRuns = {k: v for k, v in sorted(BatRuns.items(), key= lambda v: v[1], reverse = True)}
    BatName = []
    totalRunCount = []
    for key in sortedBatRuns:
        BatName.append(key)
        #print(sortedBatRuns[key],sortedBatRuns[key])
        totalRunCount.append(sortedBatRuns[key])
    del BatName[10:]
    del totalRunCount[10:]
    #print(BatName)
    #print(totalRunCount)
    return BatName,totalRunCount
#RCB()

def plot(plt_BatNames,plt_Runs):
    x = plt_BatNames
    y = plt_Runs
    plt.bar(x,y)
    plt.ylabel('Total Runs')
    plt.xlabel('Batsmen')
    plt.show()


def execute():
    plt_BatNames,plt_Runs = RCB()
    plot(plt_BatNames,plt_Runs)    
execute()