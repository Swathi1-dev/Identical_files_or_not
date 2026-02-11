def files(file1,file2):
    with open(file1,"r") as f1,open(file2,"r")as f2:
        content1=f1.read()
        content2=f2.read()
    
    if content1==content2:
        print("Files are identical")
    else:
        print("Files are not identical")
        
        
files("h1.txt","h2.txt")