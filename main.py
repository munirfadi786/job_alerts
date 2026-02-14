import os
import requests
import pandas as pd
from jobspy import scrape_jobs

def run_job_search():
    # 1. Scrape DevOps Jobs
    try:
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed"],
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=3,
            hours_old=1,  # Only check for new jobs since last run
            country_indeed='usa'
        )
    except Exception as e:
        print(f"Scraper error: {e}")
        return

    if jobs.empty:
        print("No new jobs found.")
        return

    # 2. Format the Message
    message = "🚀 *New DevOps Jobs Found!*\n\n"
    for _, row in jobs.iterrows():
        message += f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n\n"

    # 3. Send via Green-API (WhatsApp)
    # These secrets are pulled from GitHub Environment Variables
    wa_id = os.getenv("WA_INSTANCE_ID")
    wa_token = os.getenv("WA_TOKEN")
    phone = os.getenv("MY_PHONE")

    url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
    payload = {"chatId": f"{phone}@c.us", "message": message}
    
    requests.post(url, json=payload)
    print("WhatsApp message sent!")

if __name__ == "__main__":
    run_job_search()