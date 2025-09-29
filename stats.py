def wc(string):
    return len(string.split())

def cc(string):
    # fist split the string into characters
    my_list = list(string.lower())

    # read characters into dictionary
    my_dict = {}
    for character in my_list:
        my_dict[character.lower()] = 0

    # count the characters in my_list and add to
    # the dictionary
    for character in my_list:
        if character in my_dict:
            my_dict[character] += 1
    
    # sort the dictionary by value
    sorted_dict = dict(sorted(my_dict.items()))

    return sorted_dict

def sort_on(items):
        return items["num"]

def sort_by_key_value(my_dict):
    for item in my_dict:
        my_list = []

        for item in my_dict:
            new_dict = {}
            new_dict["char"] = item
            new_dict["num"] = my_dict[item]
            my_list.append(new_dict)

    my_list.sort(reverse=True, key=sort_on)
    return my_list
