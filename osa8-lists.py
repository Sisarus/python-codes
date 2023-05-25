numlist = list()
while True:
    inp = input('Enter number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Avarage: ' , average)
