class Node():
    # 限定属性
    __slots__ = ['_item','_next']
    def __init__(self,item):
        self._item = item
        self._next = None
