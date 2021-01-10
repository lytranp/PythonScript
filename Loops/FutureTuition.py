#Suppose tuition is $10,000 this year and increases 7% every year
#How many years will the tuition double ?

#Because we know that tuition double = 20,000, the condition can finish there

year = 0
tuition = 10000 

while tuition < 20000:
    year += 1
    tuition *= 1.07 

print("Tuition will be doubl in", year, 
        "years with total tuition is $", format(tuition, ".2f"))
