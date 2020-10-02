n = int(input('Enter no. here:'))
prime='t'  
for i in range (2,n):
    if n% i == 0:
        prime = 'fail'
        break
  
if prime=='fail':
    print(n,'is not prime')
else:
    print(n,'is prime')
