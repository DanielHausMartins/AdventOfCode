
def total_calories(elf) :
	total = 0
	for food in elf :
		total += int(food)
	return total

f = open("input.txt", "r")
raw_data = f.read().strip()

elves = [[int(food) for food in elf.split("\n")] for elf in raw_data.split("\n\n")]
elves_calories = {}

for i in range(len(elves)) :
	elves_calories[i+1] = total_calories(elves[i])

sorted_elves = dict(sorted(elves_calories.items(), key=lambda item: item[1], reverse=True))

for elf in list(sorted_elves.keys())[:3] :
	print("Elf #{} : {} calories".format(elf, sorted_elves[elf]))
	
	
