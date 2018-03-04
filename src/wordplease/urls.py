from django.contrib import admin
from django.urls import path
from posts.api import PostAddAPI, PostDetailAPI, PostListAPI
from posts.views import home, NewPostView, blogsList, blogDetail, postDetail
from users.views import LoginView, LogoutView, SignupView
from users.api import UserAddAPI, UserDetailAPI, UserListAPI

# Se definen el conjunto de URL's que componen ell sitio web:
urlpatterns = [

    # WEB END POINT'S

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

    # API END POINT'S

    # END POINT'S USUARIOS:
    # End Point para el REGISTRO de Usuarios.
    path('api/1.0/new-user', UserAddAPI.as_view(), name='api_user_add'),

    # End point para el DETALLE, la ACTUALIZACION y el BORRADO de un Usuario
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name='api_user_detail'),

    # END POINT'S BLOGS
    # End Point que devuelve un LISTADO con los Blogs de la plataforma
    path('api/1.0/blogs', UserListAPI.as_view(), name='api_blogs_list'),

    # END POINT'S POSTS
    # End Point que permite la CREACIÓN de un NUEVO POST.
    path('api/1.0/new-post', PostAddAPI.as_view(), name='api_post_add'),

    # End Point que permite LISTAR los POST de un BLOG.
    path('api/1.0/blogs/<str:username>', PostListAPI.as_view(), name='api_post_list'),

    # End Point para el DETALLE, la ACTUALIZACION y el BORRADO de un POST.
    path('api/1.0/posts/<int:pk>', PostDetailAPI.as_view(), name='api_post_detail')
]
