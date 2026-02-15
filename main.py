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







# --- SCRAPING LOGIC ---all_results = []
    
    # PHASE A: LAHORE
    all_results = []
    try:
        print("🔍 Phase A: Scraping Lahore...")
        jobs_lahore = scrape_jobs(
            site_name=["linkedin", "indeed"],
            search_term="DevOps Engineer",
            location="Lahore",
            results_wanted=10,
            hours_old=1,
            country_indeed='pakistan'
        )
        if not jobs_lahore.empty:
            all_results.append(jobs_lahore)
            print("✅ Phase A Success.")
    except Exception as e:
        print(f"⚠️ Phase A Error: {e}")

    # PHASE B: LINKEDIN GLOBAL
    try:
        print("🔍 Phase B: Scraping LinkedIn Global...")
        jobs_li = scrape_jobs(
            site_name=["linkedin"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=1
        )
        if not jobs_li.empty:
            all_results.append(jobs_li)
            print("✅ Phase B Success.")
    except Exception as e:
        print(f"⚠️ Phase B Error: {e}")

    # PHASE C: US REMOTE
    try:
        print("🔍 Phase C: Scraping US Remote...")
        jobs_us = scrape_jobs(
            site_name=["indeed"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=1,
            country_indeed='usa' 
        )
        if not jobs_us.empty:
            all_results.append(jobs_us)
            print("✅ Phase C Success.")
    except Exception as e:
        print(f"⚠️ Phase C Error: {e}")

    # PHASE D: UK REMOTE
    try:
        print("🔍 Phase D: Scraping UK Remote...")
        jobs_uk = scrape_jobs(
            site_name=["indeed"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=1,
            country_indeed='uk' 
        )
        if not jobs_uk.empty:
            all_results.append(jobs_uk)
            print("✅ Phase D Success.")
    except Exception as e:
        print(f"⚠️ Phase D Error: {e}")

    # PHASE E: CANADA REMOTE
    try:
        print("🔍 Phase E: Scraping Canada Remote...")
        jobs_ca = scrape_jobs(
            site_name=["indeed"], 
            search_term="DevOps Engineer",
            location="Remote",
            results_wanted=15,
            hours_old=1,
            country_indeed='canada' # Use 'canada' instead of 'ca' to be safe
        )
        if not jobs_ca.empty:
            all_results.append(jobs_ca)
            print("✅ Phase E Success.")
    except Exception as e:
        print(f"⚠️ Phase E Error: {e}")

# --- PROCESSING & SENDING ---
    if all_results:
        # 1. Merge all found data
        jobs = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        print(f"📊 Total jobs found before filtering: {len(jobs)}")

        # 2. FILTER: Exclude India (Keeping your working logic)
        if 'location' in jobs.columns:
            jobs = jobs[~jobs['location'].str.contains('India', case=False, na=False)]
            print(f"✂️ Removed jobs from India. Remaining: {len(jobs)}")

        # 3. FILTER: Exclude Reposted Jobs (Improved)
        # Check 1: The boolean column
        if 'is_reposted' in jobs.columns:
            jobs = jobs[jobs['is_reposted'] != True]
        
        # Check 2: String matching for "Reposted" in Description or Title
        # This catches LinkedIn's "Reposted 1 hour ago" text hidden in the data
        text_cols = ['description', 'title']
        for col in text_cols:
            if col in jobs.columns:
                jobs = jobs[~jobs[col].str.contains('Reposted', case=False, na=False)]
        
        print(f"✂️ Removed all Reposted jobs. Remaining: {len(jobs)}")

        # 4. FINAL LOG: Print clean data to console
        for _, row in jobs.iterrows():
            print(f"CLEAN-DATA: {row['site']} | {row['title']} | {row['location']}")

        # 5. SEND TO WHATSAPP
        if not jobs.empty:
            import requests
            url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
            
            message = "🚀 *DevOps Job Alert (Fresh & Global)*\n\n"
            for _, row in jobs.iterrows():
                # We use .get() to avoid errors if a column is missing
                message += f"🔹 *{row.get('title', 'N/A')}*\n🏢 {row.get('company', 'N/A')} | 📍 {row.get('location', 'N/A')}\n🔗 {row.get('job_url', 'N/A')}\n\n"

            target_chat = f"{phone}@c.us"
            response = requests.post(url, json={"chatId": target_chat, "message": message})
            print(f"📡 API Status: {response.status_code}")
        else:
            print("📭 No jobs left after filtering.")
            
    else:
        print("📭 No raw jobs found to process.")
if __name__ == "__main__":
    run_job_search()