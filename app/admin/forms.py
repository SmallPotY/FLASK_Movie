# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm  # 表单基类
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, \
    SelectField, SelectMultipleField  # 字符串字段,密码字段,提交字段,上传文件字段
from wtforms.validators import DataRequired, ValidationError,EqualTo
from app.models import Admin, Tag, Auth, Role

tags = Tag.query.all()
auths_list = Auth.query.all()
role_list = Role.query.all()


class LoginForm(FlaskForm):
    """管理员登陆表单"""
    account = StringField(  # 账号框
        label="账号",  # 标签
        validators=[  # 验证器
            DataRequired("请输入账号!")
        ],
        description="账号",  # 描述
        render_kw={  # 自定义属性

            "class": "form-control",
            "placeholder": "请输入账号",
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
            # "required": "required"
        }
    )
    submit = SubmitField(  # 提交按钮
        "登陆",
        description="登陆",
        render_kw={  # 自定义属性
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):  # 验证字段validate_字段名
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('账号不存在')  # 抛出wtforms.validators异常ValidationError


class TagForm(FlaskForm):
    """添加标签表单"""
    name = StringField(
        label="名称",
        validators=[DataRequired('请输入标签!')],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class MovieForm(FlaskForm):
    """添加视频"""
    title = StringField(
        label="片名",
        validators=[DataRequired("请输入片名")],
        description="片名",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入片名！"
        }
    )

    url = FileField(
        label="文件",
        validators=[DataRequired("请上传文件！")],
        description="文件",

    )

    info = TextAreaField(
        label="简介",
        validators=[DataRequired("请输入简介")],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info"
        }
    )

    logo = FileField(
        label='封面',
        validators=[DataRequired("请上传封面！")],
        description="封面",
        render_kw={
            "id": "input_logo"
        }
    )

    star = SelectField(
        label='星级',
        validators=[DataRequired('请选择星级!')],
        coerce=int,
        choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')],
        description="星级",
        render_kw={
            "class": "form-control"
        }
    )

    tag_id = SelectField(
        label="标签",
        validators=[DataRequired('请选择标签！')],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description="标签",
        render_kw={
            "class": "form-control"
        }
    )

    area = StringField(
        label="地区",
        validators=[DataRequired("请输入地区！")],
        description="地区",
        render_kw={
            "class": "form-control",
            "id": "input_area",
            "placeholder": "请输入地区！"
        }
    )

    length = StringField(
        label="片长",
        validators=[DataRequired("请输入片长！")],
        description="片长",
        render_kw={
            "class": "form-control",
            "id": "input_length",
            "placeholder": "请输入片长！"
        }
    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class PreviewForm(FlaskForm):
    """首页推荐"""
    title = StringField(
        label="推荐标题",
        validators=[
            DataRequired("请输入标题")
        ],
        description="标题",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入推荐标题！"

        }
    )

    logo = FileField(
        label='封面',
        validators=[DataRequired("请上传封面！")],
        description="封面",
        render_kw={
            "id": "input_logo"
        }
    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
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

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session['admin']
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError('旧密码错误！')


class AuthForm(FlaskForm):
    """权限"""
    name = StringField(
        label="权限名称",
        validators=[DataRequired('请输入权限名称!')],
        description="权限名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入权限名称！"
        }
    )

    url = StringField(
        label="权限地址",
        validators=[DataRequired('请输入权限地址!')],
        description="权限地址",
        render_kw={
            "class": "form-control",
            "id": "input_url",
            "placeholder": "请输入权限地址！"
        }
    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class RoleForm(FlaskForm):
    """角色名称"""
    name = StringField(
        label="角色名称",
        validators=[DataRequired('请输入角色名称！')],
        description="角色名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入角色名称！"
        }
    )

    auths = SelectMultipleField(
        label="权限列表",
        validators=[DataRequired('请选择权限列表！')],
        coerce=int,
        choices=[(v.id, v.name) for v in auths_list],
        description="权限列表",
        render_kw={
            # "name": "input_url",  # 不能添加name属性，会报错
            "class": "form-control"
        }

    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class AdminForm(FlaskForm):
    """添加管理员"""
    name = StringField(
        label="管理员名称",
        validators=[  #
            DataRequired("请输入管理员名称!")
        ],
        description="管理员名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员名称",
        }
    )

    pwd = PasswordField(  # 密码框
        label="管理员密码",
        validators=[
            DataRequired("请输入管理员密码!")
        ],
        description="管理员密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请输入管理员密码",
            # "required": "required"
        }
    )

    repwd = PasswordField(  # 密码框
        label="重复管理员密码",
        validators=[
            DataRequired("请输入重复密码!"),
            EqualTo('pwd','两次密码不一致！')
        ],
        description="管理员密码",
        render_kw={  # 自定义属性
            "class": "form-control",
            "placeholder": "请输入重复密码",
            # "required": "required"
        }
    )

    role_id = SelectField(
        label="所属角色",
        coerce=int,
        choices=[(v.id, v.name) for v in role_list],
        render_kw={
            "class": "form-control"
        }

    )

    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary"
        }
    )
