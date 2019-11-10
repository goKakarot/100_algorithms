"""594 Implement Stack

"""


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.array = []

    def push(self, x):
        # write your code here
        self.array.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.array.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.array[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.array == []