#!/bin/bash
# Script to trigger the postcode update in the API consumer microservice
curl -X POST http://localhost:6000/update_postcodes
