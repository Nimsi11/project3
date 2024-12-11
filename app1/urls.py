from django.urls import path
from.import views

urlpatterns=[path("path1",views.signup,name="signup"),
             path("path2",views.login,name="login"),
             path("path3",views.personal,name="personal"),
             path("path4",views.personaldata,name="personaldata"),
             path("path5",views.med,name="med") ]