def buy_house(value, salary):
    if value <= salary * 5:
        print("Congratulations, you can buy the house!")
    else:
        print("Sorry, you cannot afford this house.")


house_value = 180000
buyer_salary = 35000
buy_house(house_value,buyer_salary)
