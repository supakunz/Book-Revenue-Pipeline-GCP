
# Book Sales End-To-End Data Engineering Project on Google Cloud Platform

An end-to-end modern data engineering project, including deployment of ETL pipeline on Google Cloud Platform, using BigQuery for data analysis and leveraging Looker to generate an insight dashboard.

## Architecture
<img width="1258" alt="Project Architecture" src="https://github.com/user-attachments/assets/a22725d5-0be3-4519-a650-fdf3eb1b5177">


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

## ❄️ Installation

1. Clone this repository :

```bash
git clone https://github.com/SupakunZ/E-commerce.git
```

2. Navigate to the project folder and install dependencies :

```
cd E-commerce
npm install
```

3. Set up the environment variables :

 - Create a `.env.local` file in the client and server root directory.

 - Add the following variables to the .env file on client, replacing the placeholder values with your own:

```
VITE_APP_API = http://localhost:4000
VITE_STRIPE_PUBLIC_KEY = <your_stripe_public_key>
```

 - Add the following variables to the .env file on server, replacing the placeholder values with your own:

```
PORT = 4000
MONGO_URL = <your_mongoDB_url>
CLIENT_URL = http://localhost:5173 #onLocal
CLOUDINARY_NAME = <your_cloudinary_name>
CLOUDINARY_API_KEY = <your_cloudinary_api_key>
CLOUDINARY_API_SECRET = <your_cloudinary_api_secret>
STRIPE_SECRET_KEY = <your_stripe_secret_key>
STRIPE_ENDPOINT_SECRET = <your_stripe_endpoint_secret>
```

4. Launch the application in development mode :

```
npm run dev
```

## Contact
Supakun Thata (supakunt.thata@gmail.com)
