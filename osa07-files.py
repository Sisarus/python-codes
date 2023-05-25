fname = input('file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be openend: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
            count = count + 1

print('There were ', count, ' cubject lines in ' , fname)