#program for selection sort in a list

lst = []
num = int(input('How many numbers: '))

for n in range(num):

    numbers = int(input('Enter number '))
    lst.append(numbers)

def selection_sort(alist):

    for i in range(0, len(lst) - 1):
        smallest = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]

lst = input('Enter the list of numbers: ').split()
lst = [int(x) for x in lst]
selection_sort(alist)
print('Sorted list: ', end='')
print(lst)
