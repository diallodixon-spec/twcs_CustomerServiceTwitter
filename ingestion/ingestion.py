import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    # Define scope for Google Sheets and Drive API
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    # Path to credentials (mounted via docker-compose)
    creds_path = os.getenv("GOOGLE_CREDENTIALS", "capstone-466722-c2915ddca9a5.json")

    # Load credentials and authorize client
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client_gspread = gspread.authorize(creds)

    # Open the Google Sheet by URL
    sheet_url = os.getenv("GOOGLE_SHEET_URL")
    sheet = client_gspread.open_by_url(sheet_url)

    # Access specific tab (worksheet) by name
    worksheet_name = os.getenv("WORKSHEET_NAME", "ProcessingTest")
    worksheet = sheet.worksheet(worksheet_name)

    # Get all records (list of dicts)
    records = worksheet.get_all_records()

    # Output path (in shared volume)
    shared_dir = "/opt/CustomerServiceTwitter/shared-data"
    os.makedirs(shared_dir, exist_ok=True)
    output_path = os.path.join(shared_dir, "ingestion_output.json")
    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)

    print(f"✅  Retrieved {len(records)} records from Google Sheets → {output_path}")

    # Write completion flag
    done_flag = os.path.join(shared_dir, "ingestion_done.txt")
    with open(done_flag, "w") as f:
        f.write("done")
    print(f"✅  Ingestion completion flag written → {done_flag}")

if __name__ == "__main__":
    main()

