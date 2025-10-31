


def is_armstrong_number(number):

    num_str = str(number)
    
    if not num_str.isdigit():
        return False
    
    len_str = len(num_str)
    
    return sum(int(x)**len_str for x in num_str) == int(number)

# A = []
# for i in range(1000000):
#     if is_armstrong_number(i):
#         A.append(i)

# print(A)
# print(len(A))