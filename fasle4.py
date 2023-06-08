
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('ca-GrQc.txt', comments='#', delimiter='\t', nodetype=int)

#33
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
degree_distribution = [count/sum(degree_sequence) for count in degree_count]



# 34
spl_distribution = nx.all_pairs_shortest_path_length(G)
print(spl_distribution)


# 35
clustering_distribution = list(nx.clustering(G).values())
print(clustering_distribution)

# 36
wcc = sorted([len(c) for c in nx.connected_components(G)], reverse=True)
print(wcc)



# Compare
plt.hist(sw_degree_sequence, bins=60')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.legend()
plt.show()