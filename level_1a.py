import json
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

with open('level1a.json') as f:
    data = json.load(f)

neighborhoods = data['neighbourhoods']
output_list = []
l2=[]

for neighborhood_name, data in neighborhoods.items():
    distances = data['distances']
    output_list.append(f"{neighborhood_name}")
    l2.append(distances)

l2=np.array(l2)

li=["r0"]

permutation, distance = solve_tsp_dynamic_programming(l2)

data = {"n0": 70,"n1": 70,"n2": 90,"n3": 50,"n4": 70,"n5": 90,"n6": 110,"n7": 70,"n8": 110,"n9": 70,"n10": 70,"n11": 110,"n12": 110,"n13": 90,"n14": 50,"n15": 90,"n16": 110,"n17": 90,"n18": 70,"n19": 110}

print(permutation)
lii=["r0"]
for i in permutation:
    lii.append(output_list[i])

li = []
temp = []
current_sum = 0

for element in lii:
    if element in data and current_sum + data[element] <= 600:
        temp.append(element)
        current_sum += data[element]
    else:
        li.append(temp)
        temp = [element] if element in data and data[element] <= 600 else []
        current_sum = data[element] if element in data and data[element] <= 600 else 0
li.append(temp)

result = [sublist for sublist in li if sublist]

output_dict = {"v0": {}}

for i, path in enumerate(result, start=1):
    formatted_path = ["r0"] + path + ["r0"]
    output_dict["v0"]["path" + str(i)] = formatted_path

with open('level1a_output.json', 'w') as f:
    json.dump(output_dict, f, indent=2)

