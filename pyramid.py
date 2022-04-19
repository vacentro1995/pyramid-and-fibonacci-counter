def pattern():
    
    k = 0
    
    num = int(input("Enter number of rows: "))
    
    for rows in range (0, num):
        for space in range (0, num-rows-1):
            print(end = " ")
            
        while k <= num:
            if (k % 2 != 0):
                print("*", end = " ")
                
                k += 1
            
        print()
        
pattern()