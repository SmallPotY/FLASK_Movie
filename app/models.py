# -*- coding:utf-8 -*-

from datetime import datetime
from app import db


# 会员
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100))  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 电话
    info = db.Column(db.Text)  # 简介
    face = db.Column(db.String(255))  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符

    userlogs = db.relationship('Userlog', backref='user')  # 会员外键关联
    comments = db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')

    # 返回类型
    def __repr__(self):
        return "<USER %r>" % self.name

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd,pwd)


# 会员登陆日志
class Userlog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 关联 user表的id列
    ip = db.Column(db.String(100))  # 登陆IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    movies = db.relationship("Movie", backref='tag')  # 电源外键关系关联

    def __repr__(self):
        return "<Tag %r>" % self.name


# 视频
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 所属地区
    # release_time = db.Column(db.Date)   # 加入时间
    length = db.Column(db.String(100))  # 播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    comments = db.relationship("Comment", backref="movie")  # 评论外键关联
    moviecols = db.relationship("Moviecol", backref="movie")  # 收藏外键关联

    def __repr__(self):
        return "<Movie %r>" % self.title


# 推荐
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Comment %r" % self.id


# 收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Moviecol %r" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "Auth %r" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    auths = db.Column(db.String(600))   # 角色权限列表
    admins = db.relationship("Admin", backref='role')   # 管理员外键关联

    def __repr__(self):
        return "Role %r" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    adminlogs = db.relationship("Adminlog", backref="admin")
    oplogs = db.relationship("Oplog", backref="admin")

    def __repr__(self):
        return "Admin %r" % self.name

    def check_pwd(self, pwd):
        """登陆密码验证,返回True or False"""
        from werkzeug.security import check_password_hash  # 导入哈希解密
        return check_password_hash(self.pwd, pwd)  # 比较模型内的pwd与传入的pwd


# 管理员登陆日志
class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 关联 user表的id列
    ip = db.Column(db.String(100))  # 登陆IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 后台操作日志
class Oplog(db.Model):
    __tablename__ = 'oplog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 关联 user表的id列
    ip = db.Column(db.String(100))  # 登陆IP
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登陆时间

    def __repr__(self):
        return "<Oplog %r>" % self.id


if __name__ == '__main__':
    db.create_all()
    from werkzeug.security import generate_password_hash

    # role = Role(name='超级管理员',auths='')
    # db.session.add(role)
    # db.session.commit()
    #
    # admin = Admin(
    #     name='xb',
    #     pwd=generate_password_hash('1'),
    #     is_super=0,
    #     role_id=1
    # )
    # db.session.add(admin)
    # db.session.commit()
