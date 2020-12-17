#-*- encoding: utf-8 -*- 

file1 = open('./ck.txt', 'r')
file2 = open('./dz.txt', 'r')

try:
    text_line2 = file2.readline()
    list2 = text_line2.split()
    while True:
        text_line1 = file1.readline()
        if text_line1:
            list1 = text_line1.split()
            if len(list2) > 0 and list1[0] == list2[0]:
                print(" ".join(list2))
                text_line2 = file2.readline()
                list2 = text_line2.split()
            else:
                print(" ".join(list1))

            #print(list[0])
            #print(" ".join(list))
            #if len(list) == 9:
            #print(" ".join(list))
        else:
            break
finally:
    file1.close()
