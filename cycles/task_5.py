# Задание 5: Написать программу. Пользователь вводит два числа. Данные числа
# определяют числовой диапазон, для которого надо найти все числа, которые делятся
# нацело на 3, 5, 9 Например диапазон 1 - 20, количество чисел, которые делятся на 3 – 6, 5
# – 4, 9 - 2 Важно учесть, что пользователь может ввести числа в обратном порядке,
# например 37 и 16

start_num = int(input("Введите начальное число: "))
end_num = int(input("Введите конечное число: "))
divisors = [3, 5, 9]


def find_divisible_numbers(start, end, divisors):
    if start > end:
        start, end = end, start

    count_dict = {divisor: 0 for divisor in divisors}
    print(count_dict)

    for number in range(start, end + 1):
        for divisor in divisors:
            if number % divisor == 0:
                count_dict[divisor] += 1

    return count_dict


result = find_divisible_numbers(start_num, end_num, divisors)

for divisor, count in result.items():
    print(f"Количество чисел, делящихся на {divisor}: {count}")

