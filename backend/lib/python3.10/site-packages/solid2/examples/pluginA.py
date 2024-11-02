from solid2 import register_access_syntax

@register_access_syntax
def leftUp(obj, x):
    return obj.left(x).up(x)

@register_access_syntax
def rightDown(obj, x):
    return obj.right(x).down(x)

__nothing__ = None

