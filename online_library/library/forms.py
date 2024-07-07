from django import forms
from .models import Material,Review,Faculty,Department,Level

class CreateMaterialForm(forms.ModelForm):
    class Meta():
        model = Material
        fields = ("name","file","preview")
        widgets = {
             "name" : forms.TextInput(attrs={"class":"",}),
             "file" : forms.FileInput(attrs={"class":"",}),
             "preview" : forms.Textarea(attrs={"class":"",}),
        }
class ReviewForm(forms.ModelForm):
    ratings = [
    ("","Rate material"),
    (5,"⭐⭐⭐⭐⭐"),
    (4,"⭐⭐⭐⭐"),
    (3,"⭐⭐⭐"),
    (2,"⭐⭐"),
    (1,"⭐"),
    ]
    rating = forms.ChoiceField(choices=ratings,widget=forms.Select(attrs={}))
    class Meta:
        model = Review
        fields = ["rating"]

class FilterForm(forms.Form):

    faculties = [("","Faculty")]
    faculties.extend([(faculty.name,faculty.name) for faculty in Faculty.objects.all()])
    faculty = forms.ChoiceField(choices=faculties,required=False)

    departments = [("","Department")]
    departments.extend([(department.name,department.name) for department in Department.objects.all()])
    department = forms.ChoiceField(choices= departments,required=False)

    levels = [("","Level")]
    levels.extend([(level.name,level.name) for level in Level.objects.all()])
    level = forms.ChoiceField(choices=levels,required=False)
