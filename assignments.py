#A test to check input of string knowledge 
#name = input("Enter programmer's name:")
#print('Hello and welcome genius:', name)
#print("My name is Ayo et i'm learning Python")

#A little calculator
#hours = input('Enter hours:')
#rate = input('Enter rate:')
#Pay = float(hours) * float(rate)
#print('Pay:', Pay)

#Pay calculator with conditional statements
#string_hours = input('Enter hours:')
#string_rate = input('Enter rate:')
#hours = float(string_hours)
#rate = float(string_rate)
        #print(hours, rate)
#if hours > 40 :
        #print('Overtime')
    #regular = hours * rate
    #overtime = (hours - 40.0) * (rate * 0.5)
    #pay = regular + overtime
        #print('Overtime:', overtime)
#else:
        #print('Regular')
    #pay = hours * rate
#print('Pay:', pay)

#Using try and except statements
string_score = input('Enter Score:')
try:
    score = float(string_score)
except:
    print('Please type a number')
    quit()
if score > 1.0 :
    print('This number is out of range, please enter a number within the range of 0.0 to 1.0')
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else:
    print('F')
    