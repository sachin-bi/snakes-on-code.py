
# List 
# [expression for item in itearable if condition]

bigMenu = [ "biriyani", "rajma chawal", "sweet rajma potato"]

result2 = [ item for item in bigMenu if len(item) >10]
result = [ item for item in bigMenu if "rajma" in item ]

print(f"result2: {result2}")
print(f"result: {result}")