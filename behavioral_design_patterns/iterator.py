from __future__ import annotations
from typing import Any, List


# Define the Iterator interface
class Iterator:
    """
    Iterator interface.
    """

    def has_next(self) -> bool:
        """
        Check if there are more elements to iterate over.

        Returns:
            bool: True if there are more elements, False otherwise.
        """
        pass

    def next(self) -> Any:
        """
        Retrieve the next element in the iteration.

        Returns:
            Any: The next element.

        Raises:
            StopIteration: If there are no more elements to iterate over.
        """
        pass


# Define the Aggregate interface
class Aggregate:
    def create_iterator(self) -> Iterator:
        pass


# Concrete Iterator
class ListIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._collection)

    def next(self) -> Any:
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration()


# Concrete Aggregate
class SimpleList(Aggregate):
    def __init__(self):
        self._data = []

    def add_item(self, item: Any):
        self._data.append(item)

    def create_iterator(self) -> Iterator:
        return ListIterator(self._data)


# Client code
if __name__ == "__main__":
    simple_list = SimpleList()
    simple_list.add_item("Apple")
    simple_list.add_item("Banana")
    simple_list.add_item("Orange")

    iterator = simple_list.create_iterator()

    while iterator.has_next():
        print(iterator.next())
