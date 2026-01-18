# Write file
with open("data.txt", "w") as file:
    file.write("Hello File")

with open("data1.txt", "w") as file:
    file.write("Hello File111")

# Read file
with open("data.txt", "r") as file:
    print(file.read())
