from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.sdk import DAG
import sys
sys.path.append("/opt/airflow/api")
default_args = {
    "description" : "A DAG to orchestrate Data",
    "start_date" :datetime(2025,6,13),
    "catchup" : False
}
def safe_main_callable():
    from insert_records import main
    return main()
dag = DAG (
    dag_id = "weather_api",
    default_args =default_args ,
    schedule =  timedelta(minutes=5)
)


with dag:
    #task1
    task1 = PythonOperator(
        task_id = "fetch_data_task1",
        python_callable = safe_main_callable
    )
    #task2
    #task3