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

    # Admin function not on UI
    path('api/get-vehicles-data',view.viewData),

    # Not on UI
    path('api/check-member',view.check_member),

    # Admin function not on UI
    path('api/get-img',view.get_image),

    # Admin function not on UI
    path('api/add-entry',view.add_vehicle_entry),

    # Admin function not on UI
    path('api/get-members-data',view.get_members),

    # Admin function not on UI
    path('api/add-members-data',view.add_member),

    # Admin function not on UI
    path('api/search-member',view.search_member),
    
    # Admin function not on UI
    path('api/add-exit',view.exit_details),
    
    # Admin function not on UI
    path('api/search-vehicle',view.search_vehicle),
    
    # Admin function not on UI
    path('api/get-details',view.get_details),
    
    # Delete the member and the vehicle 
    path('delete/<num>/', view.delete_vehicle_entry),
]
