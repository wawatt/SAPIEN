from __future__ import annotations
import sapien.core.pysapien.renderer
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "Context",
    "Cubemap",
    "LineSetObject",
    "Material",
    "Mesh",
    "Model",
    "Node",
    "Object",
    "PointSetObject",
    "PrimitiveSet",
    "Renderer",
    "Scene",
    "Shape",
    "Texture",
    "UIButton",
    "UICheckbox",
    "UIConditional",
    "UIDisplayText",
    "UIDummy",
    "UIDuration",
    "UIFileChooser",
    "UIGizmo",
    "UIInputFloat",
    "UIInputFloat2",
    "UIInputFloat3",
    "UIInputFloat4",
    "UIInputInt",
    "UIInputInt2",
    "UIInputInt3",
    "UIInputInt4",
    "UIInputText",
    "UIInputTextMultiline",
    "UIKeyframe",
    "UIKeyframeEditor",
    "UIOptions",
    "UIPopup",
    "UISameLine",
    "UISection",
    "UISelectable",
    "UISliderAngle",
    "UISliderFloat",
    "UITreeNode",
    "UIWidget",
    "UIWindow"
]


class Context():
    def create_box_mesh(self) -> Mesh: ...
    def create_brdf_lut(self, size: int = 128) -> Texture: 
        """
        Generate BRDF LUT texture, see https://learnopengl.com/PBR/IBL/Specular-IBL
        """
    def create_capsule_mesh(self, radius: float, half_length: float, segments: int = 32, half_rings: int = 8) -> Mesh: ...
    def create_cone_mesh(self, segments: int = 32) -> Mesh: ...
    def create_cubemap_from_files(self, filenames: typing.Annotated[typing.List[str], FixedSize(6)], mipmap_levels: int) -> Cubemap: 
        """
        Load cube map, its mipmaps are generated based on roughness, details see https://learnopengl.com/PBR/IBL/Specular-IBL
        """
    def create_line_set(self, vertices: numpy.ndarray[numpy.float32], colors: numpy.ndarray[numpy.float32]) -> PrimitiveSet: ...
    def create_material(self, emission: numpy.ndarray[numpy.float32], base_color: numpy.ndarray[numpy.float32], specular: float, roughness: float, metallic: float, transmission: float = 0.0, ior: float = 1.0099999904632568) -> Material: ...
    def create_mesh_from_array(self, vertices: numpy.ndarray[numpy.float32], indices: numpy.ndarray[numpy.uint32], normals: numpy.ndarray[numpy.float32] = array([], dtype=float32), uvs: numpy.ndarray[numpy.float32] = array([], dtype=float32)) -> Mesh: ...
    def create_model(self, meshes: typing.List[Mesh], materials: typing.List[Material]) -> Model: ...
    def create_model_from_file(self, filename: str) -> Model: ...
    def create_point_set(self, vertices: numpy.ndarray[numpy.float32], colors: numpy.ndarray[numpy.float32]) -> PrimitiveSet: ...
    def create_texture_from_file(self, filename: str, mipmap_levels: int, filter: str = 'linear', address_mode: str = 'repeat') -> Texture: ...
    def create_uvsphere_mesh(self, segments: int = 32, half_rings: int = 16) -> Mesh: ...
    pass
class Cubemap():
    pass
class Node():
    def set_position(self, position: numpy.ndarray[numpy.float32]) -> None: ...
    def set_rotation(self, quat: numpy.ndarray[numpy.float32]) -> None: ...
    def set_scale(self, scale: numpy.ndarray[numpy.float32]) -> None: ...
    @property
    def children(self) -> typing.List[Node]:
        """
        :type: typing.List[Node]
        """
    @property
    def position(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    @property
    def rotation(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    @property
    def scale(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class Material():
    def set_base_color(self, rgba: numpy.ndarray[numpy.float32]) -> None: ...
    def set_emission(self, emission: float) -> None: ...
    def set_metallic(self, metallic: float) -> None: ...
    def set_roughness(self, roughness: float) -> None: ...
    def set_specular(self, specular: float) -> None: ...
    def set_textures(self, base_color: Texture = None, roughness: Texture = None, normal: Texture = None, metallic: Texture = None, emission: Texture = None, transmission: Texture = None) -> None: ...
    def set_transmission(self, transmission: float) -> None: ...
    pass
class Mesh():
    pass
class Model():
    pass
class LineSetObject(Node):
    pass
class Object(Node):
    def get_segmentation(self) -> numpy.ndarray[numpy.uint32]: ...
    def set_segmentation(self, arg0: numpy.ndarray[numpy.uint32]) -> None: ...
    @property
    def cast_shadow(self) -> bool:
        """
        :type: bool
        """
    @cast_shadow.setter
    def cast_shadow(self, arg1: bool) -> None:
        pass
    @property
    def model(self) -> Model:
        """
        :type: Model
        """
    @property
    def shading_mode(self) -> int:
        """
        :type: int
        """
    @shading_mode.setter
    def shading_mode(self, arg1: int) -> None:
        pass
    @property
    def transparency(self) -> float:
        """
        :type: float
        """
    @transparency.setter
    def transparency(self, arg1: float) -> None:
        pass
    pass
class PointSetObject(Node):
    pass
class PrimitiveSet():
    pass
class Renderer():
    def set_custom_cubemap(self, name: str, texture: Cubemap) -> None: ...
    @typing.overload
    def set_custom_property(self, name: str, value: float) -> None: ...
    @typing.overload
    def set_custom_property(self, name: str, value: int) -> None: ...
    def set_custom_texture(self, name: str, texture: Texture) -> None: ...
    pass
class Scene():
    def add_line_set(self, line_set: PrimitiveSet, parent: Node = None) -> LineSetObject: ...
    def add_node(self, parent: Node = None) -> Node: ...
    def add_object(self, model: Model, parent: Node = None) -> Object: ...
    def add_point_set(self, point_set: PrimitiveSet, parent: Node = None) -> PointSetObject: ...
    def remove_node(self, node: Node) -> None: ...
    pass
class Shape():
    pass
class Texture():
    pass
class UIWidget():
    def get_children(self) -> typing.List[UIWidget]: ...
    def remove(self) -> None: ...
    def remove_children(self) -> None: ...
    pass
class UICheckbox(UIWidget):
    @typing.overload
    def Bind(self, arg0: object, arg1: int) -> UICheckbox: ...
    @typing.overload
    def Bind(self, arg0: object, arg1: str) -> UICheckbox: ...
    def Callback(self, func: typing.Callable[[UICheckbox], None]) -> UICheckbox: ...
    def Checked(self, checked: bool) -> UICheckbox: ...
    def Id(self, id: str) -> UICheckbox: ...
    def Label(self, label: str) -> UICheckbox: ...
    def __init__(self) -> None: ...
    @property
    def checked(self) -> bool:
        """
        :type: bool
        """
    pass
class UIConditional(UIWidget):
    @typing.overload
    def Bind(self, arg0: object, arg1: str) -> UIConditional: ...
    @typing.overload
    def Bind(self, arg0: typing.Callable[[], bool]) -> UIConditional: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UIConditional: ...
    pass
class UIDisplayText(UIWidget):
    @typing.overload
    def Bind(self, arg0: object, arg1: str) -> UIDisplayText: ...
    @typing.overload
    def Bind(self, arg0: typing.Callable[[], str]) -> UIDisplayText: ...
    def Text(self, text: str) -> UIDisplayText: ...
    def __init__(self) -> None: ...
    pass
class UIDummy(UIWidget):
    def Height(self, arg0: float) -> UIDummy: ...
    def Width(self, arg0: float) -> UIDummy: ...
    def __init__(self) -> None: ...
    pass
class UIDuration():
    def __init__(self) -> None: ...
    def keyframe0(self) -> UIKeyframe: ...
    def keyframe1(self) -> UIKeyframe: ...
    def name(self) -> str: ...
    pass
class UIFileChooser(UIWidget):
    def Callback(self, func: typing.Callable[[UIFileChooser, str, str], None]) -> UIFileChooser: ...
    def Filter(self, filter: str) -> UIFileChooser: ...
    def Id(self, id: str) -> UIFileChooser: ...
    def Label(self, label: str) -> UIFileChooser: ...
    def Path(self, path: str) -> UIFileChooser: ...
    def Title(self, title: str) -> UIFileChooser: ...
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def open(self) -> None: ...
    pass
class UIGizmo(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIGizmo: ...
    def CameraMatrices(self, arg0: numpy.ndarray[numpy.float32], arg1: numpy.ndarray[numpy.float32]) -> None: ...
    def Matrix(self, matrix: numpy.ndarray[numpy.float32]) -> UIGizmo: ...
    def __init__(self) -> None: ...
    @property
    def matrix(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputFloat: ...
    def Callback(self, func: typing.Callable[[UIInputFloat], None]) -> UIInputFloat: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat: ...
    def Value(self, value: float) -> UIInputFloat: ...
    def WidthRatio(self, width: float) -> UIInputFloat: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UIInputFloat2(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputFloat2: ...
    def Callback(self, func: typing.Callable[[UIInputFloat2], None]) -> UIInputFloat2: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat2: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat2: ...
    def WidthRatio(self, width: float) -> UIInputFloat2: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat3(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputFloat3: ...
    def Callback(self, func: typing.Callable[[UIInputFloat3], None]) -> UIInputFloat3: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat3: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat3: ...
    def WidthRatio(self, width: float) -> UIInputFloat3: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputFloat4(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputFloat4: ...
    def Callback(self, func: typing.Callable[[UIInputFloat4], None]) -> UIInputFloat4: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputFloat4: ...
    def Value(self, value: numpy.ndarray[numpy.float32]) -> UIInputFloat4: ...
    def WidthRatio(self, width: float) -> UIInputFloat4: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    pass
class UIInputInt(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputInt: ...
    def Callback(self, func: typing.Callable[[UIInputInt], None]) -> UIInputInt: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt: ...
    def Value(self, value: int) -> UIInputInt: ...
    def WidthRatio(self, width: float) -> UIInputInt: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> int:
        """
        :type: int
        """
    pass
class UIInputInt2(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputInt2: ...
    def Callback(self, func: typing.Callable[[UIInputInt2], None]) -> UIInputInt2: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt2: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt2: ...
    def WidthRatio(self, width: float) -> UIInputInt2: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputInt3(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputInt3: ...
    def Callback(self, func: typing.Callable[[UIInputInt3], None]) -> UIInputInt3: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt3: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt3: ...
    def WidthRatio(self, width: float) -> UIInputInt3: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputInt4(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UIInputInt4: ...
    def Callback(self, func: typing.Callable[[UIInputInt4], None]) -> UIInputInt4: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputInt4: ...
    def Value(self, value: numpy.ndarray[numpy.int32]) -> UIInputInt4: ...
    def WidthRatio(self, width: float) -> UIInputInt4: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    pass
class UIInputText(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputText], None]) -> UIInputText: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputText: ...
    def Size(self, size: int) -> UIInputText: ...
    def Value(self, value: str) -> UIInputText: ...
    def WidthRatio(self, width: float) -> UIInputText: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> str:
        """
        :type: str
        """
    pass
class UIInputTextMultiline(UIWidget):
    def Callback(self, func: typing.Callable[[UIInputTextMultiline], None]) -> UIInputTextMultiline: ...
    def Id(self, id: str) -> UIInputText: ...
    def Label(self, label: str) -> UIInputText: ...
    def ReadOnly(self, read_only: bool) -> UIInputTextMultiline: ...
    def Size(self, size: int) -> UIInputTextMultiline: ...
    def Value(self, value: str) -> UIInputTextMultiline: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> str:
        """
        :type: str
        """
    pass
class UIKeyframe():
    def __init__(self) -> None: ...
    def frame(self) -> int: ...
    pass
class UIKeyframeEditor(UIWidget):
    def AddDurationCallback(self, func: typing.Callable[[UIKeyframe, UIKeyframe], None]) -> UIKeyframeEditor: ...
    def AddKeyframeCallback(self, func: typing.Callable[[int], None]) -> UIKeyframeEditor: ...
    def BindCurrentFrame(self, arg0: object, arg1: str) -> UIKeyframeEditor: ...
    def BindTotalFrames(self, arg0: object, arg1: str) -> UIKeyframeEditor: ...
    def DoubleClickDurationCallback(self, func: typing.Callable[[UIDuration], None]) -> UIKeyframeEditor: ...
    def DoubleClickKeyframeCallback(self, func: typing.Callable[[UIKeyframe], None]) -> UIKeyframeEditor: ...
    def MoveKeyframeCallback(self, func: typing.Callable[[UIKeyframe, int], None]) -> UIKeyframeEditor: ...
    def __init__(self, content_scale: float) -> None: ...
    def add_duration(self, duration: UIDuration) -> None: ...
    def add_keyframe(self, keyframe: UIKeyframe) -> None: ...
    def append(self, *args) -> UIKeyframeEditor: ...
    def get_durations(self) -> typing.List[UIDuration]: ...
    def get_keyframes(self) -> typing.List[UIKeyframe]: ...
    def remove_duration(self, duration: UIDuration) -> None: ...
    def remove_keyframe(self, keyframe: UIKeyframe) -> None: ...
    def set_state(self, keyframes: typing.List[UIKeyframe], durations: typing.List[UIDuration]) -> None: ...
    pass
class UIOptions(UIWidget):
    def BindIndex(self, arg0: object, arg1: str) -> UIOptions: ...
    def BindItems(self, arg0: object, arg1: str) -> UIOptions: ...
    def Callback(self, func: typing.Callable[[UIOptions], None]) -> UIOptions: ...
    def Id(self, id: str) -> UIOptions: ...
    def Index(self, index: int) -> UIOptions: ...
    def Items(self, items: typing.List[str]) -> UIOptions: ...
    def Label(self, label: str) -> UIOptions: ...
    def Style(self, style: str) -> UIOptions: ...
    def __init__(self) -> None: ...
    @property
    def index(self) -> int:
        """
        :type: int
        """
    @property
    def value(self) -> str:
        """
        :type: str
        """
    pass
class UIPopup(UIWidget):
    def EscCallback(self, func: typing.Callable[[], None]) -> UIPopup: ...
    def Id(self, id: str) -> UIPopup: ...
    def Label(self, label: str) -> UIPopup: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UIPopup: ...
    pass
class UISameLine(UIWidget):
    def Offset(self, offset: float) -> UISameLine: ...
    def Spacing(self, spacing: float) -> UISameLine: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UISameLine: ...
    pass
class UISection(UIWidget):
    def Expanded(self, expanded: bool) -> UISection: ...
    def Id(self, id: str) -> UISection: ...
    def Label(self, label: str) -> UISection: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UISection: ...
    pass
class UISelectable(UIWidget):
    def Callback(self, func: typing.Callable[[UISelectable], None]) -> UISelectable: ...
    def Id(self, id: str) -> UISelectable: ...
    def Label(self, label: str) -> UISelectable: ...
    def Selected(self, selected: bool) -> UISelectable: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> bool:
        """
        :type: bool
        """
    pass
class UISliderAngle(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UISliderAngle: ...
    def Callback(self, func: typing.Callable[[UISliderAngle], None]) -> UISliderAngle: ...
    def Id(self, id: str) -> UISliderAngle: ...
    def Label(self, label: str) -> UISliderAngle: ...
    def Max(self, max: float) -> UISliderAngle: ...
    def Min(self, min: float) -> UISliderAngle: ...
    def Value(self, value: float) -> UISliderAngle: ...
    def WidthRatio(self, width: float) -> UISliderAngle: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UISliderFloat(UIWidget):
    def Bind(self, arg0: object, arg1: str) -> UISliderFloat: ...
    def Callback(self, func: typing.Callable[[UISliderFloat], None]) -> UISliderFloat: ...
    def Id(self, id: str) -> UISliderFloat: ...
    def Label(self, label: str) -> UISliderFloat: ...
    def Max(self, max: float) -> UISliderFloat: ...
    def Min(self, min: float) -> UISliderFloat: ...
    def Value(self, value: float) -> UISliderFloat: ...
    def WidthRatio(self, width: float) -> UISliderFloat: ...
    def __init__(self) -> None: ...
    @property
    def value(self) -> float:
        """
        :type: float
        """
    pass
class UITreeNode(UIWidget):
    def Id(self, id: str) -> UITreeNode: ...
    def Label(self, label: str) -> UITreeNode: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UITreeNode: ...
    pass
class UIButton(UIWidget):
    def Callback(self, func: typing.Callable[[UIButton], None]) -> UIButton: ...
    def Id(self, id: str) -> UIButton: ...
    def Label(self, label: str) -> UIButton: ...
    def Width(self, width: float) -> UIButton: ...
    def __init__(self) -> None: ...
    pass
class UIWindow(UIWidget):
    def Id(self, id: str) -> UIWindow: ...
    def Label(self, label: str) -> UIWindow: ...
    def Pos(self, x: float, y: float) -> UIWindow: ...
    def Size(self, x: float, y: float) -> UIWindow: ...
    def __init__(self) -> None: ...
    def append(self, *args) -> UIWindow: ...
    pass
