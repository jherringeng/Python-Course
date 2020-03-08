from operator import itemgetter

x = int(raw_input('Please enter x: '))
n = int(raw_input('Please enter n: '))


xNPower = 1

def nPower(x, n):
    xNPower = 1
    if n >= 1:
        for i in range(1, n + 1):
            xNPower = xNPower * x
        print ('%d to the power %d = %d' % (x, n, xNPower))

    elif n <= -1:
        xNPower = float (xNPower)
        x = float (x)
        for i in range(n, 0):
            xNPower = xNPower / x
        print ('%d to the power %d = %f' % (x, n, xNPower))

    else:
        xNPower = 1
        print ('%d to the power %d = %d' % (x, n, xNPower))

    return

nPower(x, n)

mylist = [["john", 1, "a"], ["larry", 0, "b"]]
print (mylist)

mylistLambda = sorted(mylist, key = lambda n : n[1])

print (mylistLambda)

mylistItemgetter = sorted(mylist, key = itemgetter(1))
print (mylistItemgetter)
