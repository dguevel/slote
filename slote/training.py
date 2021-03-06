import os

import cv2
from sklearn import svm

def train():
    char_paths = [x[0] for x in os.walk('../slote/training_data')][1:]
    char_library = [x[0][23:] for x in os.walk('../slote/training_data')][1:]

    data = []
    targets = []

    for char in char_library:
        for fname in [x[2] for x in os.walk('../slote/training_data/' + char)][0]:
            img = cv2.resize(cv2.imread('../slote/training_data/' + char + '/' + fname, 0), tuple([320, 240])).reshape([1, 320 * 240])
            data.extend(img)
            targets.append(char)

    classifier = svm.SVC()
    classifier.fit(data, targets)

    return classifier
