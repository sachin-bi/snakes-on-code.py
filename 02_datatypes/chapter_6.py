line = "cows are good"
# last index is not inclusive.
# [start:end] [start:end:step]
print(f"first word: {line[0:4]}")  #op: cows
print(f"first word: {line[5:]}")   #op: are good
print(f"first word: {line[::-1]}") #op: doog era swoc

label_text = "chai speSH(ə)l"
encoded_label = label_text.encode("utf-8") 
decoded_label = encoded_label.decode("utf-8") 
print(f"label_text: {label_text}")
print(f"encoded_label: {encoded_label}")
print(f"decoded_label: {decoded_label}")