import re

print ('\nQuestion 1 \n')

dates = '''
1980-12-25
25-12-1980
1980-01-01
01-01-1980
'''
print (dates)

print ('Matching date format:')

pattern = re.compile(r'\d\d\d\d-\d\d-\d\d')
matches = pattern.finditer(dates)

for match in matches:
    print (match)

print ('Matching date and format:')

pattern = re.compile(r'1980-12-25')
matches = pattern.finditer(dates)

for match in matches:
    print (match)


print ('\nQuestion 2 \n')

ssnNo = '''
123456789
123-45-6789
987-65-4321
123.45.6789
987.65.4321
01-01-1980
'''
print (dates)

print ('Matching SSN format:')

pattern = re.compile(r'\d\d\d-\d\d-\d\d\d\d')
matches = pattern.finditer(ssnNo)

for match in matches:
    print (match)

print ('Matching SSN number and format:')

pattern = re.compile(r'123-45-6789')
matches = pattern.finditer(ssnNo)

for match in matches:
    print (match)


print ('\nQuestion 3 \n')

ipAddresses = '''
123.123.123.123
111.111.111.111
222.222.222.222
255.255.255.255
000.000.000.000
123-123-123-123
111-111-111-111
222-222-222-222
255-255-255-255
000-000-000-000
'''

print (ipAddresses)

print ('Matching IP address format:')
pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d')
matches = pattern.finditer(ipAddresses)

for match in matches:
    print (match)

print ('Matching IP address and format:')
pattern = re.compile(r'123\.123\.123\.123')
matches = pattern.finditer(ipAddresses)

for match in matches:
    print (match)
