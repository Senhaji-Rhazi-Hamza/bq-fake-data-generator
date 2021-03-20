## About 

This is a small python tool CLI that allows you to generate fake data and send them to BigQuery
## Usage

### Pre-requisite
* You should have [gcloud](https://cloud.google.com/sdk/docs/install) already configured in your local machine
* You should have [poetry](https://python-poetry.org/docs/#installation) installed in your local machine

### Install dependencies
```
poetry install  # in the root directory
```


### Use CLI
```
poetry run cli --help
```
#### Use command send_fake_data_2bq
```
poetry run cli send_fake_data_2bq \
--dest-table=<Bq table destination> \
--project_id=<project_id> \
--json-config-fake=<config_fake_file> # see example in dataconfig/fake_config.json
```

**NB:**
For the config file, for example :
```
{
  "fake_types": [
    {
      "fake_type": "name",
      "column_name":"custom_name"
    },
    {
      "fake_type": "address"
    },
    {
      "fake_type": "phone_number"
    },
    {
      "fake_type": "text",
      "kwargs": {"max_nb_chars":20}
    }
  ],
  "nrows": 80
}
```
**nrows** : Represent the number of rows we want to generate

**fake_types** : Reperesents the columns we want to generate 

**fake_type** : The type of the columns we wants, the types correspond to the providers names in the library [faker](https://faker.readthedocs.io/en/master/) 

**column_name** : The name of the column we want to generate

**kwargs** : The arguments (if any) we want to pass to the fake provider
