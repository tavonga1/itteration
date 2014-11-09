#tavonga Mudzana
#22/10/14
#itteration_class_ex_rev 4
freq=int(input("please enter how many number you wnat to average: "))
count=0
total=0

for count in range (freq):
    number=int(input("please enter the number: "))
    total=total+number
    count=count+1
    average=total/count
print(average)    
  
