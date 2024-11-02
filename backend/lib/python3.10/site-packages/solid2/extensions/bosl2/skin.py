from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/skin.scad'}", False)

_leadin_ogive = _OpenSCADConstant('_leadin_ogive')
_leadin_cut = _OpenSCADConstant('_leadin_cut')
_leadin_sqrt = _OpenSCADConstant('_leadin_sqrt')
_leadin_linear = _OpenSCADConstant('_leadin_linear')
_lead_in_table = _OpenSCADConstant('_lead_in_table')
_MAP_DIAG = _OpenSCADConstant('_MAP_DIAG')
_MAP_LEFT = _OpenSCADConstant('_MAP_LEFT')
_MAP_UP = _OpenSCADConstant('_MAP_UP')
class skin(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, refine=None, method=None, sampling=None, caps=None, closed=None, z=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("skin", {"profiles" : profiles, "slices" : slices, "refine" : refine, "method" : method, "sampling" : sampling, "caps" : caps, "closed" : closed, "z" : z, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class linear_sweep(_Bosl2Base):
    def __init__(self, region=None, height=None, center=None, twist=None, scale=None, shift=None, slices=None, maxseg=None, style=None, caps=None, cp=None, atype=None, h=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, l=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("linear_sweep", {"region" : region, "height" : height, "center" : center, "twist" : twist, "scale" : scale, "shift" : shift, "slices" : slices, "maxseg" : maxseg, "style" : style, "caps" : caps, "cp" : cp, "atype" : atype, "h" : h, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "l" : l, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rotate_sweep(_Bosl2Base):
    def __init__(self, shape=None, angle=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, tex_taper=None, shift=None, closed=None, style=None, cp=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rotate_sweep", {"shape" : shape, "angle" : angle, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "shift" : shift, "closed" : closed, "style" : style, "cp" : cp, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _ss_polygon_r(_Bosl2Base):
    def __init__(self, N=None, theta=None, **kwargs):
       super().__init__("_ss_polygon_r", {"N" : N, "theta" : theta, **kwargs})

class spiral_sweep(_Bosl2Base):
    def __init__(self, poly=None, h=None, r=None, turns=None, taper=None, r1=None, r2=None, d=None, d1=None, d2=None, internal=None, lead_in_shape=None, lead_in_shape1=None, lead_in_shape2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, height=None, l=None, length=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spiral_sweep", {"poly" : poly, "h" : h, "r" : r, "turns" : turns, "taper" : taper, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "internal" : internal, "lead_in_shape" : lead_in_shape, "lead_in_shape1" : lead_in_shape1, "lead_in_shape2" : lead_in_shape2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "height" : height, "l" : l, "length" : length, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_sweep(_Bosl2Base):
    def __init__(self, shape=None, path=None, method=None, normal=None, closed=None, twist=None, twist_by_length=None, scale=None, scale_by_length=None, symmetry=None, last_normal=None, tangent=None, uniform=None, relaxed=None, caps=None, style=None, transforms=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("path_sweep", {"shape" : shape, "path" : path, "method" : method, "normal" : normal, "closed" : closed, "twist" : twist, "twist_by_length" : twist_by_length, "scale" : scale, "scale_by_length" : scale_by_length, "symmetry" : symmetry, "last_normal" : last_normal, "tangent" : tangent, "uniform" : uniform, "relaxed" : relaxed, "caps" : caps, "style" : style, "transforms" : transforms, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class path_sweep2d(_Bosl2Base):
    def __init__(self, shape=None, path=None, closed=None, caps=None, quality=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("path_sweep2d", {"shape" : shape, "path" : path, "closed" : closed, "caps" : caps, "quality" : quality, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class _ofs_vmap(_Bosl2Base):
    def __init__(self, ofs=None, closed=None, **kwargs):
       super().__init__("_ofs_vmap", {"ofs" : ofs, "closed" : closed, **kwargs})

class _ofs_face_edge(_Bosl2Base):
    def __init__(self, face=None, firstlen=None, second=None, **kwargs):
       super().__init__("_ofs_face_edge", {"face" : face, "firstlen" : firstlen, "second" : second, **kwargs})

class sweep(_Bosl2Base):
    def __init__(self, shape=None, transforms=None, closed=None, caps=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("sweep", {"shape" : shape, "transforms" : transforms, "closed" : closed, "caps" : caps, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class subdivide_and_slice(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, numpoints=None, method=None, closed=None, **kwargs):
       super().__init__("subdivide_and_slice", {"profiles" : profiles, "slices" : slices, "numpoints" : numpoints, "method" : method, "closed" : closed, **kwargs})

class slice_profiles(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, closed=None, **kwargs):
       super().__init__("slice_profiles", {"profiles" : profiles, "slices" : slices, "closed" : closed, **kwargs})

class _closest_angle(_Bosl2Base):
    def __init__(self, alpha=None, beta=None, **kwargs):
       super().__init__("_closest_angle", {"alpha" : alpha, "beta" : beta, **kwargs})

class _smooth(_Bosl2Base):
    def __init__(self, data=None, len=None, closed=None, angle=None, **kwargs):
       super().__init__("_smooth", {"data" : data, "len" : len, "closed" : closed, "angle" : angle, **kwargs})

class rot_resample(_Bosl2Base):
    def __init__(self, rotlist=None, n=None, twist=None, scale=None, smoothlen=None, long=None, turns=None, closed=None, method=None, **kwargs):
       super().__init__("rot_resample", {"rotlist" : rotlist, "n" : n, "twist" : twist, "scale" : scale, "smoothlen" : smoothlen, "long" : long, "turns" : turns, "closed" : closed, "method" : method, **kwargs})

class _dp_distance_array(_Bosl2Base):
    def __init__(self, small=None, big=None, abort_thresh=None, **kwargs):
       super().__init__("_dp_distance_array", {"small" : small, "big" : big, "abort_thresh" : abort_thresh, **kwargs})

class _dp_distance_row(_Bosl2Base):
    def __init__(self, small=None, big=None, small_ind=None, tdist=None, **kwargs):
       super().__init__("_dp_distance_row", {"small" : small, "big" : big, "small_ind" : small_ind, "tdist" : tdist, **kwargs})

class _dp_extract_map(_Bosl2Base):
    def __init__(self, map=None, **kwargs):
       super().__init__("_dp_extract_map", {"map" : map, **kwargs})

class _skin_distance_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_distance_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _skin_aligned_distance_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_aligned_distance_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _skin_tangent_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_tangent_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _find_one_tangent(_Bosl2Base):
    def __init__(self, curve=None, edge=None, curve_offset=None, closed=None, **kwargs):
       super().__init__("_find_one_tangent", {"curve" : curve, "edge" : edge, "curve_offset" : curve_offset, "closed" : closed, **kwargs})

class associate_vertices(_Bosl2Base):
    def __init__(self, polygons=None, split=None, curpoly=None, **kwargs):
       super().__init__("associate_vertices", {"polygons" : polygons, "split" : split, "curpoly" : curpoly, **kwargs})

class texture(_Bosl2Base):
    def __init__(self, tex=None, n=None, inset=None, gap=None, roughness=None, **kwargs):
       super().__init__("texture", {"tex" : tex, "n" : n, "inset" : inset, "gap" : gap, "roughness" : roughness, **kwargs})

class _get_vnf_tile_edges(_Bosl2Base):
    def __init__(self, texture=None, **kwargs):
       super().__init__("_get_vnf_tile_edges", {"texture" : texture, **kwargs})

class _validate_texture(_Bosl2Base):
    def __init__(self, texture=None, **kwargs):
       super().__init__("_validate_texture", {"texture" : texture, **kwargs})

class _textured_linear_sweep(_Bosl2Base):
    def __init__(self, region=None, texture=None, tex_size=None, h=None, counts=None, inset=None, rot=None, tex_scale=None, twist=None, scale=None, shift=None, style=None, l=None, caps=None, height=None, length=None, samples=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_linear_sweep", {"region" : region, "texture" : texture, "tex_size" : tex_size, "h" : h, "counts" : counts, "inset" : inset, "rot" : rot, "tex_scale" : tex_scale, "twist" : twist, "scale" : scale, "shift" : shift, "style" : style, "l" : l, "caps" : caps, "height" : height, "length" : length, "samples" : samples, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _find_vnf_tile_edge_path(_Bosl2Base):
    def __init__(self, vnf=None, val=None, **kwargs):
       super().__init__("_find_vnf_tile_edge_path", {"vnf" : vnf, "val" : val, **kwargs})

class _textured_revolution(_Bosl2Base):
    def __init__(self, shape=None, texture=None, tex_size=None, tex_scale=None, inset=None, rot=None, shift=None, taper=None, closed=None, angle=None, counts=None, samples=None, style=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_revolution", {"shape" : shape, "texture" : texture, "tex_size" : tex_size, "tex_scale" : tex_scale, "inset" : inset, "rot" : rot, "shift" : shift, "taper" : taper, "closed" : closed, "angle" : angle, "counts" : counts, "samples" : samples, "style" : style, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class skin(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, refine=None, method=None, sampling=None, caps=None, closed=None, z=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("skin", {"profiles" : profiles, "slices" : slices, "refine" : refine, "method" : method, "sampling" : sampling, "caps" : caps, "closed" : closed, "z" : z, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class linear_sweep(_Bosl2Base):
    def __init__(self, region=None, height=None, center=None, twist=None, scale=None, shift=None, slices=None, maxseg=None, style=None, convexity=None, caps=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, cp=None, atype=None, h=None, l=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("linear_sweep", {"region" : region, "height" : height, "center" : center, "twist" : twist, "scale" : scale, "shift" : shift, "slices" : slices, "maxseg" : maxseg, "style" : style, "convexity" : convexity, "caps" : caps, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "cp" : cp, "atype" : atype, "h" : h, "l" : l, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rotate_sweep(_Bosl2Base):
    def __init__(self, shape=None, angle=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, tex_taper=None, shift=None, style=None, closed=None, cp=None, convexity=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rotate_sweep", {"shape" : shape, "angle" : angle, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "shift" : shift, "style" : style, "closed" : closed, "cp" : cp, "convexity" : convexity, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class spiral_sweep(_Bosl2Base):
    def __init__(self, poly=None, h=None, r=None, turns=None, taper=None, r1=None, r2=None, d=None, d1=None, d2=None, internal=None, lead_in_shape=None, lead_in_shape1=None, lead_in_shape2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, height=None, l=None, length=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spiral_sweep", {"poly" : poly, "h" : h, "r" : r, "turns" : turns, "taper" : taper, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "internal" : internal, "lead_in_shape" : lead_in_shape, "lead_in_shape1" : lead_in_shape1, "lead_in_shape2" : lead_in_shape2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "height" : height, "l" : l, "length" : length, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_sweep(_Bosl2Base):
    def __init__(self, shape=None, path=None, method=None, normal=None, closed=None, twist=None, twist_by_length=None, scale=None, scale_by_length=None, symmetry=None, last_normal=None, tangent=None, uniform=None, relaxed=None, caps=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, profiles=None, width=None, **kwargs):
       super().__init__("path_sweep", {"shape" : shape, "path" : path, "method" : method, "normal" : normal, "closed" : closed, "twist" : twist, "twist_by_length" : twist_by_length, "scale" : scale, "scale_by_length" : scale_by_length, "symmetry" : symmetry, "last_normal" : last_normal, "tangent" : tangent, "uniform" : uniform, "relaxed" : relaxed, "caps" : caps, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, "profiles" : profiles, "width" : width, **kwargs})

class path_sweep2d(_Bosl2Base):
    def __init__(self, profile=None, path=None, closed=None, caps=None, quality=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("path_sweep2d", {"profile" : profile, "path" : path, "closed" : closed, "caps" : caps, "quality" : quality, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class sweep(_Bosl2Base):
    def __init__(self, shape=None, transforms=None, closed=None, caps=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("sweep", {"shape" : shape, "transforms" : transforms, "closed" : closed, "caps" : caps, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class _textured_revolution(_Bosl2Base):
    def __init__(self, shape=None, texture=None, tex_size=None, tex_scale=None, inset=None, rot=None, shift=None, taper=None, closed=None, angle=None, style=None, atype=None, convexity=None, counts=None, samples=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_revolution", {"shape" : shape, "texture" : texture, "tex_size" : tex_size, "tex_scale" : tex_scale, "inset" : inset, "rot" : rot, "shift" : shift, "taper" : taper, "closed" : closed, "angle" : angle, "style" : style, "atype" : atype, "convexity" : convexity, "counts" : counts, "samples" : samples, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

