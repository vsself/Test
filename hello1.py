

def draw(num):
    length = num
    blank = '-'
    star = '*'
    str1 = ''
    med = (num - 1)/2
    for i in range(num):
        list1 = []
        flag =  True
        for j in range(num):
            if abs(med - j) <= abs(med - abs(med - i)):
                if flag:
                    list1.append(star)
                    flag = False
                else:
                    list1.append(blank)
                    flag = True                
            else:
                list1.append(blank)
        str1 = str1 +''.join(list1) + '\n'
    print str1
        #print '\n'
        
 
draw(7)    