from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg,Q
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Material,Course,Faculty,Department,Level,Review
from accounts.models import User,Uploader
from .forms import CreateMaterialForm,ReviewForm,FilterForm
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic.edit import FormMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.loader import render_to_string

# Create your views here.
class UploaderOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            uploader = Uploader.objects.get(user=self.request.user)
            return True
        except Uploader.DoesNotExist:
            return False

class CreateMaterial(UploaderOnlyMixin,CreateView):
    model = Material
    form_class = CreateMaterialForm
    template_name = "materialform.html"
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.course = Course.objects.get(code=self.kwargs.get("course"))
        self.object.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy("library:coursedetail",kwargs= {"pk":self.object.course.pk})

class UpdateMaterial(UploaderOnlyMixin,UpdateView):
    model = Material
    form_class = CreateMaterialForm
    template_name = "materialform.html"
    def get_success_url(self):
        return reverse_lazy("library:coursedetail",kwargs= {"pk":self.object.course.pk})

class DeleteMaterial(UploaderOnlyMixin,DeleteView):
    model = Material
    template_name = "material_delete.html"
    def get_success_url(self):
        return reverse_lazy("library:coursedetail",kwargs= {"pk":self.object.course.pk})
class CourseList(ListView):
    model = Course
    template_name = "courses.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] =  FilterForm
        context["departments"] = Department.objects.all()
        return context


class CourseDetail(DetailView):
    model = Course
    template_name = "course.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        context["media"] = settings.MEDIA_URL
        course = Course.objects.get(pk=self.kwargs.get("pk"))
        if Review.objects.filter(user=self.request.user):
            context["reviewed"] = True
        else:
            context["reviewed"] = False

        return context

@login_required
def add_review(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method=="POST":
        review = Review.objects.create(
        material = material,
        user = request.user,
        rating = request.POST.get("rating")
        )

        average_rating = Review.objects.filter(material=material).aggregate(rating=Avg("rating"))
        context = {
        "user" : request.user.username,
        "rating" : request.POST.get("rating"),
        "average_rating":average_rating

        }
        return JsonResponse(
            {
            "bool":True,
            "context":context
            })


def search_course(request):
    if request.method == "POST":
        q = request.POST["q"]
        if q:
            courses = Course.objects.filter(Q(title__icontains=q)|Q(code__icontains=q)).distinct()
    return render(request, 'base.html', {'results': courses})

def filter(request):
    if request.method == "POST":
        courses = Course.objects.all()
        if request.POST["faculty"] != "":
            faculty = Faculty.objects.get(name=request.POST["faculty"])
            courses = courses.filter(faculty=faculty)

        if request.POST["department"] != "":
            department = Department.objects.get(name=request.POST["department"])
            courses = courses.filter(department=department)

        if request.POST["level"] != "":
            level = Level.objects.get(name=request.POST["level"])
            courses = courses.filter(level=level)

        context = {
            "courses":courses
        }
        data =  render_to_string("filtered.html",context)
        return JsonResponse(
            {
            "data":data
            })
