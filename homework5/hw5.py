#1. The command to use is pwd
#2. The command to use is ls
#3. We need to navigate to brianna_repo, which we can do with cd ~/python_decal/brianna_repo. Then we can do git pull origin main.
#4. We can move homework.py to our personal directory with mv ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/
#5. You could use cat ~/python_decal/judy_decal/homework/homework.py
#6. You could use nano ~/python_decal/judy_decal/homework/homework.py  
#7. After navigating to the homework repository, you can do git add homework.py, git commit -m "a message", git push origin main.
#8. It seems like Judy tried to push without pulling the latest changes, so she can run git pull origin main and then git push origin main to try to fix the problem.
#9. You can use cd ~/Recents

def checkDataType(input):
    return str(type(input))[7:-1]

checkDataType(3.14)

def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(evenOrOdd(3))

def sumWithLoop(list):
    sum = 0
    for i in list:
        sum += i
    return sum

sumWithLoop([1,2,3,4,5])

def duplicateList(list):
    new_list = []
    for i in list:
        new_list.append(i)
        new_list.append(i)
    return new_list

duplicateList(["a","b","c"])

#The error is that there is a missing colon when defining the function, instead it should look like this:
def square(num):
    return num*num