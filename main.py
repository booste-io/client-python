import booste
from sys import argv

string = "hello, where is the golden"
out = booste.gpt2(in_string = string, length = 35)

print("\n{}".format(string))
print(" ".join(out))
print(len(out))

# window_size = 7

# sequence = [0,1,2,3,4,5]
# for i in range(100):
#     sequence.append(sequence[-1]+1)
#     if len(sequence) >= window_size:
#         end_index = len(sequence)+1
#         sequence = sequence[end_index-window_size:end_index]
#     print(sequence)
    
