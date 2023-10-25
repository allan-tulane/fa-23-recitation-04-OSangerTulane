import random, time
import tabulate


def qsort(a, pivot_fn):
  if len(a) <= 1:
    return a

  pivot = pivot_fn(a)
  left = [x for x in a if x < pivot]
  middle = [x for x in a if x == pivot]
  right = [x for x in a if x > pivot]

  return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

def selection_sort_recursive(L):
  if (len(L) == 1):
      return(L)
  else:
      m = L.index(min(L))
      L[0], L[m] = L[m], L[0]
      return    selection_sort_recursive(L[1:])
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    def qsort_fixed_pivot(a):
        return qsort(a, sizes[a])
  
    def qsort_random_pivot(a):
        return qsort(a, sizes[a])
  
    def ssort(a):
        return selection_sort_recursive(a)
  
    result = []
  
    qsort_fixed_pivot = qsort_fixed_pivot(sizes[])
    qsort_random_pivot = qsort_random_pivot(random.choice)
    ssort = selection_sort_recursive()
  
    for size in sizes:
        mylist_random = list(range(size))
        random.shuffle(mylist_random)
  
        mylist_sorted = list(range(size))
  
        result.append([
            len(mylist_random),
            time_search(qsort_fixed_pivot, mylist_random),
            time_search(qsort_random_pivot, mylist_random),
            time_search(ssort, mylist_random),
            time_search(sorted, mylist_random),
            time_search(qsort_fixed_pivot, mylist_sorted),
            time_search(qsort_random_pivot, mylist_sorted),
            time_search(ssort, mylist_sorted),
            time_search(sorted, mylist_sorted)
        ])
    return result


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
result_random = compare_sort()
result_sorted = compare_sort()
result = compare_sort()
test_print()
