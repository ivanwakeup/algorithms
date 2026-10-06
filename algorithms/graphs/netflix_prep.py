def word_ladder_length(begin_word: str, end_word: str, word_list: list) -> int:
  hm = {}
  hm[begin_word] = []
  for item in word_list:
    hm[item] = []

  if begin_word and end_word not in hm:
    return 0

  for word in [*word_list, begin_word]:
    for i in range(len(word)):
      for char in [chr(x) for x in range(ord('a'), ord('z') + 1)]:
        swapped = str(word[:i] + char + word[i+1:])
        if swapped == word:
          continue
        if swapped in hm:
          hm[word].append(swapped)

  from collections import deque
  q = deque()
  q.append((begin_word, 1))
  visited = set(begin_word)
  while q:
    item = q.popleft()
    if item[0] == end_word:
      return item[1]

    neighbors = hm[item[0]]
    for word in neighbors:
      if word not in visited:
        q.append((word, item[1]+1))
        visited.add(word)


  return 0
