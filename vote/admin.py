from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm


from vote.models import Subject, Teacher, User

# Register your models here.
from django.contrib import admin

from vote.views import USERNAME_PATTERN, to_md5_hex


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')
    ordering = ('no',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count', 'subject')
    ordering = ('subject', 'no')


class UserForm(ModelForm):
    password = forms.CharField(min_length=8, max_length=20,
                               widget=forms.PasswordInput, label='密码')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError('用户名由字母、数字和下划线构成且长度为4-20个字符')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        return to_md5_hex(self.cleaned_data['password'])

    class Meta:
        model = User
        exclude = ('no',)


class UserAdmin(admin.ModelAdmin):
    # 该list_display中无法添加model中不存在的字段
    list_display = ('no', 'username', 'password')
    ordering = ('no',)
    form = UserForm
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
