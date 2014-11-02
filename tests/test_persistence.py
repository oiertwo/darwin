# -*- coding: utf-8 -*-
import os
import os.path as op
import pytest
from darwin.utils.persist import PersistenceMixin
from darwin.utils.filenames import get_temp_file, file_size


class FooPersist(PersistenceMixin):

    def __init__(self):
        self.anint = 100
        self.abool = False
        self.afloat = 10.123456


class Foo2Persist(PersistenceMixin):

    def __init__(self):
        self.bnint = 100
        self.bbool = False
        self.bfloat = 10.123456


class TestPersistence(object):

    objdump_path = get_temp_file(suffix='.dmp').name

    def __del__(self):
        if op.exists(self.objdump_path):
            os.remove(self.objdump_path)

    def save_foo(self):
        foo = FooPersist()
        foo.afloat = 'saved'
        foo.save(self.objdump_path)

    def test_persist_save(self):
        if op.exists(self.objdump_path):
            os.remove(self.objdump_path)
        self.save_foo()
        assert(file_size(self.objdump_path) > 0)

    def test_persist_load(self):
        if not op.exists(self.objdump_path):
            self.save_foo()

        foo2 = FooPersist.from_file(self.objdump_path)
        assert(foo2.afloat == 'saved')

    def test_persist_different_object(self):
        if not op.exists(self.objdump_path):
            self.save_foo()
        pytest.raises(ValueError, Foo2Persist.from_file, self.objdump_path)
