from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
import logging
import json
import os

from .restapis import get_request, post_request, analyze_review_sentiments, backend_url
from .models import CarMake, CarModel

# Get an instance of a logger
logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(['POST'])
def login_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('userName', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'userName': username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'status': 'Authenticated'
            })
    except Exception as err:
        logger.exception(err)
    return JsonResponse({'status': 'Failed'})


@require_http_methods(['GET'])
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'status': 'Success', 'message': 'Logged out'})
    return JsonResponse({'status': 'NoUser'})


@csrf_exempt
@require_http_methods(['POST'])
def registration(request):
    try:
        data = json.loads(request.body)
        username = data.get('userName', '')
        password = data.get('password', '')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')

        if not username or not password:
            return JsonResponse({'status': 'Failed', 'message': 'Missing username or password'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'Failed', 'message': 'Username already exists'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        return JsonResponse({'status': 'Success', 'message': 'User created'})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'message': 'Unable to register user'})


@require_http_methods(['GET'])
def get_dealers(request):
    # endpoint = backend_url.rstrip('/') + '/fetchDealers'
    # dealers = get_request(endpoint)
    # if dealers is None:
    #     return JsonResponse({'status': 'Failed', 'dealers': []})
    # return JsonResponse({'status': 200, 'dealers': dealers})
    try:
        data_path = os.path.join(settings.BASE_DIR, 'database', 'data', 'dealerships.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            dealers = data.get('dealerships', [])
        return JsonResponse({'status': 200, 'dealers': dealers})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'dealers': []})


@require_http_methods(['GET'])
def get_dealers_by_state(request, state):
    # endpoint = backend_url.rstrip('/') + f'/fetchDealers/{state}'
    # dealers = get_request(endpoint)
    # if dealers is None:
    #     return JsonResponse({'status': 'Failed', 'dealers': []})
    # return JsonResponse({'status': 200, 'dealers': dealers})
    try:
        data_path = os.path.join(settings.BASE_DIR, 'database', 'data', 'dealerships.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            dealers = [d for d in data.get('dealerships', []) if d.get('state', '').lower() == state.lower()]
        return JsonResponse({'status': 200, 'dealers': dealers})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'dealers': []})


@require_http_methods(['GET'])
def get_dealer_details(request, dealer_id):
    # endpoint = backend_url.rstrip('/') + f'/fetchDealer/{dealer_id}'
    # dealer = get_request(endpoint)
    # if dealer is None:
    #     return JsonResponse({'status': 'Failed', 'dealer': []})
    # return JsonResponse({'status': 200, 'dealer': dealer})
    try:
        data_path = os.path.join(settings.BASE_DIR, 'database', 'data', 'dealerships.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            dealer = [d for d in data.get('dealerships', []) if d.get('id') == dealer_id]
        return JsonResponse({'status': 200, 'dealer': dealer})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'dealer': []})


@require_http_methods(['GET'])
def get_dealer_reviews(request, dealer_id):
    # endpoint = backend_url.rstrip('/') + f'/fetchReviews/dealer/{dealer_id}'
    # reviews = get_request(endpoint)
    # if reviews is None:
    #     return JsonResponse({'status': 'Failed', 'reviews': []})
    #
    # enhanced = []
    # for r in reviews:
    #     sentiment = analyze_review_sentiments(r.get('review', ''))
    #     if isinstance(sentiment, dict):
    #         r['sentiment'] = sentiment.get('sentiment', 'neutral')
    #     else:
    #         r['sentiment'] = 'neutral'
    #     enhanced.append(r)
    # return JsonResponse({'status': 200, 'reviews': enhanced})
    try:
        data_path = os.path.join(settings.BASE_DIR, 'database', 'data', 'reviews.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            reviews = [r for r in data.get('reviews', []) if r.get('dealership') == dealer_id]

        enhanced = []
        for r in reviews:
            sentiment = analyze_review_sentiments(r.get('review', ''))
            if isinstance(sentiment, dict):
                r['sentiment'] = sentiment.get('sentiment', 'neutral')
            else:
                r['sentiment'] = 'neutral'
            enhanced.append(r)
        return JsonResponse({'status': 200, 'reviews': enhanced})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'reviews': []})


@csrf_exempt
@require_http_methods(['POST'])
def add_review(request):
    # try:
    #     data = json.loads(request.body)
    #     endpoint = backend_url.rstrip('/') + '/insert_review'
    #     result = post_request(endpoint, data)
    #     if result is None:
    #         return JsonResponse({'status': 'Failed', 'message': 'Failed to add review'})
    #     return JsonResponse({'status': 200, 'review': result})
    # except Exception as err:
    #     logger.exception(err)
    #     return JsonResponse({'status': 'Failed', 'message': 'Invalid review payload'})
    try:
        data = json.loads(request.body)
        # For demo, just return success
        return JsonResponse({'status': 200, 'review': data})
    except Exception as err:
        logger.exception(err)
        return JsonResponse({'status': 'Failed', 'message': 'Invalid review payload'})


@require_http_methods(['GET'])
def get_cars(request):
    car_models = []
    db_carmodels = CarModel.objects.select_related('car_make').all()
    if db_carmodels.exists():
        for cm in db_carmodels:
            car_models.append({
                'CarMake': cm.car_make.name,
                'CarModel': cm.name,
            })
        return JsonResponse({'status': 200, 'CarModels': car_models})

    try:
        data_path = os.path.join(settings.BASE_DIR, 'database', 'data', 'car_records.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            seen = set()
            for record in data.get('car_records', []):
                key = (record.get('car_make', ''), record.get('car_model', ''))
                if key not in seen:
                    seen.add(key)
                    car_models.append({'CarMake': record.get('car_make', ''), 'CarModel': record.get('car_model', '')})
    except Exception as err:
        logger.exception(err)

    return JsonResponse({'status': 200, 'CarModels': car_models})


@require_http_methods(['GET'])
def analyze_review(request, review_text):
    sentiment = analyze_review_sentiments(review_text)
    return JsonResponse({'status': 200, 'sentiment': sentiment.get('sentiment', 'neutral')})
