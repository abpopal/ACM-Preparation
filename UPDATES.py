def updates(module):
    first, second = module.split()
    firstArr = first.split(",")
    secondArr = second.split(",")
    arr = firstArr + secondArr
    res = [x[0] for x in arr]

    for i in res:
        if res.count(i) == 1:
            res.pop(res.index(i))

    final = []

    for i in arr:
        if arr.count(i) > 1:
            continue
        if i[0] in res:
            final.append(i)
    result = []
    for i in range(1, len(final), 2):
        result.append(sorted(final)[i])

    return ",".join(sorted(result))

s = """a.v1,b.v2.0.1,c.v1.1,d.v0.0,e.v5.0.9,f.v0.0.0.20191010101010  
a.v1,c.v1.1.0.20191010101010,e.v5.1,f.v0.0.0.20191010101011 
"""
print(updates(s))



