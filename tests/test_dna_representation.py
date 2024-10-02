import pytest
from cdnap.dna_representation import SoftwareDNA

def test_software_dna_creation():
    dna = SoftwareDNA()
    assert dna.node_count() == 0
    assert dna.edge_count() == 0

def test_add_node():
    dna = SoftwareDNA()
    dna.add_node("func1", "function", {"name": "calculate_sum"})
    assert dna.node_count() == 1
    node = dna.get_node("func1")
    assert node["type"] == "function"
    assert node["properties"]["name"] == "calculate_sum"

def test_add_edge():
    dna = SoftwareDNA()
    dna.add_node("func1", "function")
    dna.add_node("func2", "function")
    dna.add_edge("func1", "func2", "calls")
    assert dna.edge_count() == 1
    edges = list(dna.get_edges("func1"))
    assert len(edges) == 1
    assert edges[0][1] == "func2"
    assert edges[0][2]["type"] == "calls" 