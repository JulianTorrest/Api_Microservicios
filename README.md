
# UK Postcodes Integration System

## Overview
This project consists of two microservices designed to process coordinates from a CSV file and fetch the nearest UK postcode using the Postcodes.io API.

## System Architecture
The system is divided into two parts:
1. **File Processor Microservice**: Handles the uploading and storage of coordinates.
2. **API Consumer Microservice**: Fetches postcodes from the Postcodes.io API using the stored coordinates and updates the database accordingly.

## Prerequisites
Before you start, ensure you have the following installed:
- Docker
- Docker Compose
- Python 3.8+

## Project Structure
```plaintext
.
├── api_consumer
│   ├── Dockerfile
│   └── api_consumer.py
├── file_processor
│   ├── Dockerfile
│   └── file_processor.py
└── docker-compose.yml
```

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine using Git:
```bash
git clone <repository-url>
cd into-the-cloned-directory
```

### Step 2: Build and Run the Containers
Use Docker Compose to build and start the microservices:
```bash
docker-compose up --build
```

### Step 3: Upload a CSV File
To upload a CSV file containing coordinates:
```bash
curl -F 'file=@path_to_your_file.csv' http://localhost:5000/upload
```
Replace `path_to_your_file.csv` with the path to your CSV file.

### Step 4: Trigger Postcode Updates
After uploading the coordinates, trigger the postcode fetching and updating process:
```bash
curl -X POST http://localhost:6000/update_postcodes
```

## Error Handling
- The system logs errors related to file processing and API failures.
- If coordinates cannot be assigned a postcode, the incident is recorded and an error is returned.

## API Rate Limiting
Implement rate limiting by modifying the API Consumer Microservice to include sleep intervals or request counters to comply with the API's rate limits.

## Recommendations for Production
- Add security measures such as API key authentication.
- Use a more robust database like PostgreSQL for scalability.
- Implement continuous integration and deployment pipelines for easier updates and rollbacks.
