from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('discover/', views.genre_discover, name='discover'),
    path('new-releases/', views.new_releases, name='new_releases'),
    path('forum/', views.forum_home, name='forum_home'),
    path('discussion/', views.discussion, name='discussion'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('forum/after-create/', views.forum_after_create, name='forum_after_create'),
    path('movie-topic/', views.movie_topic, name='movie_topic'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('watch-history/', views.watch_history, name='watch_history'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('settings/', views.settings, name='settings'),
    path('about-us/', views.about_us, name='about_us'),
    path('help-support/', views.help_support, name='help_support'),
    path('user-reviews/', views.user_reviews, name='user_reviews'),
    path('subscription-plans/', views.subscription_plans, name='subscription_plans'),
    path('mobile-app-download/', views.mobile_app_download, name='mobile_app_download'),
    path('live-events/', views.live_events, name='live_events'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup_view'),
    # path('signup_filled/', views.signup_filled, name='signup_filled'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('contact-done/', views.contact_done, name='contact_done'),
    path('categories/', views.categories_view, name='categories_view'),
    path('search/', views.search_view, name='search_view'),
    path('forum/thread/<int:thread_id>/', views.forum_thread_view, name='forum_thread'),
    path('forum/create/', views.create_forum_thread_view, name='create_forum_thread'),
    path('user/activity/', views.user_activity_view, name='user_activity_view'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('password-reset/request/', views.password_reset_request_view, name='password_reset_request'),
    path('password-reset/', views.password_reset, name='password_reset'),

]
