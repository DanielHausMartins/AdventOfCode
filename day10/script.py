import sys, copy, curses, time

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

with open(sys.argv[1]) as file :
	instructions = file.read().strip("\n").split("\n")

#part 1
def sig_str() :
	return (CLOCK+1) * REGISTER["X"]

def add_reg(args) :
	REGISTER["X"] += int(args[0])

def noop(args) :
	pass

def process_cycle() :
	global CLOCK, TOTAL_SIG_STR
	CRT_move_sprite()
	if CLOCK+1 in CHECK_CYCLES :
		TOTAL_SIG_STR += sig_str()
	CRT_print_pixel()
	CRT_display()
	time.sleep(0.02)
	CLOCK += 1

def read_instruction(instruction) :
	global CLOCK, TOTAL_SIG_STR
	instruction = instruction.split(" ")
	instruction = [instruction[i] if i <= len(instruction)-1 else None for i in range(3)]
	for cycle in range(INSTRUCTION_CATALOG[instruction[0]]["cycle_length"]) :
		process_cycle()	
	INSTRUCTION_CATALOG[instruction[0]]["function"](instruction[1:])


# part 2
def CRT_print_pixel() :
	global CRT
	if int(CLOCK%CRT_WIDTH) in SPRITE :
		CRT[int(CLOCK/CRT_WIDTH)][int(CLOCK%CRT_WIDTH)] = "█"

def CRT_reset() :
	global CRT
	CRT = [[" " for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]

def CRT_move_sprite() :
	global SPRITE
	position = min(max(REGISTER["X"], 0), 39)
	SPRITE = [max(position-1,0), position, min(position+1,39)]

def CRT_display() : 
	display = copy.deepcopy(CRT)
	# Sprite display for fun
	for x in SPRITE :
		if display[int(CLOCK/CRT_WIDTH)][x] == " " :
			display[int(CLOCK/CRT_WIDTH)][x] = "_"
	# Cursor display for fun
	if display[int(CLOCK/CRT_WIDTH)][CLOCK%CRT_WIDTH] != "█" :
		display[int(CLOCK/CRT_WIDTH)][CLOCK%CRT_WIDTH] = "|"
	printable = f"Clock : {CLOCK}\n" + "="*(CRT_WIDTH+4) + "\n" + "\n".join(["||" + "".join(line) + "||" for line in display]) + "\n" + "="*(CRT_WIDTH+4)
	mywindow.addstr(0,0, printable)
	mywindow.refresh()


REGISTER = {"X" : 1}
CRT_WIDTH, CRT_HEIGHT = 40,6
CRT = None
SPRITE = [0,1,2]
CLOCK = 0
CHECK_CYCLES = [20, 60, 100, 140, 180, 220]
TOTAL_SIG_STR = 0

INSTRUCTION_CATALOG = {
	"addx" : {"cycle_length" : 2, "function" : add_reg},
	"noop" : {"cycle_length" : 1, "function" : noop}
}

# Main
CRT_reset()
mywindow = curses.initscr()

for instruction in instructions :
	read_instruction(instruction)

while CLOCK < CRT_HEIGHT * CRT_WIDTH :
	process_cycle()

mywindow.addstr(10,0, f"Total signal strength : {TOTAL_SIG_STR}. Press any key to end program.")
mywindow.getch()
curses.endwin()

