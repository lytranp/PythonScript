print("\tMultiplication Table")
print("  ", end = '')
for j in range(1, 10):
    print("  ", j, end = '')
print()  # jump to the new line
print("---------------------------------------")

for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        print(format(i * j, "4d"), end = '')
    print() #jump to the new line, meaning after finish j line (1->9), jump to new line for new i
