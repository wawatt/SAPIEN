#include "sapien/component/component.h"

using namespace sapien;

std::string serializeScene(std::shared_ptr<Scene> const &scene);
std::string serializeEntity(std::shared_ptr<Entity> const &entity);
std::string serializeEntityGroup(std::vector<std::shared_ptr<Entity>> const &entities);
std::string serializeArticulationEntityGroup(
    std::shared_ptr<component::PhysxArticulation> const &articulation);
std::string serializeComponent(std::shared_ptr<component::Component> const &component);
std::shared_ptr<Scene> unserializeScene(std::string const &data);
std::shared_ptr<Entity> unserializeEntity(std::string const &data);
std::vector<std::shared_ptr<Entity>> unserializeEntityGroup(std::string const &data);
std::shared_ptr<component::Component> unserializeComponent(std::string const &data);