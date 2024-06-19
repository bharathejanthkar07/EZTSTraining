'''Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and will run until
 midnight (12 AM) i.e., for 4 hours. The contest comprises of N problems that are arranged in order of 
 difficulty, with problem 1 being the simplest and problem N being the most difficult. Max is aware that he will
 require 5*i minutes to solve the ith problem.

You will be give the Start time as T. Your task is to find and return an integer value, representing the number 
of problems Max can solve and reach the party venue within the given time frame of 4 hours.

Note: Max will leave his home at exactly 8 PM to reach the party venue'''
def party(time):
    count=0
    req=0
    i=0
    while 1:
        i+=1
        req+=i*5
        if req<=time:
            count+=1
        else:
            break
    return count
print("Time deadline: 8pm")
start=8*60
t=int(input("Enter the start time:"))
t=t*60
# nos=int(input("Enter the number of problems:"))
print("The number of possible questions can be solved are:",party(start-t))
