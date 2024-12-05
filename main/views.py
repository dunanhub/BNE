from .models import Post
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Articles
from datetime import datetime
from .forms import SearchForm
from .forms import ArticlesForm
from django.views.generic import DeleteView, DetailView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse




def PostNews(request):
    PostNews = Post.objects.order_by('Date')
    return render(request,'Glavnaya.html', {"PostNews":PostNews})

class NewsDetailView(DetailView):
    model=Post
    template_name = 'Post.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Получаем стандартный контекст
        context['date_now'] = timezone.now()  # Добавляем текущую дату в контекст
        return context



def search_view(request):
    query = request.GET.get('query', '')
    postnews = Post.objects.filter(ClubName__icontains=query) if query else Post.objects.none()

    return render(request, 'search.html', {'PostNews': postnews, 'query': query})



def register(request, id):
    detail = Post.objects.get(pk=id)

    if request.method == "POST": 
        form = ArticlesForm(request.POST)
    
        
        if form.is_valid():
            article = form.save(commit=False)  # Не сохраняем пока в базе, чтобы изменить поля
            
            # Заполняем поля NameClub и NameNews из объекта detail
            article.NameClub = detail.ClubName
            article.NameNews = detail.NewsName
            
            # Сохраняем объект в базе данных
            article.save()
            
            return redirect('home')
    else:
        form=ArticlesForm()
    
    data={
         'form':form ,
         'detail':detail
    }
    return render(request, 'RegisterPage.html',data)



class PostRegDetailView(DetailView):   
    model=Post
    template_name = 'RegisterPage.html'
    context_object_name = 'reg'