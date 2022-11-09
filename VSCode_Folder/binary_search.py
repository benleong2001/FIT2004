def binary_search(lst, score, low, high):
    """
    :Precondition: The input list is sorted
    Start in the middle
    Check if value is < or > than score

    """
    # print('low =', low)
    # print('high =', high)
    # print()

    searched_matches = []
    mid = (low + high) // 2
    key = lst[mid]

    # Score found
    if key[2] == score:
        searched_matches.append(key)
        init_mid = mid
        mid += 1
        while mid < len(lst) and lst[mid][2] == score:
            searched_matches.append(lst[mid])
            mid += 1
        mid = init_mid - 1
        while mid > 0 and lst[mid][2] == score:
            searched_matches.append(lst[mid])
            mid -= 1
        return searched_matches

    # Score does not exist
    elif low == high:
        while high < len(lst):
            new_score = lst[high][2]
            if new_score > score:
                score = new_score
                break
            high += 1

        while high < len(lst) and lst[high][2] == score:
            searched_matches.append(lst[high])
            high += 1
        return searched_matches

    # Score not yet found
    # Going right
    elif key[2] < score:
        low = mid + 1

    # Going left
    elif key[2] > score:
        high = mid - 1

    return binary_search(lst, score, low, high)


int_list = [0, 1, 1, 2, 4, 5, 6, 7, 7, 7, 9]
# int_list = [0] * 11
for i in range(len(int_list)):
    int_list[i] = [None, None, int_list[i]]

# for i in range(11):
#     print(binary_search(int_list, i, 0, len(int_list) - 1))    
# print(binary_search(int_list, 10, 0, len(int_list) - 1))    

def binary_search_iterative(lst, score):
    low, high = 0, len(lst) - 1
    searched_matches = []

    while low <= high:
        
        mid = (low + high) // 2
        key = lst[mid]

        # Score found
        if key[2] == score:
            searched_matches.append(key)
            init_mid = mid
            mid += 1
            while mid < len(lst) and lst[mid][2] == score:
                searched_matches.append(lst[mid])
                mid += 1
            mid = init_mid - 1
            while mid > 0 and lst[mid][2] == score:
                searched_matches.append(lst[mid])
                mid -= 1

            break
            

        # Score does not exist
        elif low == high:
            while high < len(lst):
                new_score = lst[high][2]
                if new_score > score:
                    score = new_score
                    break
                high += 1

            while high < len(lst) and lst[high][2] == score:
                searched_matches.append(lst[high])
                high += 1
            
            break

        # Score not yet found
        # Going right
        elif key[2] < score:
            low = mid + 1
            
        # Going left
        elif key[2] > score:
            high = mid - 1

    return searched_matches

for i in range(11):
    print(binary_search_iterative(int_list, i))  
