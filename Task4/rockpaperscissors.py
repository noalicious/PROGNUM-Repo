#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 4.3
import numpy as np

#input computer and input of player
you = input("Enter a choice (type R for rock, P for paper, S scissors): ")

computer = np.array(["R", "P", "S"])
indx = np.random.randint(0, 2, 1)
cpu=computer[indx]
print("computer plays", computer[indx])


#results
if you == cpu:
    print(f"Both players selected {you}. It's a tie!")
elif you == "R":
    if cpu == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif you == "P":
    if cpu == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif you == "S":
    if cpu == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

