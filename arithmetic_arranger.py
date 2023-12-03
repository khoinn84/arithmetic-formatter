def arithmetic_arranger(problems,Res=False):
    # verify initial input
    if len(problems) > 5:
        return "Error: Too many problems."
      
    firstline = ''
    secondline = ''
    thirdline = ''
    result = ''
    arranged_problems = ''
    middlestring = ' '*4
    lastItemCounter = 0
  
    for problem in problems:
        items = problem.split()

        # verify initial input
        if (items[1] != '+' and items[1] != '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'
        if (items[0].isnumeric() == False or items[2].isnumeric() == False):
            return 'Error: Numbers must only contain digits.'
        if (int(items[0])>9999 or int(items[2])>9999):
            return 'Error: Numbers cannot be more than four digits.'

        # length of the longer number
        maxlength = maxlen(items)

        # if this is the last item in the problems list, do not add 4 spaces at the end of first, second and third lines
        if lastItemCounter == len(problems)-1:
            middlestring = ''
        lastItemCounter += 1
      
        firstline += '  ' + fullstring(items[0], maxlength) + middlestring
        secondline += items[1] + ' ' + fullstring(items[2], maxlen(items)) + middlestring
        thirdline += '-'*(maxlength+2) + middlestring

        if Res:
            items.append(str(sumordif(items)))
            result += fullstring(items[3],maxlength+2) + middlestring
            arranged_problems = firstline +'\n'+ secondline +'\n'+ thirdline +'\n'+ result
        else:
            arranged_problems = firstline +'\n'+ secondline +'\n'+ thirdline
          
    return arranged_problems


# Find the max length of all items in a list
def maxlen(list):
    maxlen = -1
    for i in list:
        if len(i) > maxlen:
            maxlen = len(i)
    return maxlen

# Add necessary spaces at the beginning of a string  if its length is not equal to the predefined full length
def fullstring(x,fulllen):
    if len(x) == fulllen:
        return x
    else:
        return ' '*(fulllen-len(x)) + x

# If the operator is plus then return the sum, if the operator is minus then return the difference
def sumordif (list):
    if list[1] == '+':
        return int(list[0]) + int(list[2])
    elif list[1] == '-':
        return int(list[0]) - int(list[2])