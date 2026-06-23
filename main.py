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
        print("✅ Jobspy loaded successfully!")
    except ImportError:
        print("❌ Still failing to load Jobspy. Printing sys.path:")
        print(sys.path)
        return

    all_results = []
    cloud = ["DevOps Engineer", "Site Reliability Engineer", "SRE", "Cloud Engineer", "Platform Engineer", "DevSecOps Engineer", "Cloud Infrastructure Engineer", "Automation Engineer", "Kubernetes Engineer", "Azure Engineer", "AWS Engineer"]
    dev = ["Full Stack Developer", "Node.js Developer", "Python Developer", "Django", "MERN Stack"]

    SEARCH_LIST = cloud + dev
    SEARCH_TERM = " OR ".join(SEARCH_LIST)
    
    # Specific search term for Global Remote (Only Cloud/DevOps)
    REMOTE_CLOUD_TERM = " OR ".join(cloud)
    
    RESULTS_WANTED = 1000
    HOURS_OLD = 3
    REMOTE_HOURS_OLD = 2

    # ==========================================
    # PRIORITY 1: GLOBAL REMOTE (Only DevOps & Cloud)
    # ==========================================
    
    # # Global Remote: LinkedIn
    # try:
    #     print("🔍 Searching: Global Remote [LinkedIn]...")
    #     res = scrape_jobs(site_name=["linkedin"],
    #                       search_term=REMOTE_CLOUD_TERM,
    #                       location="Worldwide",
    #                       is_remote=True,
    #                       results_wanted=RESULTS_WANTED, 
    #                       hours_old=REMOTE_HOURS_OLD,
    #                       country_indeed='worldwide')
    #     if not res.empty:
    #         res['is_global_remote_target'] = True
    #         all_results.append(res)
    # except Exception as e: print(f"⚠️ Global Remote LinkedIn Error: {e}")

    # # Global Remote: Indeed
    # try:
    #     print("🔍 Searching: Global Remote [Indeed]...")
    #     res = scrape_jobs(site_name=["indeed"],
    #                       search_term=REMOTE_CLOUD_TERM,
    #                       location="Worldwide",
    #                       is_remote=True,
    #                       results_wanted=RESULTS_WANTED, 
    #                       hours_old=REMOTE_HOURS_OLD,
    #                       country_indeed='worldwide')
    #     if not res.empty:
    #         res['is_global_remote_target'] = True
    #         all_results.append(res)
    # except Exception as e: print(f"⚠️ Global Remote Indeed Error: {e}")

    # # Global Remote: ZipRecruiter
    # try:
    #     print("🔍 Searching: Global Remote [ZipRecruiter]...")
    #     res = scrape_jobs(site_name=["zip_recruiter"],
    #                       search_term=REMOTE_CLOUD_TERM,
    #                       location="Worldwide",
    #                       is_remote=True,
    #                       results_wanted=RESULTS_WANTED, 
    #                       hours_old=REMOTE_HOURS_OLD)
    #     if not res.empty:
    #         res['is_global_remote_target'] = True
    #         all_results.append(res)
    # except Exception as e: print(f"⚠️ Global Remote ZipRecruiter Error: {e}")

    # # Global Remote: Glassdoor
    # try:
    #     print("🔍 Searching: Global Remote [Glassdoor]...")
    #     res = scrape_jobs(site_name=["glassdoor"],
    #                       search_term=REMOTE_CLOUD_TERM,
    #                       location="Worldwide",
    #                       is_remote=True,
    #                       results_wanted=RESULTS_WANTED, 
    #                       hours_old=REMOTE_HOURS_OLD)
    #     if not res.empty:
    #         res['is_global_remote_target'] = True
    #         all_results.append(res)
    # except Exception as e: print(f"⚠️ Global Remote Glassdoor Error: {e}")
# ==========================================
    # PRIORITY 1: GLOBAL REMOTE (Only DevOps & Cloud)
    # ==========================================
    
    # Global Remote: LinkedIn
    res = pd.DataFrame() # Initialize as empty
    try:
        print("🔍 Searching: Global Remote [LinkedIn]...")
        res = scrape_jobs(site_name=["linkedin"],
                          search_term=REMOTE_CLOUD_TERM,
                          location="Worldwide",
                          is_remote=True,
                          results_wanted=RESULTS_WANTED, 
                          hours_old=REMOTE_HOURS_OLD,
                          country_indeed='worldwide')
    except Exception as e: print(f"⚠️ Global Remote LinkedIn Error (Bypassing): {e}")
    if not res.empty:
        res['is_global_remote_target'] = True
        all_results.append(res)

    # Global Remote: Indeed
    res = pd.DataFrame() # Reset for next search
    try:
        print("🔍 Searching: Global Remote [Indeed]...")
        res = scrape_jobs(site_name=["indeed"],
                          search_term=REMOTE_CLOUD_TERM,
                          location="Worldwide",
                          is_remote=True,
                          results_wanted=RESULTS_WANTED, 
                          hours_old=REMOTE_HOURS_OLD,
                          country_indeed='worldwide')
    except Exception as e: print(f"⚠️ Global Remote Indeed Error (Bypassing): {e}")
    if not res.empty:
        res['is_global_remote_target'] = True
        all_results.append(res)

    # Global Remote: ZipRecruiter
    res = pd.DataFrame()
    try:
        print("🔍 Searching: Global Remote [ZipRecruiter]...")
        res = scrape_jobs(site_name=["zip_recruiter"],
                          search_term=REMOTE_CLOUD_TERM,
                          location="Worldwide",
                          is_remote=True,
                          results_wanted=RESULTS_WANTED, 
                          hours_old=REMOTE_HOURS_OLD)
    except Exception as e: print(f"⚠️ Global Remote ZipRecruiter Error (Bypassing): {e}")
    if not res.empty:
        res['is_global_remote_target'] = True
        all_results.append(res)

    # Global Remote: Glassdoor
    res = pd.DataFrame()
    try:
        print("🔍 Searching: Global Remote [Glassdoor]...")
        res = scrape_jobs(site_name=["glassdoor"],
                          search_term=REMOTE_CLOUD_TERM,
                          location="Worldwide",
                          is_remote=True,
                          results_wanted=RESULTS_WANTED, 
                          hours_old=REMOTE_HOURS_OLD)
    except Exception as e: print(f"⚠️ Global Remote Glassdoor Error (Bypassing): {e}")
    if not res.empty:
        res['is_global_remote_target'] = True
        all_results.append(res)

    # ==========================================
    # PRIORITY 2: COUNTRY SPECIFIC SEARCHES
    # ==========================================

    # Pakistan / Lahore Searches
    try:
        print("🔍 Searching: LinkedIn Lahore...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Lahore", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

    try:
        print("🔍 Searching: Indeed Lahore...")
        res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Lahore", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

    try:
        print("🔍 Searching: LinkedIn PK Remote...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Pakistan", is_remote=True, results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

    try:
        print("🔍 Searching: Indeed PK Remote...")
        res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Remote", is_remote=True, results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='pakistan')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

    # UAE - Dubai Searches
    try:
        print("🔍 Searching: LinkedIn Dubai...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Dubai", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Dubai Error: {e}")

    try:
        print("🔍 Searching: Indeed Dubai...")
        res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Dubai", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='united arab emirates')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Dubai Error: {e}")

    # UAE - Abu Dhabi Searches
    try:
        print("🔍 Searching: LinkedIn Abu Dhabi...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Abu Dhabi", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Abu Dhabi Error: {e}")

    try:
        print("🔍 Searching: Indeed Abu Dhabi...")
        res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Abu Dhabi", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='united arab emirates')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Abu Dhabi Error: {e}")

    # Saudi Arabia Searches
    try:
        print("🔍 Searching: LinkedIn Saudi Arabia...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Saudi Arabia", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ LI Saudi Arabia Error: {e}")

    try:
        print("🔍 Searching: Indeed Saudi Arabia...")
        res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Saudi Arabia", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='saudi arabia')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Saudi Arabia Error: {e}")

    # European & International Searches
    try:
        print("🔍 Searching: Sweden...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Sweden", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Sweden Error: {e}")

    try:
        print("🔍 Searching: Luxembourg...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Luxembourg", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Luxembourg Error: {e}")

    try:
        print("🔍 Searching: France...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="France", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ France Error: {e}")

    try:
        print("🔍 Searching: Germany...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Germany Error: {e}")

    try:
        print("🔍 Searching: Finland...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Finland", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Finland Error: {e}")

    try:
        print("🔍 Searching: Italy...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Italy", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Italy Error: {e}")

    try:
        print("🔍 Searching: Spain...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Spain", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Spain Error: {e}")

    try:
        print("🔍 Searching: Australia...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Australia", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Australia Error: {e}")

    try:
        print("🔍 Searching: Canada...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Canada", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Canada Error: {e}")


    # --- PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        df_all['location'] = df_all['location'].fillna('').astype(str)
        if 'is_global_remote_target' not in df_all.columns:
            df_all['is_global_remote_target'] = False
        df_all['is_global_remote_target'] = df_all['is_global_remote_target'].fillna(False)

        # 1. Define the Skills Filter
        cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
        dev_regex = 'fullstack|node|python|django|mern|developer'

        # 2. Layout Structure Priorities (Includes UAE & Saudi Arabia)
        target_locations = [
            ("🌍 GLOBAL REMOTE (DEVOPS/CLOUD)", "GLOBAL_REMOTE_MARKER", True),
            ("🇵🇰 PAKISTAN", "Lahore|Pakistan|Islamabad|Karachi", False),
            ("🇦🇪 DUBAI, UAE", "Dubai", False),
            ("🇦🇪 ABU DHABI, UAE", "Abu Dhabi", False),
            ("🇸🇦 SAUDI ARABIA", "Saudi Arabia|Riyadh|Jeddah", False),
            ("🇸🇪 SWEDEN", "Sweden|Stockholm|Gothenburg", False),
            ("🇫🇷 FRANCE", "France|Paris|Lyon", False),
            ("🇩🇪 GERMANY", "Germany|Berlin|Munich|Hamburg|Frankfurt", False),
            ("🇮🇹 ITALY", "Italy", False),
            ("🇪🇸 SPAIN", "Spain", False),
            ("🇦🇺 AUSTRALIA", "Australia", False),
            ("🇨🇦 CANADA", "Canada", False)
        ]

        msg = ["🚀 *JOB REPORT BY LOCATION*"]

        # 3. Process Content
        for label, regex, is_global_remote in target_locations:
            if is_global_remote:
                country_df = df_all[df_all['is_global_remote_target'] == True]
            else:
                non_remote_pool = df_all[df_all['is_global_remote_target'] == False]
                country_df = non_remote_pool[non_remote_pool['location'].str.contains(regex, case=False, na=False)]
            
            if not country_df.empty:
                c_df = country_df[country_df['title'].str.contains(cloud_regex, case=False, na=False)]
                d_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(dev_regex, case=False, na=False)]
                
                if not c_df.empty or not d_df.empty:
                    msg.append(f"\n📍 *{label}*")
                
                if not c_df.empty:
                    msg.append("  ☁️ *Cloud:*")
                    for _, row in c_df.iterrows():
                        msg.append(f"   • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
                if not d_df.empty:
                    msg.append("  💻 *Dev:*")
                    for _, row in d_df.iterrows():
                        msg.append(f"   • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
                if not c_df.empty or not d_df.empty:
                    msg.append("---")

        final_msg = "\n".join(msg)

        # 4. SEND OUTPUT
        if wa_id and wa_token and phone:
            url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
            try:
                today = datetime.now().strftime("%Y-%m-%d")
                df_all.drop(columns=['is_global_remote_target'], errors='ignore').to_excel(f"Jobs_{today}.xlsx", index=False)
                
                requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
                print("✅ Report Sent Successfully")
            except Exception as e:
                print(f"⚠️ Error during output: {e}")
            
    else:
        print("📭 No jobs found.")

if __name__ == "__main__":
    run_job_search()



# import os
# import sys
# import requests
# import pandas as pd
# from datetime import datetime

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
#         print("✅ Jobspy loaded successfully!")
#     except ImportError:
#         print("❌ Still failing to load Jobspy. Printing sys.path:")
#         print(sys.path)
#         return

#     all_results = []
#     cloud = ["DevOps Engineer", "Site Reliability Engineer", "SRE", "Cloud Engineer", "Platform Engineer", "DevSecOps Engineer", "Cloud Infrastructure Engineer", "Automation Engineer", "Kubernetes Engineer", "Azure Engineer", "AWS Engineer"]
#     dev = ["Full Stack Developer", "Node.js Developer", "Python Developer", "Django", "MERN Stack"]

#     SEARCH_LIST = cloud + dev
#     SEARCH_TERM = " OR ".join(SEARCH_LIST)
    
#     # Specific search term for Global Remote (Only Cloud/DevOps)
#     REMOTE_CLOUD_TERM = " OR ".join(cloud)
    
#     RESULTS_WANTED = 1000
#     HOURS_OLD = 3
#     REMOTE_HOURS_OLD = 2
    


#     # A: LinkedIn Lahore
#     try:
#         print("🔍 Searching: LinkedIn Lahore...")
#         res = scrape_jobs(site_name=["linkedin"], 
#                           search_term=SEARCH_TERM,
#                           location="Lahore",
#                           results_wanted=RESULTS_WANTED,
#                           hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

#     # B: Indeed Lahore
#     try:
#         print("🔍 Searching: Indeed Lahore...")
#         res = scrape_jobs(site_name=["indeed"],
#                           search_term=SEARCH_TERM,
#                           location="Lahore",
#                           results_wanted=RESULTS_WANTED,
#                           hours_old=HOURS_OLD, 
#                           country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

#     # C: LinkedIn Pakistan Remote
#     try:
#         print("🔍 Searching: LinkedIn PK Remote...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="Pakistan",
#                           is_remote=True,
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

#     # D: Indeed Pakistan Remote
#     try:
#         print("🔍 Searching: Indeed PK Remote...")
#         res = scrape_jobs(site_name=["indeed"], 
#                           search_term=SEARCH_TERM,
#                           location="Remote",
#                           is_remote=True,
#                           results_wanted=RESULTS_WANTED,
#                           hours_old=HOURS_OLD,
#                           country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

#     # NEW PHASE: GLOBAL REMOTE (Only DevOps & Cloud)
#     try:
#         print("🔍 Searching: Global Remote DevOps & Cloud...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=REMOTE_CLOUD_TERM,
#                           location="Worldwide",
#                           is_remote=True,
#                           results_wanted=RESULTS_WANTED, hours_old=REMOTE_HOURS_OLD)
#         if not res.empty:
#             # Tag them explicitly so they can be identified later during processing
#             res['is_global_remote_target'] = True
#             all_results.append(res)
#     except Exception as e: print(f"⚠️ Global Remote Error: {e}")

#     # E: Sweden
#     try:
#         print("🔍 Searching: Sweden...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="Sweden",
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Sweden Error: {e}")

#     # F: Luxembourg
#     try:
#         print("🔍 Searching: Luxembourg...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="Luxembourg",
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Luxembourg Error: {e}")

#     # G: France
#     try:
#         print("🔍 Searching: France...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="France",
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ France Error: {e}")

#     # H: Germany
#     try:
#         print("🔍 Searching: Germany...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="Germany",
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Germany Error: {e}")

#     try:
#         print("🔍 Searching: Finland...")
#         res = scrape_jobs(site_name=["linkedin"],
#                           search_term=SEARCH_TERM,
#                           location="Finland",
#                           results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Finland Error: {e}")

#     # I: Italy
#     try:
#         print("🔍 Searching: Italy...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Italy", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Italy Error: {e}")

#     # J: Spain
#     try:
#         print("🔍 Searching: Spain...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Spain", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Spain Error: {e}")

#     # K: Austria
#     try:
#         print("🔍 Searching: Australia...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Australia", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Australia Error: {e}")

#     # L: Canada
#     try:
#         print("🔍 Searching: Canada...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Canada", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Canada Error: {e}")


#     # --- 2. PROCESSING ---
#     if all_results:
#         df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
#         df_all['location'] = df_all['location'].fillna('').astype(str)
#         if 'is_global_remote_target' not in df_all.columns:
#             df_all['is_global_remote_target'] = False
#         df_all['is_global_remote_target'] = df_all['is_global_remote_target'].fillna(False)

#         # 1. Define the Skills
#         cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
#         dev_regex = 'fullstack|node|python|django|mern|developer'

#         # 2. Define Country/Category logic sequentially to maintain layout order
#         target_locations = [
#             ("🇵🇰 PAKISTAN", "Lahore|Pakistan|Islamabad|Karachi", False),
#             ("🌍 GLOBAL REMOTE (DEVOPS/CLOUD)", "GLOBAL_REMOTE_MARKER", True), # Custom marker rule
#             ("🇸🇪 SWEDEN", "Sweden|Stockholm|Gothenburg", False),
#             ("🇫🇷 FRANCE", "France|Paris|Lyon", False),
#             ("🇩🇪 GERMANY", "Germany|Berlin|Munich|Hamburg|Frankfurt", False),
#             ("🇮🇹 ITALY", "Italy", False),
#             ("🇪🇸 SPAIN", "Spain", False),
#             ("🇦🇺 AUSTRALIA", "Australia", False),
#             ("🇨🇦 CANADA", "Canada", False)
#         ]

#         msg = ["🚀 *JOB REPORT BY LOCATION*"]

#         # 3. Nested Loop: Find Cloud vs Dev matching your custom ordered block
#         for label, regex, is_global_remote in target_locations:
            
#             # Isolate the data pool for this block
#             if is_global_remote:
#                 country_df = df_all[df_all['is_global_remote_target'] == True]
#             else:
#                 # Exclude global remote entries from standard geo blocks to keep them clean
#                 non_remote_pool = df_all[df_all['is_global_remote_target'] == False]
#                 country_df = non_remote_pool[non_remote_pool['location'].str.contains(regex, case=False, na=False)]
            
#             if not country_df.empty:
#                 # Filter Cloud jobs
#                 c_df = country_df[country_df['title'].str.contains(cloud_regex, case=False, na=False)]
                
#                 # Filter Dev jobs (Skipped completely if it's the Global Remote block)
#                 d_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(dev_regex, case=False, na=False)]
                
#                 # Only display heading if there is valid filtered content
#                 if not c_df.empty or not d_df.empty:
#                     msg.append(f"\n📍 *{label}*")
                
#                 # Print Cloud Sub-section
#                 if not c_df.empty:
#                     msg.append("  ☁️ *Cloud:*")
#                     for _, row in c_df.iterrows():
#                         msg.append(f"  • *{row['title']}* @ {row['company']}\n    🔗 {row['job_url']}")
                
#                 # Print Dev Sub-section
#                 if not d_df.empty:
#                     msg.append("  💻 *Dev:*")
#                     for _, row in d_df.iterrows():
#                         msg.append(f"  • *{row['title']}* @ {row['company']}\n    🔗 {row['job_url']}")
                
#                 if not c_df.empty or not d_df.empty:
#                     msg.append("---")

#         final_msg = "\n".join(msg)

#         # 4. SEND (Try/Except to prevent crash)
#         if wa_id and wa_token and phone:
#             url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
#             try:
#                 # Save Raw Excel first just in case
#                 today = datetime.now().strftime("%Y-%m-%d")
#                 df_all.drop(columns=['is_global_remote_target'], errors='ignore').to_excel(f"Jobs_{today}.xlsx", index=False)
                
#                 # Send WhatsApp
#                 requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
#                 print("✅ Report Sent Successfully")
#             except Exception as e:
#                 print(f"⚠️ Error during output: {e}")
            
#     else:
#         print("📭 No jobs found.")

# if __name__ == "__main__":
#     run_job_search()
