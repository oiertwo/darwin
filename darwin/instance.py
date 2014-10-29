"""
YAML Class Instantiator
"""
import sys
import yaml
import re

def import_module(module_path):
    """Import any module to the global Python environment.
       The module_path argument specifies what module to import in
       absolute or relative terms (e.g. either pkg.mod or ..mod).
       If the name is specified in relative terms, then the package argument
       must be set to the name of the package which is to act as the anchor
       for resolving the package name (e.g. import_module('..mod', 'pkg.subpkg')
       will import pkg.mod).

    Parameters
    ----------
    module_path: str
        Path to the module to be imported

    Returns
    -------
    The specified module will be inserted into sys.modules and returned.
    """
    import importlib
    mod = importlib.import_module(module_path)
    return mod


def import_pyfile(filepath, mod_name=None):
    """
    Imports the contents of filepath as a Python module.

    :param filepath: string

    :param mod_name: string
    Name of the module when imported

    :return: module
    Imported module
    """
    if sys.version_info.major == 3:
        import importlib.machinery
        loader = importlib.machinery.SourceFileLoader('', filepath)
        mod = loader.load_module(mod_name)
    else:
        import imp
        mod = imp.load_source(mod_name, filepath)

    return mod


class Instantiator():
    """
    YAML Class Instantiator for classifiers and feature selections methods.
    For now, it only works on classes with the scikit-learn interface.

    Parameters
    ----------
    """

    def __init__(self, ymlpath):
        try:
            with open(ymlpath, 'rt') as f:
                self.yamldata = yaml.load(f)
        except FileNotFoundError:
            print("Error: File do not exist")

    def get_instance(self, class_name):

        my_class = None

        class_data = self.yamldata[class_name]
        full_class_path = class_data['class']
        base_class_path = re.split(".", full_class_path)[-1]
        try:
            mod = import_class(full_class_path)
            my_class = globals()[base_class_path](**class_data['default'])
        except ImportError as e:
            print("Error: an error ocurred while importing the module")
        except FileNotFoundError as e:
            print("Error: when reading data from YAML")
            raise e

        return(my_class)
