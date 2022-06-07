from csv import DictReader
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def total_runs():
    with open("deliveries.csv","r") as deliv:
        match_reader=DictReader(deliv)
        match_runs = list(match_reader)
        tot_runs={}
        for match in match_runs:
            tot_runs[match['batting_team']] = tot_runs.get(match['batting_team'],[]) + [int(match['total_runs'])]
        teamNames = []
        totalRunsCount = []
        for key in tot_runs:
            teamNames.append(key)
            totalRunsCount.append(sum(tot_runs[key]))
    return teamNames,totalRunsCount
def plot(plt_teamNames,plt_runs):
    x = plt_teamNames
    y = plt_runs
    plt.bar(x,y)
    plt.ylabel('Total Runs')
    plt.xlabel('Team Names')
    plt.show()


def execute():
    plt_teamNames,plt_runs = total_runs()
    plot(plt_teamNames,plt_runs)
execute()
