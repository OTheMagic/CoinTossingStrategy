# CoinTossingStrategy
This repository aims to solves a coin tossing problem with winning probability over 50%. The coin tossing problem is described as follows:

## Story version:
Professor has already flipped a fair coin 1000 times. Amy will be told the 1st, 3rd, 5th, etc, 999th, all the odd-numbered flip results and Bryan will be told the 2nd, 4th, 6th, etc, 1000th, all the even-numbered flip results when they go to Professor's office. Amy has to name an even number less than or equal to 1000 after knowing all the odd information, and Bryan has to name an odd number less than or equal to 999 after knowing all the even information. If the flip results of these two numbers are the same, Amy and Bryan will win. Note that Amy and Bryan cannot communicate any more after going to Professor's office, but Amy and Bryan could figure out a way before they go to the professor's office to increase their probability of winning. Could you propose a reasonable strategy for them?

## Analytical version:
1. A fair coin is tossed $n$, an even number, times.
2. Two people A and B are to guess the results. A only knows the results of odd number tossing and is to guess a random positive even number less than n, and B only knows the results of even number tossing and is to guess a random positive odd number less than n. If the odd number A guessed and the even number B guessed have the same coin tossing results, then A and B win, that is: if A guesses 6, and B guesses 5.
3. A and B cannot communicate, but they can come with a strategy before the game starts to achieve a high winning rate. What will be a good strategy that grant a winning rate over 50%? And what's the highest possible winning rate?

## Progress
So far, we have acheived a 2/3 winning rate with our function in python.
