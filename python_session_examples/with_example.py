
with open('d:/temp/sample.txt', 'r', encoding='utf-8') as file_o:
    for line in file_o:
        print(line.strip())


file_o = open('d:/temp/sample.txt', 'r', encoding='utf-8')
for line in file_o:
    print(line.strip())
file_o.close()