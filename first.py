x='Hello world '
y=str(75)
print(x+y)
print(x+x)
print(len(x))
print(x[0:5])

# Print Marksheet
sub1=int(input("Enter english sub 1:"))

sub2=int(input("Enter english sub 2:"))

sub3=int(input("Enter english sub 3:"))

total_marks= sub1+sub2+sub3

print("Total marks is "+str(total_marks))

percentage=total_marks*100/300

if percentage>90:
 grade='A-one'
elif percentage>80:
 grade='A'
elif percentage>70:
 grade='B'
else:
 grade='F'
# Print Table of 2
table=int(input("Enter Table"))
for x in range(1,11):
 ans=table*x    
 print(ans)  
 
