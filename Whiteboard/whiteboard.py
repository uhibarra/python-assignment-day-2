# Very simple, given an integer or a floating-point number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34

num = int(input("Give me a number: "))

opp_num = int(num * (-1))

print(str(num) + " : " + str(opp_num))