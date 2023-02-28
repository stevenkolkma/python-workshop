# # print(2*21)
# # bowl = 0
# # print(bowl)
# # bowl += 1
# # print(bowl)

# # 1.3 Files and Variables

# length = 3
# height = 9
# area = length * height

# # print(area)

# # title = "King"
# name = "Arthur"
# last_name = "Pendragon"

# # print(len(name))

# # full_name = title + " " + name + " " + last_name
# # print(len(full_name))
# # print("Hello, " + full_name)

# # 1.2 Compound Datatypes

# user_1 = 'Graham'
# user_2 = "John"
# user_3 = 'Terry'

# # print("The total length of our users' name: ", len(user_1) + len(user_2) + len(user_3))
# # Creating a list
# users = ["Graham", "John", "Terry", "Eric"]
# numbers = [2, 3, 5, 7, 11, 13]
# booleans = [True, False, False]
# lists = [[1, 2], [42, 66], []]
# # print(users[1:3])
# # print(users[1:4])
# # print(users[:3])
# # print(users[2:])
# user_data = {"Graham": 1941, "John": 1939, "Terry": 1940, "Eric": 1943}
# print(user_data["Graham"])

# lists_of_objects = [{"name": "Frank", "age": 20}, {"name": "Steven", "age": 27}]
# print(lists_of_objects)

# # Conditionals and Loops
# raining = True
# if (raining):
#     print("Bring an umbrella")
# else:
#     print("It's not raining! Go outside!")

# # to_check = 13
# # if to_check > 10:
# #     print(to_check + " is greater than 10")
# # else:
# #     print(to_check + " is not greater than 10")

# user_data = {"Graham": 1941, "John": 1939, "Terry": 1940, "Eric": 1943}

# for thing in user_data:
#     print(thing)
#     print(user_data[thing])

def even_below(number: int):
    return [x for x in range(number) if x % 2 == 0]

even_below(10)