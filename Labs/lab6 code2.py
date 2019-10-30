def product_evens(n):
    if n<2:
        return 1
    if n%2!=0:
        return (n-1)*product_evens(n-3)
    else:
        return n*product_evens(n-2)
print(product_evens(9))
