"""
Some header maybe?
Version control?
Your name, student ID, email
"""

# remember, no codes outside.
# remember to remove all print() statements else you could be penalized.

def function1(argv_something):
    print("hello")
    return 123

def analyze(results, roster, score):
    """
    This function does magic
    Written by l337coderblazeIT

    Precondition:
    Postcondition:

    Input:
        results: bla lol kappa
        roster: bla bla
        score: bla bla bla
    Return:
        answer: is the answer

    Time complexity: 
        Best:
        Worst:
    Space complexity: 
        Input:
        Aux:

    """
    # do something
    answer = None
    # loop 10
    for i in range(10):
        # call the function
        something = function1()
    # return answer
    return answer

"""
This the driver, where you can have your programming codes here.
No other codes should be outside function or the driver; as I saw a lot in the code review.
"""
if __name__ == "__main__":
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
        ]
    # looking for a score of 64
    score = 64
    # running the function
    analyze(results, roster, score)