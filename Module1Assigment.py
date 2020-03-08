

string1 = 'Discover, Learning, with, Edureka'

print (string1)
print (string1.count("a"))
print (string1.count("o"))

print (string1.count("L"))
print (string1.count("N"))

string2 = 'www.edureka.in'

print (string2)
print (string2.replace("w", ""))

string2Edit = string2.replace("w", "")
string2Edit = string2Edit.replace("in", "")

print (string2Edit)

print ('0X7AE is hexadecimal')
print('3+4j is complex')
print ('-01234 is an octal integer')
print ('3.14e-2 is an exponential of log10')

character = 'a'
print ('This a %s string formatting example.' % character)

number = -1234
print('%d is a signed integer.' % number)

octal = 0o1234
print ('0o1234 = %d is an octal number.' % octal)

hexa = 0x1234
print ('0x1234 = %d is an hexadecimel number.' % hexa)

fnumber = 12.34
print ('%f is a floating point real number.' % fnumber)

expo = 1.234e5
print ('1.234e5 = %d is an exponential number.' % expo)
