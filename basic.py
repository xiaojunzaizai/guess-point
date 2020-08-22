import random
import copy
# point_set = {0:[1,2,3],1:[4,5,6],2:[7,8,9]}

# print(point_set[0][1])

# point_set1 = [[0 for i in range (3)] for j in range (3)]

# print(point_set1)

# target = 1
# target_x = 1
# target_y = 2
# target_point = [target_x,target_y]

# point_set1[target_x][target_y] = target
# print(point_set1)


# list_point = []
# print(len(point_set1))
# for i in range(len(point_set1)):
#     for j in range(len(point_set1[0])):
#         list_point.append([i,j])

# print(list_point)



def get_point_set(n,m):
    point_set = [[0 for i in range(n)] for  j in range(m)]
    return point_set

def get_list_point(point_set):
    list_point = []
    for i in range(len(point_set)):
        for j in range(len(point_set[0])):
            list_point.append([i,j])
    return list_point

def choose_target(list_point):
    length = len(list_point)
    target = random.randrange(length)
    return list_point[target]

def set_target(target,point_set):
    new_point_set = copy.deepcopy(point_set)
    new_point_set[target[0]][target[1]] = 1
    return new_point_set

def check_row(target_point,point):
    if target_point[0] == point[0]:
        return True
    else:
        return False

def check_column(target_point,point):
    if target_point[1] == point[1]:
        return True
    else:
        return False

def check_diagonal(target_point,point):
    if check_row(target_point,point):
        return False
    elif check_column(target_point,point):
        return False
    elif int(abs(target_point[0]-point[0])) == int(abs(target_point[1]-point[1])):
        return True
    else:
        return False

def check_nothing(target_point,point):
    if check_diagonal(target_point,[point[0]-1,point[1]]):
        distance = abs(point[0] - 1 - target_point[0])+1
    elif check_diagonal(target_point,[point[0],point[1]-1]) :
        distance = abs(point[0] - target_point[0])+1



def get_distance(target_point,point):
    if check_row(target_point,point):
        distance = abs(point[1] - target_point[1])
    elif check_column(target_point,point):
        distance = abs(point[0]- target_point[0])
    elif check_diagonal(target_point,point):
        distance = abs(point[0]- target_point[0])
    else:
        distance = abs(point[0]-target_point[0])+abs(point[1]- target_point[1])
    return distance

point_set = get_point_set(8,6)
list_point = get_list_point(point_set)
target = choose_target(list_point)
new_point_set = set_target(target,point_set)

print(point_set)
print()
print(list_point)
print()
print(target)
print()
print(new_point_set)

# choose_point_x= int(input('x: '))
# choose_point_y = int(input('y: '))
# choose_point = [choose_point_x,choose_point_y]
# distance = get_distance(target,choose_point)
# print(distance)



