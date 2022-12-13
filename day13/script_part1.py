import sys, math, re, copy

if len(sys.argv) != 2:
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

with open(sys.argv[1]) as file:
	pairs = file.read().strip("\n").split("\n\n")
	
pairs = [["".join([char if ord(char) not in range(65, 91) and ord(char) not in range(97,123) else "" for char in element.strip()]) for element in pair.split("\n")] for pair in pairs]

pairs = [[eval(element) for element in pair] for pair in pairs]


def compare(left, right, tab) :
	print("  "*tab + f"- Compare {left} vs {right}")
	if isinstance(left, int) and isinstance(right, int) :
		if left == right :
			return None
		return left < right
	if isinstance(left, int) :
		left = [left]
	if isinstance(right, int) :
		right = [right]
	for i in range(min(len(left),len(right))) :
		res_compare = compare(left[i], right[i], tab+1)
		if res_compare != None :
			return res_compare
	if len(left) == len(right) :
		return None
	return len(left) < len(right)

s = 0

for i in range(len(pairs)) :
	res = compare(pairs[i][0], pairs[i][1], 0)	
	if res :
		s += i+1
	print(f"Result : {res}\n\n")

print(f"Total sum : {s}")

