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
    "Microprocessor",
    "Wiring Loom",
    "Oxygen Capsule",
    "Unstable Plasma",
    "Ferrite Dust",
    "Cobalt",
    "Oxygen",
    "Sodium",
    "Sodium Diode",
    "Metal Plating",
    "Ion Battery",
    "Chlorine",
    "Sodium Nitrate",
    "Ammonia",
    "Phosphorus"
]

trade_commodoties = [
    "Decrypted User Data",
    "Star Silk"
]



system = Node("System", name="Tavala-Eki", race="Gek ")

graph.merge(system, "System", "name")
SELLS = Relationship.type("SELLS")

trading = Node("Economy Type", name="Trading")
mercantile = Node("Economy", name="Mercantile")
shipping = Node("Economy", name="Shipping")

rel = Relationship(mercantile, "IS_A_TYPE_OF", trading)
graph.merge(rel, "Economy", "name")
rel = Relationship(shipping, "IS_A_TYPE_OF", trading)
graph.merge(rel, "Economy", "name")

struggling = Node("Economy Strength", name="Struggling")
weak = Node("Economy Tier", name="weak")
rel = Relationship(struggling, "HAS_TIER_OF", weak)
graph.merge(rel, "Economy Strength", "name")

sys_has_economy_type = Relationship(system, "HAS_ECONOMY_TYPE", mercantile)
graph.merge(sys_has_economy_type, "System", "name")

sys_has_economy_strength = Relationship(system, "HAS_ECONOMY_STRENGTH", weak)
graph.merge(sys_has_economy_strength, "System", "name")

for resource_name in resource_names:
    n = Node("Resource", name=resource_name)
    graph.merge(SELLS(system, n), "System", "name")

for trade_commodity_name in trade_commodoties:
    n = Node("Trade Commodity", name=trade_commodity_name)
    graph.merge(SELLS(system, n), "System", "name")



