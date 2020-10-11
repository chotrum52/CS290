# Author: Calvin Hotrum
# Date: 07/11/2020
# Description: Project 4b - Box Class containing dimensions of the box
class Box:
    """Represents a box, contains init values for length, height, width. Can return volume of box. """

    def __init__(self, length, width, height):
        """Initializes LWH variables for box"""
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        volume_box = self._length * self._width * self._height
        return volume_box

    def get_length(self):
        """Returns box length"""
        return self._length

    def get_width(self):
        """Returns box width"""
        return self._width

    def get_height(self):
        """Returns box height"""
        return self._height

def box_sort(box_list):
    """
    Uses insertion sort to sort a list of boxes by volume from largest to smallest- descending order.
    """
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and value.volume() > box_list[pos].volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value
    return box_list
