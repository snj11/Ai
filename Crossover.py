import random
import math


def crossover():
    str1 = input("Enter 1st genes: ")
    str2 = input("Enter 2nd genes: ")
    gene1 = list(str1)
    gene2 = list(str2)
    n = len(gene1)
    k = math.floor(random.random() * n)
    print(f"The crossover point is: {k}")
    final_genes = list()
    index = 0
    while index < n:
        if index < k:
            final_genes.append(gene1[index])
        else:
            final_genes.append(gene2[index])
        index += 1
    final_str = ""
    for bit in final_genes:
        final_str += bit
    print(str1)
    print(str2)
    print(final_str)


crossover()
