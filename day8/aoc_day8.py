# This isn't the most elegant code in the world. I was trying to get it quick, don't judge

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

treelines = open(sys.argv[1], "r").read().strip("\n").strip().split("\n")

trees = [[int(tree)for tree in line] for line in treelines]
height = len(trees)
width = len(trees[0])
visible = [[0 for j in range(width)] for i in range(height)]

# left to right
for i in range(height) :
    highest = -1
    for j in range(width) :
        if trees[i][j] > highest :
            visible[i][j] = 1
            highest = trees[i][j]
# right to left
for i in range(height) :
    highest = -1
    for j in reversed(range(width)) :
        if trees[i][j] > highest :
            visible[i][j] = 1
            highest = trees[i][j]
# up to down
for j in range(width) :
    highest = -1
    for i in range(height) :
        if trees[i][j] > highest :
            visible[i][j] = 1
            highest = trees[i][j]
# down to up
for j in range(width) :
    highest = -1
    for i in reversed(range(height)) :
        if trees[i][j] > highest :
            visible[i][j] = 1
            highest = trees[i][j]

count = 0
for line in visible :
    for value in line :
        if value :
            count += 1
print(sum([sum(line) for line in visible]))

# part 2
scenic_scores = [[1 for j in range(width)] for i in range(height)]

for i in range(height) :
    for j in range(width) :
        up_distance,down_distance,left_distance,right_distance = 0,0,0,0
        # look up
        if i :
            for k in reversed(range(i)) :
                up_distance += 1
                if trees[k][j] >= trees[i][j] :
                    break
        # look down
        if i != height-1 :
            for k in range(i+1, height) :
                down_distance += 1
                if trees[k][j] >= trees[i][j] :
                    break
        # look left
        if j :
            for l in reversed(range(j)) :
                left_distance += 1
                if trees[i][l] >= trees[i][j] :
                    break
        # look right
        if j != width-1 :
            for l in range(j+1, width) :
                right_distance += 1
                if trees[i][l] >= trees[i][j] :
                    break

        scenic_scores[i][j] = up_distance * down_distance * left_distance * right_distance

print(max([max(line) for line in scenic_scores]))





