from basis import PyTypeObject
from int import MyInt

MyBoolType = PyTypeObject(tp_name="bool")

class MyBool(MyInt):
    _fields = MyInt._fields
    
    @staticmethod
    def from_python(value: bool):
        assert isinstance(value, bool)
        return MyBool(digit=(1 if value else 0))
    
    def __init__(self, digit: int):
        super().__init__(
            ob_digit=[digit], # can only be 0 or 1
            ob_size=1,
            ob_type=MyBoolType,
        )
