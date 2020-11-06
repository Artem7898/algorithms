# Сортировка пузырьком.

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


random_list_of_nums = [6, 2, 1, 8, 23]
bubble_sort(random_list_of_nums)
print('Сортировка пузырьком:')
print(random_list_of_nums)
print('___________________')


# Сортировка выбором.

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


random_list_of_nums = [50, 8, 1, 25, 13]
selection_sort(random_list_of_nums)
print('Сортировка выбором:')
print(random_list_of_nums)
print('___________________')


# Сортировка вставками.

def insertion_sorf(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = item_to_insert


random_list_of_nums = [40, 7, 16, 31, 5]
insertion_sorf(random_list_of_nums)
print('Сортировка вставками:')
print(random_list_of_nums)
print('____________________')


# Приромидная сортировка.

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


random_list_of_nums = [12, 45, 62, 5, 31]
print('Пиромидная сортировка:')
print(random_list_of_nums)
print('____________________')


# Быстрая сортировка.

def quick(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = quick(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


random_list_of_nums = [45, 7, 1, 21, 87]
quick_sort(random_list_of_nums)
print('быстроя сортировка:')
print(random_list_of_nums)
print('____________________')


# Алгоритм Евклида - нахождение наибольшего общего делителя.

def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

a = gcd_rem_division(175, 200)
print('Алгоритм Евклида:')
print(a)
print('____________________')

