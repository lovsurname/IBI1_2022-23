rabbits_number = 2
rabbits_generation = 1
water_bottle = 100
while rabbits_number < 100:
    rabbits_number = rabbits_number*2
    rabbits_generation += 1
    print(str(rabbits_generation)+" "+str(rabbits_number))
print(str(rabbits_generation)+" is the number of generations required to exceed 100 rabbits")


