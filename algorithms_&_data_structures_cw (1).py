# -*- coding: utf-8 -*-
def minimum_value(a_list):
    #get first value in list
    smallest = a_list[0]
    smallest_index = 0

    for i in range(1, len(a_list)):
        if(a_list[i] < smallest):
            smallest = a_list[i]
            smallest_index = i
    return smallest_index

def selection_sort(old_list):
    # new list
    new_list = []
    for i in range(len(old_list)):
        smallest_index = find_smallest(old_list)
        new_list.append(old_list.pop(smallest_index))
        
    return new_list

test = [1,3,-8,0,10,1,5]
sorted_test = selection_sort(test)
print(sorted_test)

def evaluate_func(func): 
    list_lengths = [10**i for i in range(1, 5)]
    times_taken = []

    for list_length in list_lengths:
        my_list = list(range(list_length))
        # Same seed for list shuffling to have same testing lists for different algorithms
        random.Random(2).shuffle(my_list)
        # special case for quick_sort algorithm
        if func.__name__ == 'quick_sort':
            low = 0
            high = list_length - 1
            start = time.time()
            func(my_list, low, high)
            end = time.time()
            times_taken.append(end - start)
        else:
            start = time.time()
            ordered_list = func(my_list)
            end = time.time()
            times_taken.append(end - start)

    plt.figure(figsize = (10,8))
    plt.scatter([math.log10(i) for i in list_lengths], [math.log10(i*1000+1) for i in times_taken], color = 'blue')
    plt.title(func.__name__)
    plt.xlabel('Powers of 10 of list lengths')
    plt.ylabel('Powers of 10 of times taken (ms)')
    plt.xticks([math.log10(i) for i in list_lengths])
    plt.yticks([math.log10(i*1000 + 1) for i in times_taken], size = 'medium')
    plt.show()

evaluate_func(selection_sort)