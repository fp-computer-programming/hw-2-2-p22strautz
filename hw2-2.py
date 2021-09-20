# Author: SCT (ADMG) 9/20/21

free_throws = 4
two_pointers = 6
three_pointers = 5

score = (free_throws) + (two_pointers * 2) + (three_pointers * 3)
score = str(score)

statement = "The player scored "
statement_2 = " points in the game."

print(statement+score+statement_2)
