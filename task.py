filter_list=[]
check_list =  []
sortlist = []
final_strings = []

def main(filepath):
    try:
        lines = list(open(filepath, 'r'))
    except:
        print("path incorrect")
    else:
        lines.sort()
        for i in lines:
            x= i.split(' ')
            if x[0] != '\n' and x[0] not in check_list:
                temp_string = x[0]
                check_list.append(temp_string)
                filter_func(temp_string,lines)
    finally:
        for a in final_strings:
            ad = a.split('=')
            if min(sortlist) == int(ad[-1].strip()):
                output= "The shortest path here is \n"+ a
        return final_strings,sortlist,output
        

    
def filter_func(temp_s,lines):
    temp = []
    for n in lines:
        if temp_s in n:
            temp.append(str(n.strip()))
    
    if len(temp) != 0:
        filter_list.append(temp)
        test(temp,temp_s)
   
def test(list,s):
    tag1=[]
    tag2=[]
    for d in list:
        xs = d.split(' ')
        if xs[0] != s:
            tag1.append(xs)
        else:
            tag2.append(xs)
    for f in tag1:
        for de in tag2:
            sortlist.append(int(de[-1])+int(f[-1]))
            fis = f[0]+' -> '+ de[0]+' -> '+de[2]+' = '+str(int(de[-1])+int(f[-1]))
            final_strings.append(fis)






if __name__ == '__main__':
    filepath = '/home/farmer/Desktop/input.txt'
    final_list,sortlist1,final_output = main(filepath)
    print(final_output)
    print(" =====================")
    print ("The possible routes are:")
    print ('\n'.join(map(str, final_list)))
