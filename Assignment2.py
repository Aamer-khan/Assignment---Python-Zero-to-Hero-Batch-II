# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Rlvgrqd40Um_ifj5o_cCOATTjakOgCx

Day-2 Assignment Lottery Game
"""

word  = "hello coders"
# Worlds contains these characters 'h' or 'e' or 'o' or 'c' or 'd'
print("choose correct character of the word '",word,"' to win the lottery")
inpchar = input(" ")

if inpchar == word[0].lower() or inpchar == word[1].lower() or inpchar == word[4].lower() or inpchar == word[6].lower() or inpchar == word[8].lower():
    print("Congratulations!!! you have won the lottery")
else:
    print("Sorry, You didn't win the lottery!!! Try next time")