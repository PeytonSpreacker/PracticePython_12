a = [5, 10, 15, 20, 25]

ends = list()

def list_ends():
    if len(a) == 0:
        print('No list available.')
    else:
        ends.append(a[0])
        ends.append(a[-1])
    print(ends)
    
list_ends()