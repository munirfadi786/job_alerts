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
import os
import sys
import pandas as pd
import requests

def run_job_search():
    # --- CONFIGURATION ---
    wa_id = "PLACEHOLDER_WA_ID"
    wa_token = "PLACEHOLDER_WA_TOKEN"
    phone = "PLACEHOLDER_PHONE"

    try:
        from jobspy import scrape_jobs
        print("✅ Jobspy loaded successfully!")
    except ImportError:
        print("❌ ImportError: Jobspy not found.")
        return

    all_results = []
    
    # 1. LAHORE - LINKEDIN
    try:
        print("🔍 Phase A1: Scraping Lahore (LinkedIn)...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=4)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Phase A1 Error: {e}")

    # 2. LAHORE - INDEED
    try:
        print("🔍 Phase A2: Scraping Lahore (Indeed)...")
        res = scrape_jobs(site_name=["indeed"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=4, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Phase A2 Error: {e}")
    
    # 3. PAKISTAN REMOTE
    try:
        print("🔍 Phase B: Scraping LinkedIn Pakistan Remote...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Pakistan", is_remote=True, results_wanted=15, hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Phase B Error: {e}")

    # 4. UAE (NEW ADDITION)
    try:
        print("🔍 Phase UAE: Scraping LinkedIn UAE...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="United Arab Emirates", results_wanted=10, hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ UAE Error: {e}")

    # 5. GLOBAL REMOTE (US/UK/Canada)
    try:
        print("🔍 Phase Global: Scraping Global Remote...")
        res_li = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Remote", results_wanted=15, hours_old=2)
        res_us = scrape_jobs(site_name=["indeed"], search_term="DevOps Engineer", location="Remote", results_wanted=15, hours_old=2, country_indeed='usa')
        if not res_li.empty: all_results.append(res_li)
        if not res_us.empty: all_results.append(res_us)
    except Exception as e: print(f"⚠️ Global Error: {e}")

    # --- PROCESSING & SENDING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
        # PRINT TO CONSOLE AS REQUESTED
        print("\n--- JOBS FOUND IN CONSOLE ---")
        for _, row in df_all.iterrows():
            print(f"FOUND: {row['title']} | {row['company']} | {row['location']}")

        # MINOR CHANGE: Filter out Database/Platform noise
        bad_keys = 'database|data platform|data engineer'
        df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

        df_all['location'] = df_all['location'].fillna('').astype(str)
        
        # SEPARATE DATA
        is_lahore = df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)
        is_uae = df_all['location'].str.contains('United Arab Emirates|UAE', case=False, na=False)
        
        jobs_lahore = df_all[is_lahore].copy()
        jobs_uae = df_all[is_uae].copy()
        jobs_others = df_all[~(is_lahore | is_uae)].copy()

        # BUILD THE MESSAGE
        message_parts = []
        
        message_parts.append("📍 *LAHORE & PK REMOTE*")
        for _, row in jobs_lahore.iterrows():
            message_parts.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n")
        
        if not jobs_uae.empty:
            message_parts.append("---\n🇦🇪 *UAE JOBS*")
            for _, row in jobs_uae.iterrows():
                message_parts.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n")

        message_parts.append("---\n🌍 *REMOTE ONLY (Global)*")
        for _, row in jobs_others.head(10).iterrows():
            message_parts.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")

        final_message = "\n".join(message_parts)

        # SEND TO WHATSAPP
        url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
        response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_message})
        print(f"📡 Status: {response.status_code} | Total Clean Jobs: {len(df_all)}")
            
    else:
        print("📭 No jobs found.")

if __name__ == "__main__":
    run_job_search()