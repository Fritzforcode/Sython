def grepr(obj, annotate_fields=True, include_attributes=False, *, indent=None):
    is_compatible = hasattr(obj, "good_repr_compatible")
    def _format(obj, level=0):
        if indent is not None:
            level += 1
            prefix = '\n' + indent * level
            sep = ',\n' + indent * level
        else:
            prefix = ''
            sep = ', '
        if isinstance(obj, list):
            if not obj:
                return '[]', True
            return '[%s%s]' % (prefix, sep.join(_format(x, level)[0] for x in obj)), False
        elif isinstance(obj, dict):
            if not obj:
                return '{}', True
            args = [f'{_format(key, level)[0]}: {_format(value, level)[0]}' for key,value in obj.items()]
            return '{%s%s}' % (prefix, sep.join(args)), False
        elif hasattr(obj, "good_repr_compatible"):
            cls = type(obj)
            args = []
            allsimple = True
            keywords = annotate_fields
            for name in obj._fields:
                try:
                    value = getattr(obj, name)
                except AttributeError:
                    keywords = True
                    continue
                if value is None and getattr(cls, name, ...) is None:
                    keywords = True
                    continue
                value, simple = _format(value, level)
                allsimple = allsimple and simple
                if keywords:
                    args.append('%s=%s' % (name, value))
                else:
                    args.append(value)
            if include_attributes and obj._attributes:
                for name in obj._attributes:
                    try:
                        value = getattr(obj, name)
                    except AttributeError:
                        continue
                    if value is None and getattr(cls, name, ...) is None:
                        continue
                    value, simple = _format(value, level)
                    allsimple = allsimple and simple
                    args.append('%s=%s' % (name, value))
            class_name = getattr(obj, "good_repr_class_name", obj.__class__.__name__)
            if allsimple and len(args) <= 3:
                return '%s(%s)' % (class_name, ', '.join(args)), not args
            return '%s(%s%s)' % (class_name, prefix, sep.join(args)), False
        return repr(obj), True
 
    if not(is_compatible) and not(isinstance(obj, list)):
        return repr(obj)
    if indent is not None and not isinstance(indent, str):
        indent = ' ' * indent
    return _format(obj)[0]


def gprint(*objects, sep=" ", end="\n"):
    print(
        *(grepr(obj) for obj in objects),
        sep=sep,
        end=end,
    )
