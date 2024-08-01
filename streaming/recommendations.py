from django.db.models import Count, Q
from .models import UserProfile, Movie, Review
from collections import defaultdict

def get_similarity(user1, user2):
    """ Calculate similarity score between two users """
    user1_likes = set(user1.liked_movies.values_list('id', flat=True))
    user2_likes = set(user2.liked_movies.values_list('id', flat=True))
    
    common_likes = user1_likes.intersection(user2_likes)
    total_likes = user1_likes.union(user2_likes)
    
    if not total_likes:
        return 0
    
    # Jaccard similarity
    return len(common_likes) / len(total_likes)

def recommend_movies(user):
    profile = UserProfile.objects.get(user=user)
    liked_movies = profile.liked_movies.all()
    
    # Calculate similarity scores with other users
    user_profiles = UserProfile.objects.exclude(user=user)
    similarity_scores = [(get_similarity(profile, up), up) for up in user_profiles]
    similarity_scores = sorted(similarity_scores, key=lambda x: x[0], reverse=True)
    
    # Aggregate recommendations
    recommended_movies = defaultdict(float)
    for score, up in similarity_scores[:10]:  # Consider top 10 similar users
        for movie in up.liked_movies.all():
            if movie not in liked_movies:
                recommended_movies[movie] += score

        # Consider highly rated movies by similar users
        highly_rated_movies = Review.objects.filter(user=up.user, rating__gte=4).values_list('movie', flat=True)
        for movie_id in highly_rated_movies:
            movie = Movie.objects.get(id=movie_id)
            if movie not in liked_movies:
                recommended_movies[movie] += score

    # Sort recommendations by score
    recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    recommended_movies = [movie for movie, score in recommended_movies]

    return recommended_movies
