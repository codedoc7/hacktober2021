def reverse_string(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1
str = "potato"
print("default string is: ", str)
print("reversed string is", reverse_string(str))
