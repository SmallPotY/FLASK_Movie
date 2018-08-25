# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm  # 表单基类
from wtforms.fields import SubmitField, StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError
from app.models import User


class RegistForm(FlaskForm):
    """会员注册"""
    name = StringField(  # 账号框
        label="昵称",  # 标签
        validators=[  # 验证器
            DataRequired("请输入昵称!")
        ],
        description="昵称",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入昵称",
        }
    )

    email = StringField(
        label="邮箱",  # 标签
        validators=[  # 验证器
            DataRequired("请输入邮箱!"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入邮箱",
            # "required": "required"
        }
    )

    phone = StringField(
        label="手机",  # 标签
        validators=[  # 验证器
            DataRequired("请输入手机!"),
            Regexp('1[3456]\d{9}', message="手机格式错误!")
        ],
        description="邮箱",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入手机",
            # "required": "required"
        }
    )

    pwd = PasswordField(  # 密码框
        label="密码",
        validators=[
            DataRequired("请输入密码!")
        ],
        description="密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请输入密码",
        }
    )

    repwd = PasswordField(  # 密码框
        label="确认密码",
        validators=[
            DataRequired("请再次输入密码!"),
            EqualTo("pwd", message="两次密码不一致！")
        ],
        description="密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请再次输入密码",
        }
    )

    submit = SubmitField(  # 提交按钮
        "注册",
        description="注册",
        render_kw={  # 自定义属性
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    # 唯一值验证
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在！")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在！")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号码已经存在！")


class LoginForm(FlaskForm):
    """登陆"""
    name = StringField(  # 账号框
        label="账号",  # 标签
        validators=[  # 验证器
            DataRequired("请输入账号!")
        ],
        description="账号",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入账号",
        }
    )

    pwd = PasswordField(  # 密码框
        label="密码",
        validators=[
            DataRequired("请输入密码!")
        ],
        description="密码",
        render_kw={  # 自定义属性
            "class": "form-control input-lg",
            "placeholder": "密码",
        }
    )

    submit = SubmitField(  # 提交按钮
        "登陆",
        description="登陆",
        render_kw={  # 自定义属性
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user != 1:
            raise ValidationError("账号不存在！")


class UserdetailForm(FlaskForm):
    """修改用户"""
    name = StringField(  # 账号框
        label="昵称",  # 标签
        validators=[  # 验证器
            DataRequired("请输入昵称!")
        ],
        description="昵称",  # 描述
        render_kw={  # 自定义属性
            "readonly ": True,
            "class": "form-control",
            "placeholder": "请输入昵称",
        }
    )

    email = StringField(
        label="邮箱",  # 标签
        validators=[  # 验证器
            DataRequired("请输入邮箱!"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入邮箱",
            # "required": "required"
        }
    )

    phone = StringField(
        label="手机",  # 标签
        validators=[  # 验证器
            DataRequired("请输入手机!"),
            Regexp('1[3456]\d{9}', message="手机格式错误!")
        ],
        description="邮箱",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入手机",
            # "required": "required"
        }
    )

    face = FileField(
        label='头像',
        description="头像",

    )

    info = TextAreaField(
        label="简介",
        validators=[DataRequired("请输入简介")],
        description="简介",
        render_kw={

            "class": "form-control",
            # "rows": '10'
        }
    )

    submit = SubmitField(  # 提交按钮
        '保存修改',
        description="登陆",
        render_kw={  # 自定义属性
            "class": "btn btn-success"
        }
    )


class PwdForm(FlaskForm):
    """修改密码"""
    old_pwd = PasswordField(  # 密码框
        label="旧密码",
        validators=[
            DataRequired("请输入旧密码!")
        ],
        description="旧密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请输入旧密码",
        }
    )

    new_pwd = PasswordField(  # 密码框
        label="新密码",
        validators=[
            DataRequired("请输入新密码!")
        ],
        description="新密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请输入新密码",
        }
    )

    submit = SubmitField(  # 提交按钮
        "提交",
        description="提交",
        render_kw={  # 自定义属性
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


class CommentForm(FlaskForm):
    """评论"""
    content = TextAreaField(
        label="评论内容",
        validators=[
            DataRequired("请输入内容!"),
        ],
        description="评论内容",  # 描述
        render_kw={
        "id":"input_content"
        }
    )

    submit = SubmitField(  # 提交按钮
        "提交",
        description="提交",
        render_kw={  # 自定义属性
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )
