from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    # 用户名
    user_name = models.CharField(max_length=30)
    # 密码
    password = models.CharField(max_length=32)
    # 电话
    user_phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user_name,self.password,self.user_phone



# 文章分类
class Category(models.Model):
    c_name = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name


# 文章标签
class Tag(models.Model):
    t_name = models.CharField(max_length=30)

    def __str__(self):
        return self.t_name



# 文章
class Article(models.Model):
    # 文章标题
    title = models.CharField(max_length=50)
    # 文章内容
    content = models.TextField()
    # 发布时间
    date_publish = models.DateTimeField(auto_now_add=True)
    # 浏览量
    page_view = models.IntegerField(default=0)

    # 与用户表关联 一对多
    user = models.ForeignKey(User)
    # 与分类表关联  一对多
    category = models.ForeignKey(Category)
    # 与标签表关联  多对多
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

