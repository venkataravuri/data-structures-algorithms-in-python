
def tower_of_hanoi(disk, source=1, auxiliary=2, target=3):

    if disk == 1:
        print(f"Move disk 1 from pole {source} to pole {target}")
        return

    tower_of_hanoi(disk - 1, source, target, auxiliary)

    print(f"Move disk {disk} from pole {source} to pole {target}")

    tower_of_hanoi(disk - 1, auxiliary, source, target)

if __name__ == '__main__':
    tower_of_hanoi(3)