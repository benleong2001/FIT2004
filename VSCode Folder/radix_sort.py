import math
from re import L


def radix_sort(lst):
    """ Radix Sort using base 10
    :Input: 
        lst: List to be sorted
    :return: The sorted list
    """
    def counting_sort_col(lst, col, base=10):
        if not lst:
            return lst
        # find max = M
        max_elem = lst[0] // (base ** col) % base
        for item in lst[1:]:
            if (col_val := item // (base ** col) % base) > max_elem:
                max_elem = col_val

        # create a list of M+1 length (0, 1, 2, ... M)
        # for stability, we need list of lists,
        # where the inner lists will contain the elements instead of counting freq
        nested_lst = [None] * (max_elem + 1)
        for i in range(len(nested_lst)):
            nested_lst[i] = []

        # containing the elements of lst in nested_lst[element]
        for item in lst:
            nested_lst[int(item // (base ** col) % base)].append(item)

        # create a new list using nested_lst
        ind = 0
        for i, nested in enumerate(nested_lst):
            for elem in nested:
                lst[ind] = elem
                ind += 1

        return lst

    # Accounting for empty list
    if not lst:
        return lst

    # We need to loop through the list log M times
    # where M is the maximum item
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem

    # Finding the highest col number
    # To determine how many times to perform counting sort
    highest_column = int(math.log10(max_elem))
    for col in range(highest_column + 1):
        lst = counting_sort_col(lst, col)

    return lst


def radix_sort_string_opt(lst):
    """ Radix Sort for strings (optimised)
    :Input: 
        lst: List to be sorted
    :return: The sorted list

    Note: It is assumed that all strings are uppercase
    """

    def counting_sort_col(lst, col):
        if not lst:
            return lst

        # find max = M
        max_elem = None
        for item in lst:
            if len(item) < col + 1:
                continue
            elif not max_elem or item[col] > max_elem:
                max_elem = item[col]

        # create a list of M+1 length (0, 1, 2, ... M)
        # for stability, we need list of lists,
        # where the inner lists will contain the elements instead of counting freq
        nested_lst = [None] * (ord(max_elem) - 64)
        for i in range(len(nested_lst)):
            nested_lst[i] = []

        # containing the elements of lst in nested_lst[element]
        for item in lst:
            if len(item) < col + 1:
                nested_lst[0].append(item)
            else:
                nested_lst[ord(item[col]) - 65].append(item)

        # create a new list using nested_lst
        ind = 0
        for nested in nested_lst:
            for elem in nested:
                lst[ind] = elem
                ind += 1

        return lst

    # Accounting for empty list
    if not lst:
        return lst

    # Finding the longest string
    max_len = len(lst[0])
    for elem in lst:
        if len(elem) > max_len:
            max_len = len(elem)

    sort_by_len_lst = [None] * (max_len + 1)
    for i in range(max_len + 1):
        sort_by_len_lst[i] = []
    for s in lst:
        sort_by_len_lst[len(s)].append(s)

    ind = 0
    for i in range(max_len, -1, -1):
        for s in sort_by_len_lst[i]:
            lst[ind] = s
            ind += 1

    # Finding the highest col number
    # To determine how many times to perform counting sort
    for col in range(max_len - 1, -1, -1):
        lst = counting_sort_col(lst, col)

    return lst


def radix_sort_string(lst):
    """ Radix Sort using base 10
    :Input: 
        lst: List to be sorted
    :return: The sorted list
    """
    def counting_sort_col(lst, col):
        if not lst:
            return lst

        # find max = M
        max_elem = lst[0][-1-col]
        for item in lst[1:]:
            if item[-1-col] == ' ':
                continue
            elif item[-1-col] > max_elem:
                max_elem = item[-1-col]

        # create a list of M+1 length (0, 1, 2, ... M)
        # for stability, we need list of lists,
        # where the inner lists will contain the elements instead of counting freq
        nested_lst = [None] * (ord(max_elem) - 64)
        for i in range(len(nested_lst)):
            nested_lst[i] = []

        # containing the elements of lst in nested_lst[element]
        for item in lst:
            if item[-1-col] == ' ':
                nested_lst[0].append(item)
            else:
                nested_lst[ord(item[-1-col]) - 65].append(item)

        # create a new list using nested_lst
        ind = 0
        for nested in nested_lst:
            for elem in nested:
                lst[ind] = elem
                ind += 1

        return lst

    # Accounting for empty list
    if not lst:
        return lst

    # ADDED CODE
    # Hash table to store the original values
    # key          : value
    # item.lower() : item
    original_hash = {}
    for s in lst:
        original_hash[s.lower()] = s

    # Change all the strings to lower case for sorting
    lst = [s.lower() for s in lst]

    # Finding the longest string
    max_len = len(lst[0])
    for elem in lst:
        if len(elem) > max_len:
            max_len = len(elem)

    # Adjusting the remaining of the list
    for i, s in enumerate(lst):
        lst[i] = s + " " * (max_len - len(s))

    # Finding the highest col number
    # To determine how many times to perform counting sort
    for col in range(max_len):
        lst = counting_sort_col(lst, col)

    # Changed from
    # return [s.strip() for s in lst]
    return [original_hash[s.strip()] for s in lst]

x = ['AAA', 'ABA', 'CCC', 'CBC', 'CAC', 'BAC', 'AAB', 'ACB']
y = []
for bla in x:
    y.append(''.join(radix_sort_string_opt([l for l in bla])))
print(radix_sort_string_opt(y))


def radix_sort_opt(lst):
    """ Radix Sort for strings (optimised)
    :Input: 
        lst: List to be sorted
    :return: The sorted list
    :precondition: The list is not empty
    Note: It is assumed that all strings are uppercase
    """
    # sort strings by length
    # short to long? long to short?
    # perform counting sort
    # top to bottom? bottom to top?
    # definitely right to left column

    def counting_sort(lst, col):
        # For this counting sort function
        # I am going from bottom to top since my longest strings are at the bottom
        # I terminate loops once I reach a string without a letter at column col

        # Finding the max letter for column col
        max_letter = lst[len(lst) - 1][col]
        for i in range(len(lst) - 2, -1, -1):
            if len(lst[i]) - 1 < col:
                break
            elif lst[i][col] > max_letter:
                max_letter = lst[i][col]

        # Creating nested_lst with inner lists as buckets
        nested_lst = [None] * (ord(max_letter) - 64)
        for i in range(len(nested_lst)):
            nested_lst[i] = []

        # Storing strings in buckets
        ind = len(lst)
        for i in range(len(lst) - 1, -1, -1):
            if len(lst[i]) - 1 < col:
                break
            nested_lst[ord(lst[i][col]) - 65].append(lst[i])
            ind -= 1 
        
        # Putting back strings in original list
        # Need to iterate buckets backwards since we traversed bottom up
        for nested in nested_lst:
            for i in range(len(nested) - 1, -1, -1):
                lst[ind] = nested[i]
                ind += 1
        

    # Finding max length
    max_len = len(lst[0])
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    # Sorting the strings from short to long
    # Using counting sort
    len_lsts = [None] * (max_len + 1)
    for i in range(len(len_lsts)):
        len_lsts[i] = []
    
    for s in lst:
        len_lsts[len(s)].append(s)
    
    ind = 0
    for len_lst in len_lsts:
        for s in len_lst:
            lst[ind] = s
            ind += 1

    # Determining column value to call counting sort
    for col in range(max_len - 1, -1, -1):
        counting_sort(lst, col)
        
    return lst

lst = ['COCONUT', 'CCC', 'AB', 'AAA', 'BABA', 'BANANA',  'BBB']
print(radix_sort_opt(lst))