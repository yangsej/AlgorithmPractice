def main():
    R, C, K = map(int, input().split())
    maze = []
    for r in range(R):
        maze.append(input())

    print(maze)

if __name__ == "__main__":
    main()

