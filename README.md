# Optimized-Data-Pipeline-Structured-Segmentation-and-Encryption-for-E-Commerce-Data
Project Overview:
This project demonstrates an optimized data engineering pipeline for processing E-commerce data. The pipeline involves multiple stages, including data pre-processing,data transformation, cryptographic encryption, format conversion, and secure data storage. The entire process is automated using Python, Apache NiFi, SQL and MinIO, ensuring efficient data handling and security.

Tools & Technologies:
Python: For data processing and encryption.
Pandas: For data cleaning and manipulation.
MinIO: S3-compatible storage for input and output data.
Apache NiFi: For data flow management, segmentation, and processing.
Fernet (Python Cryptography): For encrypting sensitive data.
SQL: For queries used for data segmentation.
Parquet: Columnar storage format for efficient querying and analysis.

Project Workflow:
Data Pre-Processing: The raw E-commerce dataset is cleaned using Pandas.
Data Segmentation: The cleaned data is processed in Apache NiFi, where it is segmented into structured components for further use.
Data Encryption: Sensitive columns in the data are encrypted using Python's Fernet encryption.
Data Conversion: The segmented data in CSV format is converted into Parquet format to optimize storage and processing efficiency.
Data Storage: The final Parquet files are uploaded to a MinIO bucket for long-term storage and access.

