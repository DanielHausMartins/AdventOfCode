import sys

if len(sys.argv) != 2 :
	raise Exception("Wrong nb or arguments. Please only use input file name as argument.")

signal = open(sys.argv[1], "r").read().strip("\n")

print("Marker size : ", end="")
marker_size = int(input())

buf = signal[:marker_size]
cursor = marker_size

while cursor != len(signal) and len(set(buf)) != len(buf) :
	buf = buf[1:] + signal[cursor]
	cursor += 1

print(f"Found marker '{buf}' at position {cursor}\n\n\n")



def auto_regex_taha(n) :
	return "(\w)"+"(\w)".join(["(?!"+"|".join([f"\{j}" for j in range(1,i+1)])+")" for i in range(1,n)])


print(auto_regex_taha(4) + "\n\n")
print(auto_regex_taha(14) + "\n\n")
print(auto_regex_taha(32) + "\n\n")



























