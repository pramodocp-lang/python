name = input("Enter Name of the students:")

sub1 = int(input("Enter the mark of Sub-1:"))
sub2 = int(input("Enter the mark of Sub-2:"))
sub3 = int(input("Enter the mark of Sub-3:"))


total = sub1 + sub2 +sub3

avg = round(total / 3, 2)

print("\nStudent Name :",  name)
print("\nTotal Marks  :",  total)
print("\nAverage      :",  avg)

if avg >= 85:
    print("PASS With Grade A")
elif avg >= 75:
    print("PASS With Grade B")
elif avg >= 60:
    print("PASS With Grade C")
elif avg >= 40:
    print("PASS With Grade D")
else: 
    print("FAIL")