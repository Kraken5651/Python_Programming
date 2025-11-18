m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

# Check for total percentage.
total_percentage = ((100)*(m1 + m2 + m3))/300


if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You have Passed the Test! : ", total_percentage)
else:
   print("You have Failed! : ", total_percentage)