# Q2
name = raw_input ('Enter your name: ')
print ('Hello %s.' % name)

# Q3
tempF = raw_input ('What is the current temperature in Farenheit: ')
tempF = float(tempF)
tempC = (tempF - 32.0) * 5.0 / 9.0

print ('%f C' %tempC)

# Q4
hoursWorked = raw_input ('How many hours do you work? ')
hoursWorked = float(hoursWorked)

hoursPay = raw_input ('How much are you paid per hour? ')
hoursPay = float(hoursPay)

weeksPay = hoursWorked * hoursPay
print ('You earn %f per week.' % weeksPay)
