from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from tweets.models import Tweet
# from tweets.serializers import TweetSerializer
from rest_framework.decorators import api_view

# def home(request):
#     return HttpResponse("Hello World")


# def home(request):
#     return render(request, 'tweets/home.html')
def home(request):
    tweets = Tweet.objects.all()
    context = {}
    context['tweets'] = tweets
    context['any_variable'] = 'hello world'
    return render(request, 'tweets/index.html', context)



# def index(request):
#     return HttpResponse("<html>Hello World</html>")

#     print("------------------------- I AM HERE")
#     queryset = Tweet.objects.all()
#     return render(request, "tweets/index.html", {'tweets': queryset})

# class index(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tweets/index.html'

#     def get(self, request):
#         queryset = Tweet.objects.all()
#         return Response({'tweets': queryset})


# class list_all_tweets(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tweets/tweet_list.html'

#     def get(self, request):
#         queryset = Tweet.objects.all()
#         return Response({'tweets': queryset})

# # Create your views here.
# @api_view(['GET', 'POST', 'DELETE'])
# def tweet_list(request):
#     if request.method == 'GET':
#         tweets = Tweet.objects.all()

#         title = request.GET.get('title', None)
#         if title is not None:
#             tweets = tweets.filter(title__icontains=title)

#         tweets_serializer = TweetSerializer(tweets, many=True)
#         return JsonResponse(tweets_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

#     elif request.method == 'POST':
#         tweet_data = JSONParser().parse(request)
#         tweet_serializer = TweetSerializer(data=tweet_data)
#         if tweet_serializer.is_valid():
#             tweet_serializer.save()
#             return JsonResponse(tweet_serializer.data,
#                                 status=status.HTTP_201_CREATED)
#         return JsonResponse(tweet_serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         count = Tweet.objects.all().delete()
#         return JsonResponse(
#             {
#                 'message':
#                 '{} Tweets were deleted successfully!'.format(count[0])
#             },
#             status=status.HTTP_204_NO_CONTENT)