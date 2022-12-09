import sys
import re

def init_crates(crates) :
	res = {}
	lines = crates.split("\n")
	for i in lines[-1].strip().split("   ") :
		res[i] = []
	# Magical regex
	regex = "\s".join(["[\s\[]([\s\w])[\s\]]" for i in range(len(res))])
	for line in lines[:-1] :
		matches = re.match(regex, line).groups()
		for i in range(len(matches)) :
			if matches[i] != " " :
				res[str(i+1)] = [matches[i]] + res[str(i+1)]
	return res

def process_move_9000(crates, move) :
	amount,src,dst = re.match("move (\d{1,2}) from (\d) to (\d)", move).groups()
	for i in range(int(amount)) :
		if crates[src] :
			removed_crate = crates[src].pop()
			crates[dst].append(removed_crate)
	return crates

def process_move_9001(crates, move) :
	amount,src,dst = re.match("move (\d{1,2}) from (\d) to (\d)", move).groups()
	crates[dst] = crates[dst] + crates[src][-int(amount):]
	crates[src] = crates[src][:-int(amount)]
	
	return crates

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

contents = open(sys.argv[1], "r").read().strip("\n").split("\n\n")
crates = contents[0].strip("\n")
moves = contents[1].strip("\n").split("\n")

crate_stacks = init_crates(crates)

for move in moves :
	crate_stacks = process_move_9001(crate_stacks, move)
	
for stack in crate_stacks :
	print(crate_stacks[stack][-1], end="")

print("\n")

















