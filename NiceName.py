#!/usr/bin/env python3

from data_generator import generate_usernames
import utilities as util
from sklearn.neighbors import KNeighborsClassifier
from word_score import generate_username_scores


""" NiceName
A python package for detecting offensive usernames.

Note: Usernames are assumed to be 25 charaters max and consist of alphanumeric characters and symbols on a keyboard (no spaces).

Authors: Harrison Whitner, Jeremy Howe
Creation Date: 11/28/20
"""


""" CONSTANTS """

TRAINING_SET_FILENAME = 'data/generated/training_set.txt'


""" FUNCTIONS """


def generate_training_set(n_samples: int, percent_offensive=0.5, percent_obfuscated=0.5, debug=False):
    """Create data which the KNN used to predict usernames is fit upon."""

    generate_usernames("./data/generated/training_usernames.txt", n_samples, percent_offensive, percent_obfuscated)
    username_array = util.file_to_array("./data/generated/training_usernames.txt")

    with open(TRAINING_SET_FILENAME, 'w') as output_file:

        for entry in username_array:

                label, username = entry.split('\t')

                jaro, lev, comparison = generate_username_scores(username)

                output_file.write(username + ' ' + str(jaro) + ' ' + str(lev) + ' ' + str(comparison) + " " + str(label) + '\n')


def predict_username_is_offensive(username: str, n_neighbors=5, weights='uniform', debug=False) -> bool:
    """Given a username, predict whether it is offensive or inoffensive using a KNN fitted on generated usernames."""
    
    knn_model = KNeighborsClassifier(n_neighbors, weights)
    training_data = util.file_to_array(TRAINING_SET_FILENAME)
    features = []
    targets = []

    for row in training_data:
        split_row = row.split()
        features.append([float(x) for x in split_row[1:4]])
        targets.append(int(split_row[4]))

    knn_model.fit(features, targets)
    test_features = generate_username_scores(username)
    test_target = knn_model.predict(test_features)

    # 0 -> inoffensive, 1 -> offensive
    print('The username', username, 'is predicted to be', 'offensive' if test_target[0] else 'inoffensive')

    return bool(test_target[0])


def main():
    generate_training_set(100, .5, .5)
    predict_username_is_offensive(input('Enter a username to score: '))

if __name__ == "__main__":
    main()
