from database import *
from scraper import *
import re
from Gemini import *

def preprocess_text(text: str) -> str:
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML
    text = re.sub(r'\s+', ' ', text)     # Normalize whitespace
    return text.lower().strip() #converts it to lowercase

def main():
    create_articles_table()
    
    # Step 1: Scrape articles
    print("Starting Data Scrapping!")
    articles = scrape_articles('thehackernews', limit=5)



    print("Summarising Content!")

    for article in articles:
        # Step 2: Preprocess
        cleaned_content = preprocess_text(article['content'])
        
        # Step 3: Summarize with Gemini
        summary = summarize_text(cleaned_content)
        
        # Step 4: Store in database
        article_data = {
            'title': article['title'],
            'author': article['author'],
            'content': cleaned_content,
            'summary': summary,
            'source_url': article['source_url']
        }
        store_article(article_data)

    
    print("Data stored in Database!")

if __name__ == "__main__":
    main()