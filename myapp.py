# a = int(input("Enter the first number "))
# b = int(input("Enter the second number "))

# result = a+b

# print(result)


user_name = input("Enter the name to store in file : ")
if user_name :
    with open('user_info.txt','a') as file:
        file.write(user_name+"\n")

show_info = input("Do you want to see all user names? y/n : ")
if show_info =='y':
    try:
        with open("user_info.txt",'r') as file:
            content = file.readlines()
    except Exception as e:
        print(e, type(e))
    else:
        for line in content:
            print(f'{line.rstrip()}')