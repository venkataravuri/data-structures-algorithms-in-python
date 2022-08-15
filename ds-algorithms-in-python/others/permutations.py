# Use Python to get all combinations of a string with repetition
a_string = 'abc'
final_list = [[]]
length = len(a_string)
groups = [list(a_string)] * length
for i in groups:
    final_list = [x+[y] for x in final_list for y in i]
permutations = [''.join(item) for item in final_list]
print(permutations)