with open("Python/FileFolder/text_file.txt", "r") as file:
    for line in file.readlines():
        print(line, end = '')
 
 
    n=29
    for i in range (1,n):
        k=n-1
        print (k, end=" ")
        for j in range (i):
            print (" ", end=" ")
        for j in range (n-1):
            print (k, end=" ")
            k=k-1
        if i < (n-1):
            for j in range (n-i-2):
                print (" ", end =" ")
            for j in range (i+1):
                k=k+1
                print (k, end =" ")
    print ()