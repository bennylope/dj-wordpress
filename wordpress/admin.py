from django.contrib import admin
from wordpress.models import (
    Option, Comment, Link, Post,
    PostMeta, Taxonomy, Term, User, UserMeta,
)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author_name', 'post_date')
    list_filter = ('comment_type', 'approved')
    search_fields = ('author_name', 'author_email', 'post__title')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'description')
    list_filter = ('visible',)
    search_fields = ('name', 'url', 'description')


class PostMetaInline(admin.TabularInline):
    model = PostMeta


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (PostMetaInline,)
    list_display = ('id', 'title', 'author', 'post_date')
    list_filter = ('status', 'post_type', 'comment_status', 'ping_status', 'author')
    search_fields = ('title',)


class UserMetaInline(admin.TabularInline):
    model = UserMeta


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (UserMetaInline,)
    list_display = ('id', 'display_name', 'email', 'status')
    list_filter = ('status',)
    search_fields = ('login', 'username', 'display_name', 'email')


@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'term')
    list_filter = ('name',)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
