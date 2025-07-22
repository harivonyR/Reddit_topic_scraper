# 🔍 Reddit Scraper using Piloterr API
Reddit topic scraper using Piloterr Website Crawler API's.

This project is a modular, production-ready web scraping pipeline for Reddit using the [Piloterr API](https://piloterr.com). It is built to support **high-volume data extraction** for use cases like:

- NLP / LLM training  
- Sentiment analysis  
- AI dataset generation  
- Reddit trend monitoring  

The scraper simulates real browser behavior to capture dynamic, JavaScript-heavy content such as comments and post lists, thanks to Piloterr’s headless rendering API.

---

## 1️⃣ Introduction & Brief Use

This tool covers a complete Reddit scraping workflow:

```python
# Step 1: Get all Reddit topics
topics = scrape_all()

# Step 2: Scrape posts from a topic page
posts = scrape_post("https://www.reddit.com/t/a_bird_story/", scroll=2)

# Step 3: Scrape comments from a specific post
comments = scrape_comment("https://www.reddit.com/r/movies/comments/aa1vas/mr_rogers_biopic_starring_tom_hanks_officially/")
````

The output can be stored in CSVs or JSON-like structures, making it directly usable for analytics, model fine-tuning, or database integration.

---

## 2️⃣ Setup, Dependencies & Running `main.py`

### 📦 Install dependencies

```bash
pip install requests beautifulsoup4
```

### 🔐 Add your Piloterr API key

Copy the example credentials:

```bash
cp credential.exemple.py credential.py
```

Edit `credential.py` and paste your API key (visit piloterr.com if you don't have one):

```python
x_api_key = "your_actual_api_key_here"
```

### ▶️ Run the main script

```bash
python main.py
```

This runs the full pipeline:

1. Extracts all Reddit topics
2. Saves them to `output/all_reddit_topics.csv`
3. Scrapes sample posts and their comments

---

## 3️⃣ Function Breakdown

### 3a) 🔌 `piloterr.py` – API Integration

#### ✅ `website_crawler(site_url)`

* Basic HTML fetcher (no JS rendering)
* Used for static pages like Reddit Topics directory

#### ✅ `website_rendering(site_url, wait_in_seconds, scroll)`

* Simulates full browser (scrolling included)
* Ideal for dynamic content: post lists, comment trees

#### 🧠 Tips:

* Use `scroll=0` for fast loading (e.g., post headers only)
* Use `scroll≥2` for full post feeds and deep comment threads
* Wait time helps ensure full page load before parsing

---

### 3b) 🧠 `reddit_topics.py` – Scraping Reddit Topics

Extracts all categorized topics from [reddit.com/topics](https://www.reddit.com/topics).

#### 🔁 Functions:

| Function             | Description                                         |
| -------------------- | --------------------------------------------------- |
| `get_letter_pages()` | Lists A-Z topic index pages                         |
| `get_subpages()`     | Fetches pagination for each letter section          |
| `scrape_topics()`    | Extracts topics + links from one page               |
| `scrape_all()`       | Full extraction pipeline across all pages           |
| `save_csv()`         | Stores topic list to `output/all_reddit_topics.csv` |

Each topic = `{ "Movies": "/t/movies/" }`

---

### 3c) 📰 `reddit_posts.py` – Scraping Posts in a Topic

Extracts post data from a topic link like `https://www.reddit.com/t/science/`.

#### ✅ `scrape_post(topic_url, wait_in_seconds, scroll)`

Returns a list of post dicts:

```json
{
  "title": "How AI is Changing Healthcare",
  "author": "TechNerd23",
  "link": "https://www.reddit.com/r/Health/comments/abc123/",
  "date": "1681234567",
  "comment_count": "45",
  "score": "210"
}
```

📌 Best used with `scroll=2` or higher for infinite feeds.

---

### 3d) 💬 `reddit_comments.py` Scraping Comments from a Post

Retrieves both post metadata and structured comment trees.

#### ✅ `scrape_comment(post_url, wait_in_seconds, scroll)`

Returns:

```json
{
  "post_details": {
    "title": "...",
    "author": "...",
    "score": "...",
    ...
  },
  "comment_details": [
    {
      "author": "user1",
      "score": "12",
      "depth": "1",
      "content": ["Paragraph 1", "Paragraph 2"]
    }
  ]
}
```

Supports:

* Nested replies via `depth`
* Metadata like `parent_id`, `score`, `timestamp`

📌 Ideal for NLP/sentiment studies or reply-chain reconstruction.

---
