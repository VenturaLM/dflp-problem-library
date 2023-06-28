(
    # Reference:
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
    # Distance metric:
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (15, 0), (15, 8), (0, 8)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [18] * 2, None, None, None, None, [4] * 2),
        ("2", "region", [26] * 2, None, None, None, None, [4] * 2),
        ("3", "region", [30] * 2, None, None, None, None, [4] * 2),
        ("4", "region", [26] * 2, None, None, None, None, [4] * 2),
        ("5", "region", [20] * 2, None, None, None, None, [4] * 2),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 2, 4, 2, 5],  # 1
                [0, 0, 5, 4, 1],  # 2
                [2, 4, 0, 1, 3],  # 3
                [4, 1, 2, 0, 2],  # 4
                [1, 1, 1, 0, 0],  # 5
            ],
            2: [
                [0, 3, 4, 3, 4],  # 1
                [4, 0, 0, 0, 1],  # 2
                [2, 1, 0, 2, 2],  # 3
                [4, 1, 5, 0, 0],  # 4
                [4, 4, 2, 0, 0],  # 5
            ],
        },
        "Fixed_shifting_costs": [
            [12] * 5,
            [12] * 5,
        ],
        "Variable_shifting_costs": [
            [1] * 5,
            [1] * 5,
        ],
        "Max_parallel_bays": 3,
    },
)
