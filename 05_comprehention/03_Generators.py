
# Dictionary
# generator - streams and save memory

totalSales = [ 4,4,5,6,1,45,12,4,23,6]

result = sum(item for item in totalSales if item>=5 )

print(f"result: {result}")