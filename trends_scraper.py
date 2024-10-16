import requests
from bs4 import BeautifulSoup

def get_editors_picks():
    print("Getting Editor's Picks...")
    url = "https://bmcbioinformatics.biomedcentral.com"
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for the section containing Editor's Picks
        # Example: Suppose the editor's picks are in a div with a class 'editor-picks'
        editors_picks_section = soup.find('div', id="editor%27s+picks")  # Modify this based on actual HTML
        
        if editors_picks_section:
            # Extract all article titles from the editor's picks section
            # Assuming that each article title is in an <a> tag inside the section
            articles = editors_picks_section.find_all('a')
            
            for article in articles:
                # Print the article title and link
                title = article.get_text(strip=True)
                if len(title) > 1:
                    link = article['href']
                    result = f"Title: {title}\nLink: {link}"
                    results.append(result)
                    print(f"Title: {title}\nLink: {link}")
        else:
            print("Editor's Picks section not found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    return results

# Call the function to get editor's picks
results = get_editors_picks()
