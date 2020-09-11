import booste
from sys import argv

string = " ".join(argv[2:])

out = booste.gpt2(in_string = string, length = argv[1])

print("\n",string)
print(" ".join(out))