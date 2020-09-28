import sys
import math
import os.path

path = 'C:\\Users\\rtb32\\Desktop\\StatTrackerPY'
dir_list = os.listdir(path)
print(dir_list)
print()
game = input()
print(game)
enterData = ''

def datafile(path, file):
    print("File not found, making one.")
    with open(os.path.join(path, file), 'w+') as fp:
        pass
    return 1
def matchStats():
    while enterData == '1':
        fo = open('ApexStats.txt', 'a')
        gameNum = ''
        gameDate = ''
        gameKills = ''
        print('Match Number?')
        input(gameNum)
        print('Match Kills?')
        input(gameKills)
        print('Match Date?')
        input(gameDate)
        fo.write(gameNum, gameDate, gameKills)
#Check for Apex data file and create one if not found.
if game == '1':
    print("Opening Apex data...")
    file = 'ApexStats.txt'
    path = 'C:\\Users\\rtb32\\Desktop\\StatTrackerPY\\APEX_Stats'
    enterData = ''
    if os.path.isfile('C:\\Users\\rtb32\\Desktop\\StatTrackerPY\\APEX_Stats\\ApexStats.txt'): #Can you call function from inside a function?
        print("Stat file found! Enter new data?")
        print('Yes/No')
        input(enterData)
        print(enterData)
        matchStats()
    else:
        print("File Not Found.")

if game == '2':
    print("Opening CSGO data...")
    path = 'C:\\Users\\rtb32\\Desktop\\StatTrackerPY\\CSGO_Stats'
    if os.path.isfile('C:\\Users\\rtb32\\Desktop\\StatTrackerPY\\CSGO_Stats\\CSGOStats.txt'):
        print('Stat file found! Enter new data?')
    else:
        datafile('C:\\Users\\rtb32\\Desktop\\StatTrackerPY\\CSGO_Stats', 'CSGOStats.txt')
dir_list = os.listdir(path)
print(dir_list)

# Check for game-specific data file first.
# If file found -- ask for data
# Open file for new data/updated data.
# Ask for more data?
# Update data file.
# Pull data from data file.
# Calculate needed expressions.
# Update data file.
# Re-loop to step 2.
