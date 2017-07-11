### PySpark!!!!


#### Vagrant

Besure to install Vagrant first (https://www.vagrantup.com/intro/getting-started/)

> vagrant up --provider virtualbox

> vagrant ssh

> mkdir gz

> wget -P gz http://data.githubarchive.org/2016-01-01-{0..5}.json.gz

> [pyspark](https://github.com/python-frederick/pyspark/blob/master/pyspark_code.md#vagrant)


#### EMR

> python create_cluster.py

Wait 10 minutes for Master and Core to report "Running"

> ssh-add key-name

> ssh -A -C -D 3128 hadoop@ec2-hostname-reported-in-emr

> hadoop dfsadmin -report
```
Configured Capacity: 31862155018240 (28.98 TB)
Present Capacity: 31858708243397 (28.98 TB)
DFS Remaining: 31858658283520 (28.98 TB)
DFS Used: 49959877 (47.65 MB)
DFS Used%: 0.00%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0
Missing blocks (with replication factor 1): 0

-------------------------------------------------
Live datanodes (20):
```

> [pyspark](https://github.com/python-frederick/pyspark/blob/master/pyspark_code.md#emr-20-nodes-1-month)

Up cluster by a lot more nodes

> hadoop dfsadmin -report | head -n 20

```
Configured Capacity: 63724310036480 (57.96 TB)
Present Capacity: 63712588763136 (57.95 TB)
DFS Remaining: 63712373317632 (57.95 TB)
DFS Used: 215445504 (205.46 MB)
DFS Used%: 0.00%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0
Missing blocks (with replication factor 1): 0

-------------------------------------------------
Live datanodes (50):
```

> [pyspark](https://github.com/python-frederick/pyspark/blob/master/pyspark_code.md#emr-50-nodes-1-year)
