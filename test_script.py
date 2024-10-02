from cdnap.dna_representation import SoftwareDNA
from cdnap.visualization import visualize_dna

# Create a new SoftwareDNA instance
dna = SoftwareDNA()

# Add some nodes and edges
dna.add_node("main", "function", {"name": "main"})
dna.add_node("calculate", "function", {"name": "calculate"})
dna.add_node("print_result", "function", {"name": "print_result"})

dna.add_edge("main", "calculate", "calls")
dna.add_edge("main", "print_result", "calls")

# Print some information about the DNA
print(f"Number of nodes: {dna.node_count()}")
print(f"Number of edges: {dna.edge_count()}")

# Try to visualize the DNA
visualize_dna(dna)