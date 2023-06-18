from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Quote,Author
from .forms import AuthorForm, QuoteForm, TagForm
from . models import Author, Quote, Tag

from .utils import get_mongodb

def main(request, page=1):
    quotes =Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes':quotes_on_page})

def about_author(request, _id):
    author = Author.objects.get(pk=_id)
    return render(request, 'quotes/author.html', context={'author': author})

def create_new_quote(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        quote_form = QuoteForm(request.POST)
        tag_form = TagForm(request.POST)

        if author_form.is_valid() and quote_form.is_valid() and tag_form.is_valid():
            author = author_form.save()  # Збереження об'єкту Author
            quote = quote_form.save(commit=False)  # Створення об'єкту Quote без збереження в базі даних
            quote.author = author  # Прив'язка об'єкту Quote до об'єкту Author
            quote.save()  # Збереження об'єкту Quote з прив'язкою до об'єкту Author
            t = tag_form.save() # Збереження об'єкту Tag
            tags = Tag.objects.filter(name__in=request.POST.getlist('name')) # Знаходимо тег
            for tag in tags:
                quote.tags.add(tag)  # Додавання тегу до об'єкту Quote
            return redirect(to='quotes:root')  # Перенаправлення на головну сторінку

    else:
        author_form = AuthorForm()
        quote_form = QuoteForm()
        tag_form = TagForm()
        
    
    return render(request, 'quotes/create_new_quote.html', {'author_form': AuthorForm(), 'quote_form': QuoteForm(), 'tag_form': TagForm})









