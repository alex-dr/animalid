"""Where the magic happens."""
import random

from animalid import alloys, animals, colors, fabrics, opinions, origins, shapes, sizes


FIRST_ADJECTIVES = opinions + shapes + sizes
SECOND_ADJECTIVES = alloys + colors + fabrics + origins


def generate_animal_id():
    """What it's all about."""
    return "_".join(
        [
            random.choice(FIRST_ADJECTIVES),
            random.choice(SECOND_ADJECTIVES),
            random.choice(animals),
        ]
    )
