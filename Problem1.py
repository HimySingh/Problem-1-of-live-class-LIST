


l= [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"Sudh", "k2":"ineuron", "k3": "Kumar", 3:6, 7:8}, ["ineuron", "data science"]]
for i in l:
    if type(i)==list or type(i)== tuple or type(i)== dict or type(i)== set:
        for j in i:
            if j== int:
                print(j)