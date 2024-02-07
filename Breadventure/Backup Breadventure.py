import random
graphCode = []
graphCode.clear()
locksLeft = 0
graphCode.append(random.randint(1, 3))
if graphCode[0] == 1:
    graphCode.append(random.randint(3, 5))
    locksLeft = graphCode[1]
    prob = random.randint(0, 3)
    if prob == 0:
        graphCode.append(0)
    else:
        graphCode.append(1)
    locksLeft -= graphCode[2]
    if graphCode[1] == 3:
        if graphCode[2] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2] == 1:
            graphCode.append(random.randint(0, 1))
    else:
        if graphCode[2] == 0:
            graphCode.append(random.randint(1, 3))
        elif graphCode[2] == 1:
            graphCode.append(random.randint(0, 2))
    locksLeft -= graphCode[3]
    if graphCode[2] == 0:
        if graphCode[3] < locksLeft:
            for i in range(random.randint(1, graphCode[3])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
        else:
            for i in range(random.randint(1, locksLeft)):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        for i in range(graphCode[3] - random.randint(0, graphCode[3])):
            graphCode.append(1)
            graphCode.append(0)
            locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
elif graphCode[0] == 2:
    graphCode.append(random.randint(2, 4))
    locksLeft = graphCode[1]
    prob = random.randint(0, 3)
    if prob == 0:
        graphCode.append(0)
    else:
        graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[2]
    if graphCode[1] == 4:
        if graphCode[2] == 0:
            graphCode.append(random.randint(1, 3))
        elif graphCode[2] == 1:
            graphCode.append(random.randint(0, 2))
    else:
        if graphCode[2] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2] == 1:
            graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[3]
    if graphCode[2] == 0:
        if not prob == 0 and locksLeft > 0:
            if graphCode[3] < locksLeft:
                for i in range(random.randint(1, graphCode[3])):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
            else:
                for i in range(random.randint(1, locksLeft)):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        if not prob == 0 and locksLeft > 0:
            for i in range(graphCode[3] - random.randint(0, graphCode[3])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
    startOfLayer2 = len(graphCode) - 1
    graphCode.append(random.randint(2, 4))
    locksLeft = graphCode[1 + startOfLayer2]
    graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[2 + startOfLayer2]
    if graphCode[1 + startOfLayer2] == 4:
        if graphCode[2 + startOfLayer2] == 0:
            graphCode.append(random.randint(1, 3))
        elif graphCode[2 + startOfLayer2] == 1:
            graphCode.append(random.randint(0, 2))
    else:
        if graphCode[2 + startOfLayer2] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2 + startOfLayer2] == 1:
            graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[3 + startOfLayer2]
    if graphCode[2 + startOfLayer2] == 0:
        if locksLeft > 0:
            if graphCode[3 + startOfLayer2] < locksLeft:
                for i in range(random.randint(1, graphCode[3 + startOfLayer2])):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
            else:
                for i in range(random.randint(1, locksLeft)):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        if locksLeft > 0:
            for i in range(graphCode[3 + startOfLayer2] - random.randint(0, graphCode[3 + startOfLayer2])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
elif graphCode[0] == 3:
    graphCode.append(random.randint(1, 3))
    locksLeft = graphCode[1]
    prob = random.randint(0, 3)
    if prob == 0:
        graphCode.append(random.randint(0, 1))
    else:
        graphCode.append(0)
    locksLeft -= graphCode[2]
    if graphCode[1] == 1:
        if graphCode[2] == 0:
            graphCode.append(1)
        elif graphCode[2] == 1:
            graphCode.append(0)
    else:
        if graphCode[2] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2] == 1:
            graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[3]
    if graphCode[2] == 0:
        if prob == 0 and locksLeft > 0:
            if graphCode[3] < locksLeft:
                for i in range(random.randint(1, graphCode[3])):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
            else:
                for i in range(random.randint(1, locksLeft)):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        if prob == 0 and locksLeft > 0:
            for i in range(graphCode[3] - random.randint(0, graphCode[3])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
    startOfLayer2 = len(graphCode) - 1
    graphCode.append(random.randint(2, 4))
    locksLeft = graphCode[1 + startOfLayer2]
    prob = random.randint(0, 3)
    if prob == 0:
        graphCode.append(0)
    else:
        graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[2 + startOfLayer2]
    if graphCode[1 + startOfLayer2] == 1:
        if graphCode[2 + startOfLayer2] == 0:
            graphCode.append(1)
        elif graphCode[2 + startOfLayer2] == 1:
            graphCode.append(0)
    else:
        if graphCode[2 + startOfLayer2] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2 + startOfLayer2] == 1:
            graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[3 + startOfLayer2]
    if graphCode[2 + startOfLayer2] == 0:
        if not prob == 0 and locksLeft > 0:
            if graphCode[3 + startOfLayer2] < locksLeft:
                for i in range(random.randint(1, graphCode[3 + startOfLayer2])):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
            else:
                for i in range(random.randint(1, locksLeft)):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        if not prob == 0 and locksLeft > 0:
            for i in range(graphCode[3 + startOfLayer2] - random.randint(0, graphCode[3 + startOfLayer2])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
    startOfLayer3 = len(graphCode) - 1
    graphCode.append(random.randint(2, 4))
    locksLeft = graphCode[1 + startOfLayer3]
    graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[2 + startOfLayer3]
    if graphCode[1 + startOfLayer3] == 1:
        if graphCode[2 + startOfLayer3] == 0:
            graphCode.append(1)
        elif graphCode[2 + startOfLayer3] == 1:
            graphCode.append(0)
    else:
        if graphCode[2 + startOfLayer3] == 0:
            graphCode.append(random.randint(1, 2))
        elif graphCode[2 + startOfLayer3] == 1:
            graphCode.append(random.randint(0, 1))
    locksLeft -= graphCode[3 + startOfLayer3]
    if graphCode[2 + startOfLayer3] == 0:
        if locksLeft > 0:
            if graphCode[3 + startOfLayer3] < locksLeft:
                for i in range(random.randint(1, graphCode[3 + startOfLayer3])):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
            else:
                for i in range(random.randint(1, locksLeft)):
                    graphCode.append(1)
                    graphCode.append(0)
                    locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
    else:
        if locksLeft > 0:
            for i in range(graphCode[3 + startOfLayer3] - random.randint(0, graphCode[3 + startOfLayer3])):
                graphCode.append(1)
                graphCode.append(0)
                locksLeft -= 1
    if not locksLeft == 0:
        loop = True
        while loop:
            graphCode.append(0)
            graphCode.append(random.randint(1, locksLeft))
            locksLeft -= graphCode[len(graphCode) - 1]
            if locksLeft == 0:
                loop = False
print(graphCode)
print(startOfLayer2)
print(startOfLayer3)