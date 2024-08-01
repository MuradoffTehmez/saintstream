from django.db import models
from django.contrib.auth.models import User

# Movie model with fields for title, release date, description, average rating, and categories
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    average_rating = models.FloatField(default=0)
    categories = models.ManyToManyField('Category', related_name='movies')
    poster = models.ImageField(upload_to='movies/posters/', blank=True, null=True)

    def __str__(self):
        return self.title


# Series model for TV shows with seasons
class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    seasons = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='series/posters/', blank=True, null=True)

    def __str__(self):
        return self.title

# Review model linking users and movies with rating and comment fields
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.movie.title} - {self.user.username}'

# Genre model for categorizing movies
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# WatchHistory model to track when users watch movies
class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

# Watchlist model to manage users' watchlist
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

# Forum and related models for discussions
class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Topic(models.Model):
    forum = models.ForeignKey(Forum, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

# Category model for movie categorization
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# BlogPost model for managing blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# SubscriptionPlan model for managing subscription plans
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# LiveEvent model for live streaming events
class LiveEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()
    streaming_url = models.URLField()
    image = models.ImageField(upload_to='live_events/', blank=True, null=True)

    def __str__(self):
        return self.title

# Profile model to extend user information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# ForumThread and ForumPost models for forum functionality
class ForumThread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Post by {self.author.username} in {self.thread.title}'

    def short_content(self):
        return self.content[:50]

    short_content.short_description = 'Short Content'