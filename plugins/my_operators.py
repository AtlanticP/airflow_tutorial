import logging
from datetime import datetime

from airflow.models import BaseOperator 
from airflow.plugins_manager import AirflowPlugin
from airflow.sensors.base import BaseSensorOperator
#%%
log = logging.getLogger(__name__)

class MyFirstOperator(BaseOperator):
    
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MyFirstOperator, self).__init__(*args, **kwargs)
        
    def execute(self, context):
        log.info('Hello World!')
        log.info(f'operator_param: {self.operator_param}')
        # task_instance = context['task_instance']
        # sensors_minute = task_instance.xcom_pull('my_sensor_task', task_instance)
        log.info('Valid miunte as determined by sensor: {sensors_minute}')

class MyFirstSensor(BaseSensorOperator):

    def __init__(self, *args, **kwargs):
        super(MyFirstSensor, self).__init__(*args, **kwargs)
      
    def poke(self, context):
        current_minute = datetime.now().minute

        if current_minute % 3!= 0:
            log.info(f'Current minute {current_minute} not is divisible by 3, sensor will retry.')
            return False
        
        log.info(f'Current minute {current_minute} is divisible by 3, sensor finishing.')                
        # task_instance = context['task_instance']
        # task_instance.xcom_push('sensors_minute', current_minute)
        return True

class MyFirstPlugin(AirflowPlugin):
    name = 'my_first_plugin'
    operators = [MyFirstOperator, MyFirstSensor]    

    
        