from django.urls import path
from . import views as view

urlpatterns = [
    # Main Home page of the website
    path('',view.home,name='home'),

    # List of all the members of in database
    path('members',view.members,name='member'),
    
    # Scan photo to get vehicle data
    path('scan',view.scanner,name='scanner'),

    # Get vehicle details
    # Not working now
    path('vehicle-details',view.vehicle_details,name='details'),

    path('api/get-vehicles-data',view.viewData),

    path('api/check-member',view.check_member),

    path('api/get-img',view.get_image),

    path('api/add-entry',view.add_vehicle_entry),

    path('api/get-members-data',view.get_members),

    path('api/add-members-data',view.add_member),

    path('api/search-member',view.search_member),
    
    path('api/add-exit',view.exit_details),
    
    path('api/search-vehicle',view.search_vehicle),
    
    path('api/get-details',view.get_details),
    
    # Delete the member and the vehicle 
    path('delete/<num>/', view.delete_vehicle_entry),

    # After scan function
    path('after/<number_platee>/', view.after_scan),

    # Register new user
    path('register/<number_platee>/', view.register_new_user),
]
