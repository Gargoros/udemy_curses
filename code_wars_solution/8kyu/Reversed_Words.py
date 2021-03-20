# Complete the solution so that it reverses all of the words within the string passed in.

# Example:

# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"

def reverse_words(s):
    n_s = (s.split(" "))[::-1]
    return " ".join(n_s)
    
