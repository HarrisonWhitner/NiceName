#!/usr/bin/env python3

""" NiceName
A python package for detecting offensive usernames.

Note: Usernames are assumed to be 25 charaters max and consist of alphanumeric characters and symbols on a keyboard (no spaces).

Authors: Harrison Whitner, Jeremy Howe
Creation Date: 11/28/20
"""

TRAINING_SET_FILENAME = 'data/generated/training_set.txt'

def generate_training_set(n_samples: int, percent_offensive=0.5, percent_obfuscated=0.5, debug=False):
    """Create data which the KNN used to predict usernames is fit upon."""
    pass

def predict_username_is_offensive(username: str) -> bool:
    """Given a username, predict whether it is offensive or inoffensive using a KNN fitted on generated usernames."""
    pass