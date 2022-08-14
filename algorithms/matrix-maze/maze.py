# https://medium.com/analytics-vidhya/maze-problem-in-python-b303797b03ee

import collections

wall, clear, goal = 0, 1, 9


def bfs(maze, width=0, height=0, start=(0, 0)):
    queue = collections.deque()
    queue.append(start)
    seen = set([start])

    while queue:
        path = queue.popleft()

        x, y = path

        if maze[y][x] == goal:
            return (True, seen)

        # Iterate through all possible directions (East, West, North, South)
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if (0 <= x2 < width and  # X-axis in range
                0 <= y2 < height and  # Y-axis in range
                maze[y2][x2] != wall and  # not a wall
                    (x2, y2) not in seen):  # not visited
                queue.append((x2, y2))
                seen.add((x2, y2))

    return (False, seen)

def main():
    # width, height = map(int, input().split())
    # mat=[list(map(int,input().split())) for i in range(height)]

    width, height = 8, 8
    maze_grid = ["1 0 1 1 1 0 0 1",
                 "1 0 0 0 1 1 1 1",
                 "1 0 0 0 0 0 0 0",
                 "1 0 1 0 9 0 1 1",
                 "1 1 1 0 1 0 0 1",
                 "1 0 1 0 1 1 0 1",
                 "1 0 0 0 0 1 0 1",
                 "1 1 1 1 1 1 1 1"]

    mat = [list(map(int, row.split())) for _, row in enumerate(maze_grid)]
    print(mat)

    ans = 0 if mat[0][0] == 0 else bfs(mat, width=width, height=height, start=(0, 0))
    print(ans[0])

    print(ans[1])


if __name__ == '__main__':
    main()
