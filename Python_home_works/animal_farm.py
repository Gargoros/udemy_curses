#На ферме есть куры, коровы и свиньи.
#У курицы две ноги, у свиньи - четыре, у коровы - четыре.
#Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров,
#просуммировать кол-во ног всех животных и вывести результат на консоль

print("We are counting animals on the farm ")
print("You have chickens, cows and pigs ")

chickens = int(input("indicate their number of chickens ")) * 2
cows     = int(input("indicate their number of cows ")) * 4
pigs     = int(input("indicate their number of pigs ")) * 4

animals_legs = chickens + cows + pigs
print(animals_legs)