import os
import sys
import requests
import pandas as pd
from datetime import datetime

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





    # PHASE A: LAHORE
    all_results = []
    cloud = ["DevOps Engineer", "Site Reliability Engineer", "SRE", "Cloud Engineer", "Platform Engineer", "DevSecOps Engineer", "Cloud Infrastructure Engineer", "Automation Engineer", "Kubernetes Engineer", "Azure Engineer", "AWS Engineer",]
    dev = ["Full Stack Developer", "Node.js Developer", "Python Developer", "Django", "MERN Stack"]

    SEARCH_LIST = cloud + dev
    SEARCH_TERM = " OR ".join(SEARCH_LIST)
    RESULTS_WANTED = 1000
    HOURS_OLD = 6

# A: LinkedIn Lahore
    try:
        print("🔍 Searching: LinkedIn Lahore...")
        res = scrape_jobs(site_name=["linkedin"], 
        search_term=SEARCH_TERM,
         location="Lahore",
          results_wanted=RESULTS_WANTED,
           hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

    # B: Indeed Lahore
    try:
        print("🔍 Searching: Indeed Lahore...")
        res = scrape_jobs(site_name=["indeed"],
         search_term=SEARCH_TERM,
          location="Lahore",
           results_wanted=RESULTS_WANTED,
            hours_old=HOURS_OLD, 
            country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

    # C: LinkedIn Pakistan Remote
    try:
        print("🔍 Searching: LinkedIn PK Remote...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="Pakistan",
           is_remote=True,
            results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)

        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

    # D: Indeed Pakistan Remote
    try:
        print("🔍 Searching: Indeed PK Remote...")
        res = scrape_jobs(site_name=["indeed"], 
        search_term=SEARCH_TERM,
         location="Remote",
          is_remote=True,
           results_wanted=RESULTS_WANTED,
            hours_old=HOURS_OLD,
             country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

    # E: Sweden
    try:
        print("🔍 Searching: Sweden...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="Sweden",
           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Sweden Error: {e}")

    # F: Luxembourg
    try:
        print("🔍 Searching: Luxembourg...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="Luxembourg",
           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Luxembourg Error: {e}")

    # G: France
    try:
        print("🔍 Searching: France...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="France",
           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ France Error: {e}")

    # # H: Germany
    try:
        print("🔍 Searching: Germany...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="Germany",
           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Germany Error: {e}")

    try:
        print("🔍 Searching: Germany...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term=SEARCH_TERM,
          location="Finland",
           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Germany Error: {e}")

    # I: Italy
    try:
        print("🔍 Searching: Italy...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Italy", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Italy Error: {e}")

    # J: Spain
    try:
        print("🔍 Searching: Spain...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Spain", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Spain Error: {e}")

    # K: Austria
    try:
        print("🔍 Searching: Austria...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Austria", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Austria Error: {e}")

    # L: Canada
    try:
        print("🔍 Searching: Canada...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Canada", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Canada Error: {e}")





    # # --- 2. PROCESSING ---
    # if all_results:
    #     df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
    #     # CONSOLE OUTPUT (Every job found)
    #     print("\n--- CONSOLE LOG: RAW JOBS ---")
    #     for _, row in df_all.iterrows():
    #         print(f"[{row.get('site', 'job')}] {row['title']} | {row['company']} | {row['location']}")

    #     # NOISE FILTER (Data/Database)
    #     good_keys = 'devops|sre|reliability|platform|infrastructure|cloud engineer|kubernetes|developer|fullstack|node|python|django|mern'
    #     df_all = df_all[df_all['title'].str.contains(good_keys, case=False, na=False)]
    #     bad_keys = 'cientist|testare'
    #     df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

    #     df_all['location'] = df_all['location'].fillna('').astype(str)

    #     # --- 3. WHATSAPP GROUPING (Updated for Europe) ---
    #     # is_local = df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)
    #     # is_europe = df_all['location'].str.contains('Sweden|Luxembourg|France|Germany', case=False, na=False)

    #     # --- 3. WHATSAPP GROUPING ---
    #     is_local = df_all['location'].str.contains('Lahore|Pakistan|Islamabad|Karachi', case=False, na=False)

    #     # Added major cities for the 4 countries to ensure no jobs are missed
    #     is_europe = df_all['location'].str.contains('Sweden|Stockholm|Gothenburg|Luxembourg|France|Paris|Lyon|Germany|Berlin|Munich|Hamburg|Frankfurt|Italy|Spain|Austria|Canada', case=False, na=False)

    #     # --- 4. BUILD MESSAGE ---
    #     msg = []
        
    #     # Section: Lahore & PK Remote
    #     msg.append("📍 *LAHORE & PK REMOTE*")
    #     local_df = df_all[is_local]
    #     if not local_df.empty:
    #         for _, row in local_df.iterrows():
    #             msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} ({row['site']})\n🔗 {row['job_url']}\n")
    #     else:
    #         msg.append("_No local jobs found._\n")

    #     # Section: Europe
    #     msg.append("---")
    #     msg.append("🇪🇺 *EUROPE DEVOPS (SE, LU, FR, DE)*")
    #     euro_df = df_all[is_europe]
    #     if not euro_df.empty:
    #         for _, row in euro_df.iterrows():
    #             msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")
    #     else:
    #         msg.append("_No jobs found in Europe._\n")

    #     final_msg = "\n".join(msg)

    #     # --- 5. SEND ---
    #     url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
    #     response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
    #     print(f"\n📡 WhatsApp Status: {response.status_code}")

    #     df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
    #     # Create a dynamic file name with today's date
    #     today = datetime.now().strftime("%Y-%m-%d_%H-%M")
    #     excel_file = f"Jobs_{today}.xlsx"
        
    #     # Save to Excel
    #     df_all.to_excel(excel_file, index=False)
    #     print(f"✅ Excel saved: {excel_file}")

    #     # CONSOLE OUTPUT 
    #     print("\n--- CONSOLE LOG: RAW JOBS ---")
            
    # else:
    #     print("📭 No jobs found.")















# --- 2. PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
        # Save Excel (Safe Mode)
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            excel_file = f"Jobs_{today}.xlsx"
            df_all.to_excel(excel_file, index=False)
            print(f"✅ Excel saved: {excel_file}")
        except Exception as e:
            print(f"⚠️ Excel save skipped: {e}")

        # --- NOISE FILTER & CATEGORIZATION ---
        df_all['location'] = df_all['location'].fillna('').astype(str)
        
        # Define filters based on your lists at the top
        cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
        dev_regex = 'fullstack|node|python|django|mern|developer'
        
        # Create separate DataFrames
        df_cloud = df_all[df_all['title'].str.contains(cloud_regex, case=False, na=False)]
        df_dev = df_all[df_all['title'].str.contains(dev_regex, case=False, na=False)]
        
        # --- 3. BUILD MESSAGE ---
        msg = ["🚀 *NEW JOB ALERTS*"]

        # SECTION 1: CLOUD & DEVOPS
        msg.append("\n☁️ *CLOUD & DEVOPS ROLES*")
        if not df_cloud.empty:
            for _, row in df_cloud.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")
        else:
            msg.append("_No Cloud jobs found in this run._\n")

        msg.append("---")

        # SECTION 2: SOFTWARE DEVELOPMENT
        msg.append("\n💻 *SOFTWARE & DEV ROLES*")
        if not df_dev.empty:
            for _, row in df_dev.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")
        else:
            msg.append("_No Dev jobs found in this run._\n")

        final_msg = "\n".join(msg)

        # --- 4. SEND ---
        if wa_id and wa_token and phone:
            url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
            response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
            print(f"📡 WhatsApp Status: {response.status_code}")
        else:
            print("❌ Secret keys missing. Message not sent.")
            
    else:
        print("📭 No jobs found.")

        
if __name__ == "__main__":
    run_job_search()