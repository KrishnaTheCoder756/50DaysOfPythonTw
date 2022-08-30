def longest_value(d: dict):
    longest = d.values()
    l1 = []
    for l in d.values():
        l1.append(l)
    print(max(l1, key=len))
    

longest_value({'fruit':'apple', 'color':'greens'})