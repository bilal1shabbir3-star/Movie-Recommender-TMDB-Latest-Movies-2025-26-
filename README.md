# Movie Recommender System 🎬

A **content-based movie recommendation system** built using the **TMDB Top 10,000 Movies dataset**. The system recommends movies based on their **title, overview, and genres**.

Instead of relying on user ratings or previous user behavior, this project analyzes the textual content of movies and finds movies with similar characteristics.

---

## 🚀 How It Works

The recommendation system follows the following pipeline:

```text
TMDB Movie Dataset
        ↓
Data Cleaning
        ↓
Feature Combination
        ↓
Text Preprocessing
        ↓
Text Vectorization
        ↓
Cosine Similarity
        ↓
Top 5 Similar Movies
```

### 1. Data Loading

The dataset contains information about movies, including:

* Movie ID
* Title
* Overview
* Vote Count
* Vote Average
* Genres

The following columns are used to build the recommendation system:

```python
['title', 'overview', 'genre_names']
```

---

### 2. Data Cleaning

Before building the recommendation system, the dataset is cleaned by:

* Removing missing values
* Removing duplicate rows
* Resetting the dataset index

This ensures that the recommendation system works with clean and consistent data.

---

### 3. Feature Engineering

The most important textual features are combined into a single column called `combined_text`.

```text
Movie Title + Movie Overview + Movie Genres
```

For example:

```text
Avatar Fire and Ash + movie overview + Science Fiction Adventure Fantasy
```

Combining these features allows the system to understand multiple aspects of each movie rather than relying on genres alone.

---

### 4. Text Preprocessing

The combined text goes through several preprocessing steps:

* Converting text to lowercase
* Removing punctuation
* Tokenization
* Lemmatization
* Removing English stopwords

Lemmatization helps convert words into their base form, allowing similar words to be treated more consistently.

For example:

```text
running → run
movies → movie
```

---

### 5. Text Vectorization

After preprocessing, the text is converted into numerical vectors using `CountVectorizer`.

```python
CountVectorizer(
    max_features=5000,
    stop_words='english'
)
```

The vectorizer represents each movie using the most important words from its combined textual information.

This allows mathematical comparison between movies.

---

### 6. Cosine Similarity

Once every movie is converted into a numerical vector, the system calculates the similarity between movies using **Cosine Similarity**.

Movies with similar:

* Genres
* Story descriptions
* Keywords
* Context

will receive higher similarity scores.

```text
Movie A ────────── 0.92
Movie B ────────── 0.81
Movie C ────────── 0.35
```

A higher score means that two movies have more similar content.

---

### 7. Generating Recommendations

When a user selects or enters a movie:

1. The system finds the movie in the dataset.
2. It retrieves that movie's similarity scores.
3. Movies are sorted from highest to lowest similarity.
4. The selected movie itself is excluded.
5. The top **5 most similar movies** are returned.

For example:

```text
Input: Avatar

Recommended Movies:
1. Avatar 4
2. Inuyashiki
3. Moonfall
4. Rebel Moon - Part One: A Child of Fire
5. Assassin's Creed
```

---

## 🔎 Fuzzy Movie Search

The web application also includes **fuzzy string matching** using `fuzzywuzzy`.

This means users do not always need to enter the exact movie title.

For example, if the dataset contains:

```text
Interstellar
```

The system can attempt to match similar user input rather than immediately failing.

A similarity threshold is used to prevent completely unrelated inputs from being matched.

---

## 🌐 Web Application

The recommendation system is deployed through a simple **Streamlit interface**.

The application allows users to:

1. Enter a movie name.
2. Search for the closest matching title.
3. Generate recommendations.
4. View the top 5 similar movies.

The application also handles invalid or very short inputs.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* CountVectorizer
* Cosine Similarity
* FuzzyWuzzy
* Streamlit
* Pickle

---

## 📁 Project Structure

```text
Movie-Recommender-TMDB-Latest-Movies-2025-26-
│
├── 2026_Movie_Recommendation_System.ipynb
│   └── Main notebook for data preprocessing,
│       vectorization, similarity calculation,
│       and recommendation generation
│
├── Movie.ipynb
│   └── Additional project notebook
│
├── Movie_Web.py
│   └── Streamlit web application
│
├── movies.pkl
│   └── Processed movie dataset
│
├── similarity.pkl
│   └── Precomputed cosine similarity matrix
│
├── README.md
│
└── LICENSE
```

---

## ▶️ Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/bilal1shabbir3-star/Movie-Recommender-TMDB-Latest-Movies-2025-26-.git
```

### 2. Navigate to the Project

```bash
cd Movie-Recommender-TMDB-Latest-Movies-2025-26-
```

### 3. Install the Required Libraries

```bash
pip install pandas numpy nltk scikit-learn streamlit fuzzywuzzy
```

### 4. Run the Streamlit Application

```bash
streamlit run Movie_Web.py
```

The application will open in your browser.

---

## 🧠 Recommendation Approach

This project uses **Content-Based Filtering**.

Unlike collaborative filtering, this approach does not require information about users or their ratings.

Instead, recommendations are based on the characteristics of the movies themselves.

```text
Movie Content
     ↓
Text Processing
     ↓
Numerical Representation
     ↓
Cosine Similarity
     ↓
Similar Movies
```

This means that if two movies have similar descriptions, themes, or genres, they are more likely to be recommended together.

---

## 📊 Dataset

The project uses a TMDB movie dataset containing approximately **10,000 movies**, including recent movies from the 2025–2026 period along with other titles in the dataset.

The recommendation model is built after cleaning the dataset and removing rows with missing or duplicate information.

---

## 🔮 Future Improvements

Possible improvements for the project include:

* Adding movie posters
* Displaying movie ratings
* Showing movie overviews
* Using the TMDB API for additional information
* Replacing Bag of Words with TF-IDF
* Using NLP embeddings such as Sentence Transformers
* Adding a hybrid recommendation system
* Improving recommendation quality with weighted features
* Deploying the application online

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Bilal Shabbir**

If you found this project useful, consider giving the repository a ⭐.
