#Клиент покупает кофе в кафе.
#За каждые 6 чашек, 1 чашка даётся в качестве бонуса.

#Задача: запросить у пользователя кол-во чашек на покупку,
#вычислить полагающееся кол-во бонусных чашек кофе и вывести это число на консоль.

customer_cups = int(input("To order, please indicate the number of coffee servings "))
bonus_cups = customer_cups // 6
full_order = bonus_cups + customer_cups
print(f"Also you got {bonus_cups} bonus cups of coffee")
print(f"Your order is {full_order} cups of coffee")

