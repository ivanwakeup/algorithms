# def binary_search(arr, l, h, v, searches):
#     if not arr:
#         return -1
#     if l == h:
#         return l if arr[l] == v else -1
#
#     mid = (l+h)//2
#     print("next search space size is {}".format(h))
#
#     if arr[mid] == v:
#         print("found value at {} index in {} recursions".format(mid, searches))
#         return mid
#     elif arr[mid] > v:
#         return binary_search(arr, l, mid, v, searches+1)
#     else:
#         return binary_search(arr, mid+1, h, v, searches+1)
#
# data = [36, 40, 51, 61, 61, 68, 86, 90, 90, 101, 108, 109, 112, 114, 119, 121, 122, 125, 128, 128, 129, 133, 134, 136, 143, 147, 149, 153, 158, 158, 170, 175, 176, 178, 182, 183, 183, 183, 184, 187, 188, 191, 193, 194, 200, 202, 202, 203, 204, 206, 207, 208, 208, 208, 210, 216, 219, 224, 224, 225, 225, 227, 232, 234, 240, 244, 244, 246, 248, 250, 250, 251, 251, 252, 254, 261, 261, 264, 264, 264, 265, 266, 266, 268, 270, 271, 271, 273, 274, 276, 277, 278, 278, 279, 279, 279, 281, 282, 282, 286, 289, 291, 291, 294, 294, 298, 300, 301, 302, 303, 303, 304, 307, 308, 308, 308, 309, 310, 311, 314, 314, 314, 315, 315, 316, 316, 318, 318, 320, 320, 321, 321, 322, 322, 325, 326, 326, 330, 330, 331, 337, 337, 339, 340, 345, 346, 347, 347, 348, 349, 350, 350, 350, 350, 351, 353, 354, 355, 356, 357, 358, 358, 359, 360, 360, 360, 361, 361, 362, 362, 364, 364, 367, 369, 369, 374, 377, 378, 378, 383, 385, 386, 386, 386, 386, 387, 389, 389, 391, 391, 392, 392, 394, 394, 397, 400, 400, 402, 403, 404, 404, 404, 404, 406, 407, 407, 409, 409, 410, 411, 412, 412, 413, 417, 417, 418, 419, 419, 420, 420, 422, 423, 424, 424, 424, 425, 426, 427, 428, 428, 429, 435, 438, 439, 440, 440, 441, 441, 441, 442, 443, 444, 444, 445, 447, 448, 448, 448, 449, 449, 451, 452, 455, 457, 458, 461, 462, 463, 463, 464, 464, 464, 465, 467, 470, 470, 470, 471, 472, 472, 473, 473, 475, 477, 479, 479, 480, 482, 483, 485, 485, 486, 486, 489, 489, 490, 491, 491, 494, 494, 495, 495, 496, 497, 497, 497, 500, 500, 500, 501, 502, 504, 504, 504, 507, 507, 508, 511, 511, 511, 512, 512, 512, 513, 514, 515, 516, 517, 521, 522, 522, 522, 523, 524, 525, 525, 526, 529, 530, 532, 533, 533, 536, 536, 537, 539, 539, 540, 541, 541, 543, 543, 544, 545, 545, 545, 547, 547, 548, 549, 549, 550, 550, 551, 552, 553, 554, 554, 555, 556, 556, 558, 559, 560, 562, 563, 564, 564, 564, 566, 566, 566, 566, 567, 567, 568, 573, 575, 575, 575, 576, 576, 576, 577, 577, 578, 579, 582, 582, 582, 585, 585, 585, 586, 586, 587, 587, 589, 591, 591, 592, 593, 593, 594, 594, 595, 596, 597, 600, 603, 604, 604, 605, 606, 606, 607, 608, 608, 612, 612, 612, 614, 614, 614, 615, 618, 618, 618, 624, 626, 629, 630, 631, 632, 634, 634, 639, 641, 641, 642, 642, 644, 646, 647, 648, 648, 649, 650, 651, 652, 653, 656, 656, 657, 659, 662, 664, 665, 669, 671, 672, 673, 674, 676, 678, 678, 679, 680, 681, 681, 682, 682, 682, 684, 687, 689, 691, 692, 693, 696, 697, 697, 699, 700, 701, 702, 704, 704, 705, 705, 706, 709, 711, 711, 711, 711, 712, 712, 713, 713, 716, 716, 716, 717, 718, 720, 723, 724, 724, 724, 725, 728, 729, 729, 733, 734, 735, 736, 736, 736, 738, 739, 739, 741, 741, 743, 744, 745, 746, 748, 748, 748, 750, 750, 750, 752, 752, 753, 755, 755, 755, 755, 756, 757, 758, 760, 761, 763, 763, 763, 764, 765, 765, 767, 767, 768, 769, 769, 769, 770, 770, 770, 770, 772, 772, 772, 772, 773, 774, 774, 775, 776, 779, 779, 780, 780, 780, 780, 781, 781, 783, 783, 783, 784, 786, 786, 786, 786, 786, 787, 788, 788, 790, 791, 792, 792, 794, 794, 794, 798, 798, 798, 798, 799, 800, 801, 803, 804, 804, 804, 805, 807, 807, 809, 810, 810, 811, 813, 818, 821, 823, 823, 824, 826, 826, 827, 828, 828, 828, 828, 831, 831, 831, 832, 833, 835, 836, 837, 839, 839, 840, 840, 841, 845, 845, 845, 845, 846, 848, 849, 849, 852, 853, 854, 854, 856, 856, 857, 857, 858, 859, 860, 860, 861, 863, 863, 864, 865, 866, 866, 868, 868, 868, 869, 869, 869, 871, 874, 875, 876, 876, 876, 877, 878, 879, 880, 880, 881, 882, 883, 883, 883, 884, 884, 887, 888, 888, 889, 890, 891, 891, 891, 892, 893, 896, 897, 898, 898, 900, 901, 901, 904, 905, 905, 906, 907, 909, 912, 914, 914, 917, 920, 921, 921, 922, 924, 928, 929, 930, 930, 931, 931, 931, 931, 932, 935, 935, 936, 936, 936, 937, 938, 940, 941, 941, 941, 943, 944, 944, 944, 945, 945, 948, 948, 949, 950, 952, 954, 956, 957, 958, 958, 959, 962, 964, 966, 966, 967, 967, 967, 967, 968, 969, 970, 971, 971, 972, 973, 973, 975, 977, 979, 981, 981, 981, 981, 983, 983, 985, 988, 989, 989, 990, 994, 995, 996, 996, 996, 999, 999, 1001, 1001, 1002, 1002, 1003, 1005, 1006, 1008, 1012, 1013, 1015, 1015, 1016, 1016, 1017, 1017, 1018, 1019, 1021, 1021, 1021, 1021, 1022, 1022, 1024, 1027, 1028, 1028, 1028, 1029, 1029, 1031, 1031, 1031, 1032, 1036, 1037, 1039, 1040, 1041, 1041, 1044, 1046, 1048, 1048, 1048, 1050, 1050, 1052, 1052, 1053, 1053, 1054, 1056, 1058, 1059, 1059, 1062, 1063, 1063, 1063, 1064, 1065, 1065, 1065, 1072, 1072, 1073, 1073, 1075, 1076, 1077, 1081, 1081, 1082, 1083, 1083, 1087, 1087, 1087, 1090, 1090, 1090, 1091, 1091, 1092, 1092, 1095, 1096, 1097, 1098, 1099, 1104, 1105, 1108, 1111, 1113, 1114, 1114, 1114, 1116, 1119, 1120, 1121, 1121, 1123, 1125, 1127, 1127, 1127, 1128, 1131, 1132, 1134, 1134, 1136, 1139, 1140, 1142, 1143, 1143, 1144, 1145, 1146, 1146, 1147, 1149, 1149, 1149, 1156, 1157, 1160, 1166, 1171, 1172, 1174, 1174, 1175, 1179, 1180, 1181, 1191, 1191, 1196, 1200, 1200, 1205, 1206, 1208, 1208, 1209, 1210, 1211, 1217, 1217, 1222, 1224, 1229, 1231, 1237, 1243, 1245, 1249, 1249, 1250, 1250, 1251, 1255, 1256, 1259, 1260, 1265, 1267, 1267, 1268, 1271, 1275, 1277, 1280, 1285, 1288, 1290, 1295, 1296, 1300, 1302, 1303, 1310, 1311, 1312, 1317, 1319, 1323, 1325, 1330, 1335, 1349, 1357, 1375, 1388]
#
# binary_search(data, 0, len(data)-1, 500, 0)









def binary_search(arr, target):
    if not arr:
        return -1
    l = 0
    h = len(arr) - 1
    #low could never be HIGHER than h
    while l < h:
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return l if arr[l] == target else -1



data = [1,2,4,48,122,155,1445,6]
target = 122
print(binary_search(data, target))