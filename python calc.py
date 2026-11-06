import math
def getNumbers(): 
 while True:
  try:
   n1 = float(input("Enter first number :"))
   n2 = float(input("Enter second number :"))
   return n1,n2
  except ValueError:
     print("Invalid input. Enter valid number")

def calculate(n1,op,n2=None):
 if op=="+":
     return n1+n2
 elif op=="-":
     return n1-n2
 elif op=="*":
     return n1*n2
 elif op=="**":
     return n1**n2
 elif op=="sqrt":
     if n1 >= 0:
        return math.sqrt(n1)
     return "Cannot find sqrt of negative numbers"
 elif op=="/":
     if n2!=0:
         return n1/n2
     else:
         print("can't be divided by zero")
 else:
     print("invalid operator")


def showHistory(history):
   if not history:
      print("No calculations yet.")
   else:
      print("------CALCULATION HISTORY------")
      for item in history:
         print(item)

def main():
 history= []
 try:
    with open("history.txt","r") as file:
       history = file.read().splitlines()
 except FileNotFoundError:
    pass
       
 while True:
  print("\n1.Calculate")
  print("2.View History")
  print("3.Clear History")
  print("4.Exit")
  choice = input("Enter your choice (1 - 4):")
  if choice == "1":
   n1,n2 = getNumbers()
   op = input("Enter valid operator(*,+,-,/,**,sqrt):").lower()
   result = calculate(n1,op,n2)
   print("Answer:",result)
   if isinstance(result,(int,float)):
      history.append(f"{n1:g} {op} {n2:g} = {result:g}")
      with open("history.txt","a") as file:
         file.write(f"{n1:g} {op} {n2:g} = {result:g}"+"\n")
  elif choice =="2":
     showHistory(history)
  elif choice=="3":
     history.clear()
     with open("history.txt","w") as file:
        file.write("")
     print("History cleared")
  elif choice == "4":
     print("Exiting Calculator...")
     break
  else:
     print("Invalid choice.")
main()