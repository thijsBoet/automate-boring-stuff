while True:
  print('Enter you age: ')
  age = input()
  try:
    age: int(age)
  except:
    print('please use numeric digits.')
    continue
  try:
    int(age) < 1
  except:
    print('Please enter a positive number.')
    continue
  break

print(f'Your age is {age}.')