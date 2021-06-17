
#------Task1------# 

# ��������� ��������
import re, math

# Input
str = input("\n ������ �������� �����: ")

# ³������� ����� �� ����
nums = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
nums = [int(i) for i in nums]

# �������� �������� ���������
print("\n ����� ��� �����:\n", str)
print("\n ����� � �����:\n", nums)

# ������� ����� � ����� ����� � ������ �� ��������
str, result = str.title(), ""
for word in str.split():	
      result += word[:-1] + word[-1].upper() + " "

# �������� ������� ����� � �����������
print("\n ������ ��� ����� ����� � ����� ��� ����� ���������� � ������������ ������� ������:")
print( " " + result[:-1])

max_num = max(nums)
print("\n ����������� �������� � �����:", max_num)

# ���������� ����� � �������� != nums.index(max_num) � ������ ����� �������
vals = []
for i in range(len(nums)):
    if i != nums.index(max_num):
        temp = math.pow(nums[i], 2)
        vals.insert(i, temp)
print(" ������ ����� ����������� � �������:\n", vals)