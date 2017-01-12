##
# Bus vs car problem with input from user
#

# Algorithm

# For bus:
# Prompt user for bus price ticket for one way
# mutiply that answer by 2 (for two way tkt)
# Calculate total cost for bus (total tkt cost * 50 days)

# For car:
# Prompt user for fuel efficiency of car (in L/km)
# Prompt user for gas price (store as constant)
# prompt user for distance to campus
# mutiply distance by 2 (store as constant)
# prompt user for maintenance cost per km (store as constant)
# prompt user for parking cost
# calculate total fuel cost ((fuel efficiency) * (gas price) * (distance to and from campus))
# calculate total maintenance cost ((distance to and from campus) * (maintenance cost per km))
# calculate total cost for driving car (((fuel cost) + (maintenance cost) + (parking cost)) *50)

print(
    'This program is desinged to determine whether it is cheaper to take the bus to campus, or to drive your car. Input your answers as numbers only (i.e. no $ signs needed)')
print()

startPrompt = input('Do you want to continue (yes or no)? ')
if startPrompt == "no":
    print()
    print('You said "no", therefore, we shall end it there.')
    quit()

# Calculations for bus

userInput = float(input('How much does a one-way bus ticket cost you (in $)? '))
busTkt = userInput * 2
totalBusCost = busTkt * 50

# Calculations for car

fuelEfficiency = float(input('How fuel efficient is your car (L/km)? '))
GAS_PRICE = float(input('What is the current gas price in your city (in $)? '))
DISTANCE = float(input('How far is campus from your house (in kms)? ')) * 2
MAINTENANCE = float(input('What is your maintenance cost per km (in $)? '))
parkingCostPerDay = float(input('How much does parking cost on campus per day? '))

totalFuelCost = fuelEfficiency * GAS_PRICE * DISTANCE
totalMaintenanceCost = DISTANCE * MAINTENANCE

totalCarCost = (totalFuelCost + totalMaintenanceCost + parkingCostPerDay) * 50

# This part decides which transportation method is cheapest based on the above calculations
print()
if totalCarCost <= totalBusCost:
    print('Take your car!')
else:
    print('I know you wanna take your car, but it\'s cheaper to take the bus.')

print()
print('Thanks for using BUS vs CAR')
