# Part 1: input your height, weight and age.
##################################################################
#bmr calculator: 

# weight = int(input("Enter your weight in lbs: \n"))
# height = int(input("Enter your height in inches: \n"))
# age = int(input("Enter your age in years: \n"))
# isMale = str(input("Are you male? (y/n)"))

# if isMale == "y":
#     isMale = True
# elif isMale == "n":
#     isMale = False
# else:
#     print("Error")
#     quit()
    
    

# Harris-Benedict Imperial Equation for males
bmr():
# Harris-Benedict Equation
    if isMale:
        bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

    bmr = round(bmr)
    print(bmr)


####################################################################
# Part 2: How active are you?


# sedintary:
# bmr = bmr

# lightly active(1-3 days of light exercise or sports)
# bmr * 1.375

# moderately active(moderate workout 3-5 days per week)
# bmr * 1.55

# Very active (hard exercise 6-7 days per week)
# bmr * 1.725

###################################################################
# part 3: Target
success = False
calories = 'placeholder'
protein_target = False
carbs_target = False
fat_target = False
calories_target = False

target = 'bulk'


# for bulking
if (target == 'bulk'):
	if (protein >= weight):
		protein_target = True
	else:
		print('select foods with more protein! {weight - protein} still needed!')
    if (calories >= bmr):
        target_calories = True
    else:
        print('EAT MOOOOOOOOORE! Still {calories_target - calories}')

# bulk success
    if (protein_target = True & target_calories = True)
        success = True

# for losing weight
elif (target == 'lose_weight'):
	if (calories <= target_calories):
		success = True
		print('within your limit! You have {target_calories - calories} extra available!')
	else:
		print('STOP EATING YOU\'RE OVER YOUR LIMIT')

# weight loss success
    if (target_calories = True)
        success = True

####################
#for success
if success = True
print('Daily goal reached!')
#accompany with visual effect

####################