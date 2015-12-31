from extendly import get_class_dict

is_active = False

d_list = get_class_dict(list)
d_map = get_class_dict(map)
d_filter = get_class_dict(filter)

def _map(self, func):
    if is_active:
        return map(func, self)
    else:
        raise AttributeError("'%s' object has no attribute 'map'" % type(self).__name__)
d_list['map'] = _map
d_map['map'] = _map
d_filter['map'] = _map

def _filter(self, func):
    if is_active:
        return filter(func, self)
    else:
        raise AttributeError("'%s' object has no attribute 'filter'" % type(self).__name__)
d_list['filter'] = _filter
d_map['filter'] = _filter
d_filter['filter'] = _filter

def _append(self, obj):
    if is_active:
        self.append(obj)
        return self
    else:
        raise AttributeError("'%s' object has no attribute 'append_chain'")

d_list['append_chain'] = _append

def _apply(self, func):
    if is_active:
        return func(self)
    else:
        raise AttributeError("'%s' object has no attribute 'apply'" % type(self).__name__)
d_list['apply'] = _apply
d_map['apply'] = _apply
d_filter['apply'] = _apply

def buildup():
    global is_active
    is_active = True

def breakdown():
    global is_active
    is_active = False

iter_chain = buildup, breakdown

__all__ = ['iter_chain']
