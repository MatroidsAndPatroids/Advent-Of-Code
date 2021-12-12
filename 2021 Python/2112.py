import utility # my own utility.py file



def bfs(edges, node, seen):
    if node.upper() != node:
        if node in seen:
            return 0
        else:
            seen.append(node)
    
    #print('bfs', node, seen)
    if node == 'end':
        return 1

    pathes = 0
    for neig in edges[node]:
        pathes += bfs(edges, neig, seen.copy())
    return pathes

def bfs2(edges, node, seen, revisit):
    if node == 'start' and not seen:
        seen.append(node)
    elif node.upper() != node:
        if node == 'start':
            return 0
        if node in seen:
            if revisit:
                return 0
            else:
                revisit = True
        else:
            seen.append(node)
    
    #print('bfs2', node, seen, revisit)
    if node == 'end':
        return 1

    pathes = 0
    for neig in edges[node]:
        pathes += bfs2(edges, neig, seen.copy(), revisit)
    return pathes
        
# All possible paths between 'start' and 'end'. May visit big caves more than once.
def numberOfAllPaths(cavemap, part2=False):
    # Parse
    edges = {}
    for line in cavemap:
        fr, to = line.split('-')
        if fr in edges.keys():
            edges[fr].append(to)
        else:
            edges[fr] = [to]
        if to in edges.keys():
            edges[to].append(fr)
        else:
            edges[to] = [fr]
    #print(edges)
    
    # BFS
    pathes = bfs2(edges, 'start', [], False) if part2 else bfs(edges, 'start', [])

    # Return
    value = pathes
    print(value)
    return value

# Verify test cases
smallExample = '''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''.strip().split('\n')
smallExample2 = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''.strip().split('\n')
smallExample3 = '''
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''.strip().split('\n')
assert numberOfAllPaths(smallExample) == 10
assert numberOfAllPaths(smallExample2) == 19
assert numberOfAllPaths(smallExample3) == 226
assert numberOfAllPaths(smallExample, part2=True) == 36
assert numberOfAllPaths(smallExample2, part2=True) == 103
assert numberOfAllPaths(smallExample3, part2=True) == 3509

# Display info message
print("\nGive a list of cave connections:")
cavemap = utility.readInputList()

# Display results
print (f"{numberOfAllPaths(cavemap) = }")
print (f"{numberOfAllPaths(cavemap, part2=True) = }")