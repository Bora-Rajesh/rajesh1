def getFact(number):
    if number ==0 or number ==1:
        return 1
    else:
        return number*getFact(number-1)
print(getFact(10))