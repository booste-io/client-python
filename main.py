import booste
from sys import argv

string = "hello, where is the golden"
out = booste.gpt2(api_key = "e24d28f3-5bd7-42ed-b00f-24540a8b40d6", in_string = string)

print("\n{}".format(string))
print(" ".join(out))


# window_size = 7

# sequence = [0,1,2,3,4,5]
# for i in range(100):
#     sequence.append(sequence[-1]+1)
#     if len(sequence) >= window_size:
#         end_index = len(sequence)+1
#         sequence = sequence[end_index-window_size:end_index]
#     print(sequence)
    
