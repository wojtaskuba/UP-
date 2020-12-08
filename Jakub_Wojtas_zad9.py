try:
    with open("plik1.txt", 'r') as f1:
        with open("plik2.txt",'w') as f2:
            for line in f1:
                f2.write(line)
except:
    print("Nastąpił wyjątek.")