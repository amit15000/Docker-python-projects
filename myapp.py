# a = int(input("Enter the first number "))
# b = int(input("Enter the second number "))

# result = a+b

# print(result)

print("Names of the Servers available")
try:
    with open("servers.txt",'r') as file:
            content = file.readlines()
except Exception as e:
        print(e, type(e))
else:
    for line in content:
        print(f'{line.rstrip()}')