from django.shortcuts import render,HttpResponse,redirect
from kenadmin import kenadmin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from kenadmin.utils import table_filter, table_sort, table_search
from kenadmin.forms import create_model_form
# Create your views here.
def index(request):
    return render(request, "kenadmin/table_index.html", {'table_list': kenadmin.enabled_admins})


def display_table_objs(request, app_name, table_name):
    # models_module = importlib.import_module('%s.models'%(app_name))
    # model_obj = getattr(models_module,table_name)
    admin_class = kenadmin.enabled_admins[app_name][table_name]
    # admin_class = king_admin.enabled_admins[crm][userprofile]

    # object_list = admin_class.model.objects.all()
    object_list, filter_condtions = table_filter(request, admin_class)  # 过滤后的结果

    object_list = table_search(request, admin_class, object_list)

    object_list, orderby_key = table_sort(request, admin_class, object_list)  # 排序后的结果

    paginator = Paginator(object_list, admin_class.list_per_page)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_sets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_sets = paginator.page(paginator.num_pages)

    return render(request, "kenadmin/table_objs.html", {"admin_class": admin_class,
                                                        "query_sets": query_sets,
                                                        "filter_condtions": filter_condtions,
                                                        "orderby_key": orderby_key,
                                                        "previous_orderby": request.GET.get("o", ''),
                                                        "search_text": request.GET.get('_q', '')})

def table_obj_add(request,app_name,table_name):
    admin_class = kenadmin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(request,admin_class)

    if request.method == "POST":
        form_obj = model_form_class(request.POST)  #
        if form_obj.is_valid():
            form_obj.save()
            return  redirect(request.path.replace("/add/","/"))
    else:
        form_obj = model_form_class()

    return render(request, "king_admin/table_obj_add.html", {"form_obj": form_obj,
                                                             "admin_class": admin_class})

def display_test(request):
    from learn.crm import models
    objectlist=models.Customer.objects.order_by("-id")

    return  HttpResponse("ok");
