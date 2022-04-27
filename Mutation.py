import random


def mutation():
    gene_str = input("Enter genes in binary representation: ")
    genes = list(gene_str)
    mutation_prob = float(input("Enter mutation probability: "))
    mutation_prob_vector = list()
    n = len(genes)
    for i in range(n):
        random_prob = random.random()
        if random_prob > mutation_prob:
            mutation_prob_vector.append(1)
        else:
            mutation_prob_vector.append(0)
    final_genes = list()
    for i in range(n):
        old_gene = genes[i]
        if mutation_prob_vector[i] == 1:
            if old_gene == '1':
                new_gene = "0"
            else:
                new_gene = "1"
        else:
            new_gene = old_gene
        final_genes.append(new_gene)

    print("Old genes:")
    print(arr_to_str(genes))
    print("Probability vector")
    print(arr_to_str(mutation_prob_vector))
    print("New genes")
    print(arr_to_str(final_genes))


def arr_to_str(arr):
    string = ""
    for item in arr:
        string += str(item)
    return string

mutation()