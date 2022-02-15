def read():
    numbers = []
    with open( "./files/number.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)        
            

def write():
    names = ["Angel", "Ricardo", "Sanchez", "Zeferino","sánchez"]
    with open("./files/names.txt", "w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
            
def add():
    names2 = ["name2"]
    with open("./files/names.txt","a",encoding="utf-8") as f:
        for name in names2:
            f.write(name)
        
    
    

def run():
    read()
    write()
    add()


if __name__ == "__main__":
    run()
    
    