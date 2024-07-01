with open('c:/Users/mohalsha/Desktop/Python_training/file2.txt', 'a') as f:
    n = 0
    while n != "stop":
        n = input("Please enter text to write to the file, enter the word stop to when done. ")
        f.write(f"{n} \n")

