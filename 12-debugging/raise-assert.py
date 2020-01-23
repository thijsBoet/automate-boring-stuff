def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be string of length 1.')

    if (width < 2) or (height < 2):
        raise Exception('"Width" and "Height must be greater or equal to 2."')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)

# raises traceback 
# raise Exception('This is an exception')

import traceback

try: 
    raise Exception('This is an error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback was written to error_log.txt')

# assert => asserts a condition if false error msg is given

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)