"""
YAML Class Instantiator
"""
import yaml


def import_module(module_path):
    """Import any module to the global Python environment

    Parameters
    ----------
    module_path: str
        Path to the module to be imported



    """

class Instantiator():
    """
    YAML Class Instantiator for classifiers and feature selections methods.
    For now, it only works on classes with the scikit-learn interface.

    Parameters
    ----------
    """

    def __init__(self, ymlpath):
        with open(ymlpath, 'rt') as f:
            self.yamldata = yaml.load(f)

    def get_instance(self, class_name):
        try:
            ret_class = import_module(self.data[class_name]['class'])
        except Exception as e:
            print("Error: when reading data from YAML")
            raise e
