import re

def multi_div(text_file,modi,fact):
    if modi == "D":
        sign = "/"
    elif modi == "M":
        sign = "*"
         
    opened = open(text_file)
    red = opened.read()
    red2 = red.split("\n")
#red3 = red.split(" ")
#def 

    new=[]
    new2 = []
    for i in red2:
        new.append(i.split())
    
#print (new)

    for i in new:
    #for j in i:
        j =(i[-1:])
        k = str(j).strip("'[]'")
    #p = float(k)
        try:
            s = float(k)
            if modi == "D": 
                s = (s / int(fact))
                j = [i[:-1]]
                j.append(s)

                new2.append(j)
            elif modi == "M":
                s = (s * int(fact))
                j = [i[:-1]]
                j.append(s)

                new2.append(j)
                   
        except:
            new2.append(i)
    with open("output.txt",'w+') as f:
        for i in new2:
            i = str(i).strip("'[]',")
            i = str(i).replace("]","")
            i = str(i).replace(",","")
            i = str(i).replace("'","")
                
            f.write(i)
            f.write("\n")
    f.close

text_file = "p.txt"
modi = raw_input("Insert D is you want to Divide or Insert M is you want to multiply: ")
fact = raw_input("insert the factor by which you want to divde or multiply:")     
    
multi_div(text_file,modi,fact)

    
