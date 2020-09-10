import booste
from sys import argv

string = " ".join(argv[2:])

print(booste.gpt2(string, argv[1]))
