
# [1, 1, 2, 2, 4, 5] -> [1, 2, 4, 5]

def remove_reps(old_list):
  prev = None
  new_list = []
  for item in old_list:
    if item != prev:
      new_list.append(item)
      prev = item
  return new_list


if __name__ == "__main__":
  print(remove_reps([1, 1, 2, 2, 4, 5]))
  print(list(set([1, 1, 2, 2, 4, 5])))