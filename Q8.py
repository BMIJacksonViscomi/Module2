#Creating a BMI function that takes a height(m) and weight(kg) arguements
def BMI(h,w):
    return round(w/(h**2),1) #CDC: BMI = Weight(kg)/Height(m)^2, rounded to the 10th decimal place

#Using susan to test out function
#Susan is 1.58 m tall
SusanHeight = 1.58 #assign to variable
#Susan weighs 60 kg
SusanWeight = 60  #assign to variable

BMI(SusanHeight,SusanWeight) #Passing variables through BMI function to return Susan's BMI