import pandas as pd


items = pd.DataFrame({
    'title': ['John Wick', 'The Hangover', 'Mad Max: Fury Road', 'The Pursuit of Happyness', 'Superbad', 'Gladiator',
              'Shape of You', 'Bohemian Rhapsody', 'Eye of the Tiger', 'Let Her Go', 'Happy'],
    'genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Action',
              'Pop', 'Rock', 'Action', 'Drama', 'Comedy'],
    'rating': [4.5, 3.0, 4.8, 2.0, 3.5, 4.1,
               4.2, 3.8, 4.7, 3.2, 3.9],
    'type': ['Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie',
             'Music', 'Music', 'Music', 'Music', 'Music']
})


def rating_to_stars(rating):
    return '⭐' * int(round(rating))

def recommend_items(items, user_preferences, content_type='both', feature_col='genre', top_n=5):
 
    items = items.copy()
    items[feature_col] = items[feature_col].str.lower()
    user_preferences = [genre.lower().strip() for genre in user_preferences]

 
    recommended = items[items[feature_col].isin(user_preferences)]
    

    if content_type == 'movie':
        recommended = recommended[recommended['type'] == 'Movie']
    elif content_type == 'music':
        recommended = recommended[recommended['type'] == 'Music']


    recommended = recommended.sort_values(by='rating', ascending=False)
    recommended['stars'] = recommended['rating'].apply(rating_to_stars)

    return recommended.head(top_n)

def main():
    print("Welcome to the Movie & Music Recommendation System!\n")
    
    all_genres = sorted(items['genre'].unique())
    print(f"Available Genres: {', '.join(all_genres)}")

    user_input = input("Enter your preferred genres (comma-separated): ")
    user_preferences = [g.strip() for g in user_input.split(',') if g.strip()]
    
    content_type = input("Would you like 'movie', 'music', or 'both' recommendations? ").strip().lower()
    if content_type not in ['movie', 'music', 'both']:
        print("Invalid choice. Showing both by default.")
        content_type = 'both'

    recommendations = recommend_items(items, user_preferences, content_type)

    if not recommendations.empty:
        print("\nTop Recommendations:\n")
        print(recommendations[['title', 'genre', 'type', 'rating', 'stars']].to_string(index=False))
  
    else:
        print("\nNo items found matching your preferences.")

if __name__ == "__main__":
    main()
