"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i * 2):  # (i * 2 -1) + 1
        print("*", end=" ")
    print()
