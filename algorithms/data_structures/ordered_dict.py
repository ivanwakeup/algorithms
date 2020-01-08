'''
how do we think about designing an orderedDict?


'''


# class MyOrderedDict(dict):
#
#     def __init__(self):
#         super(MyOrderedDict, self).__init__()
#
#     def __getitem__(self, item):
#         '''
#         get item like a normal dict, but also update the stored node to be in the most recently used position
#         :param item:
#         :return: item if exists, else throw KeyError
#         '''
#
#     def __setitem__(self, key, value):
#         '''
#         set item, and append it to the end of backing linked list -> in the most recently used position
#         :param key:
#         :param value:
#         :return:
#         '''
#
#
#
# class DoubleListNode:
#
#     def __init__(self, value):
#         self.
# class DoubleLinkedList:
#
#     def __init__(self):

from collections.abc import Hashable


class Mine(Hashable):

    def __init__(self):
        pass

    def __hash__(self):
        return 1

d = Mine()