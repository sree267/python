def rec_fact(n):
    if n==1:return 1
    else: return(n*rec_fact(n-1))
n=int(input("enter a number:"))
if n>=1:
   print("Factorial of number:",rec_fact(n))
