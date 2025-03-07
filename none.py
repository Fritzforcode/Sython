from basis import PyTypeObject, PyObject_HEAD

MyNoneType = PyTypeObject(tp_name="NoneType")

class MyNoneClass(PyObject_HEAD):
    good_repr_class_name = "MyNone"
    def __init__(self, /):
        super().__init__(ob_type=MyNoneType)
        super().make_reference_compatible()
    
    def __bool__(self, /):
        return False
    
    def __repr__(self, /):
        return "None"

MyNone = MyNoneClass()
