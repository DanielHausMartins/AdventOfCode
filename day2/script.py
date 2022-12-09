import sys

def round_score(opponent_move, my_move) :
	result = ord(my_move) - 23 - ord(opponent_move)
	if result in [-2, 1] : #win
		return ord(my_move) - 87 + 6
	elif result in [-1, 2] : #lose
		return ord(my_move) - 87
	elif result == 0 : #draw
		return ord(my_move) - 87 + 3
	else :
		raise Exception("Unknown result for round between {} and {} : {}".format(opponent_move, my_move, result))

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

f = open(sys.argv[1], "r")
total_score_part1, total_score_part2 = 0,0

#part2
cheat_table = {"A" : {"X":3,"Y":4,"Z":8},"B":{"X":1,"Y":5,"Z":9},"C":{"X":2,"Y":6,"Z":7}}

for line in f :
	if line.strip() :
		opponent,me = line.strip().split(" ")
		total_score_part1 += round_score(opponent, me) #part1
		total_score_part2 += cheat_table[opponent][me] #part2

print(f"Total score part 1 : {total_score_part1}\nTotal score part 1 : {total_score_part2}")





