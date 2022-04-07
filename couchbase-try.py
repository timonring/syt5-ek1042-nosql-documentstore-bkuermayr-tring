# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions

# get a reference to our cluster
cluster = Cluster('couchbase://localhost', ClusterOptions(
  PasswordAuthenticator('admin', '2Ut@V2yw@NrN33t')))

# get a reference to our bucket
cb = cluster.bucket('einkaufliste')

cb_coll_default = cb.default_collection()

# create/update a document in einkaufliste bucket
cb_coll_default.upsert("item-0001", {
    "title": "Birnen",
    "quantity": 3,
    "info": "Einzelne, lose Birnen",
    "type": "item"
})

cb_coll_default.upsert("item-0002", {
    "title": "Mangos",
    "quantity": 2,
    "info": "Bio-Mangos",
    "type": "item"
})

cb_coll_default.upsert("item-0003", {
    "title": "Bananen",
    "quantity": 1,
    "info": "Eine Packung Bananen 6 Stück",
    "type": "item"
})

# get document by key
result = cb_coll_default.get("item-0001")
birnen = result.content_as[str]
print(birnen)

# delete document by key
cb_coll_default.remove("item-0002")

