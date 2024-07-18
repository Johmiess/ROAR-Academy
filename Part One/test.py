# challenge 2
n = 4
layer = [1]; print(1)
prevLayer = layer 
new_layer = []
for x in range (1,n + 2):
    for totallayerlength in range(0,x):
        new_layer.insert(0,0)
    new_layer[0] = 1; new_layer[-1] = 1
    if len(new_layer) >= 2: 
        for y in range(1,len(new_layer) - 1):
            new_layer[y] = (prevLayer[y] + prevLayer[y-1])
        prevLayer = new_layer
    print(new_layer)
    new_layer = prevLayer
    new_layer = []
    