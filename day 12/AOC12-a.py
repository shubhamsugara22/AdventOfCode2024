data = open("perem.txt").read()

data = data.split()
H, W = len(data), len(data[0])

grid = {(y,x):c for y,line in enumerate(data) for x,c in enumerate(line)}

###############################################################################

diffs = [(-1,0),(0,1),(1,0),(0,-1)]
def evaluate(sy, sx):
    region = set()
    area, perimeter = 0, 0
    border = [(sy,sx)]
    while border:
        y, x = border.pop()
        if (y,x) in region: continue
        region.add((y,x))
        area += 1
        for dy, dx in diffs:
            ny, nx = y+dy, x+dx
            if grid.get((ny,nx))==grid[y,x]:
                border.append((ny,nx))
            else:
                perimeter+=1
    return area, perimeter, region

###############################################################################

def find_sides(region):
    corners, double = set(), 0
    xs, ys = set(x for y,x in region), set(y for y,x in region)
    for y in range(min(ys), max(ys)+2):
        for x in range(min(xs), max(xs)+2):
            index = sum(((y+dy,x+dx) in region)*sf 
                            for dx,dy,sf in [(-1,-1,1),(-1,0,2),(0,-1,4),(0,0,8)])
            if index not in [0,3,5,10,12,15]: corners.add((y,x))
            if index in [6, 9]: double += 1
    return len(corners)+double
    
###############################################################################

seen = set()
p1, p2 = 0, 0
for (y,x) in grid:
    if (y,x) not in seen:
        area, perimeter, region = evaluate(y,x)
        seen.update(region)
        p1 += area*perimeter
        p2 += area*find_sides(region)
print("Part 1:", p1)
print("Part 2:", p2)

