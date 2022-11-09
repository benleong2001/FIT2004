"""
The analyze function makes use of Counting Sort, Radix Sort
and Binary Search in order to output top10matches and searchedmatches:

    Counting Sort   - To sort the scores and the characters in a team.
    Radix Sort      - To sort team1 and team2.
    Binary Search   - To search for the matches where its score == input score
                    - Or the minimum score such that its score > input score

    For top10matches, the results list is sliced with index [:10].
    It takes everything before index 10.

- The counting sort functions were not modularised due to 
    minor differences scattered across each of the Counting Sort functions.
- The functions are arranged in order which they are called.

Name: Benjamin Leong Tjen Ho
Student ID: 32809824
Email: bleo0009@student.monash.edu
"""

# Functions for sorting results


def counting_sort_team(team_list: list[str], roster: int) -> list[str]:
    """
    In-place Counting Sort for the characters in a team.

    :Input:
        team_list:      A list of characters (uppercase letters).
        roster:         An integer stating the number of unique characters possible.

    :Post Condition:    The list of characters are sorted in ascending lexicographic order.

    :Return:            
        team_list:      The sorted version of team_list

    :Time Complexity:
        Best:           O(M) where M = len(team_list)
        Worst:          O(M) where M = len(team_list)

    :Space Complexity:
        Input:          O(M) where M = len(team_list)
        Aux:            O(1)
    """
    # Creating a count array
    count_array = [0] * roster

    # Counting the number of each characters in the team
    # Loop O(M) times
    for charac in team_list:
        count_array[ord(charac) - 65] += 1

    # Reassigning the characters in order
    # In total, loops O(M) times
    ind = 0
    for i in range(len(count_array)):
        for _ in range(count_array[i]):
            team_list[ind] = chr(i + 65)
            ind += 1

    # Returning the list of characters to be converted back into a string
    return team_list


def radix_sort_teams(results: list[list[str, str, int]], roster: int, team_index: int) -> None:
    """ 
    In-place Radix Sort for the Teams from results

    :Input: 
        results:            Input list to be sorted
        roster:             An integer stating the (number of) unique characters available
        team_index:         The index of the team being sorted

    :Post Condition:        The input list will be sorted

    :Time Complexity:       
        Best:               O(NM) where N = len(results), M = len(results[0][team_index])
        Worst:              O(NM) where N = len(results), M = len(results[0][team_index])

    :Aux Space Complexity:  
        Input:              O(N) where N = len(results)
        Aux:                O(N) where N = len(results)
    """

    def counting_sort(results: list[list[str, str, int]], roster: int, col: int) -> None:
        """ 
        In-place Counting Sort for each column of teams (in results)

        :Input:
            results:            A list of past tournament data
            roster:             An integer stating the (number of) unique characters available 
            col:                The column of teams currently being sorted

        :Post Condition:        Teams sorted from the right most column to column col

        :Time Complexity:       
            Best:               O(N) where N = len(results)
            Worst:              O(N) where N = len(results)

        :Aux Space Complexity:  
            Input:              O(N) where N = len(results)
            Aux:                O(N) where N = len(results)
        """
        # Type hints
        ind: int
        nesting_list: list[list[list[str, str, int]]]

        # Creating nesting_lst with inner lists as buckets
        # With size roster
        nesting_list = [None] * roster

        # Loop O(1) times
        for i in range(roster):
            nesting_list[i] = []

        # Storing strings in buckets
        # Loop O(N) times
        for result in results:
            nesting_list[ord(result[team_index][col]) - 65].append(result)

        # Putting back strings in original list
        # In total, loop O(N) times
        ind = 0
        for inner_list in nesting_list:
            for item in inner_list:
                results[ind] = item
                ind += 1

    # Sorting the order of characters before sorting the teams
    # Loop O(N) times
    for result in results:

        # The teams are strings, need to split the letters into a list for sorting
        # Rejoin them as a string before reassigning the newly sorted team
        # O(M) to sort
        result[team_index] = ''.join(counting_sort_team(
            [letter for letter in result[team_index]], roster))

    # Performing counting sort from the right most to the left most column
    # Loop O(M) times
    for col in range(len(results[0][team_index]) - 1, -1, -1):
        counting_sort(results, roster, col)


def counting_sort_score(results: list[list[str, str, int]]) -> None:
    """
    In-Place Counting Sort for scores in results

    :Input:
        results:        A list of results from past tournaments
                        in the format [team1, team2, score]

    :Post Condition:    The list of results based on the score 
                        in a non-increasing order

    :Time Complexity:
        Best:           O(N) where N = len(results)
        Worst:          O(N) where N = len(results)

    :Space Complexity:
        Input:          O(N) where N = len(results)
        Aux:            O(1)
    """
    # Type hints
    ind: int
    max_score: int
    nesting_list: list[list[list[str, str, int]]]

    # Finding the highest score value
    # Loops O(N) times
    max_score = results[0][2]
    for result in results:
        if max_score < result[2]:
            max_score = result[2]

    # Creating a nesting list of size max_score
    # Loops O(1) times
    nesting_list = [None] * (max_score + 1)
    for i in range(max_score + 1):
        nesting_list[i] = []

    # Storing the results based on their score
    # Loops O(N) times
    for result in results:
        nesting_list[max_score - result[2]].append(result)

    # Returning the results in non-increasing order
    # In total, loops O(N) times
    ind = 0
    for i in range(max_score + 1):
        for result in nesting_list[i]:
            results[ind] = result
            ind += 1


# Functions for search matches
def remove_duplicates(results: list[list[str, str, int]]) -> None:
    """ 
    In-place function to remove duplicates in a list.

    :Input:
        results:            A list to remove duplicate items from

    :Post Condition:        The duplicates in the input list would have been removed, 
                            leaving all unique items

    :Time Complexity:       
        Best:               O(N) where N = len(results)
        Worst:              O(N) where N = len(results)

    :Aux Space Complexity:  
        Input:              O(N) where N = len(results)
        Aux:                O(1)
    """
    # Type hints
    check: int
    uniq: int

    # Creating 2 pointers,
    # 1 to point at the latest unique index
    # 1 to point at the most recently checked index
    uniq, check = 0, 0

    # Loop O(N) times
    while check + 1 < len(results):
        # The checking item is unique
        if results[uniq] != results[check + 1]:
            # Swap items uniq+1 and check+1
            results[uniq + 1], results[check +
                                       1] = results[check + 1], results[uniq + 1]

            # Increase uniq since 1 more unique item is found
            uniq += 1

        # Check next item
        check += 1

    # Remove duplicates in results
    # from behind to ensure O(1) time complexity
    # Which are from index uniq+1 onwards
    for _ in range(len(results) - 1, uniq, -1):
        del results[-1]


def binary_search_matches(results: list[list[str, str, int]], score: int) -> list[list[str, str, int]]:
    """ 
    Binary Search Function to find matches in results 
        with score as its score value

    :Input:
        results:            Input list to find matches from
        score:              Score to match list items with

    :Return:        
        searchedmatches:    A list of matches that meet either requirement of:
                                - result_score == score
                                - min result_score > score

    :Time Complexity:       
        Best:               O(1)
        Worst:              O(N) where N = len(results)

    :Aux Space Complexity:  
        Input:              O(N) where N = len(results)
        Aux:                O(sm) where sm is the number of searchedmatches in results
    """
    # Type hints
    cur_score: int
    end: int
    high: int
    low: int
    mid: int
    start: int

    # If the score is above the max score in results,
    # there will be no matches
    if score > results[0][2]:
        return []

    # Pointers at each end of results
    low, high = 0, len(results) - 1

    # Start searching
    while low <= high:

        # Current score
        mid = (low + high) // 2
        cur_score = results[mid][2]

        # Score does is not in results OR score is met
        # Stop searching
        if low == high and score != cur_score or cur_score == score:
            break

        # Score not yet found
        # Going left
        elif cur_score < score:
            high = mid - 1

        # Going right
        elif cur_score > score:
            low = mid + 1

    # Score does not exist,
    # Find next score larger than input score
    if score != cur_score:

        # Loop up to O(N) times
        while results[mid][2] < score:
            mid -= 1

        # Re-assign score with new score value
        score = results[mid][2]

    # Variables to indicate first and last match where score matches
    start, end = mid, mid

    # Score found
    # Go to the first occurence where score matches
    # Loop up to O(N) times
    for i in range(start - 1, -1, -1):
        if results[i][2] != score:
            break
        start -= 1

    # Go to last occurence where score matches
    # Loop up to O(N) times
    for i in range(end + 1, len(results)):
        if results[i][2] != score:
            break
        end += 1

    return results[start: end + 1]


def analyze(results: list[list[str, str, int]], roster: int, score: int) -> list[list[list[str, str, int]], list[list[str, str, int]]]:
    """ 
    Analyzes past tournament data in order to find the top 10 matches
        as well as matches with the same score as the input score

    :Input:
        results:            A list of past tournament data, each match with the teams and scores
        roster:             An integer stating the (number of) unique characters available 
        score:              The score which team1 got against team2

    :Return:
        top10matches:       The top 10 matches ranked based on score, then lexicographic order of team1, and then team2
        searchedmatches:    A list of matches which score values equal the score input (or minimum score > input score)

    :Time Complexity:       
        Best:               O(NM) where N = len(results), M = len(results[0][0])
        Worst:              O(NM) where N = len(results), M = len(results[0][0])

    :Aux Space Complexity:  
        Input:              O(N)  where N = len(results)
        Aux:                O(NM) where N = len(results), M = len(results[0][0])
    """
    # Create the opposites of each result
    for i in range(len(results)):
        r = results[i]
        results.append([r[1], r[0], 100 - r[2]])

    # Sort team2 in ascending lexicographic order
    radix_sort_teams(results, roster, 1)

    # Sort team1 in ascending lexicographic order
    radix_sort_teams(results, roster, 0)

    # Sort score in non-increasing order
    counting_sort_score(results)

    # Removing any duplicates in results
    remove_duplicates(results)

    # Finally, returning top10matches (i.e., up to 10 highest scored matches)
    # and searchedmatches (i.e., matches where score = input score (or minimum score that is > input score))
    return [results[:10], binary_search_matches(results, score)]
