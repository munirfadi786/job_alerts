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

# --- PROCESSING & SENDING ---
    if all_results:
        # 1. Merge and clean base data
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
        # Standardize location column for filtering
        df_all['location'] = df_all['location'].fillna('').astype(str)
        
        # 2. SEPARATE DATA: Lahore vs. The Rest
        # We look for "Lahore" in the location string
        is_lahore = df_all['location'].str.contains('Lahore', case=False, na=False)
        jobs_lahore = df_all[is_lahore].copy()
        jobs_others = df_all[~is_lahore].copy()

        # 3. APPLY FILTERS TO NON-LAHORE JOBS ONLY
        if not jobs_others.empty:
            # A. Exclude India (as per your working filter)
            jobs_others = jobs_others[~jobs_others['location'].str.contains('India', case=False, na=False)]
            
            # B. Exclude Reposted (Deep scan in description/title)
            for col in ['description', 'title']:
                if col in jobs_others.columns:
                    jobs_others = jobs_others[~jobs_others[col].str.contains('Reposted', case=False, na=False)]
            
            # C. Applicant Filter: Remove if > 40 applicants
            # JobSpy uses 'emails_count' to estimate LinkedIn/Indeed applicants
            if 'emails_count' in jobs_others.columns:
                jobs_others['emails_count'] = pd.to_numeric(jobs_others['emails_count'], errors='coerce').fillna(0)
                jobs_others = jobs_others[jobs_others['emails_count'] <= 40]
            
            print(f"✂️ Global Filtered: {len(jobs_others)} jobs remaining.")

        # 4. BUILD SEPARATE MESSAGES
        final_message = ""

        # Section 1: Lahore
        if not jobs_lahore.empty:
            final_message += "📍 *LAHORE - LOCAL JOBS*\n"
            for _, row in jobs_lahore.iterrows():
                final_message += f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n\n"
            final_message += "---\n\n"

        # Section 2: Global/Remote
        if not jobs_others.empty:
            final_message += "🌍 *REMOTE & GLOBAL (Filtered <40 applicants)*\n"
            for _, row in jobs_others.iterrows():
                final_message += f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n\n"

        # 5. SEND TO WHATSAPP
        if final_message:
            import requests
            url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
            target_chat = f"{phone}@c.us"
            response = requests.post(url, json={"chatId": target_chat, "message": final_message})
            print(f"📡 API Status: {response.status_code}")
        else:
            print("📭 No jobs survived the filters.")
            
    else:
        print("📭 No jobs found at all.")
if __name__ == "__main__":
    run_job_search()