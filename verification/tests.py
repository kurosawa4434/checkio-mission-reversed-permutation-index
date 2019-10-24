"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            'input': [3, 5],
            'answer': [2, 0, 1],
        },
        {
            'input': [5, 1],
            'answer': [0, 1, 2, 3, 4],
            'explanation': 'Edge case: first permutation of length 5',
        },
        {
            'input': [5, 120],
            'answer': [4, 3, 2, 1, 0],
            'explanation': 'Edge case: last permutation of length 5',
        },
        {
            'input': [6, 271],
            'answer': [2, 1, 3, 0, 4, 5],
        },
        {
            'input': [9, 279780],
            'answer': [6, 8, 3, 4, 2, 1, 7, 5, 0],
        },
        {
            'input': [12, 12843175],
            'answer': [0, 4, 7, 5, 8, 2, 10, 6, 3, 1, 9, 11],
        },
        {
            'input': [15, 787051783737],
            'answer': [9, 0, 6, 2, 5, 7, 12, 10, 3, 8, 11, 4, 13, 1, 14],
        },
        {
            'input': [18, 3208987196401056],
            'answer': [9, 0, 6, 17, 8, 12, 11, 1, 10, 14, 3, 15, 2, 13, 16, 7, 5, 4],
        },
        {
            'input': [24, 238515587608877815254677],
            'answer': [9, 5, 4, 12, 13, 17, 7, 0, 23, 16, 11, 8, 15, 21, 2, 3, 22, 1, 10, 19, 6, 20, 14, 18],
        },
        {
            'input': [27, 6707569694907742966546817183],
            'answer': [16, 17, 10, 23, 4, 22, 7, 18, 2, 21, 13, 6, 9, 8, 19, 3, 25, 12, 26, 24, 14, 1, 0, 20, 15, 5, 11],
        },
    ],
}
