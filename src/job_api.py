from apify_client import ApifyClient
from dotenv import load_dotenv
import os
load_dotenv()

apify_client=ApifyClient(os.getenv('APIFY_API_TOKEN'))

# CREATING FUNCTION TO GET LINKEDIN JOBS
def fetch_linkedin_jobs(search_query, location="india", rows=60):
    """Fetch job listings from LinkedIn.
    
    Args:
       search_query(int): The location to search in.
       rows(int): The number of job listings to fetch.
        
    Returns:
        list: A list of job listings.
    """
    # Placeholder for actual implementation
    run_input={
        "keyword":search_query,
        "maxJobs":60,
        "freshness":"all",
        "sortBy":"relevance",
        "experience":"all"
    }
    run=apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
# ----------------------------------------------------------------------------------------------------------
# CREATING FUNCTION TO GET NAUKRI JOBS
def fetch_naukri_jobs(search_query, location="india", rows=60):
    """Fetch job listings from naukri.
    
    Args:
       search_query(int): The location to search in.
       rows(int): The number of job listings to fetch.
        
    Returns:
        list: A list of job listings.
    """
    # Placeholder for actual implementation
    run_input={
        "keyword":search_query,
        "maxJobs":60,
        "freshness":"all",
        "sortBy":"relevance",
        "experience":"all"
    }
    run=apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs=list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs