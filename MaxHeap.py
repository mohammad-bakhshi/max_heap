from heapq import merge
import sys


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    @staticmethod
    def parent(pos):

        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    @staticmethod
    def leftChild(pos):

        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    @staticmethod
    def rightChild(pos):

        return (2 * pos) + 1

    def size(self) -> int:

        return self.size

    def clear(self) -> None:

        self.Heap = [0] * (self.maxsize + 1)
        self.size = 0

        # Function that returns true if the passed
        # node is a leaf node

    @staticmethod
    def isLeaf(heap, pos):

        if pos >= (heap.size//2) and pos <= heap.size:
            return True
        return False

    # Function to swap two nodes of the heap
    @staticmethod
    def swap(heap, fpos, spos):

        heap.Heap[fpos], heap.Heap[spos] = (heap.Heap[spos],
                                            heap.Heap[fpos])

    @staticmethod
    # Function to heapify the node at pos
    def maxHeapify(heap, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not MaxHeap.isLeaf(heap, pos):
            if (heap.Heap[pos] < heap.Heap[MaxHeap.leftChild(pos)] or
                    heap.Heap[pos] < heap.Heap[MaxHeap.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (heap.Heap[MaxHeap.leftChild(pos)] >
                        heap.Heap[MaxHeap.rightChild(pos)]):
                    MaxHeap.swap(heap, pos, MaxHeap.leftChild(pos))
                    MaxHeap.maxHeapify(heap, MaxHeap.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    MaxHeap.swap(heap, pos, MaxHeap.rightChild(pos))
                    MaxHeap.maxHeapify(heap, MaxHeap.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
                self.Heap[MaxHeap.parent(current)]):
            MaxHeap.swap(self, current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print("PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extract_max(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        MaxHeap.maxHeapify(self, self.FRONT)

        return popped

    def find_max(self):

        popped = self.Heap[self.FRONT]
        return popped

    @staticmethod
    def merge(heap1, heap2, size1, size2):
        merged = MaxHeap(size1+size2)
        for i in range(1, size1+1):
            merged.insert(heap1.Heap[i])
        for i in range(1, size2+1):
            merged.insert(heap2.Heap[i])
        return merged

    def add_to_all(self, k):
        for i in range(1, self.size+1):
            self.Heap[i] += k


# Driver Code
if __name__ == "__main__":

    maxHeap1 = MaxHeap(10)
    maxHeap1.insert(5)
    maxHeap1.insert(6)
    maxHeap1.insert(2)
    maxHeap1.insert(10)

    maxHeap2 = MaxHeap(10)
    maxHeap2.insert(7)
    maxHeap2.insert(9)
    maxHeap2.insert(12)

    merged = MaxHeap.merge(maxHeap1, maxHeap2, maxHeap1.size, maxHeap2.size)

    merged.add_to_all(5)

    merged.Print()

    print("The Max val is " + str(merged.find_max()))
