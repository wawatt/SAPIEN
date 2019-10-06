//
// Created by sim on 10/2/19.
//

#include "velocity_control_service.h"
namespace sapien::robot {

VelocityControllerServer::VelocityControllerServer(ControllableArticulationWrapper *wrapper,
                                                   const std::vector<std::string> &jointName,
                                                   const std::string &serviceName, float timestep,
                                                   ros::NodeHandle *nh,
                                                   const std::string &robotName)
    : mJointName(jointName), mNodeHandle(std::move(nh)), mTimestep(timestep),
      mServerName("/sapien/" + robotName + "/" + serviceName + "/joint_velocity") {
  mServer = mNodeHandle->advertiseService(mServerName, &robot::VelocityControllerServer::executeCB,
                                          this);
  mQueue = std::make_unique<ThreadSafeQueue>();

  // Register queue to controllable wrapper
  wrapper->add_velocity_controller(mJointName, mQueue.get());
}
bool VelocityControllerServer::executeCB(sapien_ros_utils::JointVelocityControl::Request &req,
                                         sapien_ros_utils::JointVelocityControl::Response &res) {
  // Check joint name
  auto serviceJointName = req.joint_name;
  for (const auto &name : serviceJointName) {
    if (count(mJointName.begin(), mJointName.end(), name) != 1) {
      ROS_ERROR("Received service has joint name out of the scope of controller joints: %s",
                name.c_str());
      res.success = false;
      return false;
    }
  }

  // Generate joint stepSize with right order
  std::vector<float> jointVelocity(mJointName.size(), 0);
  for (size_t i = 0; i < serviceJointName.size(); ++i) {
    uint32_t index =
        std::find(mJointName.begin(), mJointName.end(), serviceJointName[i]) - mJointName.begin();
    jointVelocity[index] = req.joint_velocity[i];
  }

  // Push stepSize to the queue
  uint32_t step = req.duration.toSec() / mTimestep;
  for (size_t i = 0; i < step; ++i) {
    mQueue->pushValue(jointVelocity);
  }
  res.success = true;
  return true;
}
} // namespace sapien::robot