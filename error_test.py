# Handle errors with try/except 
numbers = [1, 0, 2] 
for n in numbers: 
   try: 
    result = 10 / n 
    print(f"10 / {n} = {result}") 
   except ZeroDivisionError: 
    print(f"Error: Division by {n} failed")