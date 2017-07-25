from rest_framework import permissions

class CarlaPermission(permissions.BasePermission):
    message = "No eres Carla"

    def has_permission(self,request,view):
        if request.method == "GET" and request.user.email == "carla.manser@gmail.com":
            return True
        else: 
            return False