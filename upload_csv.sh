
#!/bin/bash
# Script to upload a CSV file to the file processor microservice
curl -F 'file=@path_to_your_file.csv' http://localhost:5000/upload
