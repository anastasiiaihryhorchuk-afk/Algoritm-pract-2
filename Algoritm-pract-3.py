import random

def generate_array(length, min_val, max_val):
  return [random.randint(min_val, max_val) for _ in range(length)]

def print_array(arr):
  formatted_elements = [
      f"[cell - {i},value - {val}]" for i, val in enumerate(arr)
  ]
  result = "{" + ",".join(formatted_elements) + "}"
  print(result)


def bubble_sort(arr, ascending=True):

  a = arr.copy()
  n = len(a)
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      condition = (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1])
      if condition:
        a[j], a[j + 1] = a[j + 1], a[j]
        swapped = True
    if not swapped:
      break
  return a

def insertion_sort(arr, ascending=True):
  a = arr.copy()
  for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and ((key < a[j]) if ascending else (key > a[j])):
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  return a


def selection_sort(arr, ascending=True):
  a = arr.copy()
  n = len(a)
  for i in range(n):
    extremum_idx = i
    for j in range(i + 1, n):
      if ascending:
        if a[j] < a[extremum_idx]:
          extremum_idx = j
      else:
        if a[j] > a[extremum_idx]:
          extremum_idx = j
    a[i], a[extremum_idx] = a[extremum_idx], a[i]
  return a

if __name__ == "__main__":
  my_array = generate_array(8, 1, 50)

  print("Початковий несортований масив:")
  print_array(my_array)
  print("\nBubble Sort:")
  print("Прямий порядок (true):")
  print_array(bubble_sort(my_array, True))
  print("Зворотний порядок (false):")
  print_array(bubble_sort(my_array, False))

  print("\nInsertion Sort:")
  print("Прямий порядок (true):")
  print_array(insertion_sort(my_array, True))
  print("Зворотний порядок (false):")
  print_array(insertion_sort(my_array, False))

  print("\nSelection Sort:")
  print("Прямий порядок (true):")
  print_array(selection_sort(my_array, True))
  print("Зворотний порядок (false):")
  print_array(selection_sort(my_array, False))