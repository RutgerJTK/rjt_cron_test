import trends_scraper

# script.py
from datetime import datetime

def main():
    now = datetime.now()
    print(f"The current date and time is: {now}")
    results = trends_scraper.get_editors_picks()

    # Write results to a file   
    with open('results.txt', 'a') as f:
        for article in results:
            f.write(f"Articles in the spotlight today ({now}): {article}\n")  # Write each result on a new line
        

if __name__ == "__main__":
    main()
