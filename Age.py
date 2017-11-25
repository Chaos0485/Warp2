age = int(input("Укажите ваш возраст: "))

try:
    print(int(age) + 1)
except(ValueError):
    print("Ошибка ввода!")

if age < 6:
	print('Детский сад, штаны на лямках.')
elif age >= 6 and age < 18:
	print('Домашку сделал, мамкин циник?')
elif age >= 18 and age <= 24:
	print('Голодным студентам не подаем.')
elif age > 24 and age <= 60:
	print('Пора на смену, раб.')
elif age > 60:
	print('Пора подумать о завещании.')