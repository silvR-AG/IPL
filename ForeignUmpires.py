from csv import DictReader
from matplotlib import pyplot as plt

def Umpires():
    with open("umpires.csv","r") as umpire:
        ump_reader=DictReader(umpire)
        matchUmps = list(ump_reader)
        #print(matchUmps)
        Umpire = {}
        for ump in matchUmps:
            if ump[' country']!= ' India':
                Umpire[ump[' country']] = Umpire.get(ump[' country'],[]) + [ump['umpire']]
        Country = []
        UmpCount = []
        for key in Umpire:
            Country.append(key)
            UmpCount.append(len(Umpire[key]))
    return Country,UmpCount
#Umpires()

def plot(plt_Country,plt_Umps):
    x = plt_Country
    y = plt_Umps
    plt.bar(x,y)
    plt.ylabel('Total Umpires')
    plt.xlabel('Country')
    plt.show()



def execute():
    plt_Country,plt_Ump = Umpires()
    plot(plt_Country,plt_Ump)    
execute()