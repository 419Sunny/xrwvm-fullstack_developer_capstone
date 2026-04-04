from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='registration'),
    path('get_dealers', views.get_dealers, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
    # Aliases matching dealership API path names (used in course materials / cURL tasks)
    path('fetchDealers', views.get_dealers, name='fetch_dealers'),
    path('fetchDealers/<str:state>', views.get_dealers_by_state, name='fetch_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='get_dealer_details'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    path(
        'fetchReviews/dealer/<int:dealer_id>',
        views.get_dealer_reviews,
        name='fetch_reviews_by_dealer',
    ),
    path('add_review', views.add_review, name='add_review'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('analyze_review/<str:review_text>', views.analyze_review, name='analyze_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
