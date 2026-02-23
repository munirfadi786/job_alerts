# import os
# import sys
# import requests
# import pandas as pd

# def run_job_search():
#     # 1. Print Debug Information
#     print("--- DEBUGGING ENVIRONMENT ---")
#     print(f"Python Executable: {sys.executable}")
    
#     # Check Secrets
#     def mask(s):
#         return f"{s[:4]}****{s[-4:]}" if s and len(s) > 8 else "EMPTY ❌"

#     wa_id = os.getenv("WA_INSTANCE_ID")
#     wa_token = os.getenv("WA_TOKEN")
#     phone = os.getenv("MY_PHONE")

#     print(f"WA_INSTANCE_ID: {wa_id if wa_id else 'EMPTY ❌'}")
#     print(f"WA_TOKEN: {mask(wa_token)}")
#     print(f"MY_PHONE: {mask(phone)}")
#     print("----------------------------")

#     # 2. Import Libraries inside the function
#     try:
#         from jobspy import scrape_jobs
#         import pandas as pd
#         print("✅ Jobspy loaded successfully!")
#     except ImportError:
#         print("❌ Still failing to load Jobspy. Printing sys.path:")
#         print(sys.path)
#         return

#     # PHASE A: LAHORE
#     all_results = []

# # A: LinkedIn Lahore
#     try:
#         print("🔍 Searching: LinkedIn Lahore...")
#         res = scrape_jobs(site_name=["linkedin"], 
#         search_term="DevOps Engineer",
#          location="Lahore",
#           results_wanted=10,
#            hours_old=2)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

#     # B: Indeed Lahore
#     try:
#         print("🔍 Searching: Indeed Lahore...")
#         res = scrape_jobs(site_name=["indeed"],
#          search_term="DevOps Engineer",
#           location="Lahore",
#            results_wanted=10,
#             hours_old=2, 
#             country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

#     # C: LinkedIn Pakistan Remote
#     try:
#         print("🔍 Searching: LinkedIn PK Remote...")
#         res = scrape_jobs(site_name=["linkedin"],
#          search_term="DevOps Engineer",
#           location="Pakistan",
#            is_remote=True,
#             results_wanted=10, hours_old=2)

#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

#     # D: Indeed Pakistan Remote
#     try:
#         print("🔍 Searching: Indeed PK Remote...")
#         res = scrape_jobs(site_name=["indeed"], 
#         search_term="DevOps Engineer",
#          location="Remote",
#           is_remote=True,
#            results_wanted=10,
#             hours_old=5,
#              country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

#     # E: UAE All DevOps
#     try:
#         print("🔍 Searching: UAE...")
#         res = scrape_jobs(site_name=["linkedin"],
#          search_term="DevOps Engineer",
#           location="United Arab Emirates",
#            results_wanted=15, hours_old=3)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ UAE Error: {e}")

#     # F: Global Remote
# # F1: Global Remote - LinkedIn
#     try:
#         print("🔍 Searching: Global Remote (LinkedIn)...")
#         res_li = scrape_jobs(
#             site_name=["linkedin"], 
#             search_term="DevOps Engineer", 
#             location="Remote", 
#             is_remote=True, 
#             results_wanted=20, 
#             hours_old=2
#         )
#         if not res_li.empty: all_results.append(res_li)
#     except Exception as e: print(f"⚠️ Global LinkedIn Error: {e}")

#     # F2: Global Remote - Indeed
#     try:
#         print("🔍 Searching: Global Remote (Indeed)...")
#         res_in = scrape_jobs(
#             site_name=["indeed"], 
#             search_term="DevOps Engineer", 
#             location="Remote", 
#             is_remote=True, 
#             results_wanted=20, 
#             hours_old=2
#         )
#         if not res_in.empty: all_results.append(res_in)
#     except Exception as e: print(f"⚠️ Global Indeed Error: {e}")

#     # --- 2. PROCESSING ---
#     if all_results:
#         df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        
#         # CONSOLE OUTPUT (Every job found)
#         print("\n--- CONSOLE LOG: RAW JOBS ---")
#         for _, row in df_all.iterrows():
#             print(f"[{row.get('site', 'job')}] {row['title']} | {row['company']} | {row['location']}")

#         # NOISE FILTER (Data/Database)
#         bad_keys = 'database|data platform|data engineer|dba'
#         df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

#         df_all['location'] = df_all['location'].fillna('').astype(str)
#         # df_all['location'] = df_all['location'].fillna('Pakistan').replace('Pakistan')

        
#         # --- 3. WHATSAPP GROUPING ---
#         is_local = df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)
#         is_uae = df_all['location'].str.contains('United Arab Emirates|UAE|Dubai|Abu Dhabi', case=False, na=False)
#         is_global = ~(is_local | is_uae)

#         if 'is_remote' in df_all.columns:
#             is_global = is_global & ((df_all['is_remote'] == True) | (df_all['location'] == ''))

#         # --- 4. BUILD MESSAGE ---
#         msg = []
        
#         # Section: Lahore & PK Remote
#         msg.append("📍 *LAHORE & PK REMOTE*")
#         local_df = df_all[is_local]
#         if not local_df.empty:
#             for _, row in local_df.iterrows():
#                 msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} ({row['site']})\n🔗 {row['job_url']}\n")
#         else:
#             msg.append("_No local jobs found._\n")

#         # Section: UAE
#         uae_df = df_all[is_uae]
#         if not uae_df.empty:
#             msg.append("---")
#             msg.append("🇦🇪 *UAE DEVOPS*")
#             for _, row in uae_df.iterrows():
#                 msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}\n")

#         # Section: Global
#         global_df = df_all[is_global]
#         if not global_df.empty:
#             msg.append("---")
#             msg.append("🌍 *GLOBAL REMOTE*")
#             for _, row in global_df.iterrows():
#                 msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} | 📍 {row['location']}\n🔗 {row['job_url']}\n")

#         final_msg = "\n".join(msg)

#         # --- 5. SEND ---
#         url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
#         response = requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
#         print(f"\n📡 WhatsApp Status: {response.status_code}")
            
#     else:
#         print("📭 No jobs found.")

# if __name__ == "__main__":
#     run_job_search()








import os
import sys
import requests
import pandas as pd
import time

def run_job_search():
    # --- 1. DEBUG & SETUP ---
    wa_id = os.getenv("WA_INSTANCE_ID")
    wa_token = os.getenv("WA_TOKEN")
    phone = os.getenv("MY_PHONE")

    try:
        from jobspy import scrape_jobs
        print("✅ Jobspy loaded successfully!")
    except ImportError:
        print("❌ Failed to load Jobspy.")
        return

    all_results = []
    url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"

    # --- PHASE A: LAHORE & PAKISTAN (ORIGINAL) ---
    try:
        print("🔍 Searching: LinkedIn Lahore...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=2)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

    try:
        print("🔍 Searching: Indeed Lahore...")
        res = scrape_jobs(site_name=["indeed"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=2, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

    try:
        print("🔍 Searching: LinkedIn PK Remote...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Pakistan", is_remote=True, results_wanted=10, hours_old=2)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

    # --- PHASE B: UAE (ORIGINAL) ---
    try:
        print("🔍 Searching: UAE...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="United Arab Emirates", results_wanted=15, hours_old=3)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ UAE Error: {e}")

    # --- PHASE C: SCHENGEN LOOP ---
    schengen_countries = [
        {"name": "Sweden", "code": "se"}, {"name": "Germany", "code": "de"},
        {"name": "France", "code": "fr"}, {"name": "Italy", "code": "it"},
        {"name": "Spain", "code": "es"}, {"name": "Netherlands", "code": "nl"},
        {"name": "Switzerland", "code": "ch"}, {"name": "Belgium", "code": "be"},
        {"name": "Austria", "code": "at"}, {"name": "Luxembourg", "code": "lu"}
    ]

    for country in schengen_countries:
        try:
            print(f"🔍 Searching: {country['name']}...")
            res_eu = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location=country['name'], results_wanted=5, hours_old=48)
            if not res_eu.empty: all_results.append(res_eu)
            time.sleep(1) 
        except Exception as e: 
            print(f"⚠️ {country['name']} Error: {e}")

    # --- 2. PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        df_all['location'] = df_all['location'].fillna('').astype(str)
        bad_keys = 'database|data platform|data engineer|dba'
        df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

        # --- 3. LOGGING & WHATSAPP FUNCTION ---
        def process_and_send(title, df_section):
            if df_section.empty: 
                print(f"ℹ️ Section {title}: No jobs found.")
                return
            
            # Action Console Output
            print(f"\n--- CONSOLE LOG: {title} ---")
            
            header = f"🚀 *{title} ({len(df_section)} Jobs Found)*\n"
            lines = []
            for i, (_, row) in enumerate(df_section.iterrows(), 1):
                # Clean text for console
                print(f"{i}. {row['title']} | {row['company']} | {row['location']}")
                
                # Format for WhatsApp
                entry = f"{i}. *{row['title']}*\n🏢 {row['company']}\n📍 {row['location']}\n🔗 {row['job_url']}\n"
                lines.append(entry)
                
                # Split WhatsApp message if too long
                if len("\n".join(lines)) > 3000:
                    requests.post(url, json={"chatId": f"{phone}@c.us", "message": header + "\n".join(lines)})
                    lines = []
                    header = f"🚀 *{title} (Continued)*\n"

            if lines:
                requests.post(url, json={"chatId": f"{phone}@c.us", "message": header + "\n".join(lines)})
            print(f"✅ WhatsApp Section '{title}' Sent.")

        # --- 4. CATEGORIZE & RUN ---
        # 1. Lahore & PK
        pk_df = df_all[df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)]
        process_and_send("LAHORE & PK", pk_df)

        # 2. UAE
        uae_df = df_all[df_all['location'].str.contains('United Arab Emirates|UAE|Dubai', case=False, na=False)]
        process_and_send("UAE DEVOPS", uae_df)

        # 3. Sweden
        swe_df = df_all[df_all['location'].str.contains('Sweden|Stockholm', case=False, na=False)]
        process_and_send("SWEDEN", swe_df)

        # 4. Other Schengen
        others_df = df_all[~df_all['location'].str.contains('Lahore|Pakistan|UAE|Dubai|Sweden', case=False, na=False)]
        process_and_send("OTHER SCHENGEN", others_df)

        print("\n--- ALL TASKS COMPLETED ---")
    else:
        print("📭 No jobs found in any region.")

if __name__ == "__main__":
    run_job_search()