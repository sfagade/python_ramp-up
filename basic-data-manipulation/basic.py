def sort_capitalise(*args):
    new_list = [value.upper() for value in args]
    new_list.sort()
    return new_list


print(sort_capitalise("Something", "james", "jesus", "Something else"))
