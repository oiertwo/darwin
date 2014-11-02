
import os.path as op
import pytest
from unittest import TestCase
from darwin import instance

CWD = op.dirname(op.realpath(__file__))
MODULE_DIR = op.join(CWD, '..', 'darwin')


class TestImports(TestCase):

    def test_import_this(self):
        """Test import_this function"""
        cls = instance.import_this('collections.defaultdict')
        assert(cls.__module__ == 'collections')

    def test_import_this_raises(self):
        """Test import_this function raising an Exception"""
        pytest.raises(Exception, instance.import_this, 'wrong.module')

    def test_import_pyfile_ioerror(self):
        pytest.raises(IOError, instance.import_pyfile, op.join(MODULE_DIR, 'dontexists'))

    def test_import_pyfile(self):
        imp_inst = instance.import_pyfile(op.join(MODULE_DIR, 'logger.py'), 'setup_logging')
        assert('imp_inst' in sys.modules)
        assert(has_attr(imp_inst, 'import_pyfile'))


class TestInstantiator(TestCase):

    def test_learner_yaml_instance(self):
        inst = instance.Instantiator(op.join(MODULE_DIR, 'learners.yml'))
        learner_item_name = 'LinearSVC'
        cls = inst.get_class_instance(learner_item_name)
        item = inst.get_yaml_item(learner_item_name)
        assert(type(cls).__name__ == item['class'].split('.')[-1])

    def test_learner_yaml_raises_ioerror(self):
        pytest.raises(IOError, instance.Instantiator, 'notexist')

    def test_learner_yaml_raises_keyerror(self):
        inst = instance.Instantiator(op.join(MODULE_DIR, 'learners.yml'))
        learner_item_name = 'NotExist'
        pytest.raises(KeyError, inst.get_class_instance, learner_item_name)
