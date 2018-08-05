def majority_vote(sequence):
  counter = 0
  element = None
  for candidate in sequence:
    if counter == 0:
      element = candidate
      counter = 1
    else:
      if candidate == element:
        counter += 1
      else:
        counter -= 1
  return element


print majority_vote("C C C A A B B".split())