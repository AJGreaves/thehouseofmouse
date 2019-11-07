from django.urls import path
from .views import (
    results_view,
    all_products_view,
    ListingDetailView,
    famous_category_view,
    special_category_view,
    harry_potter_category_view,
    starwars_category_view,
    misc_category_view,
    jobs_category_view,
    doctor_who_category_view,
    xmas_category_view,
    halloween_category_view,
    categories_view
    )

urlpatterns = [
    path('listing/<int:pk>/', ListingDetailView.as_view(), name="listing-detail"),
    path('categories/', categories_view, name="categories"),
    path('results/', results_view, name="results"),
    path('all-products/', all_products_view, name="all-products"),
    path('categories/', categories_view, name="categories"),
    path('categories/famous', famous_category_view, name="famous"),
    path('categories/special-occasions', special_category_view, name="special-occasions"),
    path('categories/harry-potter', harry_potter_category_view, name="harry-potter"),
    path('categories/star-wars', starwars_category_view, name="star-wars"),
    path('categories/weird-misc', misc_category_view, name="weird-misc"),
    path('categories/jobs-hobbies', jobs_category_view, name="jobs-hobbies"),
    path('categories/doctor-who', doctor_who_category_view, name="doctor-who"),
    path('categories/christmas', xmas_category_view, name="christmas"),
    path('categories/halloween', halloween_category_view, name="halloween"),
]