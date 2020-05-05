print("A program with a predefined Dictionary for a person with few information, and it displays the desired information requested by the user")

person = { "name" : "Shiladitya Bhattacharyya", "gender" : "Male", "age" : "26", "address" : "Bengaluru", "phone" : "9101699437" }

key = input("What Information you need ?  ").lower()

result = person.get(key, "The information is not avaliable in our database")

print(result)
