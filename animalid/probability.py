"""Utilities for computing probabilities and such."""
from __future__ import division
import math

from animalid.random_id import FIRST_ADJECTIVES, SECOND_ADJECTIVES, animals


def compute_keyspace_size():
    """Compute how many unique keys can be generated."""
    return len(FIRST_ADJECTIVES) * len(SECOND_ADJECTIVES) * len(animals)


def compute_bits_of_entropy():
    """Compute how many bits of entropy generated phrases have."""
    return (
        math.log(len(FIRST_ADJECTIVES), 2)
        + math.log(len(SECOND_ADJECTIVES), 2)
        + math.log(len(animals), 2)
    )


def compute_probability(keyspace, trials):
    """Compute the probability of a collision.

    Uses an approximation of the full sum for computational speed.
    http://preshing.com/20110504/hash-collision-probabilities/

    :param keyspace: keyspace size
    :param trials: number of trials
    :rtype float: Probability, between 0 and 1

    """
    return 1 - math.e ** (-1 * trials * (trials - 1) / (2 * keyspace))


def _compute_expected_collisions(keyspace, trials):
    """Compute the expected number of collisions

    Uses formula from Wikipedia:
    https://en.wikipedia.org/wiki/Birthday_problem#Collision_counting

    :param keyspace: keyspace size
    :param trials: number of trials
    :rtype float: Number of expected collisions

    """
    return trials - keyspace + keyspace * ((keyspace - 1) / keyspace) ** trials


def compute_expected_collisions(trials):
    """Compute the expected number of collisions

    Uses formula from Wikipedia:
    https://en.wikipedia.org/wiki/Birthday_problem#Collision_counting

    :param trials: number of trials
    :rtype float: Number of expected collisions

    """
    keyspace = compute_keyspace_size()
    return _compute_expected_collisions(keyspace, trials)


def compute_collision_probabilities(trials):
    """Compute the probability and expected nubmer of collisions.

    :param trials: number trials to compute probabilities
    :rtype float: Probability, between 0 and 1

    """
    keyspace = compute_keyspace_size()
    return compute_probability(keyspace, trials)


def print_collision_probabilities(trials_list=[100, 1000, 10000, 100000, 1000000]):
    """Print collision probabilities for various numbers of trials

    :param trials_list: number trials to compute probabilities
    :rtype: None

    """
    print("Trials\tProbability\tExpected")
    for trials in trials_list:
        prob = compute_collision_probabilities(trials)
        expected = compute_expected_collisions(trials)
        print("{}\t{:f}\t{:f}".format(trials, prob, expected))
