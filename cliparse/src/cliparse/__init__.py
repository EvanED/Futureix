import argparse
import sys

class _Omitted(object):
    pass

def _set_dict_if_present(d, key, val):
    if val != _Omitted:
        d[key] = val

class ArgumentParser(argparse.ArgumentParser):
    """A wrapper around argparse's ArgumentParser.
    
    The only change should be the addition of a new function,
    ArgumentParser.get_arguments(). Any other difference
    is a bug.
    """
    def __init__(self,
                 description      = _Omitted,
                 epilog           = _Omitted,
                 prog             = _Omitted,
                 usage            = _Omitted,
                 add_help         = _Omitted,
                 argument_default = _Omitted,
                 parents          = _Omitted,
                 prefix_chars     = _Omitted,
                 conflict_handler = _Omitted,
                 formatter_class  = _Omitted):
        #fromfile_prefix_chars ?
        arguments = {}

        _set_dict_if_present(arguments, 'description', description)
        _set_dict_if_present(arguments, 'epilog', epilog)
        _set_dict_if_present(arguments, 'prog', prog)
        _set_dict_if_present(arguments, 'usage', usage)
        _set_dict_if_present(arguments, 'add_help', add_help)
        _set_dict_if_present(arguments, 'argument_default', argument_default)
        _set_dict_if_present(arguments, 'parents', parents)
        _set_dict_if_present(arguments, 'prefix_chars', prefix_chars)
        _set_dict_if_present(arguments, 'conflict_handler', conflict_handler)
        _set_dict_if_present(arguments, 'formatter_class', formatter_class)
                
        argparse.ArgumentParser.__init__(self, **arguments)
        
    def get_arguments(self):
        return self._actions
        
def monkey_patch_argparse():
    argparse.ArgumentParser = ArgumentParser
        
        
        
        
        
        
        
        
        