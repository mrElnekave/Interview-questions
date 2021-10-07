
inpt = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]
sample_output = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


def removeIslands(matrix):
    LAND = 1
    OCEAN = 0
    # find a possible island a "1"
    # start by travling to all of its adjacent neighbours and if they are land repeat until you arrive at the edge
    def get_adjacent(location):
        row = location[0]
        col = location[1]
        return (row+1, col), (row-1, col), (row, col+1), (row, col-1)
    # memory
    non_islands = []
    # first get for each pixel not on the edges
    for row in range(len(matrix)):
        if row == 0 or row == len(matrix)-1:
            continue
        for col in range(len(matrix[0])):
            if col == 0 or col == len(matrix[0])-1:
                continue
            if matrix[row][col] == LAND:  # possible island
                # for every island traverse all possible neighbours until one touches land or all are done
                visited_islands = []  # array of indices in matrix
                islands_to_visit = [(row, col)]
                connected_to_edge = False
                while len(islands_to_visit) > 0:
                    visiting = islands_to_visit.pop()
                    if visiting in non_islands:
                        connected_to_edge = True
                        break
                    visited_islands.append(visiting)
                    # check if connected to an edge
                    if visiting[0] == 0 or visiting[0] == len(matrix)-1 or visiting[1] == 0 or visiting[1] == len(matrix[0])-1:
                        connected_to_edge = True
                        break
                    # get adjacent
                    for potential in get_adjacent(visiting):
                        if matrix[potential[0]][potential[1]] is LAND and potential not in visited_islands:
                            islands_to_visit.append(potential)
                if not connected_to_edge:
                    for island in visited_islands:
                        matrix[island[0]][island[1]] = OCEAN
                    # turn all visited_islands to OCEAN
                if connected_to_edge:
                    non_islands.extend(visited_islands)
    return matrix


[print(i) for i in inpt]
print("\n")
[print(i) for i in removeIslands(inpt)]
print("\n")
[print(i) for i in sample_output]
print(removeIslands(inpt) == sample_output)