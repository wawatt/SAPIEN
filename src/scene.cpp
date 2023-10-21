#include "sapien/scene.h"
#include "sapien/component/physx/physx_system.h"
#include "sapien/component/sapien_renderer/sapien_renderer.h"
#include "sapien/entity.h"

namespace sapien {

Scene::Scene(std::vector<std::shared_ptr<component::System>> const &systems) {
  for (auto s : systems) {
    addSystem(s);
  }
}

void Scene::addSystem(std::shared_ptr<component::System> system) {
  auto name = system->getName();
  if (mSystems.contains(name)) {
    throw std::runtime_error("faedil to add system: a system with name [" + name +
                             "] is already added to scene");
  }
  mSystems[name] = system;
}

std::shared_ptr<component::System> Scene::getSystem(std::string const &name) const {
  try {
    return mSystems.at(name);
  } catch (std::out_of_range &e) {
    throw std::runtime_error("failed to get system: no system with anem [" + name +
                             "] is added to scene");
  }
}

std::shared_ptr<component::PhysxSystem> Scene::getPhysxSystem() const {
  return std::dynamic_pointer_cast<component::PhysxSystem>(getSystem("physx"));
}

std::shared_ptr<component::SapienRendererSystem> Scene::getSapienRendererSystem() const {
  return std::dynamic_pointer_cast<component::SapienRendererSystem>(getSystem("render"));
}

void Scene::step() { getPhysxSystem()->step(); }
void Scene::updateRender() { getSapienRendererSystem()->step(); }

void Scene::addEntity(std::shared_ptr<Entity> entity) {
  if (entity->getScene()) {
    throw std::runtime_error("failed to add entity to scene: entity is already added to a scene.");
  }

  mEntities.push_back(entity);
  entity->internalSetScene(this);
  entity->internalSetPerSceneId(mNextEntityId++);
  entity->onAddToScene(*this);
}

void Scene::removeEntity(std::shared_ptr<Entity> entity) {
  auto count = std::erase_if(mEntities, [=](auto &e) { return e == entity; });
  if (count == 0) {
    throw std::runtime_error("failed to remove entity: not added");
  }
  entity->onRemoveFromScene(*this);
  entity->internalSetPerSceneId(0);
  entity->internalSetScene(nullptr);
}

std::string Scene::packEntityPoses() {
  std::ostringstream ss;
  for (auto e : mEntities) {
    Pose pose = e->getPose();
    ss.write(reinterpret_cast<char *>(&pose), sizeof(Pose));
  }
  return ss.str();
}

void Scene::unpackEntityPoses(std::string const &data) {
  std::istringstream ss(data);
  for (auto e : mEntities) {
    Pose pose;
    ss.read(reinterpret_cast<char *>(&pose), sizeof(Pose));
    e->internalSyncPose(pose);
  }
  // TODO: check nothing is left
}

Scene::~Scene() {}

} // namespace sapien