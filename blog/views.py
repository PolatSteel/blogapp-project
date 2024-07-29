from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Blog,Category



  
# Create your views here.

def index(request):
    context = {
       "blogs": Blog.objects.filter(is_active=True,is_home=True),
       "categories" : Category.objects.all()
     }
    return render(request,"blog/index.html",context)
 
def blogs(request):
     context1 = {
       "blogs": Blog.objects.filter(is_active=True),
       "categories" : Category.objects.all()

      }
     return render(request,"blog/blogs.html",context1)

def blogdetails(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blogdetails.html", {
        "blog": blog
    })

def blogs_by_category(request,slug):
    context1 = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
    #    "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
       "categories" : Category.objects.all(),
       "selected_category" : slug
       
    }
    return render(request,"blog/blogs.html",context1)


# def blogdetails(request,id):
#      # blogs = data["blogs"]
#      # selectedblog= None
     
#      # for blog in blogs:
#      #      if( blog["id"]== id):
#      #           selectedblog = blog
     
#      blogs = data["blogs"]
#      selectedblog = [blog for blog in blogs if blog["id"]== id][0]
     
#      return render(request,"blog/blogdetails.html",{
#         "blog":selectedblog                           # Burada Tirnak icindeki degere ne yazarsan blogsdetails kisminada onu yazmak zorundayiz yoksa calismaz 
#      })

