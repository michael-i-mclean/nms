from py2neo import Graph

graph = Graph(host="localhost", user= "neo4j", password="test")

from py2neo import Node, Relationship

economy_names = [
    "Power Generation",
    "Mining",
    "Manufacturing",
    "High Tech",
    "Advanced Materials",
    "Scientific",
    "Trading"
]

resource_names = [
    "Oxygen Capsule",
    "Unstable Plasma",
    "Ferrite Dust",
    "Cobalt",
    "Oxygen",
    "Sodium",
    "Di-hydrogen Jelly",
    # "Lemmium",
    # "Sodium Diode",
    "Magno-Gold",
    # "Carbon Nanotubes",
    "Metal Plating",
    "Ion Battery",
    "Microprocessor",
    "Wiring Loom",
    # "Dioxite",
    "Gold",
    # "Silver",
    "Paraffinium",
    "Pure Ferrite",
    "Ionised Cobalt"
    # "Chlorine",
    # "Sodium Nitrate",
    # "Ammonia",
    # "Phosphorus"

]

system = Node("System", name="IvtJen", race="Vy'Keen")

graph.merge(system, "System", "name")
SELLS = Relationship.type("SELLS")

trading = Node("Economy Type", name="Trading")
mercantile = Node("Economy", name="Mercantile")
shipping = Node("Economy", name="Shipping")

rel = Relationship(mercantile, "IS_A_TYPE_OF", trading)
graph.merge(rel, "Economy", "name")
rel = Relationship(shipping, "IS_A_TYPE_OF", trading)
graph.merge(rel, "Economy", "name")

power_generation_type = Node("Economy Type", name="Power Generation")
power_generation = Node("Economy", name="Power Generation")

rel = Relationship(power_generation, "IS_A_TYPE_OF", power_generation_type)
graph.merge(rel, "Economy", "name")


struggling = Node("Economy Strength", name="Struggling")
weak = Node("Economy Tier", name="weak")
rel = Relationship(struggling, "HAS_TIER_OF", weak)
graph.merge(rel, "Economy Strength", "name")


average = Node("Economy Tier", name="Average")
satisfactory = Node("Economy Strength", name="Satisfactory")
rel = Relationship(average, "HAS_TIER_OF", satisfactory)
graph.merge(rel, "Economy Strength", "name")

balanced = Node("Economy Strength", name="Satisfactory")
rel = Relationship(average, "HAS_TIER_OF", balanced)
graph.merge(rel, "Economy Strength", "name")


sys_has_economy_type = Relationship(system, "HAS_ECONOMY_TYPE", power_generation)
graph.merge(sys_has_economy_type, "System", "name")

sys_has_economy_strength = Relationship(system, "HAS_ECONOMY_STRENGTH", balanced)
graph.merge(sys_has_economy_strength, "System", "name")

for resource_name in resource_names:
    n = Node("Resource", name=resource_name)
    graph.merge(SELLS(system, n), "System", "name")




