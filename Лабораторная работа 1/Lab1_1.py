numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
ind0 = numbers.index(None)
numbers[ind0] = (sum(numbers[:ind0])+sum(numbers[-1:ind0:-1]))/len(numbers)
print("Измененный список:", numbers)