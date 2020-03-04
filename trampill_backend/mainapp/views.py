from django.views import generic
from . import models
from . import forms


class ModelsCourseItemForm:
    model = models.CourseItem
    form_class = forms.CourseItemForm


class CourseItemListView(ModelsCourseItemForm, generic.ListView):
    pass


class CourseItemCreateView(ModelsCourseItemForm, generic.CreateView):
    pass


class CourseItemDetailView(ModelsCourseItemForm, generic.DetailView):
    pass


class CourseItemUpdateView(ModelsCourseItemForm, generic.UpdateView):
    pk_url_kwarg = "pk"


class ModelsCategoryForm:
    """
    use for category list, create, detail, update
    """
    model = models.Category
    form_class = forms.CategoryForm


class CategoryListView(ModelsCategoryForm, generic.ListView):
    pass


class CategoryCreateView(ModelsCategoryForm, generic.CreateView):
    pass


class CategoryDetailView(ModelsCategoryForm, generic.DetailView):
    pass


class CategoryUpdateView(ModelsCategoryForm, generic.UpdateView):
    pk_url_kwarg = "pk"


class ModelsCourseForm:
    """
    use for Course list, create, detail, update
    """
    model = models.Course
    form_class = forms.CourseForm


class CourseListView(ModelsCourseForm, generic.ListView):
    pass


class CourseCreateView(ModelsCourseForm, generic.CreateView):
    pass


class CourseDetailView(ModelsCourseForm, generic.DetailView):
    pass


class CourseUpdateView(ModelsCourseForm, generic.UpdateView):
    pk_url_kwarg = "pk"
