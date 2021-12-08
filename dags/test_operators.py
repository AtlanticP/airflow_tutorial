import sys
sys.path.append('/home/atl/myAir/kazynski/plugins')

from datetime import datetime
from airflow import DAG 
from airflow.operators.dummy_operator import DummyOperator 
# from airflow.operators import MyFirstOperator
from my_operators import MyFirstOperator, MyFirstSensor
#%%

dag = DAG(
    'my_test_dag',
    description='Another tutorial DAG',
    schedule_interval='*/1 * * * *',
    start_date=datetime(2021, 12, 6),
    catchup=False
    )

dummy_task = DummyOperator(task_id='dummy_task', dag=dag)

sensor_task = MyFirstSensor(task_id='my_sensor_task', poke_interval=30, dag=dag)


operator_task = MyFirstOperator(
    my_operator_param='This is a test', 
    task_id='my_first_operator_task', 
    dag=dag)

dummy_task >> sensor_task >> operator_task 