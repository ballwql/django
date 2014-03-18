#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='用户名',
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':'用户名',
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label='密码',
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'密码',
            }
        ),
    )   
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('用户名和密码为必填项')
        else:
            cleaned_data = super(LoginForm, self).clean() 
class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"原密码",
            }
        ),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"新密码",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
            }
        ),
     )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data
class CreatetaskForm(forms.Form):
    creater = forms.CharField(
        label=u"创建者",
        widget=BootstrapUneditableInput()
    )
    manager = forms.ModelChoiceField(
        queryset=Manager.objects.all(),
        required=True,
        label=u"项目负责人",
        error_messages={'required': u'必选项'},
    )  
    databases = forms.ModelMultipleChoiceField(
        queryset=Database.objects.order_by('id'),
        required=True,
        label=u"数据库",
        error_messages={'required': u'至少选择一个'},
        widget=forms.CheckboxSelectMultiple,
    )    
    sql = forms.CharField(
        required=False,
        label=u"执行SQL",
        widget=forms.Textarea(
            attrs={
                'placeholder':"请在表名前加上schema，如hospital要写成p95169.hospital",
                'rows':5,
                'style':"width:100%",
            }
        ),
    )
    desc = forms.CharField(
        required=False,
        label=u"描述",
        widget=forms.Textarea(
            attrs={
                'placeholder':"如果不是执行SQL(如数据的导入导出等)，一定要在描述里说清楚",
                'rows':5,
                'style':"width:100%",
            }
        ),
    ) 
    attachment = forms.FileField(
        required=False,
        label="附件",
        help_text="如果SQL文本过长，超过2000个字符，请上传附件"
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("以下红色标记部分为必选项")
        elif self.cleaned_data['sql'] == '' and self.cleaned_data['desc'] == u'' :
            raise forms.ValidationError("如果执行SQL为空，描述为必填项")
        else:
            cleaned_data = super(CreatetaskForm, self).clean() 
        return cleaned_data