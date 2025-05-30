from neo4j_viz import Node, VisualizationGraph
from neo4j_viz.node import NodeIdType


def test_toggle_nodes_pinned() -> None:
    nodes = [
        Node(id=42, pinned=False),
        Node(id=43),
        Node(id=44),
        Node(id="1337", pinned=True),
    ]
    VG = VisualizationGraph(nodes=nodes, relationships=[])

    pinned: dict[NodeIdType, bool] = {42: True, 43: True, "1337": False}
    VG.toggle_nodes_pinned(pinned)

    assert VG.nodes[0].pinned
    assert VG.nodes[1].pinned
    assert VG.nodes[2].pinned is None
    assert not VG.nodes[3].pinned
