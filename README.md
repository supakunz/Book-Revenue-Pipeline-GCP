
# Book Sales End-To-End Data Engineering Project on Google Cloud Platform

An end-to-end modern data engineering project, including deployment of ETL pipeline on Google Cloud Platform, using BigQuery for data analysis and leveraging Looker to generate an insight dashboard.

## Architecture
<img width="1258" alt="Project Architecture" src="https://github.com/user-attachments/assets/a22725d5-0be3-4519-a650-fdf3eb1b5177">
<img width="1258" alt="Project Architecture" src="https://github.com/user-attachments/assets/0cf6fcf2-34e0-4c5d-ad17-ddf1853492a0">

## Technology Stack
Languages: 
* Python
* SQL

Google Cloud Platform: 
* Google Storage
* Google Composer
* Big Query
* Looker Studio


## Data Storage
The raw data and output files are too large to store in the repository. They are stored on Google Drive.

- **Raw data** link : https://drive.google.com/drive/folders/13KLFWQbJXNKjIoQp4QL3Mahyfvn-isaA?usp=drive_link

- **Output** link : https://drive.google.com/drive/folders/1c_BNYN2IqQGQFtJmo-gaGyE_LwBfY6kX?usp=drive_link


## Data Modeling
![Uber Data Model](https://github.com/user-attachments/assets/73b813d1-733a-4109-b925-51384fbf3a46)

## ETL Pipeline
<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/7fef594a-c114-4943-9b58-1254a504ecec">

## Output
[<img src="https://github.com/user-attachments/assets/9f373252-43cd-43ac-970c-f262ea87e39d" width=70% height=70%>](https://lookerstudio.google.com/reporting/5737527d-e089-47f5-80f1-2adda4ff3019)
* The final output from Looker Studio can be accessed via the following link: [View Dashboard](https://lookerstudio.google.com/reporting/5737527d-e089-47f5-80f1-2adda4ff3019). Note: The dashboard reads data from a static CSV file exported from BigQuery.

## ❄️ Setup

1. Clone this repository :

```bash
git clone https://github.com/supakunz/Book-Revenue-Pipeline-GCP.git
```

2. Navigate to the project folder and Set up the environment variables :

```
cd Book-Revenue-Pipeline-GCP
```
- Create a `.env` file in the root directory.

- Add the following variables to the .env file, replacing the placeholder values with your own:

```
MYSQL_CONNECTION = mysql_default #file name in Data Storage --> <data_audible_data_merged.csv>
CONVERSION_RATE_URL = <your_api_url> #file name in Data Storage --> <data_conversion_rate.csv>
MYSQL_OUTPUT_PATH = /home/airflow/gcs/data/audible_data_merged.csv
CONVERSION_RATE_OUTPUT_PATH = /home/airflow/gcs/data/conversion_rate.csv
FINAL_OUTPUT_PATH = /home/airflow/gcs/data/output.csv
```

## Contact
Supakun Thata (supakunt.thata@gmail.com)
