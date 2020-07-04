n = int(input('Введіть чотирицифрове натуральне число:'))
a = n%10
b = n//10%10
c = n//100%10
d = n//1000
e = d * c * b * a
print('Добуток цифр цього числа:', e)

print('Число в реверсному порядку:', int(''.join(reversed(str(n)))))

list = [a, b, c, d]
print('Посортовані цифри:', sorted(list))


