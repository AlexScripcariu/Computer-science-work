import random
countries = []

for i in range(5):
    country = input("Please enter a country: ")
    countries.append(country)


print(random.choice(countries))
