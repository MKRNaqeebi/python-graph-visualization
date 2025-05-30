from neo4j_viz.options import Layout, RenderOptions


def test_render_options() -> None:
    options = RenderOptions(layout=Layout.FORCE_DIRECTED)

    assert options.to_dict() == {"layout": "forcedirected"}
