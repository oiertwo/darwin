# -*- coding: utf-8 -*-

from .instance import Instantiator
from .utils.persist import PersistenceMixin


class Learner(PersistenceMixin):

        @property
        def model_type(self):
            ''' A string representation of the underlying modeltype '''
            return self._model_type

        @property
        def model_kwargs(self):
            '''
            A dictionary of the underlying scikit-learn model's keyword arguments
            '''
            return self._model_kwargs

        @property
        def model(self):
            ''' The underlying scikit-learn model '''
            return self._model
