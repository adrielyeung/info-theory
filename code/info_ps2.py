import numpy as np
import random as rd
import matplotlib.pyplot as pl

# Load text file
file = open("list_of_engwords.txt", "r")
words = file.read().split('\n')

file.close()

# Task 1

# Manually add the two one-letter words
words.append("a")
words.append("i")

# Define information gained for each letter revealed as log_2 (N_b - N_m),
# where N_b and N_m are the number of words remaining before and after
# revealing the letter, given that all words are equally probable a priori.

def info_gain(word_pick):
    word_pick_list = list(word_pick)
    
    # Stores remaining words
    rem_words = words.copy()
    #rem_words.remove(word_pick)
    #print("Remaining num of words: ", len(rem_words))
    
    info_total = 0 # bits
    info_total_all = [0]
    
    for i in range(len(word_pick_list)):
        #print("Letter {0}: ".format(i+1), word_pick_list[i])
        
        no_rem_words_bef = len(rem_words)
        
        # Find remaning number of words after revealing letter i+1
        rem_word_ind = 0
        while rem_word_ind < len(rem_words):
            if i < len(list(rem_words[rem_word_ind])):
                # So that the word is longer than the one picked
                if list(rem_words[rem_word_ind])[i] == word_pick_list[i]:
                    # Same letter, remain
                    rem_word_ind += 1
                    continue
                else:
                    rem_words.remove(rem_words[rem_word_ind])
            else:
                rem_words.remove(rem_words[rem_word_ind])
        
        #print("Remaining num of words: ", len(rem_words))
        
        # Calculate info gained
        info_total += np.log2(no_rem_words_bef / len(rem_words))
        info_total_all.append(info_total)
        #print("Info gained from revealing letter {0}: ".format(i+1),
        #      np.log2(no_rem_words_bef / len(rem_words)), " bits")
        #print("Total amount of info gained after letter {0}: ".format(i+1),
        #      info_total, " bits")
        #print("Amount of info not revealed after letter {0}: ".format(i+1),
        #      np.log2(len(words)) - info_total, " bits")
    return info_total_all
        
# Part (d): Try wombat
#info_gain("wombat")

# Pick a word
#pick = rd.randint(0, len(words)-1)
#word_pick_rd = "versifying" # words[pick]
#info_gain(word_pick_rd)

# Part (e): Plot cumulative info gained
# Gather all words with 15 letters
fifteen_let = []
for word in words:
    if len(list(word)) == 15:
        fifteen_let.append(word)

pl.figure()
for wd in fifteen_let:
    cum_info = info_gain(wd)
    pl.plot(np.arange(0, 16), cum_info)

# Line of info gained revealing the word altogether, as comparison
pl.plot([0, 15.5], [np.log2(len(words)), np.log2(len(words))], "k--")
pl.xlabel("Letter revealed")
pl.ylabel("Cumulative information gained / bits")
pl.xticks(np.arange(0, 16))
pl.xlim(left=0)
pl.ylim(bottom=0)
pl.grid()
    
