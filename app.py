import random
import datetime

def comparison(birthdayList):
    sameBirthday = 0
    hashset = set()
    for i, date in enumerate(birthdayList):
        if date in hashset:
            sameBirthday += 1
        hashset.add(date)
    return sameBirthday

def simulation_count(simulationNumber):
    if simulationNumber == 10_000:
        print("10,000 simulations run...")
    elif simulationNumber == 20_000:
        print("20,000 simulations run...")
    elif simulationNumber == 30_000:
        print("30,000 simulations run...")
    elif simulationNumber == 40_000:
        print("40,000 simulations run...")
    elif simulationNumber == 50_000:
        print("50,000 simulations run...")
    elif simulationNumber == 60_000:
        print("60,000 simulations run...")
    elif simulationNumber == 70_000:
        print("70,000 simulations run...")
    elif simulationNumber == 80_000:
        print("80,000 simulations run...")
    elif simulationNumber == 90_000:
        print("90,000 simulations run...")
    elif simulationNumber == 99_999:
        print("100,000 simulations run...")

def simulation(numBirthdays):
    numSameBirthdays = 0
    list = []
    print(f"\n\nGenerating {numBirthdays} random birthdays 100,000 times...")
    foo = input("Press Enter to continue...")
    for i in range(100_001):
        simulation_count(i)
        list = generateBirthdays(numBirthdays)
        numSameBirthdays += comparison(list)
    print(f"Out of 100,000 simulations of {numBirthdays} people, there was a "
      f"matching birthday in that group {numSameBirthdays} times. This means "
      f"that {numBirthdays} people have a {numSameBirthdays / 1000:.2f}% chance of "
      f"having a matching birthday in their group. "
      "That's probably more than you would think!")



def firstComparison(birthdayList):
    hashset = set()
    for i, date in enumerate(birthdayList):
        if date in hashset:
            print(f"\nIn this simulation, multiple people have a birthday on {date}")
        hashset.add(date)

def generateBirthdays(birthdaysRequested):
    startDate = datetime.datetime(1980,1,1)
    birthdayList = []
    for i in range(birthdaysRequested):
        randomDay = random.randrange(366)
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