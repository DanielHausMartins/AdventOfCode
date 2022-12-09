import sys

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

# Part 1
print(sum([ord(l)-38 if l.isupper() else ord(l)-96 for l in [[i for i in r[:int(len(r)/2)] if i in r[int(len(r)/2):]][0] for r in open(sys.argv[1], "r").read().strip().split("\n")]]))

# Part 2
rs = open(sys.argv[1], "r").read().strip().split("\n")
print(sum([ord(l)-38 if l.isupper() else ord(l)-96 for l in [[i for i in g[0] if i in g[1] and i in g[2]][0] for g in [rs[i:i+3] for i in range(0,len(rs),3)]]]))

