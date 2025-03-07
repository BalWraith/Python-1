import os;os.system('cls')
for i in range(1,13):
    ## i = {0} (i = 1-12) 1 is the start num and 13 is the num it stops at so the last num printed is 12
    ## i ** 2 = {1} (i to the power of 2 is the num square)
    ## i ** 3 = {2} (i to the power of 3 is the num cubed )
    ## {0:2}(2 spaces) = the colon 2 is the FIELD WIDTH-(the amount of space it can take up)-
    ## {1:4}(4 spaces) = the colon 4 is the FIELD WIDTH-(the amount of space it can take up)-
    ## {2:4}(4 spaces) = the colon 4 is the FIELD WIDTH-(the amount of space it can take up)-
    print('No. {0:2} squared is {1:3} and cubed is {2:4}'.format(i ,i **2 ,i ** 3))


        ## OUTPUT with Field Width = 
    # No.  1 squared is   1 and cubed is    1
    # No.  2 squared is   4 and cubed is    8
    # No.  3 squared is   9 and cubed is   27
    # No.  4 squared is  16 and cubed is   64
    # No.  5 squared is  25 and cubed is  125
    # No.  6 squared is  36 and cubed is  216
    # No.  7 squared is  49 and cubed is  343
    # No.  8 squared is  64 and cubed is  512
    # No.  9 squared is  81 and cubed is  729
    # No. 10 squared is 100 and cubed is 1000
    # No. 11 squared is 121 and cubed is 1331
    # No. 12 squared is 144 and cubed is 1728

        ## OUTPUT without Field Width =
    # No. 1 squared is 1 and cubed is 1
    # No. 2 squared is 4 and cubed is 8
    # No. 3 squared is 9 and cubed is 27
    # No. 4 squared is 16 and cubed is 64
    # No. 5 squared is 25 and cubed is 125
    # No. 6 squared is 36 and cubed is 216
    # No. 7 squared is 49 and cubed is 343
    # No. 8 squared is 64 and cubed is 512
    # No. 9 squared is 81 and cubed is 729
    # No. 10 squared is 100 and cubed is 1000
    # No. 11 squared is 121 and cubed is 1331
    # No. 12 squared is 144 and cubed is 1728

print()
print("LEFT")

for left in range(1,13):
    ## {2:<4} makes the nums move to the left
    print('No. {0:2} squared is {1:<3} and cubed is {2:<4}'.format(left ,left **2 ,left ** 3))
 
    ## OUTPUT  =
    # No.  1 squared is 1   and cubed is 1   
    # No.  2 squared is 4   and cubed is 8   
    # No.  3 squared is 9   and cubed is 27  
    # No.  4 squared is 16  and cubed is 64  
    # No.  5 squared is 25  and cubed is 125 
    # No.  6 squared is 36  and cubed is 216 
    # No.  7 squared is 49  and cubed is 343 
    # No.  8 squared is 64  and cubed is 512 
    # No.  9 squared is 81  and cubed is 729 
    # No. 10 squared is 100 and cubed is 1000
    # No. 11 squared is 121 and cubed is 1331
    # No. 12 squared is 144 and cubed is 1728

print()
print("RIGHT")
for right in range(1,13):
    ## {2:>4} makes the nums move to the right
    print('No. {0:2} squared is {1:>3} and cubed is {2:>4}'.format(right ,right **2 ,right ** 3))

    ## OUTPUT =
    # RIGHT
    # No.  1 squared is   1 and cubed is    1
    # No.  2 squared is   4 and cubed is    8
    # No.  3 squared is   9 and cubed is   27
    # No.  4 squared is  16 and cubed is   64
    # No.  5 squared is  25 and cubed is  125
    # No.  6 squared is  36 and cubed is  216
    # No.  7 squared is  49 and cubed is  343
    # No.  8 squared is  64 and cubed is  512
    # No.  9 squared is  81 and cubed is  729
    # No. 10 squared is 100 and cubed is 1000
    # No. 11 squared is 121 and cubed is 1331
    # No. 12 squared is 144 and cubed is 1728

print()
print("CENTER")
for center in range(1,13):
    ## {2:^4} makes the nums move to the left
    print('No. {0:2} squared is {1:^3} and cubed is {2:^4}'.format(center ,center **2 ,center ** 3))

    ## OUTPUT =
    # CENTER
    # No.  1 squared is  1  and cubed is  1  
    # No.  2 squared is  4  and cubed is  8  
    # No.  3 squared is  9  and cubed is  27 
    # No.  4 squared is 16  and cubed is  64 
    # No.  5 squared is 25  and cubed is 125 
    # No.  6 squared is 36  and cubed is 216 
    # No.  7 squared is 49  and cubed is 343
    # No.  8 squared is 64  and cubed is 512
    # No.  9 squared is 81  and cubed is 729
    # No. 10 squared is 100 and cubed is 1000
    # No. 11 squared is 121 and cubed is 1331
    # No. 12 squared is 144 and cubed is 1728

print()

print("Pi is approximately {0:12}".format(22 / 7)) # default 15 after .
print("Pi is approximately {0:12f}".format(22 / 7)) # default float 6 after .
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

## OUTPUT =
# Pi is approximately 3.142857142857143
# Pi is approximately     3.142857
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately           3.14285714285714279370154144999105483293533325195312      
# Pi is approximately                     3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.142857142857142793701541449991054832935333251953125000     

















print('\n'*8)