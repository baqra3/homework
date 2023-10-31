my_age = int(input("Enter Your Age: "))
fathers_age = int(input("Enter Your Fathers Age:"))
year = int(input("Enter Year: "))

for i in range(30):
    print(str(year + i )+ " წელს მამაჩემი ჩემზე იქნება " + str((fathers_age + i) / ( my_age + i)) + "ჯერ დიდი")