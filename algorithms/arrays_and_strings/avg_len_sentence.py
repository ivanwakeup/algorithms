def avg_sentence_len(sentence):
    words = sentence.split(" ")
    total = 0
    for word in words:
        total += len(word)
    return total/len(words)


print(avg_sentence_len("this that thoseee"))