# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as pl
import math

#%% Q2

# Expected info gain - mutual info
def mut_info(p0, lam1):
    return -(p0*np.log2(p0+(1-p0)*np.exp(-lam1)) + (1-p0)*np.exp(-lam1)*(np.log2(np.exp(1))*lam1 + np.log2(p0 + (1-p0)*np.exp(-lam1))) + (1-p0)*(1-np.exp(-lam1))*np.log2(1-p0))

#%% Q2(b)

p0=0.5

Lam = np.linspace(0, 20, 1000)
I_arr = []

for lam in Lam:
    I_arr.append(mut_info(p0, lam))

fig1, ax1 = pl.subplots(1, 1)
ax1.plot(Lam, I_arr, 'b-')
ax1.set_xlabel(r"$\lambda_1$")
ax1.set_ylabel(r"$I(X, Y|K)$ / bits")
ax1.set_xticks(np.arange(0, 21, 2))

#%% Q2(c)

p0 = np.linspace(0, 1, 1000)

Lam = [1, 10, 100]

fig2, ax2 = pl.subplots(3, 1)

for lam_ind in range(len(Lam)):
    I_arr = []
    for p in p0:
        I_arr.append(mut_info(p, Lam[lam_ind]))
    
    ax2[lam_ind].plot(p0, I_arr, 'b-', label=r"$\lambda_1={0}$".format(Lam[lam_ind]))
    ax2[lam_ind].set_ylabel(r"$I(X, Y|K)$ / bits")
    ax2[lam_ind].set_xticks(np.arange(0, 1.1, 0.1))
    ax2[lam_ind].legend()

ax2[2].set_xlabel(r"$p_0$")

#%% Q2(d)

Lam = np.linspace(0, 20, 500)
p0 = np.linspace(0, 0.99, 500)
I_arr = []
cap = []

for lam in Lam:
    I_arr.append(mut_info(0.5, lam))
    I_testp = []
    
    # Calculate channel capacity
    for p in p0:
        I_testp.append(mut_info(p, lam))
    
    I_max_ind = np.argmax(I_testp)
    cap.append(mut_info(p0[I_max_ind], lam))
    
fig5, ax5 = pl.subplots(1, 1)
ax5.plot(Lam, np.array(cap) - np.array(I_arr), 'b-', label="Channel capacity - Mutual info")
ax5.set_xlabel(r"$\lambda_1$")
ax5.set_ylabel(r"$I(X, Y|K)$ difference / bits")
ax5.set_xticks(np.arange(0, 21, 2))
ax5.legend()

#%% Q6(c)
    
def majority(p, K):
    prob_total = 0
    for k in np.arange((K+1)/2, K+1):
        prob_total += math.factorial(K)/(math.factorial(k)*math.factorial(K-k))*(1-p)**k*p**(K-k)
    return prob_total

K_arr = np.arange(1, 16, 2)
PP = [0.01, 0.1, 0.4]

fig3, ax3 = pl.subplots(3, 1)

for pp in range(len(PP)):
    pt_arr = []
    for KK in K_arr:
        pt_arr.append(majority(PP[pp], KK))
    
    ax3[pp].plot(K_arr, pt_arr, 'b-', label=r"$P = {0}$".format(PP[pp]))
    ax3[pp].set_xticks(np.arange(0, 16))
    ax3[pp].set_ylim([0, 1])
    ax3[pp].set_ylabel(r"$P$ (correct maj dec)")
    ax3[pp].legend()

ax3[2].set_xlabel(r"$K$")

#%% Q7

import os
os.chdir("C:/Users/Adriel/Documents/School/Info_Theory")

# Load text file
file = open("list_of_engwords.txt", "r")
words = file.read().split('\n')

file.close()

# Manually add the two one-letter words
words.append("a")
words.append("i")

# Find length of each word
length_words = []
for word in words:
    length_words.append(len(word))

length_words = np.array(length_words)

# Create list of corresponding index of each letter
alphabets = list("abcdefghijklmnopqrstuvwxyz")

#%% Q7(a) Eng alphabets
 
dot = np.array([1,3,2,2,1,3,1,4,2,1,1,3,0,1,0,2,1,2,3,0,2,3,1,2,1,2])
dash = np.array([1,1,2,1,0,1,2,0,0,3,2,1,2,1,3,2,3,1,0,1,1,1,2,2,3,2])

length = dot+dash

# 0 = dot, 1 = dash
morse = ["01", "1000", "1010", "100", "0", "0010", "110", "0000", "00", "0111", "101", "0100", "11", "10", "111", "0110", "1101", "010", "000", "1", "001", "0001", "011", "1001", "1011", "1100"]

# Separate codewords of different lengths into different cases
for le in np.arange(1, 5):
    print("{0}-symbol".format(le))
    req = np.where(length==le)[0]
    ham = []
    pos = [[],[]]
    
    for i in range(len(req)):
        for j in range(i+1, len(req)):
            diff = 0
            for k in range(le):
                if list(morse[req[i]])[k] != list(morse[req[j]])[k]:
                    diff += 1
            
            ham.append(diff)
            pos[0].append(req[i])
            pos[1].append(req[j])
    
    ham = np.array(ham) # to find max, min and mean
    
    print("Min Hamming distance = {0}, between letters {1} and {2}.".format(np.min(ham), alphabets[pos[0][np.argmin(ham)]], alphabets[pos[1][np.argmin(ham)]]))
    print("Max Hamming distance = {0}, between letters {1} and {2}.".format(np.max(ham), alphabets[pos[0][np.argmax(ham)]], alphabets[pos[1][np.argmax(ham)]]))
    print("Mean Hamming distance = {0}.".format(np.mean(ham)))

#%% Q7(a) Numbers

morse_no = ["11111", "01111", "00111", "00011", "00001", "00000", "10000", "11000", "11100", "11110"] # for ease of use put codeword for zero at the beginning

ham_no = []
pos_no = [[],[]]

for i in range(len(morse_no)):
    for j in range(i+1, len(morse_no)):
        diff = 0
        for k in range(5):
            if list(morse_no[i])[k] != list(morse_no[j])[k]:
                diff += 1
        
        ham_no.append(diff)
        pos_no[0].append(i)
        pos_no[1].append(j)

ham_no = np.array(ham_no) # to find max, min and mean

print("Min Hamming distance = {0}, between numbers {1} and {2}.".format(np.min(ham_no), pos_no[0][np.argmin(ham_no)], pos_no[1][np.argmin(ham_no)]))
print("Max Hamming distance = {0}, between numbers {1} and {2}.".format(np.max(ham_no), pos_no[0][np.argmax(ham_no)], pos_no[1][np.argmax(ham_no)]))
print("Mean Hamming distance = {0}.".format(np.mean(ham_no)))

#%% Q7(b)
min_ham = []
max_ham = []
mean_ham = []

for le in np.arange(2, 21):
    print("{0}-letter word".format(le))
    req = np.where(length_words==le)[0]
    ham = []
    
    for i in range(len(req)):
        for j in range(i+1, len(req)):
            diff = 0
            list_i = list(words[req[i]])
            list_j = list(words[req[j]])
            
            # Letter-by-letter comparison
            for let_ind in range(le):
                if list_i[let_ind] == list_j[let_ind]:
                    continue
                else:
                    diff += 1
            
            ham.append(diff)
    
    ham = np.array(ham) # to find max, min and mean
    
    print("Min Hamming distance = {0}.".format(np.min(ham)))
    min_ham = np.append(min_ham, np.min(ham))
    #min_ham.append(np.min(ham))
    print("Max Hamming distance = {0}.".format(np.max(ham)))
    max_ham = np.append(max_ham, np.max(ham))
    #max_ham.append(np.max(ham))
    print("Mean Hamming distance = {0}.".format(np.mean(ham)))
    mean_ham = np.append(mean_ham, np.mean(ham))
    #mean_ham.append(np.mean(ham))


#%% Q7(b) Plot
fig4, ax4 = pl.subplots(1,1)
ax4.plot(np.arange(2, 21), min_ham, 'r-', label="Min Hamming dist")
ax4.plot(np.arange(2, 21), max_ham, 'g-', label="Max Hamming dist")
ax4.plot(np.arange(2, 21), mean_ham, 'b-', label="Mean Hamming dist")
ax4.set_xlabel("Length of word")
ax4.set_ylabel("Hamming distance")
ax4.set_xticks(np.arange(0, 21, 2))
ax4.set_yticks(np.arange(0, 21, 2))
ax4.legend()

#%% Save data
np.savetxt("Min_Ham.csv", min_ham, delimiter=',')
np.savetxt("Max_Ham.csv", max_ham, delimiter=',')
np.savetxt("Mean_Ham.csv", mean_ham, delimiter=',')
