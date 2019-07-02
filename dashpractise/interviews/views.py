from django.shortcuts import render, redirect
from .models import Interview
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlencode
from django.contrib import messages
# Create your views here.
def index(request):
    inter = Interview.objects.all()
    context = {
        'inter': inter
    }
    return render(request, 'interviews/index.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        interview = Interview.objects.get_or_create(name=name, email=email, phone=phone)
        interview.save()
        return redirect('interviews.index')
    return render(request, 'interviews/add.html')
# def index(request):
#     DB = Interview.objects
#     if request.GET.get('name'):
#         name = request.GET.get('name').strip()
#         DB = DB.filter(name__contains=name)
#     if request.GET.get('email'):
#         email = request.GET.get('email').strip()
#         DB = DB.filter(email__contains=email)
#     if request.GET.get('phone'):
#         phone = request.GET.get('phone').strip()
#         DB = DB.filter(phone__contains=phone)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(DB, 5)
#     try:
#         results = paginator.page(page)
#     except PageNotAnInteger:
#         results = paginator.page(1)
#     except EmptyPage:
#         results = paginator.page(paginator.num_pages)
#     # Get the index of the current page
#     index = results.number - 1  # edited to something easier without index
#     # This value is maximum index of your pages, so the last page - 1
#     max_index = len(paginator.page_range)
#     # You want a range of 7, so lets calculate where to slice the list
#     start_index = index - 3 if index >= 3 else 0
#     end_index = index + 3 if index <= max_index - 3 else max_index
#     # Get our new page range. In the latest versions of Django page_range returns
#     # an iterator. Thus pass it to list, to make our slice possible again.
#     page_range = list(paginator.page_range)[start_index:end_index]
#     searchingVariables = request.GET;
#     querySring = searchingVariables.copy()
#     if 'page' in querySring:
#         querySring.pop("page")
#     if 'direction' in querySring:
#         querySring.pop("direction")
#     if 'order_by' in querySring:
#         querySring.pop("order_by")
#
#     querySring = urlencode(querySring)
#     context = {
#         'results': results,
#         'page': page,
#         'searchingVariables': searchingVariables,
#         'querySring': querySring,
#         'page_range': page_range,
#     }
#     return render(request, 'interviews/index.html', context)
#
# def interview_Add(request):
#     interview = Interview.objects.all()
#     form = ""
#     validationErrors = {}
#     if request.method == "POST":
#         form = request.POST
#
#         if request.POST["name"] == "":
#             validationErrors["name"] = "The name field is required."
#
#         if request.POST["email"] == "":
#             validationErrors["action"] = "The Email field is required."
#
#         if request.POST["phone"] == "":
#               validationErrors["phone"] = "The Phone field is required."
#
#         if not validationErrors:
#             interview = Interview()
#             interview.name = request.POST["name"]
#             interview.email = request.POST["email"]
#             interview.phone = request.POST["phone"]
#             interview.save()
#             messages.success(request, "Added successfully.")
#             return redirect('/interviews/')
#
#     context = {
#         "form": form,
#         "errors": validationErrors,
#         "interview": interview
#
#     }
#     return render(request, "interviews/add.html", context)
