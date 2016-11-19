"""Download the file mazes.py. The file contains mazes, your future script should be able to traverse
Implement function that will take maze as argument and will return a string representing the sequence of steps (example: 'SSSSEEENEESS'- S = South, N = North etc.) leading from the starting point to the goal. Permitted are only moves up - 'S', down - 'N', left - 'W', right - 'E'.
Implement the function that will generate randomly distributed maze
Implement a function that will depict the maze in ASCII art
Put it all together into one program that will generate random maze, determine the starting point and end point, then find the shortest path and lastly print it all to the command line in ASCII art
Prepared mazes are represented by lists of lists of zeros and ones. Ones represent walls and zeros are paths which you can use to move on
begin 1,1 end 10,10
začnu na buňce, pak hledá, kde je 0, kudy může jít. Ty buňky přidává do zásobníku, než se dostane na konec
pak vytiskne nejkratší cesta"""
from collections import deque
from mazes import maze1


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width)
             for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

maze2graph(maze1)


def find_path_bfs(maze):
    start, goal = (1, 1), (10, 10)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

print(find_path_bfs(maze1))
