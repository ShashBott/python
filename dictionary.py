list1 = ['name', 'age', 'weight']
list2 = ["shashwat",20, 60]
dict = dict(zip(list1, list2))
print(dict)


dict1={1: 'one', 2: 'two', 3: 'three'}
dict2={4: 'four', 5: 'five', 6: 'six'}
dict1.update(dict2)
print("\n",dict1)

name = ['Shashwat', 'Modiji']
defaults = {"designation": 'Prime Minister', "salary": 120000}
result = dict.fromkeys(name, defaults)
print("\n",result)

sDict = {"name": "Shashwat","age":20, "salary": 120000, "city": "Lucknow" }
keys = ["name", "salary"]
nDict = {k: sDict[k] for k in keys}
print("\n",nDict)

for k in keys:
      sDict.pop(k)
print("\n",sDict)


ssDict = {"name": "Shashwat","age":20, "salary": 120000}
ssDict["UID"] = ssDict.pop("name")
print("\n",ssDict)


sample_dict ={
    'emp1': {'name': 'shashwat', 'salary': 120000},
    'emp2': {'name': 'modiji', 'salary': 120000}
}
print("\nbefore",sample_dict)
sample_dict['emp1']['salary'] =0
print("after removal",sample_dict)


