import random



def jumble(word):
    # sample() method shuffling the characters of the word
    random_word = random.sample(word, len(word))
 
    # join() method join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled


ip_word=input("enter any text to jumble: ") # enter some word 
print(len(ip_word))
word_arry=[]
for i in range(10):
    print(jumble(ip_word))


