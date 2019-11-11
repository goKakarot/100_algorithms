"""494 Implement Stack by Two Queues

Algorithm:
因为queue是先进先出, 所以要吐出最后一个元素必须先清空前面的各项元素,
使用连个deque做腾挪完成stack的pop操作

Note:
构造的时候，初始化两个队列，queue1，queue2。
queue1主要用来存储，queue2则主要用来帮助queue1弹出元素以及访问栈顶。

"""


from collections import deque


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def move_item(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

    def swap(self):
        self.queue1, self.queue2 = self.queue2, self.queue1

    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.move_item()
        self.queue1.popleft()
        self.swap()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.move_item()
        item = self.queue1.popleft()
        self.swap()
        self.queue1.append(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue1) == 0