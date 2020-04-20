from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Student
from django.db.models import Q
from django.db.models import Sum

# Create your views here.
def department_list(request):
    department_list = Student.objects.all()
    return render(request, "department_app/department_list.html", {
        'department_list': department_list
    })

def department_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DepartmentForm()
        else:
            department = Student.objects.get(pk=id)
            form = DepartmentForm(instance=department)
        return render(request, "department_app/department_form.html",{
            'form': form
        })
    else:
        if id == 0:
            form = DepartmentForm(request.POST)
        else:
            department = Student.objects.get(pk=id)
            form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        return redirect('/department/list')

def department_delete(request, id):
    department = Student.objects.get(pk=id)
    department.delete()
    return redirect('/department/list')

def mech_dept(request):
    list = Student.objects.filter(dept_id=1)
    if list:
        return render(request, "department_app/mech_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def elect_dept(request):
    list = Student.objects.filter(dept_id=2)
    if list:
        return render(request, "department_app/elect_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def civil_dept(request):
    list = Student.objects.filter(dept_id=3)
    if list:
        return render(request, "department_app/civil_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def comp_engr_dept(request):
    list = Student.objects.filter(dept_id=4)
    if list:
        return render(request, "department_app/comp_engr_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def sci_lab_dept(request):
    list = Student.objects.filter(dept_id=5)
    if list:
        return render(request, "department_app/sci_lab_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def food_dept(request):
    list = Student.objects.filter(dept_id=6)
    if list:
        return render(request, "department_app/food_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def pharm_dept(request):
    list = Student.objects.filter(dept_id=7)
    if list:
        return render(request, "department_app/pharm_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def agric_dept(request):
    list = Student.objects.filter(dept_id=8)
    if list:
        return render(request, "department_app/agric_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def dispense_dept(request):
    list = Student.objects.filter(dept_id=9)
    if list:
        return render(request, "department_app/dispense_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def comp_sci_dept(request):
    list = Student.objects.filter(dept_id=10)
    if list:
        return render(request, "department_app/comp_sci_dept.html", {
            'list': list
        })
    else:
        return render(request, "department_app/none.html")

def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(fullname__icontains=query)
            results = Student.objects.filter(lookups)
            context = {
                'results': results,
                'submitbutton': submitbutton
            }
            return render(request, 'department_app/search.html', context)
        else:
            return render(request, 'department_app/none.html')
    else:
        return render(request, 'department_app/department_list.html')