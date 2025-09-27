#!/bin/bash
# wait-for-ingestion.sh
echo "Waiting for ingestion to complete..."

# check if a completion file exists (created by ingestion when done)
while [ ! -f /opt/CustomerServiceTwitter/ingestion_done.txt ]; do
  sleep 5
done

echo "Ingestion completed. Starting metrics..."
# Run the original command for metrics
exec python /app/main.py

