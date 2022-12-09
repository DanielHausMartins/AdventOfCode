import copy
import sys

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

moves = open(sys.argv[1], "r").read().strip("\n").strip().split("\n")

# For visualization purposes
def represent() :
    matrix = [["." for j in range(20)] for i in range(20)]
    for i in range(len(rope)) :
        matrix[rope[i][1]][rope[i][0]] = f"{i}"
    matrix.reverse()
    print("\n".join(["".join(line) for line in matrix]) + "\n\n========\n")

# Returns tail node's next position from head node position
def node_next_move(head_node, tail_node) :
    for (i,j) in [(1,0),(0,1)] :
        if abs(head_node[i] - tail_node[i]) >= 2 :
            tail_node[i] += int((head_node[i] - tail_node[i])/abs(head_node[i] - tail_node[i]))
            if head_node[j] != tail_node[j] :
                tail_node[j] += int((head_node[j] - tail_node[j])/abs(head_node[j] - tail_node[j]))
    
    return tail_node

# Returns node position after move
def move(direction,node) :
    offset = DIRECTION_MAPPING[direction]
    return [node[0] + offset[0], node[1] + offset[1]]

# Static variables
ROPE_LENGTH = 10
DIRECTION_MAPPING = {
    "U" : (0, 1),
    "D" : (0, -1),
    "R" : (1, 0),
    "L" : (-1, 0)
}

# Dynamic variables
rope = [[0,0] for i in range(ROPE_LENGTH)]
past_tail_positions = []

for line in moves :
    direction, distance = line.split(" ")
    for step in range(int(distance)) :
        rope[0] = move(direction, rope[0])
        for i in range(len(rope)-1) :
            rope[i+1] = node_next_move(rope[i], rope[i+1])
        if rope[-1] not in past_tail_positions :
            past_tail_positions.append(copy.copy(rope[-1]))
    #represent()
print(len(past_tail_positions))


