
#------Task1------# 

# Імпортуємо бібліотеки
import re, math

# Input
str = input("\n Введіть довільний рядок: ")

# Відділяємо Числа від букв
nums = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
nums = [int(i) for i in nums]

# Виводимо проміжний результат
print("\n Рядок без чисел:\n", str)
print("\n Числа з рядка:\n", nums)

# Змінюємо перщі й остані букву у словах на заголовні
str, result = str.title(), ""
for word in str.split():	
      result += word[:-1] + word[-1].upper() + " "

# Виводимо змінений рядок й максимальне
print("\n Робимо щоб кожне слово в рядку без чисел починалось і закінчувалось великою літерою:")
print( " " + result[:-1])

max_num = max(nums)
print("\n Максимальне значення в масиві:", max_num)

# Переводимо числа з індексом != nums.index(max_num) у степінь згідно індексу
vals = []
for i in range(len(nums)):
    if i != nums.index(max_num):
        temp = math.pow(nums[i], 2)
        vals.insert(i, temp)
print(" Массив чисел поднесенных в степень:\n", vals)