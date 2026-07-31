# def palindrome(string):
#     end = len(string) -1
#     start = 0
#     while(start < end):
#         if string[start] != string[end]:
#             return False
#         else :
#             start+=1
#             end-=1
#     return True
# print(palindrome("naman"))

string = "namam"
reverse = string[::-1]
if string == reverse:
    print("True")
else :
    print("False")