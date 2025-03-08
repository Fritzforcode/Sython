from basis import PyTypeObject, PyObject_VAR_HEAD

_1BYTE_KIND = 0
_2BYTE_KIND = 1
_4BYTE_KIND = 2

def _string_to_int_array(s: str) -> list[int]:
    return [ord(char) for char in s]

def _int_array_to_string(array: list[int]) -> str:
    s = ""
    for item in array:
        s += chr(item)
    return s

def _determine_str_kind(array: list[int]):
    max_code_point = max(array) if array else 0
    if max_code_point   < 256  : return _1BYTE_KIND
    elif max_code_point < 65536: return _2BYTE_KIND
    else                       : return _4BYTE_KIND

MyStrType = PyTypeObject(tp_name="str")

class MyStr(PyObject_VAR_HEAD):
    _fields = ["length", "hash", "kind", "data"] + PyObject_VAR_HEAD._fields
    _instances = {}

    @staticmethod
    def from_python(value: str):
        assert isinstance(value, str)
        return MyStr.__new__(
            cls=MyStr,
            data=_string_to_int_array(value),
            hash=0,
        )
    def to_python(self):
        return _int_array_to_string(self.data)
    

    def __new__(cls, data: list[int], hash: int = 0, ob_type=MyStrType):
        key = tuple(data)
        if key in MyStr._instances:
            return MyStr._instances[key]
        instance = super(MyStr, cls).__new__(cls)
        MyStr._instances[key] = instance

        super().__init__(instance, ob_type=ob_type)
        instance.length = len(data)
        instance.hash = hash
        instance.kind = _determine_str_kind(data)
        # "state" varies accross python implementation
        instance.data = data
        super().make_reference_compatible(instance)
        # TODO: add remaining fields
        return instance

    def __init__(*args, **kwargs):
        raise NotImplementedError("Please use __new__")

    # TODO: add remaining methods
    


