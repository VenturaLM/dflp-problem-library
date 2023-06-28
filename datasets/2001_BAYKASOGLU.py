(
    """
    @report{,
    author = {Adil Baykasogy Lu and Nabil N Z Gindy},
    journal = {Computers & Operations Research},
    keywords = {Dynamic layout,Optimization,Simulated annealing},
    pages = {1403-1426},
    title = {A simulated annealing algorithm for dynamic layout problem},
    volume = {28},
    year = {2001},
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
        ("1", "region", [1] * 3, None, None, None, None, [1] * 3),
        ("2", "region", [1] * 3, None, None, None, None, [1] * 3),
        ("3", "region", [1] * 3, None, None, None, None, [1] * 3),
        ("4", "region", [1] * 3, None, None, None, None, [1] * 3),
        ("5", "region", [1] * 3, None, None, None, None, [1] * 3),
        ("6", "region", [1] * 3, None, None, None, None, [1] * 3),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 25, 3, 20, 56, 78],
                [50, 0, 70, 100, 50, 40],
                [20, 45, 0, 30, 70, 70],
                [10, 10, 45, 0, 45, 78],
                [25, 54, 21, 29, 0, 45],
                [78, 54, 98, 54, 10, 0],
            ],
            2: [
                [0, 45, 80, 40, 100, 120],
                [50, 0, 60, 20, 45, 89],
                [200, 25, 0, 40, 45, 100],
                [60, 40, 45, 0, 100, 110],
                [100, 50, 50, 40, 0, 40],
                [50, 50, 42, 42, 78, 0],
            ],
            3: [
                [0, 75, 300, 20, 54, 59],
                [30, 0, 70, 10, 78, 10],
                [10, 95, 0, 40, 10, 24],
                [90, 100, 45, 0, 210, 20],
                [100, 45, 15, 54, 0, 89],
                [11, 25, 69, 78, 78, 0],
            ],
        },
        "Fixed_shifting_costs": [
            [40, 40, 30, 50, 60, 50],
            [40, 40, 30, 50, 60, 50],
            [40, 40, 30, 50, 60, 50],
        ],
    },
)
