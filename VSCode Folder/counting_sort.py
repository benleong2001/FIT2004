import math

def counting_sort(lst):
    """ Counting Sort for integers
    :Input:
        lst:
    :Output, return or postcondition:
    :Time Complexity:
    :Aux Space Complexity:
    :Pre Condition: Input list is not empty
    """
    # Checking pre-condition
    if not lst:
        raise Exception("Empty list does not need sort")

    # Find max = M
    max_elem = lst[0]
    for item in lst[1:]:
        if item > max_elem:
            max_elem = item

    # create a list of M+1 length (0, 1, 2, ... M)
    freq_lst = [0] * (max_elem + 1)

    # count the freq of each elem of the original list
    for item in lst:
        freq_lst[item] += 1

    # create a new list using the frequency
    ind = 0
    for i, freq in enumerate(freq_lst):
        for _ in range(freq):
            lst[ind] = i
            ind += 1

    return lst


def counting_sort_stable(lst):
    if not lst:
        return lst
    # find max = M
    max_elem = lst[0]
    for item in lst[1:]:
        if item > max_elem:
            max_elem = item

    # create a list of M+1 length (0, 1, 2, ... M)
    # for stability, we need list of lists,
    # where the inner lists will contain the elements instead of counting freq
    nested_lst = [None] * (max_elem + 1)
    for i in range(len(nested_lst)):
        nested_lst[i] = []

    # containing the elements of lst in nested_lst[element]
    for item in lst:
        nested_lst[item].append(item)

    # create a new list using nested_lst
    ind = 0
    for i, nested in enumerate(nested_lst):
        for elem in nested:
            lst[ind] = elem
            ind += 1

    return lst


def counting_sort_lower_alpha(lst):
    if not lst:
        return lst
    # find max = M
    max_elem = lst[0]
    for item in lst[1:]:
        if item > max_elem:
            max_elem = item

    # create a list of M+1 length (0, 1, 2, ... M)
    # for stability, we need list of lists,
    # where the inner lists will contain the elements instead of counting freq
    nested_lst = [None] * (ord(max_elem) - 96)
    for i in range(len(nested_lst)):
        nested_lst[i] = []

    # containing the elements of lst in nested_lst[element]
    for item in lst:
        nested_lst[ord(item) - 97].append(item)

    # create a new list using nested_lst
    ind = 0
    for i, nested in enumerate(nested_lst):
        for elem in nested:
            lst[ind] = elem
            ind += 1

    return lst


# For Assignment 1
def counting_sort_score(results):
    """ Counting Sort for score in results
    :Input:
        lst:
    :Output, return or postcondition:
    :Time Complexity:
    :Aux Space Complexity:
    :Pre Condition: Input list is not empty
    """
    # Checking pre-condition
    if not results:
        raise Exception("Empty list does not need sorting")

    # Find max integer in input list
    max_score = results[0][2]
    for result in results[1:]:
        score = result[2]
        if score > max_score:
            max_score = score

    # Create a list of max_score + 1 length (0, 1, 2, ... M)
    nested_lst = [None] * (max_score + 1)
    for i in range(len(nested_lst)):
        nested_lst[i] = []

    # Store the results in their respective buckets in nested_lst according to their scores
    for result in results:
        nested_lst[max_score - result[2]].append(result)

    # Override the results values with the results from nested_lst
    ind = 0
    for i in range(len(nested_lst)):
        for result in nested_lst[i]:
            results[ind] = result
            ind += 1


def counting_sort_team(team):
    """
    :Input:
        team: A list of gacha characters in a team
                e.g., ['B', 'A', 'C']
    :Post condition: The list sorted
    """
    max_value = ord(team[0])
    for i in range(1, len(team)):
        value = ord(team[i])
        if value > max_value:
            max_value = value
    
    nested_list = [None] * (ord(max_value) - 64)
    for i in range(len(nested_list)):
        nested_list[i] = []

    for charac in team:
        nested_list[ord(charac) - 65].append(charac)

    ind = 0
    for i in range(len(nested_list)):
        for charac in nested_list[i]:
            team[ind] = charac
            ind += 1

    return team

