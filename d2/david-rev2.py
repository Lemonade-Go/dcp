"""
d2 solution without using built in mul
"""

def solve(input_array):
    running_product = []
    reversed_product = []
    final = []
    tmp_product = 1

    for i in input_array:
        tmp_product *= i
        running_product.append(tmp_product)

    tmp_product = 1
    for i in reversed(input_array):
        tmp_product *= i
        reversed_product.append(tmp_product)

    reversed_product.reverse()

    print(running_product)
    print(reversed_product)

    for i in range(len(input_array)):
        print("i: "+str(i))
        my_product = 1
        
        if (i - 1) >= 0:
            print("i - 1 >= 0")
            my_product *= running_product[i - 1]
            print(running_product[i-1])

        if (i + 1) < len(input_array):
            print("i + 1 < len(input_array)")
            my_product *= reversed_product[i+1]
            print(reversed_product[i+1])
        
        print(my_product)
        final.append(my_product)
        print(final)

    print(final)

    return final

if __name__ == "__main__":
    input_array = [1,2,3,4,5]
    solve(input_array)
