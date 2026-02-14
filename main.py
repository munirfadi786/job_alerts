import os
import requests
import sys

def run_job_search():
    # We import these INSIDE the function to avoid immediate crash
    import pandas as pd
    from jobspy import scrape_jobs

    print(f"Step 1: Searching for jobs...")
    try:
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed"],
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=3,
            hours_old=1,
            country_indeed='pk'
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

    # 3. Send via Green-API
    wa_id = os.getenv("WA_INSTANCE_ID")
    wa_token = os.getenv("WA_TOKEN")
    phone = os.getenv("MY_PHONE")

    url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
    payload = {"chatId": f"{phone}@c.us", "message": message}
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ WhatsApp message sent successfully!")
    else:
        print(f"❌ Failed to send. Status: {response.status_code}")

if __name__ == "__main__":
    run_job_search()