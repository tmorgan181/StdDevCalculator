#Trenton Morgan 2020
#StdDevCalculator.py

#Simple program to calculate the standard deviation of a given population using
#the equation stdDev = sqrt(sum((x - mean)^2) / n) for all x in the population

#Import math module
import math

#Get population size
print("Welcome to the standard deviation calculator!")
popSize = int(input("Please enter the population size: "))
print("Population size is", popSize, "\n")

#Get value inputs
valueList = []
for i in range(popSize):
    value = float(input("Please enter value: "))
    valueList.append(value)
print()

#Calculate mean
print("Calculating mean...")
totalSum = 0
for i in valueList:
    totalSum += i
mean = totalSum / popSize
print("The population mean is", mean, "\n")

#Calculate standard deviation
print("Calculating standard deviation...")
squareSum = 0
for i in valueList:
    diff = i - mean
    square = pow(diff, 2)
    squareSum += square
stdDev = math.sqrt(squareSum / popSize)
print("The standard deviation is", stdDev)
