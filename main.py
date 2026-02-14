import os
import sys

def run_job_search():
    # 1. Print Debug Information
    print("--- DEBUGGING ENVIRONMENT ---")
    print(f"Python Executable: {sys.executable}")
    
    # Check Secrets
    def mask(s):
        return f"{s[:4]}****{s[-4:]}" if s and len(s) > 8 else "EMPTY ❌"

    wa_id = os.getenv("WA_INSTANCE_ID")
    wa_token = os.getenv("WA_TOKEN")
    phone = os.getenv("MY_PHONE")

    print(f"WA_INSTANCE_ID: {wa_id if wa_id else 'EMPTY ❌'}")
    print(f"WA_TOKEN: {mask(wa_token)}")
    print(f"MY_PHONE: {mask(phone)}")
    print("----------------------------")

    # 2. Import Libraries inside the function
    try:
        from jobspy import scrape_jobs
        import pandas as pd
        print("✅ Jobspy loaded successfully!")
    except ImportError:
        print("❌ Still failing to load Jobspy. Printing sys.path:")
        print(sys.path)
        return

    # 3. Scraping Logic
    try:
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed"],
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=3,
            hours_old=1,
            country_indeed='usa'
        )
        print(f"Found {len(jobs)} jobs.")
    except Exception as e:
        print(f"Scraper error: {e}")
        return

    if not jobs.empty:
        import requests
        url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
        message = "🚀 *New DevOps Jobs Found!*\n\n"
        for _, row in jobs.iterrows():
            message += f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n\n"
        
        requests.post(url, json={"chatId": f"{phone}@c.us", "message": message})
        print("📱 WhatsApp send attempted.")
    else:
        print("📭 No jobs to send.")

if __name__ == "__main__":
    run_job_search()