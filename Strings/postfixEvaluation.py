def postfixEvaluate(expression):
    stack =[0]
    i=0
    operators=['+','*','/','-']
    while i<len(expression):

        if expression[i] not in operators:

            stack.append(expression[i])

        else:

            num2 = int(stack.pop(-1))
            num1 = int(stack.pop(-1))

            stack.append(evalExp(num1,num2,expression[i]))

        i+=1

    if len(stack)==2:
        return stack[-1]



def evalExp(num1,num2,exp):

    if exp=='+':
        return str(num1+num2)
    elif exp=="*":
        return str(num1*num2)
    elif exp=="/":
        return str(num1//num2)
    else:
        return str(num1-num2)

n=int(input())

for _ in range(n):
    exp = input()
    print(postfixEvaluate(exp))
