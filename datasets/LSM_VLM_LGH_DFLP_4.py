(
    "",
    "Manhattan",
    ((1, [(0, 0), (13, 0), (13, 6), (0, 6)], []),),
    (
        ("1", "region", [12, 16, 19, 16, 18], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("2", "region", [15, 14, 14, 18, 12], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("3", "region", [12, 14, 15, 12, 16], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("4", "region", [12, 11, 12, 11, 15], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("5", "region", [16, 16, 12, 13, 8], 1, None, None, None, [4, 4, 4, 4, 4]),
        ("6", "region", [11, 7, 6, 8, 9], 1, None, None, None, [4, 4, 4, 4, 4]),
    ),
    {
        "Flow": {
            1: [
                [0, 18, 16, 3, 9, 5],
                [4, 0, 16, 19, 19, 9],
                [14, 11, 0, 9, 4, 6],
                [19, 13, 14, 0, 16, 16],
                [4, 19, 6, 5, 0, 18],
                [9, 13, 6, 13, 16, 0],
            ],
            2: [
                [0, 19, 16, 7, 19, 1],
                [13, 0, 13, 13, 11, 9],
                [8, 16, 0, 9, 9, 11],
                [0, 14, 7, 0, 1, 14],
                [2, 15, 8, 16, 0, 6],
                [14, 20, 10, 18, 14, 0],
            ],
            3: [
                [0, 18, 19, 10, 14, 9],
                [7, 0, 12, 17, 1, 6],
                [9, 17, 0, 0, 5, 14],
                [4, 5, 0, 0, 3, 14],
                [16, 2, 5, 5, 0, 20],
                [10, 0, 7, 3, 5, 0],
            ],
            4: [
                [0, 9, 6, 14, 19, 11],
                [11, 0, 11, 12, 14, 5],
                [18, 9, 0, 19, 18, 4],
                [5, 12, 8, 0, 1, 19],
                [0, 9, 3, 11, 0, 10],
                [10, 19, 5, 0, 0, 0],
            ],
            5: [
                [0, 18, 5, 14, 9, 17],
                [19, 0, 0, 7, 1, 18],
                [1, 12, 0, 1, 6, 13],
                [0, 8, 19, 0, 14, 4],
                [9, 8, 11, 15, 0, 13],
                [1, 1, 3, 0, 3, 0],
            ],
        },
        "Fixed_shifting_costs": [
            [48, 31, 39, 33, 17, 15],
            [48, 21, 29, 37, 46, 60],
            [46, 32, 47, 44, 33, 47],
            [27, 26, 43, 19, 55, 49],
            [33, 28, 35, 37, 54, 34],
        ],
        "Variable_shifting_costs": [
            [1, 4, 1, 5, 3, 1],
            [5, 5, 3, 1, 2, 2],
            [4, 1, 3, 4, 2, 5],
            [4, 3, 1, 4, 5, 4],
            [2, 2, 2, 1, 5, 2],
        ]
    },
)
