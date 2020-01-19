from typing import List

check_list: List[int] = [1, 2, 3]
people = {"pramod": check_list, "shyam": 32}

print(people["pramod"])

number = {1: "pramod", 2: "hamen", 3: "shyam"}

print(number[1])
print(4 in number)


print(number.get(1,"this is not their "))