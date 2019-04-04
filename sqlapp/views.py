from django.shortcuts import render
from django.http import HttpResponse
from django.views import views
from django.http import JsonResponse

# Create your views here.

from django.views.generic import View
from django.shortcuts import redirect, render
from django.forms.models import modelform_factory
from django.http import HttpResponse

from .models import MyModel

class RestView(View):
  def get(self, request):
    # retrieve some object and render in template
    object = MyModel.objects.get(pk=request.GET['pk'])
    return render(request, 'object_detail.html',
                  {'object': object})

  def put(self, request):
    # create an object and redirect to detail page
     modelform = modelform_factory(MyModel)
    form = modelform(request.PUT)
    if form.is_valid():
        form.save()
    return redirect('restview')

  def delete(self, request):
    # delete an object and send a confirmation response
    MyModel.objects.get(pk=request.DELETE['pk']).delete()
    return HttpResponse()

    $.ajax({
    type: 'POST',
    url: '/restview',
    data: { pk: pk },
    success: function() {
        alert('Object deleted!')
    },
    headers: { 'X_METHODOVERRIDE': 'DELETE' }
});
