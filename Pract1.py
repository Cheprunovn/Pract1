#1.FizzBuzz
#��������� ����� �� 1 �� 100
#���� ����� ������� �� 3 - ������� ������ ���� Fizz
#���� �� 5 - ������� ������ ���� Buzz
#���� � �� 3 � �� 5 - ������� ������ ���� FizzBuzz
def first():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


#2. ������������� 1� ������ �� ��������� 2��
#��� ������ a = [1, 4, 6] � ������  b = [11, 33, 22]
#���� ������������� ������ ������ �� ������� ������ ���������� ������ [1,6,4]
def second():
    a = [1, 4, 6]
    b = [11, 33, 22]
    print(sorted(a, key=lambda x: b[a.index(x)])) 


#3. ��� ������ �����.
#����� ������� ��� �����, ������� ����������� � ������ �� ����� ������
#(������� �����).
#Example
#["bella","label","roller"] -> ["e","l","l"] ["cool","lock","cook"] -> ["c","o"]
def third():
    words = ["cool","lock","cook"]
    a = set(words[0])
    for i in words[1:]:
        a = a.intersection(set(i))
        result = list(a)
    print(result)

#4.#���� ������� �����, ������������� �� � ����� �����.
def fourth(n):
    rim_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    a = None
    for i in n:
        if a and rim_numbers[i] > rim_numbers[a]:
            result += rim_numbers[i] - 2 * rim_numbers[a]
        else:
            result += rim_numbers[i]
            a = i
    return(result)


first()
second()
third()
print(fourth("XXVII"))