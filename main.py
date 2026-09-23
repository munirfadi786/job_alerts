

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
#     finance = ["Accountant", "Cashier", "Financial Accountant", "Junior Accountant", "Senior Accountant"]

#     SEARCH_LIST = cloud + dev
#     SEARCH_TERM = " OR ".join(SEARCH_LIST)
#     FINANCE_SEARCH_TERM = " OR ".join(finance)
    
#     # Specific search term for Global Remote (Only Cloud/DevOps)
#     REMOTE_CLOUD_TERM = " OR ".join(cloud)
    
#     RESULTS_WANTED = 1000
#     HOURS_OLD = 3
#     REMOTE_HOURS_OLD = 1

#     try:
#         print("🔍 Searching: Global Remote [LinkedIn]...")
#         linkedin_countries = [
#             "usa", "united kingdom", "canada", "australia", 
#             "germany", "netherlands", "singapore", "united arab emirates",
#             "switzerland", "ireland", "luxembourg", "sweden", 
#             "norway", "denmark", "new zealand", "qatar"
#         ]
#         for target_country in linkedin_countries:
            
#             res = pd.DataFrame()
#             try:
#                 res = scrape_jobs(
#                     site_name=["linkedin"],
#                     search_term=REMOTE_CLOUD_TERM,
#                     location=target_country,
#                     is_remote=True,
#                     results_wanted=RESULTS_WANTED, 
#                     hours_old=REMOTE_HOURS_OLD
#                 )
#                 if not res.empty:
#                     res['is_global_remote_target'] = True
#                     all_results.append(res)
#             except Exception as country_err:
#                 print(f"⚠️ LinkedIn Remote skipped country '{target_country}': {country_err}")
#     except Exception as e: 
#         print(f"⚠️ Global Remote LinkedIn General Error: {e}")

#     # Global Remote: Indeed
#     res = pd.DataFrame() # Reset for next search
#     try:
#         print("🔍 Searching: Global Remote [Indeed]...")
#         res = scrape_jobs(site_name=["indeed"],
#                           search_term=REMOTE_CLOUD_TERM,
#                           location="Worldwide",
#                           is_remote=True,
#                           results_wanted=RESULTS_WANTED, 
#                           hours_old=REMOTE_HOURS_OLD,
#                           country_indeed='worldwide')
#     except Exception as e: print(f"⚠️ Global Remote Indeed Error (Bypassing): {e}")
#     if not res.empty:
#         res['is_global_remote_target'] = True
#         all_results.append(res)

#     # Global Remote: ZipRecruiter
#     # res = pd.DataFrame()
#     # try:
#     #     print("🔍 Searching: Global Remote [ZipRecruiter]...")
#     #     res = scrape_jobs(site_name=["zip_recruiter"],
#     #                       search_term=REMOTE_CLOUD_TERM,
#     #                       location="Worldwide",
#     #                       is_remote=True,
#     #                       results_wanted=RESULTS_WANTED, 
#     #                       hours_old=REMOTE_HOURS_OLD)
#     # except Exception as e: print(f"⚠️ Global Remote ZipRecruiter Error (Bypassing): {e}")
#     # if not res.empty:
#     #     res['is_global_remote_target'] = True
#     #     all_results.append(res)

#     # Global Remote: Glassdoor
#     # res = pd.DataFrame()
#     # try:
#     #     print("🔍 Searching: Global Remote [Glassdoor]...")
#     #     res = scrape_jobs(site_name=["glassdoor"],
#     #                       search_term=REMOTE_CLOUD_TERM,
#     #                       location="Worldwide",
#     #                       is_remote=True,
#     #                       results_wanted=RESULTS_WANTED, 
#     #                       hours_old=REMOTE_HOURS_OLD)
#     # except Exception as e: print(f"⚠️ Global Remote Glassdoor Error (Bypassing): {e}")
#     # if not res.empty:
#     #     res['is_global_remote_target'] = True
#     #     all_results.append(res)

#     # ==========================================
#     # PRIORITY 2: COUNTRY SPECIFIC SEARCHES
#     # ==========================================

#     # Pakistan / Lahore Searches
#     try:
#         print("🔍 Searching: LinkedIn Lahore...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Lahore", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI Lahore Error: {e}")

#     try:
#         print("🔍 Searching: Indeed Lahore...")
#         res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Lahore", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Lahore Error: {e}")

#     try:
#         print("🔍 Searching: LinkedIn PK Remote...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Pakistan", is_remote=True, results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI PK Remote Error: {e}")

#     try:
#         print("🔍 Searching: Indeed PK Remote...")
#         res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Remote", is_remote=True, results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='pakistan')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed PK Remote Error: {e}")

#     # UAE - Dubai Searches
#     try:
#         print("🔍 Searching: LinkedIn Dubai...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Dubai", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI Dubai Error: {e}")

#     try:
#         print("🔍 Searching: Indeed Dubai...")
#         res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Dubai", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='united arab emirates')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Dubai Error: {e}")

#     # UAE - Abu Dhabi Searches
#     try:
#         print("🔍 Searching: LinkedIn Abu Dhabi...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Abu Dhabi", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ LI Abu Dhabi Error: {e}")

#     try:
#         print("🔍 Searching: Indeed Abu Dhabi...")
#         res = scrape_jobs(site_name=["indeed"], search_term=SEARCH_TERM, location="Abu Dhabi", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='united arab emirates')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Abu Dhabi Error: {e}")

#     # Germany Searches (Tech & Finance)
#     try:
#         print("🔍 Searching: Germany Tech...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Germany Tech Error: {e}")

#     try:
#         print("🔍 Searching: Germany Finance (Accountant/Cashier)...")
#         res = scrape_jobs(site_name=["linkedin"], search_term=FINANCE_SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Germany Finance Error: {e}")

#     try:
#         print("🔍 Searching: Indeed Germany Finance...")
#         res = scrape_jobs(site_name=["indeed"], search_term=FINANCE_SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='germany')
#         if not res.empty: all_results.append(res)
#     except Exception as e: print(f"⚠️ Indeed Germany Finance Error: {e}")


#     # # --- PROCESSING ---
#     # if all_results:
#     #     df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
#     #     df_all['location'] = df_all['location'].fillna('').astype(str)

#     #     # Explicitly remove jobs from excluded regions
#     #     df_all = df_all[~df_all['location'].str.contains('bangladesh|north korea|india|sri lanka|nepal|philippines|vietnam|indonesia|russia|belarus|iran|cuba|nigeria|egypt|venezuela', case=False, na=False)]
#     #     if 'is_global_remote_target' not in df_all.columns:
#     #         df_all['is_global_remote_target'] = False
#     #     df_all['is_global_remote_target'] = df_all['is_global_remote_target'].fillna(False)

#     #     # 1. Define the Skills Filter
#     #     cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
#     #     dev_regex = 'fullstack|node|python|django|mern|developer'
#     #     finance_regex = 'accountant|cashier|finance|financial'

#     #     # 2. Layout Structure Priorities
#     #     target_locations = [
            
#     #         ("🇵🇰 PAKISTAN", "Lahore|Pakistan|Islamabad|Karachi", False),
#     #         ("🇵🇰 PAKISTAN (INDEED)", "Lahore|Pakistan|Islamabad|Karachi", False),
#     #         ("🇦🇪 DUBAI, UAE", "Dubai", False),
#     #         ("🇦🇪 ABU DHABI, UAE", "Abu Dhabi", False),
#     #         ("🇩🇪 GERMANY", "Germany|Berlin|Munich|Hamburg|Frankfurt", False),
#     #         ("🌍 GLOBAL REMOTE (DEVOPS/CLOUD)", "GLOBAL_REMOTE_MARKER", True)
#     #     ]

#     #     msg = ["🚀 *JOB REPORT BY LOCATION*"]

#     #     # 3. Process Content
#     #     for label, regex, is_global_remote in target_locations:
#     #         if is_global_remote:
#     #             country_df = df_all[df_all['is_global_remote_target'] == True]
#     #         else:
#     #             non_remote_pool = df_all[df_all['is_global_remote_target'] == False]
#     #             country_df = non_remote_pool[non_remote_pool['location'].str.contains(regex, case=False, na=False)]
            
#     #         if not country_df.empty:
#     #             c_df = country_df[country_df['title'].str.contains(cloud_regex, case=False, na=False)]
#     #             d_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(dev_regex, case=False, na=False)]
#     #             f_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(finance_regex, case=False, na=False)]
                
#     #             if not c_df.empty or not d_df.empty or not f_df.empty:
#     #                 msg.append(f"\n📍 *{label}*")
                
#     #             if not c_df.empty:
#     #                 msg.append("   ☁️ *Cloud:*")
#     #                 for _, row in c_df.iterrows():
#     #                     msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
#     #             if not d_df.empty:
#     #                 msg.append("   💻 *Dev:*")
#     #                 for _, row in d_df.iterrows():
#     #                     msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")

#     #             if not f_df.empty:
#     #                 msg.append("   📊 *Finance & Accounting:*")
#     #                 for _, row in f_df.iterrows():
#     #                     msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
#     #             if not c_df.empty or not d_df.empty or not f_df.empty:
#     #                 msg.append("---")

#     #     final_msg = "\n".join(msg)
#     #                 # Print all scraped jobs to the runner logs for debugging
#     #     if 'df_all' in locals() and not df_all.empty:
#     #         print(f"📊 TOTAL UNIQUE JOBS FOUND: {len(df_all)}")
#     #         for _, row in df_all.iterrows():
#     #             print(f"JOB: {row.get('title')} | COMPANY: {row.get('company')} | SITE: {row.get('site')} | LOC: {row.get('location')}")

#     #     # 4. SEND OUTPUT
#     #     if wa_id and wa_token and phone:
#     #         url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
#     #         try:
#     #             today = datetime.now().strftime("%Y-%m-%d")
#     #             df_all.drop(columns=['is_global_remote_target'], errors='ignore').to_excel(f"Jobs_{today}.xlsx", index=False)
                
#     #             requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
#     #             print("✅ Report Sent Successfully")
#     #         except Exception as e:
#     #             print(f"⚠️ Error during output: {e}")
            
#     # else:
#     #     print("📭 No jobs found.")

# # --- PROCESSING ---
#     if all_results:
#         df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
#         df_all['location'] = df_all['location'].fillna('').astype(str)

#         # Force print raw jobs immediately to GitHub Actions logs
#         print(f"📊 RAW SCRAPED JOBS FOUND: {len(df_all)}", flush=True)
#         for _, row in df_all.iterrows():
#             print(f"JOB: {row.get('title')} | COMPANY: {row.get('company')} | SITE: {row.get('site')} | LOC: {row.get('location')}", flush=True)

#         # Explicitly remove jobs from excluded regions
#         df_all = df_all[~df_all['location'].str.contains('bangladesh|north korea|india|sri lanka|nepal|philippines|vietnam|indonesia|russia|belarus|iran|cuba|nigeria|egypt|venezuela', case=False, na=False)]
#         if 'is_global_remote_target' not in df_all.columns:
#             df_all['is_global_remote_target'] = False
#         df_all['is_global_remote_target'] = df_all['is_global_remote_target'].fillna(False)

#         # 1. Define the Skills Filter
#         cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
#         dev_regex = 'fullstack|node|python|django|mern|developer'
#         finance_regex = 'accountant|cashier|finance|financial'

#         # 2. Layout Structure Priorities
#         target_locations = [
#             ("🇵🇰 PAKISTAN", "Lahore|Pakistan|Islamabad|Karachi", False),
#             ("🇵🇰 PAKISTAN (INDEED)", "Lahore|Pakistan|Islamabad|Karachi", False),
#             ("🇦🇪 DUBAI, UAE", "Dubai", False),
#             ("🇦🇪 ABU DHABI, UAE", "Abu Dhabi", False),
#             ("🇩🇪 GERMANY", "Germany|Berlin|Munich|Hamburg|Frankfurt", False),
#             ("🌍 GLOBAL REMOTE (DEVOPS/CLOUD)", "GLOBAL_REMOTE_MARKER", True)
#         ]

#         msg = ["🚀 *JOB REPORT BY LOCATION*"]

#         # 3. Process Content
#         for label, regex, is_global_remote in target_locations:
#             if is_global_remote:
#                 country_df = df_all[df_all['is_global_remote_target'] == True]
#             else:
#                 non_remote_pool = df_all[df_all['is_global_remote_target'] == False]
#                 country_df = non_remote_pool[non_remote_pool['location'].str.contains(regex, case=False, na=False)]
            
#             if not country_df.empty:
#                 c_df = country_df[country_df['title'].str.contains(cloud_regex, case=False, na=False)]
#                 d_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(dev_regex, case=False, na=False)]
#                 f_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(finance_regex, case=False, na=False)]
                
#                 if not c_df.empty or not d_df.empty or not f_df.empty:
#                     msg.append(f"\n📍 *{label}*")
                
#                 if not c_df.empty:
#                     msg.append("    ☁️ *Cloud:*")
#                     for _, row in c_df.iterrows():
#                         msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
#                 if not d_df.empty:
#                     msg.append("    💻 *Dev:*")
#                     for _, row in d_df.iterrows():
#                         msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")

#                 if not f_df.empty:
#                     msg.append("    📊 *Finance & Accounting:*")
#                     for _, row in f_df.iterrows():
#                         msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
#                 if not c_df.empty or not d_df.empty or not f_df.empty:
#                     msg.append("---")

#         final_msg = "\n".join(msg)

#         # 4. SEND OUTPUT
#         if wa_id and wa_token and phone:
#             url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
#             try:
#                 today = datetime.now().strftime("%Y-%m-%d")
#                 df_all.drop(columns=['is_global_remote_target'], errors='ignore').to_excel(f"Jobs_{today}.xlsx", index=False)
                
#                 requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
#                 print("✅ Report Sent Successfully")
#             except Exception as e:
#                 print(f"⚠️ Error during output: {e}")
            
#     else:
#         print("📭 No jobs found.")

# if __name__ == "__main__":
#     run_job_search()

import os
import sys
import json
import smtplib
from email.message import EmailMessage
import requests
import pandas as pd
from datetime import datetime

# def sync_to_google_sheet(df):
#     if df.empty:
#         return

#     script_url = os.getenv("GOOGLE_SCRIPT_URL")
#     if not script_url:
#         print("⚠️ GOOGLE_SCRIPT_URL secret not found. Skipping Google Sheets sync.")
#         return

#     try:
#         df = df.fillna("")
#         df['scraped_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Convert dataframe rows into a list of lists to send to Apps Script
#         headers = list(df.columns)
#         rows = [headers] + df.values.tolist()
        
#         response = requests.post(script_url, json=rows)
#         if response.status_code == 200:
#             print(f"✅ Successfully pushed {len(df)} jobs to Google Sheets via Web App!")
#         else:
#             print(f"⚠️ Failed to push to Google Sheets. Response: {response.text}")
#     except Exception as e:
#         print(f"⚠️ Error syncing to Google Sheets: {e}")
import requests
import json

# Your deployed Google Apps Script Web App URL
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyQrqqp3rYudT41MyCxCbDQ-SDOii3zySDNNDiiVkuld8hAinzjcLbloEyJxyH8myo6Zg/exec"



def send_to_google_sheet(df):
    if df.empty:
        print("⚠️ No data to send to Google Sheets.")
        return

    # Clean the dataframe by dropping raw date/datetime objects that cause JSON errors
    df_clean = df.select_dtypes(exclude=['datetime64', 'datetimetz']).copy()
    cols_to_drop = [col for col in df_clean.columns if 'date' in col.lower()]
    df_clean = df_clean.drop(columns=cols_to_drop, errors='ignore')

    # ADD A CLEAN FORMATTED DATE & TIME COLUMN (Day-Month-Year format)
    # This creates a string like "23-09-2026 23:24:02" so it won't break JSON and is easy to read
    df_clean['Sync_Date_Time'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # Convert DataFrame to a list of lists (including headers)
    data_to_send = [df_clean.columns.tolist()] + df_clean.values.tolist()
    
    try:
        response = requests.post(WEB_APP_URL, json=data_to_send)
        print(f"📡 Google Sheet Response: {response.text}")
    except Exception as e:
        print(f"❌ Error sending data to Google Sheet: {e}")


def send_email_report(excel_filename):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("EMAIL_RECEIVER")

    if not sender_email or not sender_password or not receiver_email:
        print("⚠️ Email secrets not fully configured. Skipping email report.")
        return

    try:
        msg = EmailMessage()
        msg['Subject'] = f"🚀 Daily Job Search Report - {datetime.now().strftime('%Y-%m-%d')}"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content("Hello! Attached is your daily scraped job report spreadsheet containing the latest listings.")

        if os.path.exists(excel_filename):
            with open(excel_filename, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(excel_filename)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            
        print("✅ Email Report Sent Successfully!")
    except Exception as e:
        print(f"⚠️ Error sending email: {e}")

def run_job_search():
    # 1. Print Debug Information
    print("--- DEBUGGING ENVIRONMENT ---")
    print(f"Python Executable: {sys.executable}")
    
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
    finance = ["Accountant", "Cashier", "Financial Accountant", "Junior Accountant", "Senior Accountant"]

    SEARCH_LIST = cloud + dev
    SEARCH_TERM = " OR ".join(SEARCH_LIST)
    FINANCE_SEARCH_TERM = " OR ".join(finance)
    
    REMOTE_CLOUD_TERM = " OR ".join(cloud)
    
    RESULTS_WANTED = 1000
    HOURS_OLD = 3
    REMOTE_HOURS_OLD = 1

    # try:
    #     print("🔍 Searching: Global Remote [LinkedIn]...")
    #     linkedin_countries = [
    #         "usa", "united kingdom", "canada", "australia", 
    #         "germany", "netherlands", "singapore", "united arab emirates",
    #         "switzerland", "ireland", "luxembourg", "sweden", 
    #         "norway", "denmark", "new zealand", "qatar"
    #     ]
    #     for target_country in linkedin_countries:
    #         res = pd.DataFrame()
    #         try:
    #             res = scrape_jobs(
    #                 site_name=["linkedin"],
    #                 search_term=REMOTE_CLOUD_TERM,
    #                 location=target_country,
    #                 is_remote=True,
    #                 results_wanted=RESULTS_WANTED, 
    #                 hours_old=REMOTE_HOURS_OLD
    #             )
    #             if not res.empty:
    #                 res['is_global_remote_target'] = True
    #                 all_results.append(res)
    #         except Exception as country_err:
    #             print(f"⚠️ LinkedIn Remote skipped country '{target_country}': {country_err}")
    # except Exception as e: 
    #     print(f"⚠️ Global Remote LinkedIn General Error: {e}")

    # Global Remote: Indeed
    res = pd.DataFrame()
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

    # ==========================================
    # PRIORITY 2: COUNTRY SPECIFIC SEARCHES
    # ==========================================

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

    try:
        print("🔍 Searching: Germany Tech...")
        res = scrape_jobs(site_name=["linkedin"], search_term=SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Germany Tech Error: {e}")

    try:
        print("🔍 Searching: Germany Finance (Accountant/Cashier)...")
        res = scrape_jobs(site_name=["linkedin"], search_term=FINANCE_SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD)
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Germany Finance Error: {e}")

    try:
        print("🔍 Searching: Indeed Germany Finance...")
        res = scrape_jobs(site_name=["indeed"], search_term=FINANCE_SEARCH_TERM, location="Germany", results_wanted=RESULTS_WANTED, hours_old=HOURS_OLD, country_indeed='germany')
        if not res.empty: all_results.append(res)
    except Exception as e: print(f"⚠️ Indeed Germany Finance Error: {e}")

    # --- PROCESSING ---
    if all_results:
        df_all = pd.concat(all_results).drop_duplicates(subset=['job_url'])
        df_all['location'] = df_all['location'].fillna('').astype(str)

        print(f"📊 RAW SCRAPED JOBS FOUND: {len(df_all)}", flush=True)
        for _, row in df_all.iterrows():
            print(f"JOB: {row.get('title')} | COMPANY: {row.get('company')} | SITE: {row.get('site')} | LOC: {row.get('location')}", flush=True)

        df_all = df_all[~df_all['location'].str.contains('bangladesh|north korea|india|sri lanka|nepal|philippines|vietnam|indonesia|russia|belarus|iran|cuba|nigeria|egypt|venezuela', case=False, na=False)]
        if 'is_global_remote_target' not in df_all.columns:
            df_all['is_global_remote_target'] = False
        df_all['is_global_remote_target'] = df_all['is_global_remote_target'].fillna(False)

        cloud_regex = 'devops|sre|reliability|platform|infrastructure|cloud|kubernetes|azure|aws'
        dev_regex = 'fullstack|node|python|django|mern|developer'
        finance_regex = 'accountant|cashier|finance|financial'

        target_locations = [
            ("🇵🇰 PAKISTAN", "Lahore|Pakistan|Islamabad|Karachi", False),
            ("🇵🇰 PAKISTAN (INDEED)", "Lahore|Pakistan|Islamabad|Karachi", False),
            ("🇦🇪 DUBAI, UAE", "Dubai", False),
            ("🇦🇪 ABU DHABI, UAE", "Abu Dhabi", False),
            ("🇩🇪 GERMANY", "Germany|Berlin|Munich|Hamburg|Frankfurt", False),
            ("🌍 GLOBAL REMOTE (DEVOPS/CLOUD)", "GLOBAL_REMOTE_MARKER", True)
        ]

        msg = ["🚀 *JOB REPORT BY LOCATION*"]

        for label, regex, is_global_remote in target_locations:
            if is_global_remote:
                country_df = df_all[df_all['is_global_remote_target'] == True]
            else:
                non_remote_pool = df_all[df_all['is_global_remote_target'] == False]
                country_df = non_remote_pool[non_remote_pool['location'].str.contains(regex, case=False, na=False)]
            
            if not country_df.empty:
                c_df = country_df[country_df['title'].str.contains(cloud_regex, case=False, na=False)]
                d_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(dev_regex, case=False, na=False)]
                f_df = pd.DataFrame() if is_global_remote else country_df[country_df['title'].str.contains(finance_regex, case=False, na=False)]
                
                if not c_df.empty or not d_df.empty or not f_df.empty:
                    msg.append(f"\n📍 *{label}*")
                
                if not c_df.empty:
                    msg.append("    ☁️ *Cloud:*")
                    for _, row in c_df.iterrows():
                        msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
                if not d_df.empty:
                    msg.append("    💻 *Dev:*")
                    for _, row in d_df.iterrows():
                        msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")

                if not f_df.empty:
                    msg.append("    📊 *Finance & Accounting:*")
                    for _, row in f_df.iterrows():
                        msg.append(f"    • *{row['title']}* @ {row['company']} ({row['site'].upper()})\n     🔗 {row['job_url']}")
                
                if not c_df.empty or not d_df.empty or not f_df.empty:
                    msg.append("---")

        final_msg = "\n".join(msg)

        # 4. SEND OUTPUT (Excel, Google Sheets, Email, WhatsApp)
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            excel_filename = f"Jobs_{today}.xlsx"
            
            df_to_export = df_all.drop(columns=['is_global_remote_target'], errors='ignore')
            df_to_export.to_excel(excel_filename, index=False)
            
            send_to_google_sheet(df_to_export)
            send_email_report(excel_filename)
            
            if wa_id and wa_token and phone:
                url = f"https://7103.api.greenapi.com/waInstance{wa_id}/sendMessage/{wa_token}"
                requests.post(url, json={"chatId": f"{phone}@c.us", "message": final_msg})
                print("✅ WhatsApp Report Sent Successfully")
                
        except Exception as e:
            print(f"⚠️ Error during output delivery: {e}")
            
    else:
        print("📭 No jobs found.")

if __name__ == "__main__":
    run_job_search()
