import os
os.system("cls")
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#          170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#          170, 183, 185, 187, 188, 191]
# data = [ 104, 105, 110, 120, 130, 130, 150, 160,
#          170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150, 160,
#          170, 183, 185, 187, 188, 191]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
# #          170, 183, 185, 187, 188, 191]
# data = []
# min_valid = 100
# max_valid = 200

# # process the low values in the list
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
    
# print(stop)
# del data[:stop]
# print(data)

# # process the high values in the list
# start = 0
# for index in range(len(data) - 1,-1, -1):
#     # we have the index of the last item to keep.
#     # Set "start" to the position of the first
#     # item to delete, which is 1 after 'index'.
#     if data[index] <= max_valid:
#         start = index + 1
#         break
# print(start)
# del data[start + 1:]
# print(data)


print("\n"*3)