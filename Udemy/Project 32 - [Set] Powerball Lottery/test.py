def fibonnaci(n):
  assert n >= 0 and int(n) == n, "fibonnaci number cannot negatif or decimal"
  if n in [0,1]:
    print(f"if condition = {n}")
    return n
  else:
    print(f"else {fibonnaci(n-1)} + {fibonnaci(n-2)} = {fibonnaci(n-1) + fibonnaci(n-2)}")
    return fibonnaci(n-1) + fibonnaci(n-2)
  
print(fibonnaci(6))