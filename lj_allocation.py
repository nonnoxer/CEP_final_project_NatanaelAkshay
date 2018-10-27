def start():
    """Gets desired input files and runs allocate()"""
    venuefile = input("What is your desired venue file? ")
    choicefile = input("What is your desired choice file? ")
    allocate(venuefile, choicefile)

def venues(venuefile):
    """Formats venuefile into a list"""
    file = open(venuefile, "r")
    venues = file.readlines()
    for i in range(len(venues)):
        venues[i] = venues[i].strip().split(",")
    for i in range(len(venues)):
        venues[i][1] = int(venues[i][1])
    return venues

def choices(choicefile):
    """Formats choicefile into a list"""
    file = open(choicefile, "r")
    choices = file.readlines()
    for i in range(len(choices)):
        choices[i] = choices[i].strip().split(",")
    return choices[1:]

def joinname(lst, available):
    """Checks if names in list have commas and joins them if so"""
    if len(lst) == 4 + len(available):
        return lst
    elif len(lst) == 5 + len(available):
        lst[2] = lst[2] + ", " + lst[3]
        lst.remove(lst[3])
        return lst

def sortchoices(choicefile):
    """Sorts choices chronologically"""
    sort = choices(choicefile)
    for i in range(len(sort)):
        sort[i][0] = sort[i][0].strip().split(" ")
        if "-" in sort[i][0][0]:
            sort[i][0][0] = sort[i][0][0].strip().split("-")
        elif "/" in sort[i][0][0]:
            sort[i][0][0] = sort[i][0][0].strip().split("/")
        sort[i][0][1] = sort[i][0][1].strip().split(":")
    sort.sort(key = lambda x: x[0][1][2])
    sort.sort(key = lambda x: x[0][1][1])
    sort.sort(key = lambda x: x[0][1][0])
    sort.sort(key = lambda x: x[0][0][2])
    sort.sort(key = lambda x: x[0][0][1])
    sort.sort(key = lambda x: x[0][0][0])
    return sort

def findchoice(lst, top):
    """Finds top choice of given student"""
    allocated = 0
    while top != 0:
        if str(top) in lst:
            allocated = lst.index(str(top))
            top = 0
        else:
            top = top - 1
    return allocated

def outputmain(lst):
    """Creates master output file"""
    file = open("allocations.csv", "w+")
    for i in range(len(lst)):
        file.write(lst[i][0][0] + ",'" + lst[i][0][1] + "'," + lst[i][0][2] + "," + "LJ" + str(lst[i][1] + 1) + "\n")
    file.close()

def findclass(sortied):
    """Finds the classes existing"""
    classes = []
    for i in range(len(sortied)):
        if sortied[i][3].strip() not in classes:
            classes.append(sortied[i][3])
    return sorted(classes)

def outputclass(lst, classes):
    """Creates output file for each class"""
    for i in range(len(classes)):
        file = open(classes[i] + ".csv", "w+")
        for j in range(len(lst)):
            if lst[j][0][2] == classes[i]:
                file.write(lst[j][0][0] + ",'" + lst[j][0][1] + "'," + "LJ" + str(lst[j][1] + 1) + "\n")
        file.close()

def outputlj(lst, venuefile):
    """Creates output file for each LJ"""
    available = venues(venuefile)
    for i in range(len(available)):
        file = open("LJ" + str(i + 1) + ".csv", "w+")
        for j in range(len(lst)):
            if lst[j][1] == i:
                file.write(lst[j][0][0] + ",'" + lst[j][0][1] + "'," + lst[j][0][2] + "\n")
        file.close()

def random_allocate(allocate, sortied, available):
    """Randomly allocates invalid submissions to empty slot"""
    for i in range(len(available)):
        while available[i][1] > 0 and len(sortied) > 0:
            allocate.append([[sortied[0][1], sortied[0][2], sortied[0][3]], i])
            sortied.remove(sortied[0])
    return allocate

def allocate(venuefile, choicefile):
    """Allocates students to respective LJs and runs output functions"""
    available = venues(venuefile)
    sortied = sortchoices(choicefile)
    for i in range(len(sortied)):
        sortied[i] = joinname(sortied[i], available)
    allocate = []
    top = len(available)
    choice = 0
    classes = findclass(sortied)
    while top > 0:
        for i in range(len(available)):
            x = 0
            while available[i][1] > 0 and x < len(sortied):
                if findchoice(sortied[x], top) - 4 == i:
                    available[i][1] = available[i][1] - 1
                    allocate.append([sortied[x][1:4], i])
                    sortied.remove(sortied[x])
                x = x + 1
        top = top - 1
        choice = choice + 1
    if len(sortied) > 0:
        allocate = random_allocate(allocate, sortied, available)
    outputmain(allocate)
    outputlj(allocate, venuefile)
    outputclass(allocate, classes)

start()
