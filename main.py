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
    # try:
    #     print("🔍 Searching for FRESH jobs (less than 1 hour old)...")
        
    #     # Search A: Lahore specific (100km radius)
    #     jobs_lahore = scrape_jobs(
    #         site_name=["linkedin", "indeed"],
    #         search_term="DevOps Engineer",
    #         location="Lahore",
    #         distance=100, 
    #         results_wanted=10,
    #         hours_old=1,  # Only jobs from the last hour
    #         country_indeed='pakistan'
    #     )

    #     # Search B: Remote specific (Worldwide/Pakistan market)
    #     jobs_remote = scrape_jobs(
    #         site_name=["linkedin", "indeed"],
    #         search_term="DevOps Engineer",
    #         location="Remote",
    #         results_wanted=10,
    #         hours_old=1,
    #         country_indeed='Pakistan'
    #     )

    #     # Merge and clean results
    #     import pandas as pd
    #     jobs = pd.concat([jobs_lahore, jobs_remote]).drop_duplicates(subset=['job_url'])
        
    #     print(f"📊 Fresh jobs found: {len(jobs)}")
        
    #     # Debug: Print found titles in logs
    #     for _, row in jobs.iterrows():
    #         print(f"FOUND: {row['title']} at {row['company']} ({row['location']})")

    # except Exception as e:
    #     print(f"❌ Scraper error: {e}")
    #     return


    # 3. Scraping Logic
    # try:
    #     print("🔍 Searching for FRESH jobs (less than 1 hour old)...")
        
    #     # Search A: Lahore specific (Keep 'pakistan' here)
    #     jobs_lahore = scrape_jobs(
    #         site_name=["linkedin", "indeed"],
    #         search_term="DevOps Engineer",
    #         location="Lahore",
    #         distance=100, 
    #         results_wanted=10,
    #         hours_old=1,
    #         country_indeed='pakistan'
    #     )

    #     # Search B: Remote Worldwide (Remove country_indeed here to fix the error)
    #     # We focus on LinkedIn for global remote as it doesn't crash on 'Worldwide'
    #     jobs_remote = scrape_jobs(
    #         site_name=["linkedin"], 
    #         search_term="DevOps Engineer",
    #         location="Remote",
    #         results_wanted=15,
    #         hours_old=1
    #     )

    #     # Merge and clean results
    #     jobs = pd.concat([jobs_lahore, jobs_remote]).drop_duplicates(subset=['job_url'])
        
    #     # Optional: Extra filter to make sure they are actually remote if not in Lahore
    #     if not jobs.empty:
    #         jobs = jobs[
    #             jobs['location'].str.contains('Lahore', case=False, na=False) | 
    #             jobs['location'].str.contains('Remote', case=False, na=False)
    #         ]

    #     print(f"📊 Fresh jobs found: {len(jobs)}")
        
    #     for _, row in jobs.iterrows():
    #         print(f"FOUND: {row['title']} at {row['company']} ({row['location']})")

    # except Exception as e:
    #     print(f"❌ Scraper error: {e}")
    #     return

    # if not jobs.empty:
    #     import requests
    #     url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
    #     message = "🚀 *New DevOps Jobs Found!*\n\n"
    #     for _, row in jobs.iterrows():
    #         message += f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n\n"

    #     # Check exactly what is being sent
    #     print(f"DEBUG: Final URL: https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/HIDDEN_TOKEN")
    #     print(f"DEBUG: Final ChatId: {phone}@c.us")
    #     print(f"DEBUG: Jobs found to send: {len(jobs)}")

    #     # Make the request
        
    #     response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": message})
    #     print(f"API STATUS: {response.status_code}")
    #     print(f"API TEXT: {response.text}")
        
    #     requests.post(url, json={"chatId": f"{phone}@c.us", "message": message})
    #     print("📱 WhatsApp send attempted.")
    # else:
    #     print("📭 No jobs to send.")









# 3. Scraping Logic
    all_results = []
    
    # --- PHASE A: LAHORE ---
    try:
        print("🔍 Phase A: Scraping Lahore...")
        jobs_lahore = scrape_jobs(
            site_name=["linkedin", "indeed"],
            search_term="DevOps Engineer",
            location="Lahore",
            distance=100, 
            results_wanted=15,
            hours_old=24,
            country_indeed='pakistan'
        )
        print(f"✅ Found {len(jobs_lahore)} jobs in Lahore.")
        all_results.append(jobs_lahore)
    except Exception as e:
        print(f"⚠️ Phase A failed but continuing: {e}")

    # --- PHASE B: GLOBAL REMOTE ---
    try:
        print("🔍 Phase B: Scraping Global Remote (LinkedIn)...")
        # Explicitly setting country_indeed to 'usa' prevents the 'jordan' error
        jobs_remote_li = scrape_jobs(
            site_name=["linkedin"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=24
        )
        print(f"✅ Found {len(jobs_remote_li)} Global LinkedIn jobs.")
        all_results.append(jobs_remote_li)
    except Exception as e:
        print(f"⚠️ Phase B failed but continuing: {e}")

    # --- PHASE C: US REMOTE ---
    try:
        print("🔍 Phase C: Scraping US Remote (Indeed)...")
        jobs_remote_ind = scrape_jobs(
            site_name=["indeed"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=24,
            country_indeed='usa'
        )
        print(f"✅ Found {len(jobs_remote_ind)} US Indeed jobs.")
        all_results.append(jobs_remote_ind)
    except Exception as e:
        print(f"⚠️ Phase C failed but continuing: {e}")

    # --- DATA CONSOLIDATION & PRINTING ---
    if all_results:
        jobs = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        print(f"📊 Total unique jobs found: {len(jobs)}")
        
        # THIS IS WHERE YOUR DATA WILL SHOW IN THE CONSOLE:
        for _, row in jobs.iterrows():
            print(f"PIPELINE-DATA: {row['site']} | {row['title']} | {row['company']} | {row['location']}")
    else:
        print("❌ No jobs found in any phase.")
        return

if __name__ == "__main__":
    run_job_search()