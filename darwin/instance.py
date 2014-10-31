"""
YAML Class Instantiator
"""
import re
import sys
import yaml
import logging
import importlib

log = logging.getLogger(__name__)


def import_this(object_module_path):
    """Import any class or function to the global Python environment.
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
    try:
        mod = import_module(object_module_path)
        obj_name = re.split('.', object_module_path)[-1]
        return getattr(mod, obj_name)
    except:
        log.exception('Error importing object {}.'.format(object_module_path))
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


class Instantiator(object):
    """
    YAML Class Instantiator for classifiers and feature selections methods.
    For now, it only works on classes with the scikit-learn interface.

    Parameters
    ----------
    ymlpath: str
        Path to a YAML Path with the syntax of learners.yml and selectors.yml
    """

    def __init__(self, ymlpath):
        try:
            with open(ymlpath, 'rt') as f:
                self.yamldata = yaml.load(f)
        except IOError:
            log.exception("File {} not found.".format(ymlpath))
            raise
        except:
            log.exception("Error reading file {}.".format(ymlpath))
            raise

    def get_yaml_item(self, item_name):
        """Return the item in the YAML file corresponding to the given item_name

        Parameters
        ----------
        item_name: str

        Returns
        -------
        yml_item: dict
            The item in the YAML file corresponding to the given item_name

        Raises
        ------
        KeyError
            If the item_name is not found
        """
        try:
            return self.yamldata[item_name]
        except KeyError as ke:
            log.exception('Could not find item {}.'.format(item_name))
            raise

    def get_class_instance(self, class_name):
        """Import the needed module for the class and return the instance of a class defined in the yml file.

        Parameters
        ----------
        class_name: str

        Returns
        -------
        cls: class
            The class

        Raises
        ------
        KeyError
            If the item_name is not found

        ImportError
            If the there is any error importing the class

        """
        try:
            class_data = self.get_yaml_item(class_name)
            cls = import_this(class_data['class'])
            default_params = class_data.get('default', {})
            return cls(**default_params)
        except ImportError:
            log.exception("Error when importing module "
                          "class {}.".format(class_name))
            raise
        except:
            log.exception("Error when importing module "
                          "class {}.".format(class_name))
            raise
