"""
Author: Aqeel Ahlam Rauf
Date: 10/07/2021

Not yet completed..
"""
def main():
    test = [5, 3, 1, 8, 10, 2]
    SelectionSort(test)



def SelectionSort(array):
    """[summary]

    Args:
        array ([type]): [description]
    """

    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        swap(i, minimum, array)

    print(array)


def swap(positionA, positionB, array):
    (array[positionA], array[positionB]) = (array[positionB], array[positionA])

   


if __name__ == '__main__':
    main()