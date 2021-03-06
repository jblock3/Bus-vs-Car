##
# Bus vs car problem with input from user
#

# Algorithm

# For bus:
# Prompt user for bus price ticket for one way
# multiply that answer by 2 (for two way tkt)
# Calculate total cost for bus (total tkt cost * 180 days)

# For car:
# Prompt user for fuel efficiency of car (in L/km)
# Prompt user for gas price (store as constant)
# prompt user for distance to campus
# multiply distance by 2 (store as constant)
# prompt user for maintenance cost per km (store as constant)
# prompt user for parking cost
# calculate total fuel cost ((gas price) / (fuel efficiency) * (distance to campus))
# calculate total maintenance cost ((distance to and from campus) * (maintenance cost per km))
# calculate total cost for driving car (((fuel cost) + (maintenance cost) + (parking cost)) * 180)

print('This program is designed to determine whether it is cheaper to take the bus to campus, or to drive your car over a period of 180 days (avg. amount of days of school per year). Input your answers as numbers only (i.e. no $ signs needed)')
print()

startPrompt = input('Do you want to continue (yes or no)? ')
if startPrompt == "no":
    print()
    print('You said "no", therefore, we shall end it there.')
    print()
    print('See you next time!')
    quit()

# Calculations for bus

userInput = float(input('How much does a one-way bus ticket cost you (in $)? '))
busTkt = userInput * 2
totalBusCost = busTkt * 180

# Calculations for car

fuelEfficiency = float(input('How fuel efficient is your car (km/L)? '))
GAS_PRICE = float(input('What is the current gas price in your city (in $)? '))
DISTANCE = float(input('How far is campus from your house (in kms)? ')) * 2
MAINTENANCE = float(input('What is your maintenance cost (in $/km)? '))
parkingCostPerDay = float(input('How much does parking cost on campus per day? '))

totalFuelCost = GAS_PRICE / fuelEfficiency * DISTANCE
totalMaintenanceCost = DISTANCE * MAINTENANCE

totalCarCost = (totalFuelCost + totalMaintenanceCost + parkingCostPerDay) * 180

# This part decides which transportation method is cheapest based on the above calculations
print()
if totalCarCost <= totalBusCost:
    print('Take your car!')
else:
    print('I know you wanna take your car, but it\'s cheaper to take the bus.')

print()


print('It will cost you, over a period of 180 days,' + ' ' + '$' + "%.2f" % totalBusCost + ' ' + 'to take the bus,' + ' ' + 'and' + ' ' + '$' + "%.2f" % totalCarCost + ' ' + 'to take your car!')

print()
print('Thanks for using BUS vs CAR')
print()
print('See you soon ;)')
