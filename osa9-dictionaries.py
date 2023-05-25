counts = dict()

names = ["kasi","pasi", "kasi", "Jussi", "Jussi", "Marjatta"]
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)

jjj = { "pekka" : 1, "ananas": 2, "Jussi": 100}

for aaa, bbb in jjj.items() :
    print(aaa, bbb)

c = {'a': 10, 'b':1, 'c':22}

print(sorted([(v,k) for k,v in c.items()]))



import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)