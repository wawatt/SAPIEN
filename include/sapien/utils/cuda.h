#pragma once
#include <cuda_runtime.h>
#include <stdexcept>
#include <string>

#define checkCudaErrors(call)                                                                     \
  do {                                                                                            \
    cudaError_t err = call;                                                                       \
    if (err != cudaSuccess) {                                                                     \
      throw std::runtime_error("CUDA error: " + std::string(cudaGetErrorString(err)));            \
    }                                                                                             \
  } while (0)

namespace sapien {

struct CudaEvent {
  CudaEvent() {}

  void init() {
    checkCudaErrors(cudaGetDevice(&cudaId));
    checkCudaErrors(cudaEventCreate(&event));
  }

  CudaEvent(CudaEvent const &) = delete;
  CudaEvent &operator=(CudaEvent const &) = delete;

  CudaEvent(CudaEvent &&other) {
    // copy
    cudaId = other.cudaId;
    event = other.event;

    // destory other
    other.event = nullptr;
  }

  CudaEvent &operator=(CudaEvent &&other) {
    // destroy self
    if (event) {
      checkCudaErrors(cudaEventDestroy(event));
    }

    // copy
    cudaId = other.cudaId;
    event = other.event;

    // destroy other
    other.event = nullptr;

    return *this;
  }

  void record(cudaStream_t stream) const {
    if (!event) {
      throw std::runtime_error("cuda event is not initialized");
    }
    cudaEventRecord(event, stream);
  }

  void wait(cudaStream_t stream) const {
    if (!event) {
      throw std::runtime_error("cuda event is not initialized");
    }
    cudaStreamWaitEvent(stream, event);
  }

  ~CudaEvent() {
    if (event) {
      cudaEventDestroy(event);
    }
  }

  int cudaId{-1};
  cudaEvent_t event{nullptr};
};

}; // namespace sapien