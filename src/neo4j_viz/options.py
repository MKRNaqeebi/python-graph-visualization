from __future__ import annotations

import warnings
from enum import Enum
from typing import Any, Optional

import enum_tools.documentation
from pydantic import BaseModel, Field


@enum_tools.documentation.document_enum
class CaptionAlignment(str, Enum):
    """
    The alignment of the caption text for nodes and relationships.
    """

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


@enum_tools.documentation.document_enum
class Layout(str, Enum):
    FORCE_DIRECTED = "forcedirected"
    HIERARCHICAL = "hierarchical"
    """
    The nodes are then arranged by the directionality of their relationships
    """
    COORDINATE = "free"
    """
    The coordinate layout sets the position of each node based on the `x` and `y` properties of the node.
    """
    GRID = "grid"


@enum_tools.documentation.document_enum
class Renderer(str, Enum):
    """
    The renderer used to render the visualization.
    """

    WEB_GL = "webgl"
    """
    The WebGL renderer is optimized for performance and handles large graphs better.
    However, it does not render text, icons, and arrowheads on relationships.
    """
    CANVAS = "canvas"
    """
    The canvas renderer has worse performance than the WebGL renderer, so is less well suited to render large graphs.
    However, it can render text, icons, and arrowheads on relationships.
    """

    @classmethod
    def check(self, renderer: Renderer, num_nodes: int) -> None:
        if renderer == Renderer.CANVAS and num_nodes > 10_000:
            warnings.warn(
                "To visualize more than 10.000 nodes, we recommend using the WebGL renderer "
                "instead of the canvas renderer for better performance. You can set the renderer "
                "using the `renderer` parameter"
            )
        if renderer == Renderer.WEB_GL:
            warnings.warn(
                "Although better for performance, the WebGL renderer cannot render text, icons "
                "and arrowheads on relationships. If you need these features, use the canvas renderer "
                "by setting the `renderer` parameter"
            )


class RenderOptions(BaseModel, extra="allow"):
    """
    Options as documented at https://neo4j.com/docs/nvl/current/base-library/#_options
    """

    layout: Optional[Layout] = None
    renderer: Optional[Renderer] = None

    pan_X: Optional[float] = Field(None, serialization_alias="panX")
    pan_Y: Optional[float] = Field(None, serialization_alias="panY")

    initial_zoom: Optional[float] = Field(None, serialization_alias="initialZoom", description="The initial zoom level")
    max_zoom: Optional[float] = Field(
        None, serialization_alias="maxZoom", description="The maximum zoom level allowed."
    )
    min_zoom: Optional[float] = Field(None, serialization_alias="minZoom", description="The minimum zoom level allowed")
    allow_dynamic_min_zoom: Optional[bool] = Field(None, serialization_alias="allowDynamicMinZoom")

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)
