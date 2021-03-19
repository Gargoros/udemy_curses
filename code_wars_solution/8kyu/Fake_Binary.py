# Given a string of digits, 
# you should replace any digit below 5 with '0' 
# and any digit 5 
# and above with '1'. 
# Return the resulting string.

def fake_bin(x):
    num = [1 if int(num) >= 5 else 0 for num in x]
    return "".join(map(str, num))