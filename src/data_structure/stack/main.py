from stack import Stack


stack = Stack(10)

msg = input("Input String: ")
for char in msg:
    stack.push(char)

print(f"Output String: ", end="")
while not stack.is_empty():
    char = stack.pop()
    print(char, end="")

print("")
