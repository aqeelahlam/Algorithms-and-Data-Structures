import sys

"""
Author: Aqeel Ahlam Rauf
Date: 10/07/2021

Disjoint Set Data Stucture (Or Union-Find):
- Union - Joins two Subsets together
- Find - Returns the parent of an element found in the set.
- Reference: https://www.geeksforgeeks.org/union-find/

Eg: Parent Array: 

[-1, -1, -1, -1, -3, 4, 4, 6]

- In this case, Negative indicates a parent. 
- @position 4: -3 indicates that we have three elements under the parent element 4
- @position 5: 4 indicates that the parent of element 5 is at position 4

Command Line Input: python3 z_algo.py text pattern

"""

def main():
    size = int(input("Enter Size of Array\n"))
    
    while True:
        first = int(input("Enter First Element:\n"))
        second = int(input("Enter Second Element:\n"))
        parent = InitializeSet(int(size))
        Union(first, second, parent)
    print(parent)


def InitializeSet(N):
    parentArray = [-1] * N

    return parentArray


def find(element, parent):
    """
    This function is used to the find the root of a given node/vertex.
    :param vertex: The vertex
    :param parent: Parent Array
    :Time Complexity: O(1) Amortized
    :return: vertex if the input vertex is the root, else returns the root of given vertex
    """
    while parent[element] >= 0:
        element = parent[element]

    return element


def Union(nodeA, nodeB, parent):
    """
    This function is used to merge two nodes or vertices together.
    This performs the union of two sets.
    This function is implemented using Union by height (rank) where find uses Path Splitting implementation
    :param nodeA: Node or Sub-Tree of a
    :param nodeB: Node or Sub-Tree of b
    :param parent: parent array
    :return: parent array
    """

    rootA = find(nodeA, parent)  # Find the root of tree with element a
    rootB = find(nodeB, parent)  # Find the root of tree with element b

    if rootA == rootB:  # Since a and b are already in the same tree, we can't union them
        pass

    heightA = -parent[rootA]
    heightB = -parent[rootB]

    # The smaller tree is merged into the bigger tree
    if heightA > heightB:
        parent[rootB] = rootA

    # The smaller tree is merged into the bigger tree
    elif heightB > heightA:
        parent[rootA] = rootB

    else:  # if heightA == heightB
        # Arbitrarily break the tie by choosing A to be the parent of B

        parent[rootB] = rootA
        parent[rootA] = -(heightA + 1)

    return parent


if __name__ == "__main__":
    main()
    # parent = InitializeSet(8)
    # print(Union(4, 5, parent))
    # print(Union(6, 7, parent))
    # print(Union(5, 7, parent))




