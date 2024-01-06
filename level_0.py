import json
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
with open('c:/hackathon_2024/level0.json') as f:
    data = json.load(f)

restaurants = data['restaurants']
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
for i in permutation:
    li.append(output_list[i])

li.append('r0')

output = {"v0": {"path":[f'{i}' for i in li]}}
with open('level0_output.json', 'w') as f:
    json.dump(output, f)
