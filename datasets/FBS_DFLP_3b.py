(
    """
    @article{kulturel2019,
    author = {Sadan Kulturel-Konak},
    doi = {10.1080/03155986.2017.1346915},
    issn = {19160615},
    issue = {1},
    journal = {INFOR},
    keywords = {Facilities planning and design,Mixed-integer programming,Simulated annealing,Variable neighbourhood search,Zone-based dynamic facility layout problem},
    pages = {1-31},
    publisher = {University of Toronto Press Inc.},
    title = {The zone-based dynamic facility layout problem},
    volume = {57},
    year = {2019},
    }
    """,
    # Distance metric
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (15, 0), (15, 12), (0, 12)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [23] * 6, None, None, None, None, [5] * 6),
        ("2", "region", [16] * 6, None, None, None, None, [5] * 6),
        ("3", "region", [33] * 6, None, None, None, None, [7] * 6),
        ("4", "region", [13] * 6, None, None, None, None, [5] * 6),
        ("5", "region", [10] * 6, None, None, None, None, [4] * 6),
        ("6", "region", [19] * 6, None, None, None, None, [5] * 6),
        ("7", "region", [10] * 6, None, None, None, None, [4] * 6),
        ("8", "region", [26] * 6, None, None, None, None, [6] * 6),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 4, 19, 20, 19, 18, 12, 18],  # 1
                [15, 0, 11, 1, 14, 14, 9, 18],  # 2
                [9, 15, 0, 1, 13, 12, 3, 4],  # 3
                [12, 14, 9, 0, 0, 6, 18, 9],  # 4
                [8, 13, 17, 19, 0, 16, 14, 1],  # 5
                [4, 16, 12, 11, 0, 0, 8, 1],  # 6
                [14, 12, 6, 2, 2, 9, 0, 20],  # 7
                [19, 15, 11, 2, 11, 15, 6, 0],  # 8
            ],
            2: [
                [0, 20, 2, 12, 20, 14, 20, 18],  # 1
                [9, 0, 14, 13, 13, 9, 4, 19],  # 2
                [15, 16, 0, 10, 4, 5, 5, 15],  # 3
                [14, 9, 4, 0, 15, 2, 5, 13],  # 4
                [13, 20, 16, 18, 0, 13, 6, 13],  # 5
                [1, 10, 5, 19, 1, 0, 14, 19],  # 6
                [1, 0, 9, 3, 20, 13, 0, 14],  # 7
                [5, 4, 3, 20, 4, 20, 0, 0],  # 8
            ],
            3: [
                [0, 3, 16, 17, 5, 14, 13, 6],  # 1
                [9, 0, 11, 18, 16, 18, 2, 15],  # 2
                [8, 12, 0, 3, 14, 7, 10, 12],  # 3
                [13, 14, 16, 0, 5, 4, 17, 6],  # 4
                [10, 13, 7, 18, 0, 3, 10, 18],  # 5
                [11, 5, 7, 8, 16, 0, 11, 2],  # 6
                [7, 11, 12, 1, 3, 11, 0, 15],  # 7
                [12, 10, 17, 17, 19, 5, 16, 0],  # 8
            ],
            4: [
                [0, 13, 16, 2, 18, 4, 15, 3],  # 1
                [10, 0, 3, 7, 16, 14, 13, 14],  # 2
                [16, 17, 0, 10, 1, 8, 7, 8],  # 3
                [19, 8, 9, 0, 3, 11, 6, 10],  # 4
                [16, 2, 14, 16, 0, 1, 18, 5],  # 5
                [6, 3, 10, 1, 8, 0, 19, 4],  # 6
                [2, 15, 9, 15, 0, 0, 0, 16],  # 7
                [5, 6, 2, 12, 19, 5, 20, 0],  # 8
            ],
            5: [
                [0, 3, 15, 0, 17, 5, 7, 9],  # 1
                [15, 0, 8, 7, 4, 4, 7, 1],  # 2
                [15, 15, 0, 20, 1, 11, 11, 7],  # 3
                [0, 4, 5, 0, 14, 11, 8, 13],  # 4
                [13, 13, 19, 5, 0, 5, 11, 3],  # 5
                [5, 9, 10, 15, 8, 0, 17, 5],  # 6
                [4, 12, 6, 15, 8, 16, 0, 14],  # 7
                [12, 13, 4, 4, 17, 18, 19, 0],  # 8
            ],
            6: [
                [0, 7, 6, 16, 0, 4, 20, 8],  # 1
                [1, 0, 4, 12, 5, 16, 8, 17],  # 2
                [14, 8, 0, 1, 11, 13, 18, 15],  # 3
                [8, 9, 15, 0, 5, 8, 6, 16],  # 4
                [7, 17, 7, 11, 0, 5, 2, 4],  # 5
                [20, 10, 6, 3, 11, 0, 16, 16],  # 6
                [13, 13, 10, 17, 5, 18, 0, 18],  # 7
                [6, 8, 7, 3, 6, 4, 9, 0],  # 8
            ],
        },
        "Fixed_shifting_costs": [
            [45, 53, 39, 47, 50, 58, 60, 36],  # 1-2
            [45, 53, 39, 47, 50, 58, 60, 36],  # 2-3
            [45, 53, 39, 47, 50, 58, 60, 36],  # 3-4
            [45, 53, 39, 47, 50, 58, 60, 36],  # 4-5
            [45, 53, 39, 47, 50, 58, 60, 36],  # 5-6
        ],
        "Variable_shifting_costs": [
            [2, 2, 3, 2, 1, 2, 1, 3],  # 1-2
            [2, 2, 3, 2, 1, 2, 1, 3],  # 2-3
            [2, 2, 3, 2, 1, 2, 1, 3],  # 3-4
            [2, 2, 3, 2, 1, 2, 1, 3],  # 4-5
            [2, 2, 3, 2, 1, 2, 1, 3],  # 5-6
        ],
        "Max_parallel_bays": 5,
    },
)
