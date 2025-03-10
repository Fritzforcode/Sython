PY_RELEASE_LEVEL_ALPHA = 0xA
PY_RELEASE_LEVEL_BETA  = 0xB
PY_RELEASE_LEVEL_GAMMA = 0xC
PY_RELEASE_LEVEL_FINAL = 0xF

PY_MAJOR_VERSION = 3
PY_MINOR_VERSION = 14
PY_MICRO_VERSION = 0
PY_RELEASE_LEVEL = PY_RELEASE_LEVEL_ALPHA
PY_RELEASE_SERIAL = 5

PY_VERSION = "3.14.0a5+"

def _Py_PACK_FULL_VERSION(X, Y, Z, LEVEL, SERIAL):
    return ((X & 0xff) << 24) | \
           ((Y & 0xff) << 16) | \
           ((Z & 0xff) << 8) | \
           ((LEVEL & 0xf) << 4) | \
           (SERIAL & 0xf)

# Packed version as an integer
PY_VERSION_HEX = _Py_PACK_FULL_VERSION(
    PY_MAJOR_VERSION,
    PY_MINOR_VERSION,
    PY_MICRO_VERSION,
    PY_RELEASE_LEVEL,
    PY_RELEASE_SERIAL
)
