def feedAnimals(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0

    animals.sort()
    food.sort()
    count = 0

    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break

    return count


if __name__ == "__main__":
    print(feedAnimals([3, 4, 7], [8, 1, 2]))
    print(feedAnimals([3, 8, 1, 4], [1, 1, 2]))
    print(feedAnimals([1, 2, 2], [7, 1]))
    print(feedAnimals([8, 2, 3, 2], [1, 4, 3, 8]))
