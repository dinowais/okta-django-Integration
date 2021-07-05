from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# @login_required()
def TestView(TemplateView):
    template_name = "kukkker.html"

    def get(self, request, *args, **kwargs):
        print("><<<<<<????????"*1000)
        return self.render_to_response({})
