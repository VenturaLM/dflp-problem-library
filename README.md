## Description

The Dynamic Facility Layout Problem (DFLP) addresses the task of devising effective facility arrangements within a specified timeframe, accommodating variations in product types and demands across different periods. The primary objective of the DFLP is to identify the most favorable configuration of facilities within a given spatial context, aiming to minimize expenses, enhance operational efficiency, and accomplish specific goals. Key considerations in the DFLP encompass aspects such as product flow, material handling, facility capacities, and the dynamic nature of demand fluctuations over time.

The present repository contains a set of datasets associated with DFLP. Data files are Python (.py) files with the following structure:

- Bibliographic reference in '.bibtex' style.
- Distance metric.
- List of plants.
- List of facilities.
- Material flow matrices.
- Fixed shifting cost matrices (if applicable).
- Variable shifting cost matrices (if applicable).
- Maximum number of allowed parallel bays (if applicable).

## Example

```
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
```

## Considerations
1. In datasets where the same value of 'Min.Area', 'ARMax', 'Fixed_shifting_costs', or 'Variable_shifting_costs' is maintained for all periods, the following Python notation can be found:

```
"Fixed_shifting_costs": [
    [12] * 5,
    [12] * 5,
]
```

This is similar to:

```
"Fixed_shifting_costs": [
    [12, 12, 12, 12, 12],
    [12, 12, 12, 12, 12],
]
```

2. Some files may have a somewhat unconventional structure, as illustrated in the following example. 

```
"Flow": {
    1: [
        [0, 13, 9, 3, 0, 13, 11, 20, 11, 0, 2, 20, 8, 0, 20, 8, 15, 20, 20, 14],
        [18, 0, 4, 7, 0, 12, 20, 0, 9, 0, 16, 6, 15, 19, 7, 12, 9, 4, 0, 17],
        [
            18,
            11,
            0,
            1,
            3,
            3,
            9,
            16,
            19,
            17,
            1,
            19,
            14,
            7,
            17,
            13,
            10,
            6,
            10,
            13,
        ],
        ...
    ],
    ...
```

This depends on the Python file formatting package you are using. It only affects the visual appearance of the file, without altering its functionality, so there is no need to worry. In any case, feel free to download the file and format it according to your preferences.
