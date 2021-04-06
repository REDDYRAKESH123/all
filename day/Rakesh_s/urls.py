from  django .urls import path
from . import views         # from username import views another decleration


urlpatterns= [
    path('bt/',views.home,),
    path('Boom/',views.chk),
    path('home/',views.home,name="home"),
    path('lg/',views.login,name="login"),
    path('rg/',views.register,name="register"),
    path('re/',views.rg,name='rg'),
    path("",views.bthm),
    path("home1/",views.home1,name='hm')	
]