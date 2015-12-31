from extendly import get_class_dict
from functools import partial

is_active = False

d_builtin = get_class_dict(type(print))
d_func = get_class_dict(type(lambda: ...))

def _partial(self, *args, **kwargs):
	if is_active:
		return partial(self, *args, **kwargs)
	else:
		raise AttributeError("'%s' object has no attribute 'partial'" % type(self).__name__)

d_builtin['partial'] = _partial
d_func['partial'] = _partial

def buildup():
	global is_active
	is_active = True

def breakdown():
	global is_active
	is_active = False

func_partial = buildup, breakdown
