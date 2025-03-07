from basis import PyObject_VAR_HEAD, PyTypeObject
from not_implemented import MyNotImplemented

INT_BASE = 0x8000

def int_to_digits(n: int) -> list[int]:
    if n == 0:
        return [0]
    digits = []
    n = abs(n)
    while n:
        digits.append(n % INT_BASE)
        n //= INT_BASE
    return digits

def digits_to_int(digits: list[int], is_negative: bool) -> int:
    n = 0
    for i, digit in enumerate(digits):
        n += (INT_BASE ** i) * digit
    return -n if is_negative else n


MyIntType = PyTypeObject(tp_name="int")

class MyInt(PyObject_VAR_HEAD):
    _fields = ["ob_size", "ob_digit"] + PyObject_VAR_HEAD._fields
    
    @staticmethod
    def from_python(value: int):
        assert isinstance(value, int)
        ob_digit = int_to_digits(value)
        if value < 0:
            ob_size = -len(ob_digit)
        else:
            ob_size = len(ob_digit)  
        return MyInt(
            ob_digit=ob_digit,
            ob_size=ob_size
        )
    def to_python(self):
        return digits_to_int(
            digits=self.ob_digit, 
            is_negative=self.ob_size < 0,
        )
      
    def __init__(self, ob_digit: list[int], ob_size: int, ob_type=MyIntType):
        super().__init__(ob_type=ob_type)
        self.ob_digit = ob_digit 
        self.ob_size = ob_size
        super().make_reference_compatible()
    
    def __abs__(self, /):
        if self.ob_size >= 0:
            return self
        return MyInt(
            ob_digit=self.ob_digit.copy(), # Ensure list is copied
            ob_size=abs(self.ob_size),
        )
    
    def __add__(self, value, /):
        if isinstance(value, MyInt):
            return MyInt.from_python(
                self.to_python() + value.to_python()
            )
        else:
            return MyNotImplemented
        # TODO: add float, complex and bool compatability
    
    def __and__(self, value, /):
        if isinstance(value, MyInt):
            return MyInt.from_python(
                self.to_python() & value.to_python()
            )
        else:
            return MyNotImplemented
        # TODO: add float, complex and bool compatability

    # TODO: add remaining methods
