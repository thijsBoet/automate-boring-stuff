def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(div42by(2))
print(div42by(0))

# ---------------------------------------------------------------------------------------------------------------------

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That surely are many cats.')
    elif int(numCats) <= 0:
        print('You have no cats.')
    else:
        print('That is not many cats.')
except ValueError:
    print('You did not enter a number.')
