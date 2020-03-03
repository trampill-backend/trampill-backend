from django.views import generic
from . import models
from . import forms


class CourseItemListView(generic.ListView):
    model = models.CourseItem
    form_class = forms.CourseItemForm


class CourseItemCreateView(generic.CreateView):
    model = models.CourseItem
    form_class = forms.CourseItemForm


class CourseItemDetailView(generic.DetailView):
    model = models.CourseItem
    form_class = forms.CourseItemForm


class CourseItemUpdateView(generic.UpdateView):
    model = models.CourseItem
    form_class = forms.CourseItemForm
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    pk_url_kwarg = "pk"


class CourseListView(generic.ListView):
    model = models.Course
    form_class = forms.CourseForm


class CourseCreateView(generic.CreateView):
    model = models.Course
    form_class = forms.CourseForm


class CourseDetailView(generic.DetailView):
    model = models.Course
    form_class = forms.CourseForm


class CourseUpdateView(generic.UpdateView):
    model = models.Course
    form_class = forms.CourseForm
    pk_url_kwarg = "pk"
