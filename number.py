print("-"*100)
print("This is code for Kaprekar number, for Example: 20+25=45 and 45*45=2025")
print("-"*100)
print("\n")
print("Enter the range in which you want to find such numbers ")
a=int(input("Starting Number: "))
b=int(input("Ending Number: "))
if(a>=b):
    print("Please Enter range properly")
    exit()

else:
    for i in range(a,b):
        pow1=len(str(i*i))/2
        if pow1==0.5:
            pow1=1
        else:
            pow1=int(pow1)
        if (len(str(i*i))%2==0):
            num=int(((i*i)/pow(10,pow1)))
            whole=((i*i)%pow(10,pow1))
            sum=num+whole
            if sum==i:
                print(i)
        elif(i==1):
            print(i)
        else:
            pow1+=1
            num=int(((i*i)/pow(10,pow1)))
            whole=((i*i)%pow(10,pow1))
            sum=num+whole
            if sum==i:
                print(i)
