from lib2to3.pytree import convert


def convert_add(list1):
    list2 = [int(x) for x in list1]
    result = 0
    for i in list2:
        result+=i

    return f'''The final list is {list2}
After summing up the list - {list2} we get {result}'''
    

print(convert_add(['1', '3', '5']))