from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Loc
from .serializers import LocSerializer

# Create your views here.


class LocationView(APIView):
    def get(self,request):
        locations = Loc.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = LocSerializer(locations,many=True)
        return Response({"locations": serializer.data})

    def post(self,request):
        location = request.data.get('locations')

        # create an article from the above data
        serializer = LocSerializer(data=location)
        if serializer.is_valid(raise_exception=True):
            location_saved = serializer.save()
        return Response({"location": serializer.data})


    # def put(self,request,pk):
    #     saved_article = get_object_or_404(Article.objects.all(),pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article,data=data,partial=True) # bcz we want to update only some fields not  a whole article so partial is true
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success":f"Article {article_saved.title} updated successfully."})
    #
    # def delete(self,request,pk):
    #     # get object with this pk
    #     article = get_object_or_404(Article.objects.all(),pk=pk)
    #     article.delete()
    #     return Response({"message":f"Article with id {pk} has been deleted."},status=204)
