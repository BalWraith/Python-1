import os
os.system("cls")
data = [104, 101, 4, 105, 308, 103, 5, 
        107, 100, 306, 106, 102, 108]
min_vlaid = 100
max_vlaid = 200
#                             #start,stop,step
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_vlaid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_vlaid or value > max_vlaid:
        print(top_index - index, value)
        del data[top_index - index]
print()
print(data)








print("\n"*1)