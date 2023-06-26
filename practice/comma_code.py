'''Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.'''

fruits = ["Apple","Orange","Banana","Peach","Grapes"]

def list_to_str(list):
    last_val = list[-1]
    list.remove(last_val)
    list.append('and '+ last_val)
    str = ", ".join(list)
    print(str)

list_to_str(fruits)