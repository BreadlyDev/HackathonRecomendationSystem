from rest_framework import permissions, generics, status, views, response as r

from . import models as m, serializers as s

from AI.ai import recommender


class MusicByValueCreateAPIView(generics.CreateAPIView):
    serializer_class = s.MusicByValueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MusicByValueListAPIView(generics.ListAPIView):
    queryset = m.MusicByValue.objects.all()
    serializer_class = s.MusicByValueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return m.MusicByValue.objects.filter(user=user)


class MusicByValueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.MusicByValue.objects.all()
    serializer_class = s.MusicByValueSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecommendationBySongAPIView(views.APIView):

    def get(self, request):
        result = recommender(request.data['song'])

        if not result:
            return r.Response('Песня не найдена')
        return r.Response(result)
