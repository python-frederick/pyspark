### Vagrant

```python
infolder = "gz/"

rdd = sc.textFile(infolder)

test = sqlContext.read.json(rdd)

test.registerTempTable("test")

sqlContext.sql("select * from test").show()

data = sqlContext.sql("select * from test where type like '%PullRequest%'")

pull_requests = data.selectExpr(
    "actor.id as actor_id",
    "actor.login as actor_login",
    "actor.url as actor_url",
    "repo.id as repo_id",
    "repo.name as repo_name",
    "repo.url as repo_url",
    "public",
    "created_at",
    "id as pull_request_id",
    "type"
)

pull_requests.count()

pull_requests.registerTempTable("pullrequests")

sqlContext.sql("select actor_id, repo_id from pullrequests").show()
```

### EMR 20 nodes 1 month
Total run time: 5 minutes

```python
infolder = "s3n://fredpy-pysparkdemo/2016/06/*/" # This bucket was created for this demo, you will need to setup a process to download the GHA files for this to work

rdd = sc.textFile(infolder)

test = sqlContext.read.json(rdd)

test.count()

test.registerTempTable("test")

sqlContext.sql("select DISTINCT count(repo.url) from test where type = 'CreateEvent'").show()

sqlContext.sql("select count(actor.id) from test").show()

sqlContext.sql("select DISTINCT actor.login from test").show()

Note number of results for all sqlContexts
```

### EMR 20 nodes 1 year
Total run time: 14 minutes

```python
infolder = "s3n://fredpy-pysparkdemo/2016/*/*/" # This bucket was created for this demo, you will need to setup a process to download the GHA files for this to work

rdd = sc.textFile(infolder)

test = sqlContext.read.json(rdd)

test.count()

test.registerTempTable("test")

sqlContext.sql("select DISTINCT count(repo.url) from test where type = 'CreateEvent'").show()

sqlContext.sql("select count(actor.id) from test").show()

sqlContext.sql("select DISTINCT actor.login from test").show()
```

Note number of results for all sqlContexts and compare to 1 month
