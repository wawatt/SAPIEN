from __future__ import annotations
import numpy
import sapien.pysapien
import typing
__all__ = ['DepthSensorEngine']
class DepthSensorEngine:
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: float, arg10: float, arg11: float, arg12: float, arg13: bool, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int, arg23: int, arg24: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg25: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg26: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg27: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg28: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg29: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg30: numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]] | list | tuple, arg31: float, arg32: float, arg33: float, arg34: bool, arg35: float, arg36: float, arg37: float, arg38: float, arg39: float) -> None:
        ...
    @typing.overload
    def compute(self, left_array: numpy.ndarray[numpy.uint8], right_array: numpy.ndarray[numpy.uint8], bbox: bool = False, bbox_start_x: int = 0, bbox_start_y: int = 0, bbox_width: int = 0, bbox_height: int = 0) -> None:
        ...
    @typing.overload
    def compute(self, left_cuda: sapien.pysapien.CudaArray, right_cuda: sapien.pysapien.CudaArray, bbox: bool = False, bbox_start_x: int = 0, bbox_start_y: int = 0, bbox_width: int = 0, bbox_height: int = 0) -> None:
        ...
    def get_cuda(self) -> sapien.pysapien.CudaArray:
        ...
    def get_ndarray(self) -> numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]]:
        ...
    def get_point_cloud_cuda(self) -> sapien.pysapien.CudaArray:
        ...
    def get_point_cloud_ndarray(self) -> numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]]:
        ...
    def get_rgb_point_cloud_cuda(self, arg0: sapien.pysapien.CudaArray) -> sapien.pysapien.CudaArray:
        ...
    def get_rgb_point_cloud_ndarray(self, arg0: sapien.pysapien.CudaArray) -> numpy.ndarray[typing.Any, numpy.dtype[numpy.float32]]:
        ...
    def set_census_window_size(self, arg0: int, arg1: int) -> None:
        ...
    def set_ir_noise_parameters(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        ...
    def set_lr_max_diff(self, arg0: int) -> None:
        ...
    def set_matching_block_size(self, arg0: int, arg1: int) -> None:
        ...
    def set_penalties(self, arg0: int, arg1: int) -> None:
        ...
    def set_uniqueness_ratio(self, arg0: int) -> None:
        ...
