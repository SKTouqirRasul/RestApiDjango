from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serialize import StatusSerializer
from testapp.models import Status
from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404

# Create your views here.

class StatusListSearchAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    '''def get(self,request,format=None):
        qs=Status.objects.all()
        Serializer = StatusSerializer(qs, many=True)
        return Response(Serializer.data)'''


class StatusAPIView(
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    #mixins.ListModelMixin,
                    generics.GenericAPIView):

    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


    '''def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs'''

    '''def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset,id=passed_id)
            self.check_object_permissions(request,obj)
        return obj'''


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


    #def get(self,request,*args,**kwargs):
    #    return self.list(request,*args,**kwargs)








'''
class StatusAPIView(mixins.ListModelMixin,generics.GenericAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

'''
class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    #def perform_create(self, serializer):
    #    serializer.save(user= self.request.user)
'''
class SttusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer



'''
'''
class SttusDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    def get_object(self,*args,**kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('abc')
        return Status.objects.get(id=kw_id)
'''
'''
class SttusUpdateAPIView(generics.UpdateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
'''
'''
class SttusDeleteAPIView(generics.DestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
'''
