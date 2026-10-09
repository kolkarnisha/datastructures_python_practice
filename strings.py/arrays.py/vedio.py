#exception handling/error handlig
''' for suppose'''
num=int(input("enter a number"))
print(100/num)
'''  1.division by zero
     2.wrong input type
     3.file not found
     4.database connection failure
     5.api failure'''
try:
    num=int(input("enter a number:"))
    print(100/num)
except:
    print("something went wrong check your input")
try:
    num=int(input("enter a number:"))
    print(100/num)
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("enter numbers only")
# else:
#     print("exectued sucessfully")
finally:
    print("program ended")
balance=5000
try:
    amount=int(input("enter amount:"))
    if amount>0:
        if amount>balance:
            raise Exception("insufficient balance available")
        balance-=amount
        print("withdraw sucess")
except Exception as e:
    print("enter numbers only")
    print(e)


