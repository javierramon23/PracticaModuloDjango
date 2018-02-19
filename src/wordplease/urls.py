from django.contrib import admin
from django.urls import path
from posts.views import home, NewPostView, blogsList, blogDetail, postDetail
from users.views import LoginView, LogoutView, SignupView
from users.api import UserAddAPI, UserDetailAPI
from posts.api import BlogListAPI

# Se definen el conjunto de URL's que componen ell sitio web:
urlpatterns = [
    path('admin/', admin.site.urls),
    # Se define la URL de la página de ALTA.
    path('signup/', SignupView.as_view(), name='signup_page'),
    # Se define la URL de la página de LOGIN.
    path('login/', LoginView.as_view(), name='login_page'),
    # Se define la URL de la página de LOGOUT.
    path('logout/', LogoutView.as_view(), name='logout_page'),
    # Se define la URL de la página para CREAR un post.
    path('new-post/', NewPostView.as_view(), name='new_post_page'),
    # Se define la URL de la página de BLOGS
    path('blogs/', blogsList, name='blog_list_page'),
    # Se define la URL de la páginas con el DETALLE de un BLOG.
    path('blogs/<str:user_name>', blogDetail, name='blog_detail_page'),
    # Se define la URL de la página con el DETALLE de un POST
    path('blogs/<str:user_name>/<int:pk>', postDetail, name='post_detail_page'),
    # Se define la URL de la página de HOME.
    path('', home, name='home_page'),

    # API END POINT's

    # End Point para el REGISTRO de Usuarios.
    path('api/1.0/users', UserAddAPI.as_view(), name='api_user_add'),
    # End point para el DETALLE, la ACTUALIZACION y el BORRADO de un Usuario
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name='api_user_detail'),

    # End Point que devuelve un LISTADO con los Blogs de la plataforma
    path('api/1.0/blog', BlogListAPI.as_view(), name='api_blog_list')
]
