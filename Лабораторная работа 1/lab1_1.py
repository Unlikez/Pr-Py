numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_num = sum(numbers[:4]) + sum(numbers[5:])  # TODO заменить значение пропущенного элемента средним арифметическим
count_num = len(numbers)
average_num = sum_num / count_num
numbers[4] = average_num
print("Измененный список:", numbers)
