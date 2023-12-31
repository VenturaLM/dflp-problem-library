(
    """
    @article{ROSENBLATT1986,
    author = {MEIR J. ROSENBLATT},
    isbn = {0315880678},
    issn = {0091-6749},
    issue = {1},
    journal = {Management Science},
    pages = {76-86},
    title = {The Dynamics of Plant Layout},
    volume = {32},
    url = {https://doi.org/10.1287/mnsc.32.1.76},
    year = {1986},
    }
    """,
    # Distance metric
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (3, 0), (3, 2), (0, 2)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
        ("2", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
        ("3", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
        ("4", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
        ("5", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
        ("6", "region", [1] * 5, [1] * 5, 0, 0, 0, [1] * 5),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 63, 605, 551, 116, 136],  # 1
                [63, 0, 635, 941, 50, 191],  # 2
                [104, 71, 0, 569, 136, 55],  # 3
                [65, 193, 622, 0, 77, 90],  # 4
                [162, 174, 607, 591, 0, 179],  # 5
                [156, 13, 667, 611, 175, 0],  # 6
            ],
            2: [
                [0, 175, 804, 904, 56, 176],  # 1
                [63, 0, 743, 936, 45, 177],  # 2
                [168, 85, 0, 918, 138, 134],  # 3
                [51, 94, 962, 0, 173, 39],  # 4
                [97, 104, 730, 634, 0, 144],  # 5
                [95, 115, 983, 597, 24, 0],  # 6
            ],
            3: [
                [0, 90, 77, 553, 769, 139],  # 1
                [168, 0, 114, 653, 525, 185],  # 2
                [32, 35, 0, 664, 898, 87],  # 3
                [27, 166, 42, 0, 960, 179],  # 4
                [185, 56, 44, 926, 0, 104],  # 5
                [72, 128, 173, 634, 687, 0],  # 6
            ],
            4: [
                [0, 112, 15, 199, 665, 649],  # 1
                [153, 0, 116, 173, 912, 671],  # 2
                [10, 28, 0, 182, 855, 542],  # 3
                [29, 69, 15, 0, 552, 751],  # 4
                [198, 71, 42, 24, 0, 758],  # 5
                [62, 109, 170, 90, 973, 0],  # 6
            ],
            5: [
                [0, 663, 23, 128, 119, 50],  # 1
                [820, 0, 5, 98, 141, 66],  # 2
                [822, 650, 0, 137, 78, 91],  # 3
                [826, 570, 149, 0, 93, 151],  # 4
                [915, 515, 53, 35, 0, 177],  # 5
                [614, 729, 178, 10, 99, 0],  # 6
            ],
        },
        "Fixed_shifting_costs": [
            [887, 964, 213, 367, 289, 477],  # 1-2
            [887, 964, 213, 367, 289, 477],  # 2-3
            [887, 964, 213, 367, 289, 477],  # 3-4
            [887, 964, 213, 367, 289, 477],  # 4-5
        ],
    },
)
