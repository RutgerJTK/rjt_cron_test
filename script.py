# script.py
from datetime import datetime

def main():
    now = datetime.now()
    print(f"The current date and time is: {now}")


    # Write results to a file   
    with open('results.txt', 'a') as f:
        f.write(f"Run date: {datetime.now()}\n")
        f.write("Your results here...\n")        

if __name__ == "__main__":
    main()
