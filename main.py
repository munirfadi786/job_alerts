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

def run_job_search():
    # --- 1. DEBUG & SETUP (ORIGINAL) ---
    print("--- DEBUGGING ENVIRONMENT ---")
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

    # --- PHASE A: LAHORE & PAKISTAN (STRICTLY ORIGINAL) ---
    # A1: LinkedIn Lahore
    try:
        print("🔍 Searching: LinkedIn Lahore...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

    # A2: Indeed Lahore
    try:
        print("🔍 Searching: Indeed Lahore...")
        res = scrape_jobs(site_name=["indeed"], search_term="DevOps Engineer", location="Lahore", results_wanted=10, hours_old=24, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

    # A3: LinkedIn Pakistan Remote
    try:
        print("🔍 Searching: LinkedIn PK Remote...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="Pakistan", is_remote=True, results_wanted=10, hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

    # A4: Indeed Pakistan Remote
    try:
        print("🔍 Searching: Indeed PK Remote...")
        res = scrape_jobs(site_name=["indeed"], search_term="DevOps Engineer", location="Remote", is_remote=True, results_wanted=10, hours_old=5, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

    # --- PHASE B: UAE (STRICTLY ORIGINAL) ---
    try:
        print("🔍 Searching: UAE...")
        res = scrape_jobs(site_name=["linkedin"], search_term="DevOps Engineer", location="United Arab Emirates", results_wanted=15, hours_old=24)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ UAE Error: {e}")

    # --- PHASE C: FULL SCHENGEN LIST (COUNTRY BY COUNTRY) ---
    # This list covers all 29 Schengen states as of 2026
    schengen_countries = [
        {"name": "Sweden", "code": "se"}, {"name": "Germany", "code": "de"},
        {"name": "France", "code": "fr"}, {"name": "Italy", "code": "it"},
        {"name": "Spain", "code": "es"}, {"name": "Netherlands", "code": "nl"},
        {"name": "Switzerland", "code": "ch"}, {"name": "Belgium", "code": "be"},
        {"name": "Austria", "code": "at"}, {"name": "Norway", "code": "no"},
        {"name": "Denmark", "code": "dk"}, {"name": "Finland", "code": "fi"},
        {"name": "Luxembourg", "code": "lu"}, {"name": "Portugal", "code": "pt"},
        {"name": "Poland", "code": "pl"}, {"name": "Czech Republic", "code": "cz"},
        {"name": "Greece", "code": "gr"}, {"name": "Hungary", "code": "hu"},
        {"name": "Iceland", "code": "is"}, {"name": "Estonia", "code": "ee"},
        {"name": "Latvia", "code": "lv"}, {"name": "Lithuania", "code": "lt"},
        {"name": "Slovakia", "code": "sk"}, {"name": "Slovenia", "code": "si"},
        {"name": "Malta", "code": "mt"}, {"name": "Croatia", "code": "hr"},
        {"name": "Bulgaria", "code": "bg"}, {"name": "Romania", "code": "ro"},
        {"name": "Liechtenstein", "code": "li"}
    ]

    for country in schengen_countries:
        try:
            print(f"🔍 Searching Schengen: {country['name']}...")
            res_eu = scrape_jobs(
                site_name=["linkedin"], 
                search_term="DevOps Engineer", 
                location=country['name'], 
                results_wanted=50, 
                hours_old=24
            )
            if not res_eu.empty: all_results.append(res_eu)
        except Exception as e: print(f"⚠️ {country['name']} Error: {e}")

    # --- 2. PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        df_all['location'] = df_all['location'].fillna('').astype(str)
        
        # Noise Filter
        bad_keys = 'database|data platform|data engineer|dba'
        df_all = df_all[~df_all['title'].str.contains(bad_keys, case=False, na=False)]

        # --- 3. WHATSAPP MESSAGE BUILDING ---
        msg = ["🚀 *DAILY DEVOPS JOB FEED*"]

        # 1. LAHORE / PK Section
        local_df = df_all[df_all['location'].str.contains('Lahore|Pakistan', case=False, na=False)]
        if not local_df.empty:
            msg.append("\n📍 *LAHORE & PK REMOTE*")
            for _, row in local_df.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']} ({row['site']})\n🔗 {row['job_url']}")

        # 2. UAE Section
        uae_df = df_all[df_all['location'].str.contains('United Arab Emirates|UAE|Dubai', case=False, na=False)]
        if not uae_df.empty:
            msg.append("\n🇦🇪 *UAE DEVOPS*")
            for _, row in uae_df.iterrows():
                msg.append(f"🔹 *{row['title']}*\n🏢 {row['company']}\n🔗 {row['job_url']}")

        # 3. SCHENGEN Section
        # Matches any country in our list
        schengen_names = "|".join([c['name'] for c in schengen_countries])
        eur_df = df_all[df_all['location'].str.contains(schengen_names, case=False, na=False)]
        if not eur_df.empty:
            msg.append("\n🇪🇺 *SCHENGEN AREA*")
            for _, row in eur_df.iterrows():
                msg.append(f"🔹 *{row['title']}* | 📍 {row['location']}\n🏢 {row['company']}\n🔗 {row['job_url']}")

        final_msg = "\n".join(msg)
        if len(final_msg) > 4000: final_msg = final_msg[:4000] + "..."

        # --- 4. SEND ---
        url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
        requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
        print("📡 Report Sent to WhatsApp!")
    else:
        print("📭 No jobs found.")

if __name__ == "__main__":
    run_job_search()