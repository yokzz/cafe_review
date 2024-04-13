from django.shortcuts import render
from cafe.models import Review

def get_reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, template_name="cafe/review_list.html", context=context)