
import numpy as np
from sklearn import svm, datasets

from darwin.pipeline import ClassificationPipeline


def test_binary_classification_with_classification_pipeline():
    # generate the dataset
    n_samples=100
    n_features=20
    x, y = datasets.make_gaussian_quantiles(mean=None, cov=1.0, n_samples=n_samples,
                                            n_features=n_features, n_classes=2,
                                            shuffle=True, random_state=1)

    # another way to generate the data
    # x, y = datasets.make_hastie_10_2(n_samples=10, random_state=1)

    # -- test with darwin
    classifier_name='linsvm'
    cvmethod='10'
    n_feats = x.shape[1]

    pipe = ClassificationPipeline(n_feats=n_feats, clfmethod=classifier_name,
                                  cvmethod=cvmethod)

    results, metrics = pipe.cross_validation(x, y)

    assert(results is not None)
