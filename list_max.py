# Author: Calvin Hotrum
# Date: 07/22/2020
# Description: 6a- Using recursion to find the maximum value in a list
def list_max(list):
    """Takes as a parameter a list of numbers, uses recursion to compare values, and
        Returns max value of list. """
    if len(list) == 1: return list[0] #base

    if list_max(list[1:]) > list[0]:
        return list_max(list[1:]) #recurse through list-1 until max
    else:
       return list[0]
