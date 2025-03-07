f = open("Ardit_Sulce_python/todos.txt", "a")
f.writelines(["see you soon!", "Over and out."])
f.close

f = open("Ardit_Sulce_python/todos.txt", "r")
print(f.read())