#file to find the countries with the most gold medals in the 2016 summer olympics
import pandas as pd
import numpy as np
import collections

def main():
    #read file
    data = pd.read_csv("AlteryxDataCSV/athlete_events.csv")
    #print(data) #test print

    #drops not needed columns
    data=data.drop(['ID'],axis=1)
    data=data.drop(['Sex'],axis=1)
    data=data.drop(['Age'],axis=1)
    data=data.drop(['Height'],axis=1)
    data=data.drop(['Weight'],axis=1)
    data=data.drop(['NOC'],axis=1)
    data=data.drop(['Year'],axis=1)
    data=data.drop(['Season'],axis=1)
    data=data.drop(['City'],axis=1)

    #drops any row that isn't 2016 summer
    data=data.drop(data[(data.Games!='2016 Summer')].index)
    #test prints
    #pd.set_option("display.max_rows", None, "display.max_columns", None)
    #print(data)

    #drops any row without gold medals
    data=data.drop(data[(data.Medal != 'Gold')].index)

    #test prints
    #print(data.Games)
    #print(data)

    #counts gold medal countries
    goldWinningCountries = []
    for currentTeam in data.Team:
        goldWinningCountries.append(currentTeam)

    Frequencies=collections.Counter(goldWinningCountries)
    print(Frequencies)



main()
