# Write a function, 
# gooseFilter / goose-filter / goose_filter / GooseFilter, 
# that takes an array of strings as an argument 
# and returns a filtered array containing the same elements 
# but with the 'geese' removed.

# The elements in the returned array should be in the same order
#  as in the initial array passed to your function, 
# albeit with the 'geese' removed. Note that all of the strings
#  will be in the same case as those provided, and some elements may be repeated.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]