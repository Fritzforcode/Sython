from basis import PyTypeObject, PyObject_HEAD

MyNotImplementedType = PyTypeObject(tp_name="NotImplementedType")

class MyNotImplementedClass(PyObject_HEAD):
    good_repr_class_name = "MyNotImplemented"
    def __init__(self, /):
        super().__init__(ob_type=MyNotImplementedType)
        super()._make_reference_compatible()
    
    def __bool__(self, /):
        return True
        # TODO: "DeprecationWarning: NotImplemented should not be used in a boolean context"
    
    __reduce__ = None # pickle isn't (yet) implemented

    def __repr__(self, /):
        from str import MyStr
        return MyStr.from_python("NotImplemented")

MyNotImplemented = MyNotImplementedClass()
