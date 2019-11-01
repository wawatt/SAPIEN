from .single_gripper_env import SingleGripperEnv
from .base_env import SapienEnv
import sapyen_robot


class SingleGripperRecorder(SingleGripperEnv, SapienEnv):
    def __init__(self, partnet_dir, partnet_id):
        SapienEnv.__init__(self, partnet_dir, partnet_id)
        self._load_robot()
        self._prepare_controller()
        self.ps3 = sapyen_robot.SingleKinovaGripper(self.manger)

        # Init
        self.renderer.show_window()
        self.ps3.set_demonstration_mode()
        self.dump_data = []
        self.control_signal = []
        self.object_force_array = []
        self.robot_force_array = []

    def step(self):
        self.sim.step()
        self.sim.update_renderer()
        self.renderer.render()
        self.ps3.step()

        # Cache
        self.control_signal.append(self.ps3.get_cache())
        self.dump_data.append(self.sim.dump())
        self.object_force_array.append(self.obj.get_cfrc_ext())
        self.robot_force_array.append(self.robot.get_cfrc_ext())

    def generate_header(self):
        header = {}
        header.update({"robot_joint_name": self.robot.get_joint_names()})
        header.update({"robot_link_name": self.robot.get_link_names()})
        header.update({"object_joint_name": self.obj.get_joint_names()})
        header.update({"object_link_name": self.obj.get_link_names()})
        return header
