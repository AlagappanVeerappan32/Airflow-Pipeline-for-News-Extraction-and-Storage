# Airflow-Pipeline-for-News-Extraction-and-Storage

## Description:
This project leverages Apache Airflow to create a robust pipeline for extracting top news stories from the New York Times API, performing data transformation, and storing the processed data in an Amazon S3 bucket. By automating these tasks with Airflow, you can ensure timely updates and efficient management of your news data.

## Features:

1.Utilizes the New York Times API to fetch the latest top news stories.
2.Extracts raw data using Python and the New York Times Python API.
3.Filters and transforms the raw data to obtain the required subset.
4.Configures an EC2 instance to host Airflow and its dependencies.
5.Implements a custom DAG (Directed Acyclic Graph) in Airflow to orchestrate the data pipeline.
6.Executes the DAG to trigger the extraction, transformation, and storage processes.
7.Stores the processed data in an S3 bucket for easy access and scalability.


## Usage:

1.Start your Airflow webserver and scheduler on the EC2 instance.
2.Access the Airflow web interface and trigger the news_extraction_dag to initiate the pipeline.
3.Monitor the progress of the pipeline execution through the Airflow UI.
4.Once the DAG completes successfully, check the specified S3 bucket for the stored data.

## Architecture:

