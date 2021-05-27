amt=int(input('enter amount'))
if(amt in range(1000,2000)):
    print('Discount is 10%')
    discount=amt*10/100
    bill_amt=amt-discount
elif(amt in range(2000,3000)):
    print('Discount is 20%')
    discount=amt*20/100
    bill_amt=amt-discount
elif(amt in range(3000,5000)):
    print('Discount is 30%')
    discount=amt*30/100
    bill_amt=amt-discount
elif(amt>=5000):
    print('Discount is 40%')
    discount=amt*40/100
    bill_amt=amt-discount  
else:
    print('Your Expenses are less than 1000 , there is no discount')
    bill_amt=amt
print (bill_amt)
