"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    """
    A node in a unidirectional linked list.
    """

    def __init__(self, value, next_ref, index):
        self.value = value
        self.next_ref = next_ref
        self.index = index


class CustomList:
    """
    An unidirectional linked list.
    """

    def __init__(self, *data):
        self.first = None
        self.last = None
        self.index_count = 0

        if data:
            for arg in data:
                self.append(arg)

    def append(self, value) -> None:
        if self.first is None:
            # self.first and self.last will reference to one area of memory
            self.last = self.first = Item(value, None, 0)
        else:
            # add to current Item reference on new Item
            index = self.last.index + 1
            self.last.next_ref = self.last = Item(value, None, index)

    def add_start(self, value) -> None:
        index = 0
        self.first = Item(value, self.first, index)
        # rebuild indexes
        for item in self:
            item.index = index
            index += 1

    def remove(self, value) -> None:
        self.__delitem__(self.find(value))

    def find(self, value):
        for item in self:
            if item.value == value:
                return item.index
        raise ValueError

    def clear(self) -> None:
        self.first = None
        self.last = None

    def __getitem__(self, index):
        for item in self:
            if item.index == index:
                return item.value
        raise IndexError

    def __setitem__(self, index, data) -> None:
        for item in self:
            if item.index is index:
                item.value = data
                return
        raise IndexError

    def __delitem__(self, index) -> None:
        if self.__len__() < index or index < 0:
            raise IndexError
        if self.first.index is index:
            self.first = self.first.next_ref
        else:
            prev_item = self.first
            for item in self:
                if item.index is index:
                    prev_item.next_ref = item.next_ref
                    break
                prev_item = item
        # rebuild indexes
        index = 0
        for item in self:
            item.index = index
            index += 1

    def __len__(self) -> int:
        counter = 0
        for i in self:
            counter += 1
        return counter

    def __iter__(self):
        if self.first is not None:
            current = self.first
            yield current
            while current.next_ref is not None:
                current = current.next_ref
                yield current

    def __str__(self):
        out = ""
        if self.first is not None:
            current = self.first
            out = '[index: ' + str(current.index) + " V= " + str(current.value) + "]"
            while current.next_ref is not None:
                current = current.next_ref
                out += ', [index: ' + str(current.index) + " V= " + str(current.value) + "]"
        return out

