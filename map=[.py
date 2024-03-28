map={
    5: [3,7],
    3:[2,4],
    7:[8],
    2:[],
    4:[8],
    8:[]#goal
}
def bfs(start,goal):
    box=[start]
    expored_set=[]

    while box !=[]:
        node=box.pop(0)
        expored_set.append(node)
        if (node==goal):
            print("fundet");
            return
        #lerada chayald war agretawa    
        value=map.get(node,[])
        for child in value:
            if child not in box and child not in expored_set:
                box.append(child)
                print("try")
bfs(5,8)








map={
    5: [3,7],
    3:[2,4],
    7:[8],
    2:[],
    4:[8],
    8:[]#goal
}
def dfs(start,goal):
    box=[start]
    expored_set=[]

    while box !=[]:
        node=box.pop()
        expored_set.append(node)
        if (node==goal):
            print("fundet");
            return
        #lerada chayald war agretawa    
        value=reversed (map.get(node,[]))
        for child in value:
            if child not in box and child not in expored_set:
                box.append(child)
                print("try")
bfs(5,8)
print("slawwww")

print("hello")





























