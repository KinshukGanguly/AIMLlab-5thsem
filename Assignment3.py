sorted_dict={}
sorted_dict2

dict1={10:"ten",12:"twelve",2:"two"}
lk=sorted(list(dict1.keys()))

print("Sorted keys=",lk)

for k in lk:
 sorted_dict[k]=dict1[k]

print("Ditionary sorted as per value=",sorted_dict)



