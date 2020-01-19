for x in range(20):
    file = open("demo.txt", 'ra')
    #w means
    file.write("\nthis is third line")
    print(file.read())
    file.close()