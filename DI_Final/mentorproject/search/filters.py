import django_filters
from accounts.models import *
from accounts.forms import AutocompleteProfileForm
from dal.autocomplete import ModelSelect2Multiple
from django import forms



# allows to filter by name, skill, location etc.

class ProfileFilter(django_filters.FilterSet):
    skills_wanted = django_filters.filters.ModelMultipleChoiceFilter(field_name='skills_wanted', queryset=Skill.objects.all(), widget=ModelSelect2Multiple(url='skill-autocomplete')),
    skills_have = django_filters.filters.ModelMultipleChoiceFilter(field_name='skills_have', queryset=Skill.objects.all(), widget=ModelSelect2Multiple(url='skill-autocomplete')),
    human_language = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset= HumanLanguage.objects.all(), field_name='human_language'),
    location = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset=Location.objects.all(), field_name='location')
    class Meta:
        model = Profile
        fields = ['profile_type']



class ProfileFilterTeacherside(django_filters.FilterSet):
    skills_wanted = django_filters.filters.ModelMultipleChoiceFilter(field_name='skills_wanted', queryset=Skill.objects.all(), widget=ModelSelect2Multiple(url='skill-autocomplete')),
    human_language = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset= HumanLanguage.objects.all(), field_name='human_language'),
    location = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset=Location.objects.all(), field_name='location')
    
    class Meta:
        model = Profile
        exclude = ['profile_type', 'image', 'company', 'linkedin', 'github']
        


class ProfileFilterStudentside(django_filters.FilterSet):
    skills_have = django_filters.filters.ModelMultipleChoiceFilter(field_name='skill_have', queryset=Skill.objects.all(), widget=ModelSelect2Multiple(url='skill-autocomplete')),
    human_language = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset= HumanLanguage.objects.all(), field_name='human_language'),
    location = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset=Location.objects.all(), field_name='location')
    class Meta:
        model = Profile
        exclude = ['profile_type', 'image', 'company', 'linkedin', 'github']


