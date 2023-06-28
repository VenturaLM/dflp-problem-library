(
    """
    @article{Conway1994,
    author = {Daniel G. Conway and M. A. Venkataramanan},
    doi = {10.1016/0305-0548(94)90023-X},
    issn = {03050548},
    issue = {8},
    journal = {Computers and Operations Research},
    pages = {955-960},
    title = {Genetic search and the dynamic facility layout problem},
    volume = {21},
    year = {1994},
    }
    """,
    # Distance metric
    "Manhattan",
    # List of plants:
    (  # (level, [(x,y) coordinates of polygon vertexes], [Exterior type of every side])
        (1, [(0, 0), (3, 0), (3, 3), (0, 3)], []),
    ),
    # List of facilities:
    (  # (Name, Type, Min.Area, Min.Side, ARMin, AROpt1, AROpt2,  ARMax)
        ("1", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("2", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("3", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("4", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("5", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("6", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("7", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("8", "region", [1] * 5, None, None, None, None, [1] * 5),
        ("9", "region", [1] * 5, None, None, None, None, [1] * 5),
    ),
    # Dictionary of relation tables:
    {  # Table name : [Data rows]
        "Flow": {
            1: [
                [0, 3622, 258, 493, 697, 296, 627, 552, 287],  # 1
                [991, 0, 316, 443, 570, 684, 334, 283, 1043],  # 2
                [673, 6522, 0, 484, 114, 324, 611, 762, 762],  # 3
                [791, 4369, 203, 0, 170, 1031, 598, 923, 788],  # 4
                [867, 5146, 56, 203, 0, 1121, 309, 154, 361],  # 5
                [894, 3264, 71, 62, 769, 0, 664, 343, 282],  # 6
                [714, 3113, 240, 506, 831, 1183, 0, 1144, 311],  # 7
                [588, 1319, 319, 161, 826, 1194, 744, 0, 773],  # 8
                [1096, 6521, 335, 317, 459, 439, 416, 1222, 0],  # 9
            ],
            2: [
                [0, 136, 6371, 886, 1596, 213, 499, 1378, 476],  # 1
                [657, 0, 3461, 1275, 567, 254, 405, 263, 449],  # 2
                [590, 528, 0, 488, 498, 273, 311, 1277, 486],  # 3
                [179, 684, 1305, 0, 1748, 101, 462, 1008, 559],  # 4
                [772, 550, 6113, 478, 0, 261, 53, 1134, 1285],  # 5
                [511, 822, 2046, 1105, 1404, 0, 384, 405, 875],  # 6
                [577, 690, 2362, 925, 944, 139, 0, 847, 312],  # 7
                [300, 461, 3343, 514, 676, 128, 487, 0, 214],  # 8
                [291, 560, 6306, 397, 235, 243, 466, 963, 0],  # 9
            ],
            3: [
                [0, 265, 720, 3275, 361, 230, 580, 221, 1433],  # 1
                [695, 0, 816, 5276, 636, 683, 637, 1877, 203],  # 2
                [901, 1535, 0, 2322, 323, 592, 129, 857, 979],  # 3
                [1138, 298, 987, 0, 400, 1051, 163, 238, 924],  # 4
                [619, 478, 856, 4205, 0, 615, 81, 991, 990],  # 5
                [647, 1373, 441, 722, 608, 0, 128, 603, 1040],  # 6
                [1008, 1383, 772, 3552, 497, 836, 0, 1795, 211],  # 7
                [1348, 682, 233, 892, 206, 600, 448, 0, 679],  # 8
                [1291, 2281, 595, 3972, 89, 840, 257, 348, 0],  # 9
            ],
            4: [
                [0, 753, 632, 1686, 722, 241, 192, 510, 63],  # 1
                [840, 0, 897, 795, 3331, 1274, 426, 611, 442],  # 2
                [2138, 895, 0, 1277, 3019, 693, 88, 470, 514],  # 3
                [561, 445, 1444, 0, 1123, 385, 523, 2015, 428],  # 4
                [335, 421, 1549, 560, 0, 820, 251, 1480, 455],  # 5
                [636, 515, 776, 1590, 5257, 0, 781, 504, 416],  # 6
                [571, 625, 765, 1304, 5312, 954, 0, 647, 82],  # 7
                [1675, 297, 176, 1137, 1240, 1313, 715, 0, 321],  # 8
                [1187, 1550, 751, 441, 840, 336, 252, 1695, 0],  # 9
            ],
            5: [
                [0, 1017, 663, 1460, 1118, 804, 256, 1291, 246],  # 1
                [854, 0, 1102, 1476, 1109, 2931, 975, 1032, 403],  # 2
                [850, 1017, 0, 1503, 412, 4102, 613, 1083, 140],  # 3
                [525, 205, 792, 0, 1060, 3647, 196, 591, 981],  # 4
                [1653, 113, 1133, 1501, 0, 2160, 203, 706, 695],  # 5
                [981, 686, 184, 852, 450, 0, 155, 560, 962],  # 6
                [781, 1010, 353, 319, 648, 2043, 0, 914, 185],  # 7
                [2031, 701, 930, 755, 1113, 1883, 772, 0, 175],  # 8
                [867, 580, 377, 478, 284, 4879, 106, 325, 0],  # 9
            ],
        },
        "Fixed_shifting_costs": [
            [802, 985, 517, 500, 736, 910, 768, 564, 923],
            [802, 985, 517, 500, 736, 910, 768, 564, 923],
            [802, 985, 517, 500, 736, 910, 768, 564, 923],
            [802, 985, 517, 500, 736, 910, 768, 564, 923],
            [802, 985, 517, 500, 736, 910, 768, 564, 923],
        ],
    },
)
