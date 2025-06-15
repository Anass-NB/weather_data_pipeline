from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.sdk import DAG
import sys
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount  # ✅ This is the Mount class





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
    task1 = PythonOperator(
        task_id = "fetch_data_task1",
        python_callable = safe_main_callable
    )
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        working_dir='/usr/app',
        command="run --select stg_weather_data",
        mounts = [
            Mount(source="/home/anass/repos/weather-data-project/dbt/my_project",target="/usr/app",type="bind"),
            Mount(source="/home/anass/repos/weather-data-project/dbt/profiles.yml",target="/root/.dbt/profiles.yml",type="bind"),
            ],
        docker_url='unix://var/run/docker.sock',  # Unix socket for Docker
        network_mode='weather-data-project_mynetwork',
        auto_remove='success'
    )
    task1 >> task2