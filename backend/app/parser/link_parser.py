from app.core.constants import PROFILE_PARTS
def extract_links(links):
    return{
        "github":extract_github(links),
        "linkedin":extract_linkedin(links),
        "leetcode":extract_leetcode(links),
        "portfolio":extract_portfolio(links),
        "mail":extract_mail(links)
    }

def extract_github(links):
    profile=None
    repositories=[]
    for link in links:
        if "github.com" not in link:
            continue
        link=link.rstrip("/")
        parts=link.split("/")
        
        if len(parts)<=PROFILE_PARTS:
            profile=link
        else :
            repositories.append(link)

    return{
        "profile":profile,
        "repositories":repositories
    }
def extract_linkedin(links):
    for link in links:
        if "linkedin.com" in link:
            return link.rstrip("/")  
    return None
def extract_leetcode(links):
    for link in links:
        if "leetcode.com" in link:
            return link.rstrip("/")  
    return None
def extract_portfolio(links):
    for link in links:
        if link.startswith("mailto:"):
            continue
        if "github.com" in link:
            continue
        if "leetcode.com" in link:
            continue
        if "linkedin.com" in link:
            continue
        return link.rstrip("/")
    return None
def extract_mail(links):
    for link in links:
        if link.startswith("mailto:"):
            return link.removeprefix("mailto:")
    return None
