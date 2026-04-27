import streamlit as st
import pickle as pk
from fuzzywuzzy import fuzz, process

movies = pk.load(open('movies.pkl', 'rb'))
similarity = pk.load(open('similarity.pkl', 'rb'))

# The Webpage settings
st.title("Welcome!")
st.subheader("  To Movie Recommender")
st.write("(Here you can find movies based on the context and the genres.)")
movie_name = st.text_input("Enter the name of a movie:")

st.markdown(
    """
    <div style="
        color: var(--st-text-color); 
        background-color: var(--st-secondary-background-color);
        padding: 10px;
        border-radius: 5px;
    ">
    </div>
    """,
    unsafe_allow_html=True
)


# Function to recommend movies


def recommend(movie):
    # get index of the input movie
    movie_ind = movies[movies['title'] == movie].index[0]
    # calculates the distance of the input movie at the index present in the dataset
    distance = similarity[movie_ind]
    # to get the top 5 movie's sorted based on the distance along with the movie's index
    movies_list = sorted(list(enumerate(distance)),
                         reverse=True, key=lambda x: x[1])[1:6]

    movies_recommended = []
    for i in movies_list:
        # it basically get the title of the movie by using the index that we get by using the enumerate function
        movies_recommended.append(movies.iloc[i[0]].title)
    return movies_recommended


if st.button('Recommend'):
    # 1. Clean the input and check length
    search_term = movie_name.strip()

    if len(search_term) < 3:
        st.warning("Please enter at least 3 characters.")
    else:
        # 2. Find the absolute BEST match using strict fuzz.ratio
        # score_cutoff=70 means anything below 70% is ignored (None)
        match = process.extractOne(
            search_term,
            movies['title'].tolist(),
            scorer=fuzz.ratio,
            score_cutoff=70
        )

        if match:
            # match is (title, score)
            matched_title = match[0]
            st.success(f"Matched: {matched_title} (Score: {match[1]})")

            # 3. Call your function
            recommendations = recommend(matched_title)
            for movie in recommendations:
                st.write(movie)
        else:
            # This triggers for "sfdad" because its ratio score will be very low
            st.error(
                f"No movie found matching '{search_term}' in our database. Try a different name!")
