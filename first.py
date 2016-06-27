# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]
def second_elements(input_list):
    if type(input_list) is list:
        output = []
        for i in range(len(input_list)):
            if (i + 1) % 2 == 0:
                output.append(input_list[i])
        return output
    else:
        raise

print(second_elements([1, 2, 3, 4, 5]))
