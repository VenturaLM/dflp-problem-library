(
    """
    @article{Emami2013,
    author = {Saeed Emami and Ali S. Nookabadi},
    doi = {10.1007/s00170-013-4820-5},
    issn = {02683768},
    issue = {9-12},
    journal = {International Journal of Advanced Manufacturing Technology},
    keywords = {Keyword: Multi-objective optimization,MADM,MODFLP,Nondominated solution set},
    pages = {2215-2228},
    title = {Managing a new multi-objective model for the dynamic facility layout problem},
    volume = {68},
    year = {2013},
    }
    """,
    # Distance metric
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (11, 0), (11, 6), (0, 6)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [18] * 3, 0, [4] * 3, 0, 0, [4] * 3),
        ("2", "region", [14] * 3, 0, [4] * 3, 0, 0, [4] * 3),
        ("3", "region", [21] * 3, 0, [4] * 3, 0, 0, [4] * 3),
        ("4", "region", [13] * 3, 0, [4] * 3, 0, 0, [4] * 3),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 6, 1, 2],  # 1
                [0, 0, 4, 7],  # 2
                [0, 3, 0, 4],  # 3
                [1, 5, 6, 0],  # 4
            ],
            2: [
                [0, 5, 2, 3],  # 1
                [7, 0, 1, 7],  # 2
                [1, 0, 0, 5],  # 3
                [6, 6, 4, 0],  # 4
            ],
            3: [
                [0, 1, 7, 6],  # 1
                [0, 0, 6, 4],  # 2
                [7, 7, 0, 3],  # 3
                [3, 3, 2, 0],  # 4
            ],
        },
        "Fixed_shifting_costs": [
            [8, 8, 8, 8],
            [8, 8, 8, 8],
        ],
        "Variable_shifting_costs": [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ],
        "Max_parallel_bays": 3,
    },
)
