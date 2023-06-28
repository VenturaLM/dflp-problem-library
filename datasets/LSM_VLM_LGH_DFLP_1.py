(
    "",
    "Manhattan",
    ((1, [(0, 0), (14, 0), (14, 9), (0, 9)], []),),
    (
        ("1", "region", [25, 18, 25, 24, 20], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("2", "region", [12, 15, 15, 19, 20], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("3", "region", [10, 10, 12, 11, 12], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("4", "region", [10, 9, 9, 7, 11], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("5", "region", [7, 10, 6, 9, 10], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("6", "region", [21, 7, 25, 17, 10], 1, None, None, None, [4, 4, 4, 4, 4]),
    ),
    {
        "Flow": {
            1: [
                [0, 10, 5, 2, 10, 2],
                [7, 0, 0, 2, 9, 5],
                [7, 3, 0, 10, 4, 3],
                [9, 5, 9, 0, 7, 6],
                [3, 5, 1, 9, 0, 1],
                [10, 7, 10, 10, 0, 0],
            ],
            2: [
                [0, 0, 4, 1, 6, 8],
                [1, 0, 7, 9, 2, 8],
                [8, 2, 0, 1, 9, 2],
                [10, 9, 8, 0, 1, 7],
                [10, 6, 10, 3, 0, 8],
                [6, 2, 0, 8, 2, 0],
            ],
            3: [
                [0, 2, 4, 1, 4, 0],
                [0, 0, 3, 9, 9, 7],
                [0, 7, 0, 5, 2, 4],
                [5, 6, 10, 0, 2, 10],
                [9, 0, 3, 7, 0, 7],
                [10, 9, 6, 7, 10, 0],
            ],
            4: [
                [0, 4, 7, 6, 4, 8],
                [8, 0, 4, 3, 8, 3],
                [1, 7, 0, 7, 3, 5],
                [8, 8, 4, 0, 1, 2],
                [7, 6, 3, 3, 0, 9],
                [8, 6, 3, 6, 10, 0],
            ],
            5: [
                [0, 6, 3, 5, 6, 8],
                [5, 0, 9, 1, 8, 8],
                [7, 7, 0, 2, 0, 5],
                [2, 5, 2, 0, 4, 7],
                [10, 8, 8, 9, 0, 10],
                [7, 6, 2, 2, 6, 0],
            ],
        },
        "Fixed_shifting_costs": [
            [38, 15, 34, 60, 20, 50],
            [24, 28, 45, 47, 29, 40],
            [59, 28, 41, 42, 57, 16],
            [54, 24, 32, 33, 34, 22],
            [50, 60, 38, 23, 51, 54],
        ],
        "Variable_shifting_costs": [
            [2, 1, 4, 1, 2, 4],
            [4, 1, 5, 5, 1, 5],
            [4, 5, 2, 1, 3, 5],
            [1, 3, 1, 5, 2, 1],
            [2, 2, 3, 5, 2, 2],
        ]
    },
)
