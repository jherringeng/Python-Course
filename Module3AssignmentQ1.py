import random

level = raw_input ('Choose level (easy, intermediate, and hard): ')

questionsNo = raw_input ('Please give us the number of question you want to attempt: ')
questionsNo = int(questionsNo)

questionType = raw_input ('Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ')

i = 1
for i in range(questionsNo):

    if level == 'easy':
        op1 = random.randint(1,11)
        op2 = random.randint(1,11)
    elif level == 'intermediate':
        op1 = random.randint(-21,21)
        op2 = random.randint(-21,21)
    else:
        op1 = random.randint(-101,101)
        op2 = random.randint(-101,101)

    op1 = float(op1)
    op2 = float(op2)

    if questionType == 'M':
        operator = 'multiplied by'
        ans = op1 * op2

    elif questionType == 'A':
        operator = 'added to'
        ans = op1 + op2

    elif questionType == 'D':
        operator = 'divided by'
        ans = op1 / op2

    else:
        operator = 'subtracted by'
        ans = op1 - op2

    ansInput = raw_input('What\'s %d %s by %d?' %(op1, operator, op2))
    ansInput = float(ansInput)

    print(ans)
