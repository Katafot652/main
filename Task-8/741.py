import operator

buildings = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601
}

# за значеннями (висотою): спадання, потім зростання
print(sorted(buildings.items(), key=operator.itemgetter(1), reverse=True))
print(sorted(buildings.items(), key=operator.itemgetter(1)))

# за ключами (назвою): зростання, потім спадання
print(sorted(buildings.items(), key=operator.itemgetter(0)))
print(sorted(buildings.items(), key=operator.itemgetter(0), reverse=True))
