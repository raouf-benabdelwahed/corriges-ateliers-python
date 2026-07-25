numbers = [number for number in range(1,101)]
print(numbers)
parite = ["pair" if s % 2 == 0 else "impair" for s in numbers]
print(parite)