def list_common_elements(list1, list2):
    list3 = []

    if not isinstance(list1, list):
        return "This first parameter must be a list"
    if not isinstance(list2, list):
        return "This second parameter must be a list"
    if len(list1) == 0:
        return "The fist list can not be empty"
    if len(list2) == 0:
        return "The second list can not be empty"
    for item in list1:
        if item in list2 and item not in list3:
            list3.append(item)
    if len(list3) == 0:
        return "There are no common elements in both lists"
    return list3
