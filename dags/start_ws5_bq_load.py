# ตัวอย่างการ load data ลงใน Google BigQuery *ด้วย BashOperator

import os
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.utils.dates import days_ago
from scripts.etl.extract_data import get_data_from_mysql, get_conversion_rate
from scripts.etl.transform_data import merge_data

# path ที่จะใช้
mysql_output_path = os.getenv("MYSQL_OUTPUT_PATH")
conversion_rate_output_path = os.getenv("CONVERSION_RATE_OUTPUT_PATH")
final_output_path = os.getenv("FINAL_OUTPUT_PATH")


with DAG(
    "workshop5_bq_load_dag",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["workshop"]
) as dag:

    dag.doc_md = """
    # Load to BigQuery ด้วยคำสั่ง bq load
    bq command เป็น command-line tool ที่สามารถใช้จัดการกับ BigQuery ได้
    ดูเพิ่มเติมได้ที่นี่ https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table
    """

    t1 = PythonOperator(
        task_id="get_data_from_mysql",
        python_callable=get_data_from_mysql,
        op_kwargs={"transaction_path": mysql_output_path},
    )

    t2 = PythonOperator(
        task_id="get_conversion_rate",
        python_callable=get_conversion_rate,
        op_kwargs={"conversion_rate_path": conversion_rate_output_path},
    )

    t3 = PythonOperator(
        task_id="merge_data",
        python_callable=merge_data,
        op_kwargs={
            "transaction_path": mysql_output_path,
            "conversion_rate_path": conversion_rate_output_path, 
            "output_path": final_output_path
        },
    )

# สร้าง t4 ที่เป็น BashOperator เพื่อใช้งานกับ BigQuery และใส่ dependencies

    t4 = BashOperator(
        task_id="bq_load", # โหลดข้อมูลไปยัง Google BigQuery
        bash_command="bq load \
            --source_format=CSV --autodetect \
            workshop_5.audible_data \
            gs://asia-east2-workshop5-ed4f532e-bucket/data/output.csv",
            # workshop_5.audible_data * [DATASET].[TABLE_NAME]
    )

    [t1, t2] >> t3 >> t4
