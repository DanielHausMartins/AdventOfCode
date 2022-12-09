import sys
import re

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

pairs = open(sys.argv[1], "r").read().strip().split("\n")

pairs = [[[int(number) for number in elf.split("-")] for elf in pair.split(",")] for pair in pairs]

total = 0

#Part 1
for pair in pairs :
	if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1] :
		print("/!\ Elf {} is contained within Elf {}".format(pair[0], pair[1]))
		total += 1
	elif pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1] :
		print("/!\ Elf {} is contained within Elf {}".format(pair[1], pair[0]))
		total += 1
	else :
		print ("		Elves {} and {} are good".format(pair[0], pair[1]))

print(total)
print("Press any key for part 2")
toto = input()

total = 0

for pair in pairs :
	if pair[0][1] < pair[1][0] :
		print("Elf {} is before Elf {}".format(pair[0], pair[1]))
	elif pair[1][1] < pair[0][0] :
		print("Elf {} is before Elf {}".format(pair[1], pair[0]))
	else :
		total += 1
		print ("	/!\ Elves {} and {} Overlap".format(pair[0], pair[1]))

print(total)














