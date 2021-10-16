from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def list_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/list.html', {'reviews': reviews})


@login_required
def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.save()
        return redirect('list_reviews')
    
    return render(request, 'reviews/form-create.html', {'form': form})


@login_required
def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('list_reviews')

    return render(request, 'reviews/form-update.html', {'form': form, 'review': review})


@login_required
def delete_review(request, id):
    task = get_object_or_404(Review, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('list_reviews')

def show_review(request, id):
    review = get_object_or_404(Review, pk=id)
    return render(request, 'reviews/show.html', {'review': review})


# Rascunho do Luan
# from list.html import input

# @login_required
# def search_review(request):
#     review = Review.objects.all()

#     for review in reviews:
#         if input == Review.title or input == Review.content:
#             return render(request)