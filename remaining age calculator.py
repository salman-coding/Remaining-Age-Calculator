# Remaining Age Calculator
# Default Age is 90 Years :D

age = input("What is your current age?")

a = 1080   #months in 90 years
b = 4680   #weeks in 90 years
c = 32850  #days in 90 years

x= int(age)*12  #your age in months
y= int(age)*52  #your age in weeks
z= int(age)*365 #your age in days

remainingAge_months= a-x
remainingAge_weeks= b-y
remainingAge_days= c-z

print(f"you have {remainingAge_days} days,{remainingAge_weeks} weeks, and {remainingAge_months} left.")








