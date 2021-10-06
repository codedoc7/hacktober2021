def fibonacii(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        i = fibonacii(n-1)
        i.append(sum(i[:-3:-1]))
        return i
        
i=fibonacii(10)

print(i)
