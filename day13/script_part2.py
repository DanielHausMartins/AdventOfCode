import sys, math, re, copy

if len(sys.argv) != 2:
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

with open(sys.argv[1]) as file:
	lines = file.read().strip("\n").replace("\n\n", "\n").split("\n")

lines = ["".join([char if ord(char) not in range(65, 91) and ord(char) not in range(97,123) else "" for char in line.strip()]) for line in lines]

# DANGEROUS
lines = [eval(line) for line in lines]

def compare(left, right, tab) :
	#print("  "*tab + f"- Compare {left} vs {right}")
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

tmp = None
ordered_check = True

lines.append([[2]])
lines.append([[6]])

iterations = 1

while True :
	for i in range(len(lines) - 1) :
		res = compare(lines[i], lines[i+1], 0)	
		if not res :
			#print(f"/!\ {lines[i]} and {lines[i+1]} not in order, inverting.")
			tmp = copy.deepcopy(lines[i])
			lines[i] = copy.deepcopy(lines[i+1])
			lines[i+1] = copy.deepcopy(tmp)
			ordered_check = False
		#print(f"{lines[i]} and {lines[i+1]} in order.")
	#print("\nTrying again\n")
	if int(iterations % 50) == 0 :
		print(f"Loop #{iterations}")
	iterations += 1
	if ordered_check :
		break
	ordered_check = True

res = 1
for i in range(len(lines)) :
	if lines[i] == [[2]] or lines[i] == [[6]]:
		res *= i+1

print("\n".join([str(line) for line in lines]))
print(f"Iterations : {iterations}")
print(f"Result : {res}")



