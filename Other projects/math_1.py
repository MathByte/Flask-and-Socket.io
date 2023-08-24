
xt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
yt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = []
for x in xt:
    for y in yt:
        for z in zt:
            if x != y and x != z and z != y:
                if x + y + z == 24:
                    a = [x, y, z]
                    if (any(a == i for i in ans)):                        
                        pass
                    else:
                        ans.append(tuple(sorted((x, y, z))))






print(ans )
"""
for x in range (1, 10):
    for y in range (1, 10):
        for z in range (1, 10):
            for t in range (1, 10):
                if x != y and x != z and z != y and x != t and y != t and z != t:
                    if x + y + z + t == 19:
                        print(x,y,z, t)

"""