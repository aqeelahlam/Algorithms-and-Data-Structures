"""
Author: Aqeel Ahlam Rauf
Date: 10/07/2021

Disjoint Set Data Stucture (Or Union-Find):
- Union - Joins two Subsets together
- Find - Returns the parent of an element found in the set.
- Reference: https://www.geeksforgeeks.org/union-find/

Not yet completed..
"""

def main():
    pass

def initializeSet(N):
    """
    This function is used to initialize the parent array used for the set
    :param N: N is the total number of Vertices
    :return: parent array of size N
    """
    parentArray = [-1] * N

    return parentArray

def find(vertex, parent):
    """
    This function is used to the find the root of a given node/vertex.
    The find function has been implemented using path splitting.
    :param vertex: The vertex
    :param parent: Parent Array
    :Time Complexity: O(1) Amortized
    :return: vertex if the input vertex is the root, else returns the root of given vertex
    """
    Parent = parent[vertex]

    # if the current Parent of the node is already the root, we return the vertex
    if Parent < 0:
        return vertex

    grandParent = parent[Parent]

    while grandParent >= 0:
        # Update vertex to be pointing at grandparent
        parent[vertex] = grandParent
        vertex = Parent

        # Update the parent & grandparent values
        Parent = parent[vertex]
        grandParent = parent[Parent]

    return Parent


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

if __name__ == '__main__':
    main()