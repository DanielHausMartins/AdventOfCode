import sys, math, re, copy

if len(sys.argv) != 2:
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

magic_regex = r"""Monkey (?P<name>.*):\n  Starting items: (?P<items>.*)\n  Operation: new = (?P<operation>.*)\n  Test: divisible by (?P<test>\d+)\n    If true: throw to monkey (?P<true_monke>\d+)\n    +If false: throw to monkey (?P<false_monke>\d+)"""

class Monke:
	def __init__(self, name="", items=[], operation=[], test=None, true_monke=None, false_monke=None):
		self.name = name
		self.items = items
		self.operation = operation
		self.test = test
		self.true_monke = true_monke
		self.false_monke = false_monke
		self.items_inspected = 0

	def inspect(self):
		for item in copy.copy(self.items):
			self.items.remove(item)
			item = int(item % big_factor)
			item = self.get_item_worry(self.operation[0], item, self.operation[1:])
			if int(item % self.test) == 0:
				self.gib_to_monke(item, self.true_monke)
			else:
				self.gib_to_monke(item, self.false_monke)
			self.items_inspected += 1

	def gib_to_monke(self, item, destination_monke):
		for monke in monkes:
			if monke.name == destination_monke:
				monke.items.append(item)
	
	def get_item_worry(self, operation, item, args): 
		#return int(int(operation([int(arg) if arg != "old" else item for arg in args]))/3)
		return int(operation([int(arg) if arg != "old" else item for arg in args]))

	def print_monke(self) :
		print(f"Monke {self.name} : {self.items}")

def parse_monke(monke_string):
	res = re.search(magic_regex, monke_string.strip())
	operation = res.group("operation").split(" ")
	operation = [OPERATIONS[operation[1]], operation[0], operation[2]]	
	
	return Monke(name=res.group("name"), items=[int(item.strip()) for item in res.group("items").split(",")], operation=operation, test=int(res.group("test")), true_monke=res.group("true_monke"), false_monke=res.group("false_monke"))



with open(sys.argv[1]) as file:
	funky_monkys = file.read().strip("\n").split("\n\n")

OPERATIONS = {"*" : math.prod, "+" : sum}
monkes = []

# Parsing
for monke in funky_monkys:
	monkes.append(parse_monke(monke))

big_factor = 1

# First print
for monke in monkes:
		monke.print_monke()
		big_factor *= monke.test 

# Processing rounds
for r in range(10000):
	print(f"\n==========\n Round {r+1}\n==========\n")
	for monke in monkes:
		monke.inspect()
	for m in monkes :
		m.print_monke()
		print(f"\tMonke {m.name} inspected items {m.items_inspected} times.")
	

