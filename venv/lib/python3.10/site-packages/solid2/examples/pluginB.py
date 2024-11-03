from solid2 import register_access_syntax

@register_access_syntax
def leftUp(obj):
    return obj.left(1).up(1)

@register_access_syntax
def rightDown(obj):
    return obj.right(1).down(1)

