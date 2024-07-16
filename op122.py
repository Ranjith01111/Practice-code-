a = int(input('Enter your mark'))

if (avg <= 100 and avg > 90):
    print('Grade O')
elif (avg <= 90 and avg > 80):
    print('Grade A')
elif (avg <= 80 and avg > 70):
    print('Grade B')
elif (avg <= 70 and avg > 60):
    print('Grade C')
elif (avg <= 60 and avg > 50):
    print('Grade D')
else:
    print('Better luck next time')
