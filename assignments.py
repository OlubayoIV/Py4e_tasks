#A test to check input of string knowledge 
name = input("Enter programmer's name:")
print('Hello and welcome genius:', name)
print("My name is Ayo et i'm learning Python")

#A little calculator
hours = input('Enter hours:')
rate = input('Enter rate:')
Pay = float(hours) * float(rate)
print('Pay:', Pay)

#Pay calculator with conditional statements
string_hours = input('Enter hours:')
string_rate = input('Enter rate:')
hours = float(string_hours)
rate = float(string_rate)
        ##print(hours, rate)
if hours > 40 :
        ##print('Overtime')
    regular = hours * rate
    overtime = (hours - 40.0) * (rate * 0.5)
    pay = regular + overtime
        ##print('Overtime:', overtime)
else:
        ##print('Regular')
    pay = hours * rate
print('Pay:', pay)

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

#loops and iteration assignment
largest = None
smallest = None
while True :
    try :
        str_val = input('Enter a number: ')
        if str_val == 'done' :
            break
        str_val = int(str_val)
        if largest == None or largest < str_val :
            largest = str_val
        elif smallest is None or smallest > str_val:
            smallest = str_val
    except :
        print('Please enter a numerical value')
        continue
   
print('Maximum is', largest)
print('Minimum is', smallest)

#find slice and convert
text = "X-DSPAM-Confidence:    0.8475"
trouve = text.find(" ")
#print(trouve)
fin = (text[trouve+4 : ])
print(fin)
enfin = float(fin)
print(enfin)

#finding files as always
fhand = input('Enter a file name: ')
#fname = open('mbox-short.txt')
try :
    fname = open(fhand)
except:
    print(fhand.upper()," to you too MF")
    quit()
count = 0
total = 0
for line in fname:
    if line.startswith('X-DSPAM-Confidence: ') :
        #sline = line
        #if line.startswith() :
            #line = line.rstrip()
        #count = count + 1
    #count = count + 1
        #print(line)
        sline = (line[20:100])
        sline = float(sline)
        count = count + 1
        total = total + sline
        #print(sline)
        #print(total)
        #print(count)
#print('There are ',count, 'inside this program')
print('With a average of: ', total/count)