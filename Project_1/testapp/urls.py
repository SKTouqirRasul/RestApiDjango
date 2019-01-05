from django.urls import path
from testapp.views import ( StatusAPIView,
                           #StatusCreateAPIView,
                           StatusListSearchAPIView,
                           #SttusDetailAPIView,
                           #SttusDeleteAPIView,
                           #SttusUpdateAPIView
                           )

urlpatterns = [
    path('',StatusListSearchAPIView.as_view()),
    path('<int:pk>/',StatusAPIView.as_view()),
    #path('<int:pk>/',SttusDetailAPIView.as_view())
    #path('<int:pk>/update',SttusUpdateAPIView.as_view()),
    #path('<int:pk>/delete',SttusDeleteAPIView.as_view())

]
