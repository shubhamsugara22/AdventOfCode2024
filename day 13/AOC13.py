import numpy as np
import re
from pathlib import Path

with open('claw.txt') as f:
    scenarios = f.read().split('\n\n')
    
# def parse(scenario):
#     output = {}
#     a,b,prize = scenario.splitlines()
#     output['A'] = [int(item.split('+')[1]) for item in a.split(':')[1].split(', ')]
#     output['B'] = [int(item.split('+')[1]) for item in b.split(':')[1].split(', ')]
#     output['Prize'] = [int(item.split('=')[1]) for item in prize.split(':')[1].split(', ')]
#     return output

# scenarios = [parse(scenario) for scenario in scenarios]

    
def parse2(scenario):
    output = {}
    a,b,prize = scenario.splitlines()
    output['A'] = [int(item.split('+')[1]) for item in a.split(':')[1].split(', ')]
    output['B'] = [int(item.split('+')[1]) for item in b.split(':')[1].split(', ')]
    output['Prize'] = [10000000000000+int(item.split('=')[1]) for item in prize.split(':')[1].split(', ')]
    return output

scenarios = [parse2(scenario) for scenario in scenarios]

def solve2(scenario):
    ax,ay = scenario['A']
    bx,by = scenario['B']
    tx,ty = scenario['Prize']
    b = (tx*ay-ty*ax)//(ay*bx-by*ax)
    a = (tx*by-ty*bx)//(by*ax-bx*ay)
    if ax*a+bx*b==tx and ay*a+by*b==ty:
        return 3*a+b
    else:
        return 0
                
answer2 = sum(solve2(scenario) for scenario in scenarios)
print(answer2)


# def solve(scenario):
#     ax,ay = scenario['A']
#     bx,by = scenario['B']
#     tx,ty = scenario['Prize']
#     outputs = []
#     for a in range(100):
#         for b in range(100):
#             if ax*a+bx*b==tx and ay*a+by*b==ty:
#                 outputs.append(3*a+b)
#     if not outputs:
#         return 0
#     else:
#         return min(outputs)

                
# answer = sum(solve(scenario) for scenario in scenarios)
# print(answer)
