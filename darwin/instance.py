"""
YAML Class Instantiator
"""
import sys
import yaml
import logging

log = logging.getLogger(__name__)


def import_class(class_module_path):
    """Import any class to the global Python environment.
       The module_path argument specifies what class to import in
       absolute or relative terms (e.g. either pkg.mod or ..mod).
       If the name is specified in relative terms, then the package argument
       must be set to the name of the package which is to act as the anchor
       for resolving the package name.

    Parameters
    ----------
    module_path: str
        Path to the module to be imported

    Returns
    -------
    The specified module will be inserted into sys.modules and returned.
    """
    import importlib
    try:
        mod = importlib.import_module(class_module_path)
        class_name = class_module_path.split('.')[-1]
        return getattr(mod, class_name)
    except:
        log.exception('Error importing class {}.'.format(class_module_path))
        raise


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
    try:
        mod = importlib.import_module(module_path)
        return mod
    except:
        log.exception('Error importing module {}.'.format(module_path))
        raise


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


    def get_instance(self, class_name):