from django.urls import path
from . import views
from .views import campus_list,base_data


urlpatterns = [
    path('', views.base_data, name='base_data'),

    path('insert_campus/', views.insert_campus,name="insert_campus"),
    path('insert_stream/', views.insert_stream,name="insert_stream"),
    path('insert_facility/', views.insert_facility,name="insert_facility"),
    path('insert_course/', views.insert_course,name="insert_course"),
    path('insert_lab/', views.insert_lab,name="insert_lab"),
    path('insert_subject/', views.insert_subject,name="insert_subject"),
    path('insert_faculty/', views.insert_faculty,name="insert_faculty"),
    path('insert_student/', views.insert_student,name="insert_student"),

    path('insert_campus/<int:id>', views.update_campus),
    path('insert_stream/<int:id>', views.update_stream),
    path('insert_facility/<int:id>', views.update_facility),
    path('insert_course/<int:id>', views.update_course),
    path('insert_lab/<int:id>', views.update_lab),
    path('insert_subject/<int:id>', views.update_subject),
    path('insert_faculty/<int:id>', views.update_faculty),
    path('insert_student/<int:id>', views.update_student),

    path('edit_campus/<int:id>',views.edit_campus,name="edit_campus"),
    path('edit_stream/<int:id>',views.edit_stream,name="edit_stream"),
    path('edit_facility/<int:id>',views.edit_facility,name="edit_facility"),
    path('edit_course/<int:id>',views.edit_course,name="edit_course"),
    path('edit_lab/<int:id>',views.edit_lab,name="edit_lab"),
    path('edit_subject/<int:id>',views.edit_subject,name="edit_subject"),
    path('edit_faculty/<int:id>',views.edit_faculty,name="edit_faculty"),
    path('edit_student/<int:id>',views.edit_student,name="edit_student"),

    path('delete_campus/<int:id>',views.delete_campus,name="delete_campus"),
    path('delete_stream/<int:id>',views.delete_stream,name="delete_stream"),
    path('delete_facility/<int:id>',views.delete_facility,name="delete_facility"),
    path('delete_course/<int:id>',views.delete_course,name="delete_course"),
    path('delete_lab/<int:id>',views.delete_lab,name="delete_lab"),
    path('delete_subject/<int:id>',views.delete_subject,name="delete_subject"),
    path('delete_faculty/<int:id>',views.delete_faculty,name="delete_faculty"),
    path('delete_student/<int:id>',views.delete_student,name="delete_student"),

    #path('update_campus/<int:id>', views.update_campus,name="update_campus"),
    path('campus_list/', views.campus_list,name="campus_list"),
    path('stream_list/', views.stream_list,name="stream_list"),
    path('facility_list/', views.facility_list,name="facility_list"),
    path('course_list/', views.course_list,name="course_list"),
    path('lab_list/', views.lab_list,name="lab_list"),
    path('subject_list/', views.subject_list,name="subject_list"),
    path('faculty_list/', views.faculty_list,name="faculty_list"),
    path('student_list/',views.student_list,name ="student_list")


    #path('',views.home,name="home"),
    #path('product/',views.product_details,name = "product_details"),
    #pythopath('customer/',views.customer_details,name="customer_details")
]