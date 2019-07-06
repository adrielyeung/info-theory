# info-theory
(Course taken in autumn 2018)

The study of Information Theory aims to quantify information gained from a message, based on previous (prior) knowledge. It also considers the quality of the transmission of the channel. These are quantified using laws of probability. The few coding exercises demonstrate a few different concepts in Information Theory.

Programs written in Python 3, and contain the following exercises:
- PS2 (code): Calculate information gained as each letter of an English word is received, based on list of English words ```list_of_engwords.txt``` (manually adding 1-letter words "a" and "I").
- PS2 (plot): Cumulative information gain plot as each letter is revealed for all 15-letter English words.
- PS3 (Q1c, d): Kullback-Leibner (KL) divergence for (c) uniform vs binomial distribution (with *N* = 10 and *N* = 100, with *p* from 0 to 1; and (d) Poisson vs binomial.
- PS3 (Q5a): Plot of maximum code efficiency if equal length binary code used to transmit a message comprised of *N* possible symbols against *N*.
- PS4 (Q2b): For a Poisson channel, plot expected information gain per transmitted symbol as function of average number of photons to denote symbol "1".
- PS4 (Q2c): Similar plot but as function of probability of sending symbol "0".
- PS4 (Q2d): Difference between channel capacity and mutual information as function of average number of photons to denote symbol "1".
- PS4 (Q6c): Plot of probability of a majority decision being correct *P* as a function of number of repeats *K*.
- PS4 (Q7b): Minimum, maximum and mean Hamming distances between words with 2-20 letters (in CSV files), based on list of English words ```list_of_engwords.txt``` (manually adding 1-letter words "a" and "I")

## Acknowledgements
Credits to Dr. Daniel Mortlock for teaching the course and designing these tasks.
