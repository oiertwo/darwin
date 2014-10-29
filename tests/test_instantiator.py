from unittest import TestCase

__author__ = 'oier'

import darwin.instance as ins

class TestInstantiator(TestCase):
    def test_get_instance(self):
        c = ins.Instantiator("tests/test.yml")
        c.get_instance("SVM")