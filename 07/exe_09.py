fname = input("Enter file: ")

if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

print(di)

x = sorted(di.items())
print(x)

tmp = list()
for k,v in di.items():
    print(k,v)
    newr = (v,k)
    tmp.append(newr)

print("Flipped ", tmp)

tmp = sorted(tmp, reverse=True)
print("Shorted ", tmp)

for v, k in tmp[:5]: #print first 5
    print(k,v)


 