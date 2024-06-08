import random
import datetime
from tqdm import tqdm

def comparison(birthdayList):
    # At least one pair must have a matching birthday; One set with multiple birthdays is not counted.
    if (len(birthdayList) - len(set(birthdayList)) > 0):
        return 1
    return 0

def simulation(numBirthdays):
    numSameBirthdays = 0
    print(f"\n\nGenerating {numBirthdays} random birthdays 1,000,000 times...")
    input("Press Enter to continue...")
    for i in tqdm(range(1_000_000)):
        birthdayList = generateBirthdays(numBirthdays)
        numSameBirthdays += comparison(birthdayList)
    percentage = numSameBirthdays / 10000
    print(f"Out of 1,000,000 simulations of {numBirthdays} people, there was a matching birthday in the group {numSameBirthdays} times.")
    print(f"This means that {numBirthdays} people have a {percentage:.2f}% chance of having at least one matching birthday in their group. ")

def firstComparison(birthdayList):
    hashset = set()
    for i in range(len(birthdayList)):
        if birthdayList[i] in hashset:
            print(f"\nIn this simulation, multiple people have a birthday on {birthdayList[i]}")
        hashset.add(birthdayList[i])

def generateBirthdays(birthdaysRequested):
    # 1980 is a leap year
    startDate = datetime.datetime(1980,1,1)
    birthdayList = []
    for i in range(birthdaysRequested):
        # Takes into account 1980 is a leap year
        randomDay = random.randrange(0,367)
        newDate = startDate + datetime.timedelta(days=randomDay)
        birthdayList.append(newDate.strftime("%b %d"))
    return birthdayList

def main():
    print("Birthday Paradox")

    birthdaysRequested = int(input("How many birthdays shall I generate? (Max 100) >"))
    print(f"\nHere are {birthdaysRequested} birthdays:")
    
    birthdayList = generateBirthdays(birthdaysRequested)
    print(birthdayList)

    firstComparison(birthdayList)

    simulation(birthdaysRequested)

if __name__ == "__main__":
    main()