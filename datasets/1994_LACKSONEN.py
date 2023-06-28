(
    """
    @report{Lacksonen1994,
    author = {Thomas A Lacksonen},
    issue = {I},
    journal = {Opl Res. Soc},
    keywords = {dynamic layouts,facilities layout,mixed integer linear programming},
    pages = {59-69},
    title = {Static and Dynamic Layout Problems with Varying Areas},
    volume = {45},
    year = {1994},
    }
    """,
    # Distance metric
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (6, 0), (6, 6), (0, 6)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [5] * 2, None, None, None, None, [2] * 2),
        ("2", "region", [2] * 2, None, None, None, None, [2] * 2),
        ("3", "region", [3] * 2, None, None, None, None, [2] * 2),
        ("4", "region", [4] * 2, None, None, None, None, [2] * 2),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 0, 0, 0],  # 1
                [10, 0, 0, 0],  # 2
                [4, 8, 0, 0],  # 3
                [0, 2, 6, 0],  # 4
            ],
            2: [
                [0, 0, 0, 0],  # 1
                [6, 0, 0, 0],  # 2
                [2, 6, 0, 0],  # 3
                [11, 6, 5, 0],  # 4
            ],
        },
        "Fixed_shifting_costs": [
            [4] * 4,  # 1-2
        ],
    },
)
