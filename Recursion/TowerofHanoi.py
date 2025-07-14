def TowerofHanoi(n, fromRod , auxRod, toRod):
    if n == 1:
        print(f"move disk {n} from rod {fromRod} to rod {toRod}")
        return 1
    count = TowerofHanoi(n-1, fromRod, auxRod, toRod)
    print(f"move disk {n} from rod {fromRod} to rod {toRod}")
    count += 1
    count += TowerofHanoi(n-1, auxRod, toRod, fromRod)
    return count

print(TowerofHanoi(2,"A","B","C"))
