# # Code about  Neutralisation
# for i in range(1, 10):

#   if "+".join("-"):
#     print("0", end="")
# print()
# for i in range(1, 10):
#    if "+".join("+"):
#     print("+", end="")
# print()
# for i in range(1, 10):
#   if "-".join("-"):
#     print("-", end="")

def interact_strings(string1, string2):
    result = ""
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            result += string1[i]
        else:
            result += "0"
    return result

string1 = "+-++-"
string2 = "-++--"
result = interact_strings(string1, string2)
print(result)