import click 
import pandas as pd
from bqfdgn.utils import open_json
from bqfdgn import gen_fake_data
from faker import Faker

fake = Faker()

@click.group()
def cli():
    pass


@cli.command('send_fake_data_2bq')
@click.option(
  '--dest-table',
  required= True,
  help="destination table bq : <dataset_id.table_id>"
  )
@click.option(
  '--project-id',
  required= True,
  help="GCP project name "
  )

@click.option(
  '--if-exists',
  default='replace',
  help="parameter to state if the data should be appended, replaced in the bqTable"
  )
@click.option(
  '--json-config-fake',
  required=True,
  help="path file for the json config file, look an example in dataconfig/"
  )
@click.option(
  '--loop',
  default=1,
  help="when set to value > 1 the number of rows from the config file are multiplied by the loop value",
  type=click.types.INT
)
def send_fake_data_2bq(dest_table, project_id, if_exists, json_config_fake, loop):
    fake_config = open_json(json_config_fake)
    for _ in range(loop):
      ldic = gen_fake_data(fake_config, fake)
      df = pd.DataFrame(ldic)
      df.to_gbq(
      dest_table,
      project_id=project_id,
      if_exists=if_exists
      )
      if_exists='append'


if __name__ == '__main__':
    cli()
