# generating random numbers
import random
import string
print(random.random())  # random floating number b/w 0 and 1
print(random.randint(1, 10))  # b/w 1 and 10
print(random.choice([1, 2, 3, 4]))  # random choice
print(random.choices([1, 2, 3, 4, 5], k=2))  # random list of length 2
# generate pwd
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))
# we can also shuffl numbers using random
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
