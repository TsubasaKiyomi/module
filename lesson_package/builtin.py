# import builtins

# builtins.print()

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# for key in ranking:
#     print(key)  #ABC

# print(sorted(ranking)) #['A', 'B', 'C']

#  key=ranking.getにすると値のrankingが返されるが数字が低い物から返される。
# print(sorted(ranking, key=ranking.get))  #['B', 'C', 'A']

# reverse=True にすると数字が大きい物から表示される。
print(sorted(ranking, key=ranking.get, reverse=True))  # ['A', 'C', 'B']
