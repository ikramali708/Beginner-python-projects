# print("Hello Wrld!")


# print("This is a test.")

# a=5
# print(a)
# print(type(a))

# a="This is InventStarts"
# print(a)
# print(type(a))

# user_name = input("Enter your name: ")   # Snake case variable
# print("Hello, " + user_name + "! Welcome to the program.")


# userName=input("Enter your age:") #Camel case variable
# print("Your age is: " + userName)


# UserName = input("Enter your Gender:") #Pascal case variable
# print("Gender is: " + UserName)







# firstNumer=input("Enter first number:")
# second_number=input("Enter second number")

# if firstNumer>second_number:
#   print("First number is greater")


# else:
#   print("Second Number  is greater")




# print("Hi! Welcome to TechStar.")
# userName=input("What is your Good Name:")
# print("Happy to you see Here, Mr." + userName + "How can I help you Dear,"+userName)
# user_input=input("Press '1' to know about us! Press '2' for our services!")


# print(user_input)
# if user_input==1:{
#  print("Techstar is Pakistan Widely IT Company that provides custom solution to grow your business ideas")
# }

# if  user_input==2:
#     print("We Grow your Business through Web, App and custom software")


first_name="Ikram"
last_name="Ali"
full_name=first_name + " " + last_name

ha_3Times="Ha" * 3

print(full_name)

print(ha_3Times)

first_char_of_first_name=first_name[0]
print("First character of first name is: " + first_char_of_first_name)

firs_char_of_second_name=last_name[0]
print("First character of second name is: " + firs_char_of_second_name)

age=25
print(f"My age is:{age}")

# is_Python_Easy=False
# if is_Python_Easy:
#     print("Python is easy to learn")
 
# ...Lists...
empty_list=[]
numbers=[1,2,4,5,6,7,8,9,10]
mixed_list=["Ikram", 25, True, 3.14]


numbers.append(11)  # Adding an element to the list
numbers.pop()
numbers.remove(4)  # Removing an element from the list
numbers.insert(2, 30)  # Inserting an element at a specific index
print("Updated numbers list:", numbers)
random_number=numbers[-2]  # Accessing an element by index
print("Random number from the list:", random_number)
# ...Lists...


#tuple
empty_tuple=()
numbers_tuple=(1,2,3,4,5,6,7,8)
mixed_tuple=("Ikram", 25, True, 3.14)
print("Empty tuple:", empty_tuple)
print("Numbers tuple:", numbers_tuple)
print("Mixed tuple:", mixed_tuple)
# Accessing elements in a tuple
first_element = mixed_tuple[0]

print("First element of mixed tuple:", first_element)

#Dictionary

empty_dict={}
numbers_dict={"one": 1, "two": 2, "three": 3, "four": 4}
mixed_dict={"name": "Ikram", "age": 25, "is_student": True, "height": 3.14}
print("Empty dictionary:", empty_dict)
print("Numbers dictionary:", numbers_dict)
print("Mixed dictionary:", mixed_dict)

# Accessing elements in a dictionary
age_value = mixed_dict["age"]
print("Age from mixed dictionary:", age_value)

mixed_dict.pop("age")  # Removing an element from the dictionary
print("Updated mixed dictionary after removing age:", mixed_dict)

print(mixed_dict.items())


a=True; b=False

print("Equall", a and b)
print("Not Equall", a or b)
print("Not Equall", not a)


#For Loop

# numbers = [1, 2, 3, 4, 5]
# print("Numbers:")
# for num in numbers: 
#     print(num)


table=3
for i in range(1, 11):
        result = table * i
        print(f"{table} x {i} = {result}")

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


# Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")


# While Loop
# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1


# for i in range(1, 11):
#     if i == 5:
#         print("Skipping number 5")
#         continue  # Skip the rest of the loop for this iteration
#     print(i)


# table,count=4,1
# while count <= 10:
#     if count == 5:
#         print("Skipping count 5")
#         count += 1
#         continue
#     result = table * count
#     print(f"{table} x {count} = {result}")
#     count += 1


    #Print sum of numbers

num = 12345
count = 0
while num != 0:
    num //= 10 
    count += 1
print("Number of digits:", count)



#if Statement

number=input("Enter a number: ")
if int(number) > 0:
    print("The number is positive.")
elif int(number) < 0:
    print("The number is negative.")
else:
    print("The number is zero.")