from extendly import get_class_dict

is_active = False

d_int = get_class_dict(int)
d_float = get_class_dict(float)

def _times(self, func):
	if is_active:
		for i in range(int(self)):
			func()
	else:
		raise AttributeError("'%s' object has no attribute 'times'" % type(self).__name__)

d_float['times'] = _times
d_int['times'] = _times

def buildup():
	global is_active
	is_active = True

def breakdown():
	global is_active
	is_active = False

num_times = buildup, breakdown