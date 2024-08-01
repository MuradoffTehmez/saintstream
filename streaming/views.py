from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Avg
from .models import (
    BlogPost, Category, Forum, ForumPost, ForumThread, LiveEvent, Movie, 
    SubscriptionPlan, Topic, UserProfile, Review, WatchHistory, Watchlist, Series
)
from .forms import (
    CommentForm, ForumThreadForm, PasswordResetForm, SearchForm, SignupForm, 
    LoginForm, ProfileForm, ContactForm, ReviewForm
)

@login_required
def movie_detail(request, movie_id):
    try:
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = movie.reviews.all()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                # Update average rating
                avg_rating = movie.reviews.aggregate(Avg('rating'))['rating__avg']
                movie.average_rating = avg_rating
                movie.save()
                return redirect('movie_detail', movie_id=movie.id)
        else:
            form = ReviewForm()

        return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form})
    except Exception as e:
        print(f"Error in movie_detail view: {e}")
        return render(request, 'error.html')

@login_required
def recommendations(request):
    try:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        watched_movies = user_profile.watched_movies.all()
        recommended_movies = Movie.objects.exclude(id__in=watched_movies)
        return render(request, 'recommendations.html', {'movies': recommended_movies})
    except Exception as e:
        print(f"Error in recommendations view: {e}")
        return render(request, 'error.html')

@login_required
def watchlist(request):
    try:
        watchlist = Watchlist.objects.filter(user=request.user)
        return render(request, 'watchlist.html', {'watchlist': watchlist})
    except Exception as e:
        print(f"Error in watchlist view: {e}")
        return render(request, 'error.html')

def search(request):
    try:
        query = request.GET.get('q', '')
        movies = Movie.objects.filter(title__icontains=query)
        series = Series.objects.filter(title__icontains=query)
        return render(request, 'search.html', {'movies': movies, 'series': series})
    except Exception as e:
        print(f"Error in search view: {e}")
        return render(request, 'error.html')

def search_view(request):
    try:
        form = SearchForm(request.GET or None)
        results = []
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Movie.objects.filter(Q(title__icontains=query) | Q(categories__name__icontains=query)).distinct()
        return render(request, 'search.html', {'form': form, 'results': results})
    except Exception as e:
        print(f"Error in search_view: {e}")
        return render(request, 'error.html')

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    try:
        return render(request, 'admin_dashboard.html')
    except Exception as e:
        print(f"Error in admin_dashboard view: {e}")
        return render(request, 'error.html')

def categories_view(request):
    try:
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})
    except Exception as e:
        print(f"Error in categories_view: {e}")
        return render(request, 'error.html')

def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Handle contact form submission (e.g., send email)
                return redirect('contact_done')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    except Exception as e:
        print(f"Error in contact view: {e}")
        return render(request, 'error.html')

def contact_done(request):
    try:
        return render(request, 'contact_done.html')
    except Exception as e:
        print(f"Error in contact_done view: {e}")
        return render(request, 'error.html')

def home(request):
    try:
        # Logic to display featured content
        return render(request, 'home.html')
    except Exception as e:
        print(f"Error in home view: {e}")
        return render(request, 'error.html')

def genre_discover(request):
    try:
        # Logic for genre discovery
        return render(request, 'discover.html')
    except Exception as e:
        print(f"Error in genre_discover view: {e}")
        return render(request, 'error.html')

def new_releases(request):
    try:
        movies = Movie.objects.order_by('-release_date')[:10]
        return render(request, 'new_releases.html', {'movies': movies})
    except Exception as e:
        print(f"Error in new_releases view: {e}")
        return render(request, 'error.html')

def forum_home(request):
    try:
        forums = Forum.objects.all()
        return render(request, 'forum_home.html', {'forums': forums})
    except Exception as e:
        print(f"Error in forum_home view: {e}")
        return render(request, 'error.html')

def discussion(request):
    try:
        # Logic for discussions
        return render(request, 'discussion.html')
    except Exception as e:
        print(f"Error in discussion view: {e}")
        return render(request, 'error.html')

def create_profile(request):
    try:
        # Logic for creating a profile
        return render(request, 'create_profile.html')
    except Exception as e:
        print(f"Error in create_profile view: {e}")
        return render(request, 'error.html')

def forum_after_create(request):
    try:
        # Logic for after creating a forum
        return render(request, 'forum_after_create.html')
    except Exception as e:
        print(f"Error in forum_after_create view: {e}")
        return render(request, 'error.html')

def movie_topic(request):
    try:
        # Logic for movie topics
        return render(request, 'movie_topic.html')
    except Exception as e:
        print(f"Error in movie_topic view: {e}")
        return render(request, 'error.html')

@login_required
def dashboard(request):
    try:
        # Logic for dashboard
        return render(request, 'dashboard.html')
    except Exception as e:
        print(f"Error in dashboard view: {e}")
        return render(request, 'error.html')

@login_required
def watch_history(request):
    try:
        history = WatchHistory.objects.filter(user=request.user)
        return render(request, 'watch_history.html', {'history': history})
    except Exception as e:
        print(f"Error in watch_history view: {e}")
        return render(request, 'error.html')

@login_required
def settings(request):
    try:
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('settings')
        else:
            form = ProfileForm(instance=request.user)
        return render(request, 'settings.html', {'form': form})
    except Exception as e:
        print(f"Error in settings view: {e}")
        return render(request, 'error.html')

def about_us(request):
    try:
        return render(request, 'about_us.html')
    except Exception as e:
        print(f"Error in about_us view: {e}")
        return render(request, 'error.html')

def help_support(request):
    try:
        return render(request, 'help_support.html')
    except Exception as e:
        print(f"Error in help_support view: {e}")
        return render(request, 'error.html')

@login_required
def user_reviews(request):
    try:
        reviews = Review.objects.filter(user=request.user)
        return render(request, 'user_reviews.html', {'reviews': reviews})
    except Exception as e:
        print(f"Error in user_reviews view: {e}")
        return render(request, 'error.html')

def subscription_plans(request):
    try:
        plans = SubscriptionPlan.objects.all()
        return render(request, 'subscription_plans.html', {'plans': plans})
    except Exception as e:
        print(f"Error in subscription_plans view: {e}")
        return render(request, 'error.html')

def mobile_app_download(request):
    try:
        return render(request, 'mobile_app_download.html')
    except Exception as e:
        print(f"Error in mobile_app_download view: {e}")
        return render(request, 'error.html')

def live_events(request):
    try:
        events = LiveEvent.objects.all()
        return render(request, 'live_events.html', {'events': events})
    except Exception as e:
        print(f"Error in live_events view: {e}")
        return render(request, 'error.html')

def blog(request):
    try:
        posts = BlogPost.objects.all()
        return render(request, 'blog.html', {'posts': posts})
    except Exception as e:
        print(f"Error in blog view: {e}")
        return render(request, 'error.html')

def login_view(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    except Exception as e:
        print(f"Error in login_view: {e}")
        return render(request, 'error.html')

def signup_view(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    except Exception as e:
        print(f"Error in signup_view: {e}")
        return render(request, 'error.html')

def faq(request):
    try:
        return render(request, 'faq.html')
    except Exception as e:
        print(f"Error in faq view: {e}")
        return render(request, 'error.html')

def privacy_policy(request):
    try:
        return render(request, 'privacy_policy.html')
    except Exception as e:
        print(f"Error in privacy_policy view: {e}")
        return render(request, 'error.html')

def terms_conditions(request):
    try:
        return render(request, 'terms_conditions.html')
    except Exception as e:
        print(f"Error in terms_conditions view: {e}")
        return render(request, 'error.html')

def password_reset(request):
    return render(request, 'password_reset.html')

def profile(request):
    return render(request, 'profile.html')

def forum_thread_view(request, thread_id):
    return render(request, 'forum_thread.html', {'thread_id': thread_id})

def create_forum_thread_view(request):
    return render(request, 'create_forum_thread.html')

def user_activity_view(request):
    return render(request, 'user_activity.html')

def profile_edit_view(request):
    return render(request, 'profile_edit.html')

def password_reset_request_view(request):
    return render(request, 'password_reset_request.html')