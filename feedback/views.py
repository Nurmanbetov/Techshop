from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import FeedBackForm


@require_POST
def feedback(request):
    context = {}
    form = FeedBackForm(request.POST, require.FILES)
    if forms.is_valid():
        feedback = form.save()
        if request.is_authenticated:
            feedback.user = request.user
            feedback.save()
            
        context["message"] = "Ваше обрашение принято, спасибо!"
        context["type"] = "success"
        return render(request, "core/message.html", context)

    context["message"] = "Форма заполнено не верно!"
    context["type"] = "warnings"
    return render(request, "core/message.html", context)

    


