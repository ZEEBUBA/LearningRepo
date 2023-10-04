#GRADING APP

while(True):
    grade=int(input('Enter your score : '))
    if(grade>74):
        print('Your grade is A')
    elif((grade>64)or(grade==74)):
        print('Your grade is B')
    elif((grade>59)or(grade==64)):
        print('Your grade is C')
    elif((grade>49)or(grade==59)):
        print('Your grade is D')
    elif((grade>39)or(grade==49)):
        print('Your grade is E')
    elif(grade<=39):
        print('Your grade is F')
    else:
        print('INVALID INPUT')
   
#DAYS OF THE WEEK

    while (True):
        day=int(input('Enter a day '))
        if day==1:
            print('Today is Sunday')
        elif day==2:
            print('Today is Monday')
        elif day==3:
            print('Today is Tuesday')
        elif day==4:
            print('Today is Wednesday')
        elif day==5:
            print('Today is Thursday')
        elif day==6:
            print('Today is Friday')
        elif day==7:
            print('Today is Saturday')
        else:
            print('Invalid Input')
