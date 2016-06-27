# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def write_string_three_times(file_name, input_string):
    try:
        f = open(file_name, 'w')
        f.write(input_string * 3)
        f.close()
    except IOError:
        pass
