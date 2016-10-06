# Animal ID

Generate fun, unique animal ID's for your projects!

Tired of _boring_, _lame_, _untypeable_ and _hard-to-remember_ randomly generated ID's?
Be _bored no more_ with ``animalid``, the latest and greatest in pseudorandom animal technology!

Add ``animalid`` to your project today and enjoy all these _great_ features:

- Pseudorandom animal ID's!

## Installing

Installation is easy!

Simply run

```bash
pip install animalid
```

Or clone this repository and run

```bash
pip install .
```

## Usage

``animalid`` is easy to use!

After adding ``animalid`` to your ``setup.py`` or ``requirements.txt`` file for your project, generate _fun_, _unique_ animal-based pseudo-random ID's like this:

```python
from animalid.random_id import generate_animal_id


def great_awesome_code(fun_parameters):
    """Informative, pep257-compliant docstring!"""
    do_neat_things()
    cool_animal_id = generate_animal_id()
    spectacularly_successful_result = do_things_with(cool_animal_id)
```

### Randomness

Statistics about the probability of collisions, expected numbers of collisions, and more, see the ``animalid.probability`` module.

```python
from animalid.probability import print_collision_probabilities


print_collision_probabilities()
```

Keys will be randomly drawn from the keyspace using the builtin ``random`` library (``random.choice()``).

Effort should be made to ensure that the keyspace is uniform, that is, no ID is more likely to be chosen than any other.

Right now the keyspace size is just over two billion.
When it comes to preventing ID collisions, this is not a large number.
We should expect at least one collision in about 70,000 trials, which takes about 110 _ms_ to generate on my laptop.

### ID Length

Right now, ID's are guaranteed to be at most 62 characters in length.


## Development

Want to contribute to ``animalid``?
Great!
Just fork this repository, make your changes, test them out, and then submit a pull request!

Don't forget to add awesome unit tests and follow existing guidelines

### Testing

To test your changes, you're going to want to install the test dependencies.
Simply run

```bash
pip install --editable .[testing]
pytest
pydocstyle
```

## ASCII Art

Please contribute original ASCII art to illustrate your favorite animal ID's!

```
><(((v(*>

weird_lumber_goatfish
```
