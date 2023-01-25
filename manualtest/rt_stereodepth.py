import sapien.core as sapien
import numpy as np
import transforms3d.euler
import PIL.Image as im
import matplotlib.pyplot as plt
import open3d as o3d
from sapien.core import Pose
from sapien.sensor import StereoDepthSensor, StereoDepthSensorConfig

def build_scene(sim, renderer):
    scene_config = sapien.SceneConfig()
    scene = sim.create_scene(scene_config)

    ground_material = renderer.create_material()
    ground_material.base_color = np.array([202, 164, 114, 256]) / 256
    ground_material.specular = 0.5
    scene.add_ground(0, render_material=ground_material)
    scene.set_timestep(1 / 240)

    builder = scene.create_actor_builder()
    material = renderer.create_material()
    material.base_color = [0.2, 0.2, 0.8, 1.0]
    material.roughness = 0.5
    material.metallic = 0.0
    builder.add_sphere_visual(radius=0.06, material=material)
    builder.add_sphere_collision(radius=0.06)
    sphere1 = builder.build()
    sphere1.set_pose(Pose(p=[-0.05, 0.05, 0.06]))

    builder = scene.create_actor_builder()
    material = renderer.create_material()
    material.ior = 1.2
    material.transmission = 1.0
    material.base_color = [1.0, 1.0, 1.0, 1.0]
    material.roughness = 0.3
    material.metallic = 0.0
    builder.add_sphere_visual(radius=0.07, material=material)
    builder.add_sphere_collision(radius=0.07)
    sphere2 = builder.build()
    sphere2.set_pose(Pose(p=[0.05, -0.05, 0.07]))

    builder = scene.create_actor_builder()
    material = renderer.create_material()
    material.base_color = [0.8, 0.7, 0.1, 1.0]
    material.roughness = 0.01
    material.metallic = 0.95
    builder.add_capsule_visual(radius=0.02, half_length=0.1, material=material)
    builder.add_capsule_collision(radius=0.02, half_length=0.1)
    cap = builder.build()
    cap.set_pose(Pose(p=[0.15, -0.01, 0.01], q=transforms3d.euler.euler2quat(0, 0, -0.7)))

    builder = scene.create_actor_builder()
    material = renderer.create_material()
    material.base_color = [0.8, 0.2, 0.2, 1.0]
    material.roughness = 0.01
    material.metallic = 1.0
    builder.add_box_visual(half_size=[0.09, 0.09, 0.09], material=material)
    builder.add_box_collision(half_size=[0.09, 0.09, 0.09])
    box = builder.build()
    box.set_pose(Pose(p=[0.05, 0.17, 0.09]))

    builder = scene.create_actor_builder()
    material = renderer.create_material()
    material.base_color = [0.9, 0.6, 0.5, 1.0]
    material.roughness = 0.0
    material.metallic = 1.0
    builder.add_visual_from_file(
        '../3rd_party/kuafu/resources/models/suzanne.dae', scale=[0.1, 0.1, 0.1], material=material)
    builder.add_box_collision(half_size=[0.1, 0.1, 0.1])
    monkey = builder.build()
    monkey.set_pose(Pose(p=[0.15, -0.25, 0.1], q=transforms3d.euler.euler2quat(0, 0, -1)))

    scene.set_ambient_light([0.3, 0.3, 0.3])
    scene.add_directional_light([0, 0.5, -1], color=[3.0, 3.0, 3.0])

    return scene

def main():
    sim = sapien.Engine()

    renderer = sapien.SapienRenderer()
    sim.set_renderer(renderer)
    sapien.render_config.camera_shader_dir = "rt"
    sapien.render_config.rt_samples_per_pixel = 32
    sapien.render_config.rt_max_path_depth = 8
    sapien.render_config.rt_use_denoiser = True

    scene = build_scene(sim, renderer)

    sensor_config = StereoDepthSensorConfig()
    sensor = StereoDepthSensor('sensor', scene, sensor_config)
    sensor.set_pose(
        Pose([-0.28, -0.28, 0.46], [0.8876263, -0.135299, 0.3266407, 0.2951603]))

    scene.step()
    scene.update_render()
    sensor.take_picture()
    sensor.compute_depth()
    depth = sensor.get_depth()

    rgb = sensor.get_rgb()
    im.fromarray((rgb * 255).astype(np.uint8)).show()

    ir_l, ir_r = sensor.get_ir()
    im.fromarray((ir_l * 255).astype(np.uint8)).show()
    im.fromarray((ir_r * 255).astype(np.uint8)).show()

    plt.imshow(depth)
    plt.show()

    pc = sensor.get_pointcloud(frame='world', with_rgb=True)
    pc1 = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(pc[..., :3]))
    pc1.colors = o3d.utility.Vector3dVector(pc[..., 3:])
    o3d.visualization.draw_geometries([pc1])


main()