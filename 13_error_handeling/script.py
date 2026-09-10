file = open("name.txt","w")

try:
    file.write("hello")
finally:
    file.close()
    

with open("hello.txt","w") as file:
    file.write("hh")
    

    