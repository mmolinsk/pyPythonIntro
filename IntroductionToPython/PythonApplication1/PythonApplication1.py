userStr = input("Enter a sentence and I will rewrite it, replacing all numbers with their spelled out word(s)\n") # get user's string to convert
userStr = userStr.split() # split the string at every space

def numbers_to_strings (x): # method that gets a number, and returns that number's string equal
           x = int(x)       # for numbers 0 - 20
           switcher = {
              0: "zero",
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty"
           }
           return switcher.get(x, "error") # return the string gotten from switcher based on x. If it's not found in switchwer, return "error"

def big_numbers_to_strings (x):  # method that gets a number, and returns that number's string equal for numbers 20-99
           y = x%10   # get the second number of the 2 digit number
           x = str(x) 
           x = int(x[0] + '0') # get the first digit of the 2 digit number
           switcher = {
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              20: "twenty ",
              30: "thirty ",
              40: "fourty ",
              50: "fifty ",
              60: "sixty ",
              70: "seventy ",
              80: "eighty ",
              90: "ninety "
           }
           return switcher.get(x, "") + switcher.get(y, "") # return the full number in words

for x in userStr:  # loop trhough the user's string list of words
    if x.isdigit():  # if that 'word' is an number
        num = userStr.index(x) # get the index of the number
        userStr.remove(x) # remove the number from the string' list
        x = int(x) # convert it to an int
        if x-10 < 11: # if number is between 0 and 20
            userStr.insert(num, numbers_to_strings(x)) # use corresponding method 
        else: # otherswise
            userStr.insert(num, big_numbers_to_strings(x))  # use corresponding method 

outStr = ""
for y in userStr: # loop back through the list of words
    outStr = outStr + y + " " # and turn it back into a string
print("Your new string: " + outStr) # print it

