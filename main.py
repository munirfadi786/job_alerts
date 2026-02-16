import os
import sys
import requests
import pandas as pd

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

# # PHASE A1: LAHORE - LINKEDIN ONLY
#     try:
#         print("🔍 Phase A1: Scraping Lahore (LinkedIn)...")
#         jobs_lahore_li = scrape_jobs(
#             site_name=["linkedin"],
#             search_term="DevOps Engineer",
#             location="Lahore",
#             results_wanted=10,
#             hours_old=4
#         )
#         if not jobs_lahore_li.empty:
#             all_results.append(jobs_lahore_li)
#             print(f"✅ LinkedIn Lahore: {len(jobs_lahore_li)} jobs.")
#     except Exception as e:
#         print(f"⚠️ Phase A1 Error: {e}")

#     # PHASE A2: LAHORE - INDEED ONLY
#     try:
#         print("🔍 Phase A2: Scraping Lahore (Indeed)...")
#         jobs_lahore_in = scrape_jobs(
#             site_name=["indeed"],
#             search_term="DevOps Engineer",
#             location="Lahore",
#             results_wanted=10,
#             hours_old=4,
#             country_indeed='pakistan'
#         )
#         if not jobs_lahore_in.empty:
#             all_results.append(jobs_lahore_in)
#             print(f"✅ Indeed Lahore: {len(jobs_lahore_in)} jobs.")
#     except Exception as e:
#         print(f"⚠️ Phase A2 Error: {e}")
    
#     # PHASE B: LINKEDIN PAKISTAN REMOTE
#     try:
#         print("🔍 Phase B: Scraping LinkedIn Pakistan Remote...")
#         jobs_pk_remote = scrape_jobs(
#             site_name=["linkedin"], 
#             search_term="DevOps Engineer",
#             location="Pakistan",
#             is_remote=True,      # This catches "Pakistan (Remote)"
#             results_wanted=15,
#             hours_old=24         # Expanded hours to catch Ciklum-style posts
#         )
#         if not jobs_pk_remote.empty:
#             all_results.append(jobs_pk_remote)
#             print("✅ Phase B Success.")
#     except Exception as e:
#         print(f"⚠️ Phase B Error: {e}")

#     # PHASE B: LINKEDIN GLOBAL
#     try:
#         print("🔍 Phase B: Scraping LinkedIn Global...")
#         jobs_li = scrape_jobs(
#             site_name=["linkedin"], 
#             search_term="DevOps Engineer",
#             location="Remote",
#             results_wanted=15,
#             hours_old=2
#         )
#         if not jobs_li.empty:
#             all_results.append(jobs_li)
#             print("✅ Phase B Success.")
#     except Exception as e:
#         print(f"⚠️ Phase B Error: {e}")

#     # PHASE C: US REMOTE
#     try:
#         print("🔍 Phase C: Scraping US Remote...")
#         jobs_us = scrape_jobs(
#             site_name=["indeed"], 
#             search_term="DevOps Engineer",
#             location="Remote",
#             results_wanted=15,
#             hours_old=2,
#             country_indeed='usa' 
#         )
#         if not jobs_us.empty:
#             all_results.append(jobs_us)
#             print("✅ Phase C Success.")
#     except Exception as e:
#         print(f"⚠️ Phase C Error: {e}")

#     # PHASE D: UK REMOTE
#     try:
#         print("🔍 Phase D: Scraping UK Remote...")
#         jobs_uk = scrape_jobs(
#             site_name=["indeed"], 
#             search_term="DevOps Engineer",
#             location="Remote",
#             results_wanted=15,
#             hours_old=2,
#             country_indeed='uk' 
#         )
#         if not jobs_uk.empty:
#             all_results.append(jobs_uk)
#             print("✅ Phase D Success.")
#     except Exception as e:
#         print(f"⚠️ Phase D Error: {e}")

#     # PHASE E: CANADA REMOTE
#     try:
#         print("🔍 Phase E: Scraping Canada Remote...")
#         jobs_ca = scrape_jobs(
#             site_name=["indeed"], 
#             search_term="DevOps Engineer",
#             location="Remote",
#             results_wanted=15,
#             hours_old=2,
#             country_indeed='canada' # Use 'canada' instead of 'ca' to be safe
#         )
#         if not jobs_ca.empty:
#             all_results.append(jobs_ca)
#             print("✅ Phase E Success.")
#     except Exception as e:
#         print(f"⚠️ Phase E Error: {e}")

# # --- PROCESSING & SENDING ---
#     if all_results:
#         # 1. Merge and clean base data
#         df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
#         df_all['location'] = df_all['location'].fillna('').astype(str)
        
#         # 2. SEPARATE DATA: Lahore vs. The Rest
#         is_lahore = df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)
#         jobs_lahore = df_all[is_lahore].copy()
#         jobs_others = df_all[~is_lahore].copy()

#         # 3. APPLY FILTERS TO GLOBAL JOBS (Excluding India & Non-Remote)
#         if not jobs_others.empty:
#             # Only keep jobs marked as Remote
#             if 'is_remote' in jobs_others.columns:
#                 jobs_others = jobs_others[jobs_others['is_remote'] == True]
            
#             # EXCLUDE INDIA (Still strictly here)
#             jobs_others = jobs_others[~jobs_others['location'].str.contains('India', case=False, na=False)]
            
#             # TITLE CLEANUP (Remove Reposts)
#             jobs_others = jobs_others[~jobs_others['title'].str.contains('reposted|re-posted', case=False, na=False)]
            
#             print(f"✂️ Global Filtered: {len(jobs_others)} jobs remaining.")

#         # 4. BUILD THE MESSAGE
#         message_parts = []

#         # Section 1: Lahore (Handle "No Jobs" case)
#         message_parts.append("📍 *LAHORE - LOCAL JOBS*")
#         if not jobs_lahore.empty:
#             for _, row in jobs_lahore.iterrows():
#                 message_parts.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n")
#         else:
#             message_parts.append("_No local jobs found in the last hour._\n")

#         message_parts.append("---") # Visual Separator

#         # Section 2: Global/Remote
#         message_parts.append("🌍 *REMOTE ONLY (Global)*")
#         if not jobs_others.empty:
#             for _, row in jobs_others.iterrows():
#                 message_parts.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")
#         else:
#             message_parts.append("_No fresh remote jobs found after filtering._")

#         # Combine all parts into one string
#         final_message = "\n".join(message_parts)

#         # 5. SEND TO WHATSAPP
#         import requests
#         url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
#         target_chat = f"{phone}@c.us"
#         response = requests.post(url, json={"chatId": target_chat, "message": final_message})
        
#         print(f"📡 API Status: {response.status_code}")
#         print(f"📊 Final Stats: Lahore: {len(jobs_lahore)} | Global: {len(jobs_others)}")
            
#     else:
#         print("📭 No jobs found in any phase.")

# if __name__ == "__main__":
#     run_job_search()

# A: LinkedIn Lahore
    try:
        print("🔍 Searching: LinkedIn Lahore...")
        res = scrape_jobs(site_name=["linkedin"], 
        search_term="DevOps Engineer",
         location="Lahore",
          results_wanted=10,
           hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

    # B: Indeed Lahore
    try:
        print("🔍 Searching: Indeed Lahore...")
        res = scrape_jobs(site_name=["indeed"],
         search_term="DevOps Engineer",
          location="Lahore",
           results_wanted=10,
            hours_old=24, 
            country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

    # C: LinkedIn Pakistan Remote
    try:
        print("🔍 Searching: LinkedIn PK Remote...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term="DevOps Engineer",
          location="Pakistan",
           is_remote=True,
            results_wanted=10, hours_old=24)

        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

    # D: Indeed Pakistan Remote
    try:
        print("🔍 Searching: Indeed PK Remote...")
        res = scrape_jobs(site_name=["indeed"], 
        search_term="DevOps Engineer",
         location="Remote",
          is_remote=True,
           results_wanted=10,
            hours_old=24,
             country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

    # E: UAE All DevOps
    try:
        print("🔍 Searching: UAE...")
        res = scrape_jobs(site_name=["linkedin"],
         search_term="DevOps Engineer",
          location="United Arab Emirates",
           results_wanted=15, hours_old=3)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ UAE Error: {e}")

    # F: Global Remote
# F1: Global Remote - LinkedIn
    try:
        print("🔍 Searching: Global Remote (LinkedIn)...")
        res_li = scrape_jobs(
            site_name=["linkedin"], 
            search_term="DevOps Engineer", 
            location="Remote", 
            is_remote=True, 
            results_wanted=20, 
            hours_old=2
        )
        if not res_li.empty: all_results.append(res_li)
    except Exception as e: print(f"⚠️ Global LinkedIn Error: {e}")

    # F2: Global Remote - Indeed
    try:
        print("🔍 Searching: Global Remote (Indeed)...")
        res_in = scrape_jobs(
            site_name=["indeed"], 
            search_term="DevOps Engineer", 
            location="Remote", 
            is_remote=True, 
            results_wanted=20, 
            hours_old=2
        )
        if not res_in.empty: all_results.append(res_in)
    except Exception as e: print(f"⚠️ Global Indeed Error: {e}")

    # --- 2. PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
        # CONSOLE OUTPUT (Every job found)
        print("\n--- CONSOLE LOG: RAW JOBS ---")
        for _, row in df_all.iterrows():
            print(f"[{row.get('site', 'job')}] {row['title']} | {row['company']} | {row['location']}")

        # NOISE FILTER (Data/Database)
        bad_keys = 'database|data platform|data engineer|dba'
        df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

        df_all['location'] = df_all['location'].fillna('').astype(str)
        # df_all['location'] = df_all['location'].fillna('Pakistan').replace('Pakistan')

        
        # --- 3. WHATSAPP GROUPING ---
        is_local = df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)
        is_uae = df_all['location'].str.contains('United Arab Emirates|UAE|Dubai|Abu Dhabi', case=False, na=False)
        is_global = ~(is_local | is_uae)

        if 'is_remote' in df_all.columns:
            is_global = is_global & ((df_all['is_remote'] == True) | (df_all['location'] == ''))

        # --- 4. BUILD MESSAGE ---
        msg = []
        
        # Section: Lahore & PK Remote
        msg.append("📍 *LAHORE & PK REMOTE*")
        local_df = df_all[is_local]
        if not local_df.empty:
            for _, row in local_df.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} ({row['site']})\n🔗 {row['job_url']}\n")
        else:
            msg.append("_No local jobs found._\n")

        # Section: UAE
        uae_df = df_all[is_uae]
        if not uae_df.empty:
            msg.append("---")
            msg.append("🇦🇪 *UAE DEVOPS*")
            for _, row in uae_df.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n")

        # Section: Global
        global_df = df_all[is_global]
        if not global_df.empty:
            msg.append("---")
            msg.append("🌍 *GLOBAL REMOTE*")
            for _, row in global_df.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")

        final_msg = "\n".join(msg)

        # --- 5. SEND ---
        url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
        response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
        print(f"\n📡 WhatsApp Status: {response.status_code}")
            
    else:
        print("📭 No jobs found.")

if __name__ == "__main__":
    run_job_search()