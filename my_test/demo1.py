import demo2
import helper


def go(matrix):
    # Showcasing Global tracing across modules
    helper.DEBUG = 1  # watchvar helper.DEBUG
    sol = demo2.Solution(matrix)
    ans = sol.findPath()

    # Things left
    # Check for variable deletion locally
    # Check for global variables existence


class Node:
    def __init__(self, data):
        self.data = data
        self.nextr = None
        self.nextl = None


def go2():
    root = Node(1)  # watchvar btree:nextl:nextr:data root
    root.nextr = Node(2)
    root.nextl = Node(0)
    root.nextl.nextl = Node(-2)
    root.nextr.nextr = Node(2)
    binarySearch(root, -2)


def binarySearch(root, target: int):
    x = root  # watchvar ref:root:btree x
    while x is not None:
        if x.data == target:
            return x
        if x.data < target:
            x = x.nextr
        else:
            x = x.nextl
    return None


def main():
    go([[1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1]])


if __name__ == "__main__":
    main()
    # print("Done")
