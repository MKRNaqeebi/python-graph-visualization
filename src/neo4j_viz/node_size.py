from typing import Union

RealNumber = Union[int, float]


def verify_radii(node_radius_min_max: tuple[RealNumber, RealNumber]) -> None:
    if not isinstance(node_radius_min_max, tuple):
        raise ValueError(f"`node_radius_min_max` must be a tuple of two values, but was {node_radius_min_max}")

    if len(node_radius_min_max) != 2:
        raise ValueError(f"`node_radius_min_max` must be a tuple of two values, but was {node_radius_min_max}")

    min_size, max_size = node_radius_min_max
    if not isinstance(min_size, (int, float)):
        raise ValueError(f"Minimum node size must be a real number, but was of type {type(min_size)}")

    if not isinstance(max_size, (int, float)):
        raise ValueError(f"Maximum node size must be a real number, but was of type {type(max_size)}")

    if min_size < 0:
        raise ValueError(f"Minimum node size must be non-negative, but was {min_size}")

    if max_size < 0:
        raise ValueError(f"Maximum node size must be non-negative, but was {max_size}")

    if min_size > max_size:
        raise ValueError(
            f"Minimum node size must be less than or equal to maximum node size, but was {min_size} > {max_size}"
        )
