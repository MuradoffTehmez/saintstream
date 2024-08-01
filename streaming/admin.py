from django.contrib import admin
from .models import Movie, Series, Review, UserProfile, ForumPost, Genre, WatchHistory, Watchlist, BlogPost, SubscriptionPlan, LiveEvent, Category

# Single registration with admin.ModelAdmin classes
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'seasons')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'comment', 'rating', 'user')
    search_fields = ('movie__title', 'user__username')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('get_topic', 'author', 'other_field', 'short_content', 'thread', 'content', 'created_at', 'updated_at')
    search_fields = ('topic__title', 'author__username')

    def get_topic(self, obj):
        return obj.topic.title 
    get_topic.short_description = 'Topic'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'watched_at')
    search_fields = ('user__username', 'movie__title')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')
    search_fields = ('user__username', 'movie__title')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_months')
    search_fields = ('name',)

@admin.register(LiveEvent)
class LiveEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date')
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
