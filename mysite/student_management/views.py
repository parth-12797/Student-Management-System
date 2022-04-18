
from django.shortcuts import render, get_object_or_404, redirect
from .models import Campus, Stream, Facility, Course, Lab, Subject, Faculty, Students_data
from django.http import HttpResponse


def campus_list(request):
    campus_det= Campus.objects.all()

    context={
        'campus_details':campus_det,
        'btn_text':"Insert"
    }
    return render(request,'student_management/campus.html',context)



def stream_list(request):
    stream_det= Stream.objects.all()
    context={
        'stream_details':stream_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/stream.html',context)



def facility_list(request):
    facility_det= Facility.objects.all()

    context={
        'facility_details':facility_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/facility.html',context)

def course_list(request):
    course_det= Course.objects.all()

    context={
        'course_details':course_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/course.html',context)

def lab_list(request):
    lab_det= Lab.objects.all()

    context={
        'lab_details':lab_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/lab.html',context)


def subject_list(request):
    subject_det= Subject.objects.all()

    context={
        'subject_details':subject_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/subject.html',context)



def faculty_list(request):
    faculty_det= Faculty.objects.all()

    context={
        'faculty_details':faculty_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/faculty.html',context)

def student_list(request):
    student_det= Students_data.objects.all()
    context={
        'student_details':student_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/student.html',context)



def insert_campus(request):
    if request.method == 'POST':

        if request.POST.get('Campus_name') and request.POST.get('Campus_location'):
            campus = Campus()
            campus.Campus_name = request.POST.get('Campus_name')
            campus.Campus_location = request.POST.get('Campus_location')
            campus.save()
            campus_det = Campus.objects.all()
            context = {
                'campus_details': campus_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/campus.html', context)
    else:
        return render(request, 'student_management/error.html')

def insert_stream(request):
    if request.method == 'POST':

        if request.POST.get('Stream_name'):
            stream = Stream()
            stream.Stream_name = request.POST.get('Stream_name')

            stream.save()
            stream_det = Stream.objects.all()
            context = {
                'stream_details': stream_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/stream.html', context)
    else:
        return render(request, 'student_management/error.html')



def insert_facility(request):
    if request.method == 'POST':

        if request.POST.get('Facility_name'):
            facility = Facility()
            facility.Facility_name = request.POST.get('Facility_name')

            facility.save()
            facility_det = Facility.objects.all()
            context = {
                'facility_details': facility_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/facility.html', context)
    else:
        return render(request, 'student_management/error.html')

def insert_course(request):
    if request.method == 'POST':

        if request.POST.get('Course_name') and request.POST.get('Stream_name'):
            course = Course()
            course.Course_name = request.POST.get('Course_name')
            course.Stream_name = request.POST.get('Stream_name')
            course.save()
            course_det = Course.objects.all()
            context = {
                'course_details': course_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/course.html', context)
    else:
        return render(request, 'student_management/error.html')


def insert_lab(request):
    if request.method == 'POST':

        if request.POST.get('lab_name') and request.POST.get('Course_name'):
            lab = Lab()
            lab.lab_name = request.POST.get('lab_name')
            lab.Course_name = request.POST.get('Course_name')
            lab.save()
            lab_det = Lab.objects.all()
            context = {
                'lab_details': lab_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/lab.html', context)
    else:
        return render(request, 'student_management/error.html')


def insert_subject(request):
    if request.method == 'POST':

        if request.POST.get('Subject_name') and request.POST.get('Course_name'):
            subject = Subject()
            subject.Subject_name = request.POST.get('Subject_name')
            subject.Course_name = request.POST.get('Course_name')
            subject.save()
            subject_det = Subject.objects.all()
            context = {
                'subject_details': subject_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/subject.html', context)
    else:
        return render(request, 'student_management/error.html')


def insert_faculty(request):
    if request.method == 'POST':

        if request.POST.get('Faculty_name') and request.POST.get('Subject_name') and request.POST.get('Course_name'):
            faculty = Faculty()
            faculty.Faculty_name=request.POST.get('Faculty_name')
            faculty.Subject_name = request.POST.get('Subject_name')
            faculty.Course_name = request.POST.get('Course_name')
            faculty.save()
            faculty_det = Faculty.objects.all()
            context = {
                'faculty_details': faculty_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/faculty.html', context)
    else:
        return render(request, 'student_management/error.html')



def insert_student(request):
    if request.method == 'POST':

        if request.POST.get('Student_name'):

            student = Students_data()
            student.Student_name=request.POST.get('Student_name')
            student.Student_email=request.POST.get('Student_email')

            student.Subjects = request.POST.get('Subjects')
            student.Labs = request.POST.get('Labs')
            student.Course_name = request.POST.get('Course_name')
            student.Stream = request.POST.get('Stream')
            student.Facility = request.POST.get('Facility')
            student.save()
            student_det = Students_data.objects.all()
            context = {
                'student_details': student_det,
                'btn_text': "Insert"
            }
        return render(request, 'student_management/student.html', context)
    else:
        return render(request, 'student_management/error.html')




def update_campus(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('Campus_name') and request.POST.get('Campus_location'):
                campus =Campus.objects.get(id=id)
                campus._id=id
                campus.Campus_location=request.POST.get('Campus_location')
                campus.Campus_name=request.POST.get('Campus_name')
                campus.save()
                campus_det = Campus.objects.all()
                context = {
                    'campus_details': campus_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/campus.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')


def update_stream(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('Stream_name') :
                stream =Stream.objects.get(id=id)
                stream._id=id

                stream.Stream_name=request.POST.get('Stream_name')
                stream.save()
                stream_det = Stream.objects.all()
                context = {
                    'stream_details': stream_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/stream.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')



def update_facility(request,id):
    if request.method == 'POST':
        if(id>0):


            if request.POST.get('Facility_name') :
                facility =Facility.objects.get(id=id)
                facility._id=id

                facility.Facility_name=request.POST.get('Facility_name')
                facility.save()
                facility_det = Facility.objects.all()
                context = {
                    'facility_details': facility_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/facility.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')


def update_course(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('Course_name') and request.POST.get('Stream_name'):
                course =Course.objects.get(id=id)
                course._id=id
                course.Course_name=request.POST.get('Course_name')
                course.Stream_name=request.POST.get('Stream_name')
                course.save()
                course_det = Course.objects.all()
                context = {
                    'course_details': course_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/course.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')


def update_lab(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('lab_name') and request.POST.get('Course_name'):
                lab =Lab.objects.get(id=id)
                lab._id=id
                lab.lab_name_name=request.POST.get('lab_name')
                lab.Course_name=request.POST.get('Course_name')
                lab.save()
                lab_det =Lab.objects.all()
                context = {
                    'lab_details': lab_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/lab.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')

def update_subject(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('Subject_name') and request.POST.get('Course_name'):
                subject =Subject.objects.get(id=id)
                subject._id=id
                subject.Subject_name=request.POST.get('Subject_name')
                subject.Course_name=request.POST.get('Course_name')
                subject.save()
                subject_det =Subject.objects.all()
                context = {
                    'subject_details': subject_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/subject.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')

def update_faculty(request,id):
    if request.method == 'POST':
        if(id>0):

            if request.POST.get('Faculty_name') and request.POST.get('Subject_name') and request.POST.get('Course_name'):
                faculty =Faculty.objects.get(id=id)
                faculty._id=id
                faculty.Faculty_name=request.POST.get('Faculty_name')
                faculty.Subject_name=request.POST.get('Subject_name')
                faculty.Course_name=request.POST.get('Course_name')
                faculty.save()
                faculty_det =Faculty.objects.all()
                context = {
                    'faculty_details': faculty_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/faculty.html', context)

        else:
            pass
    else:
        return render(request, 'student_management/error.html')

def update_student(request,id):

    if request.method == 'POST':

        if(id>0):


            if request.POST.get('Student_name'):

                student =Students_data.objects.get(id=id)
                student._id = id
                student.Student_name = request.POST.get('Student_name')
                student.Student_email = request.POST.get('Student_email')

                student.Subjects = request.POST.get('Subjects')
                student.Labs = request.POST.get('Labs')
                student.Course_name = request.POST.get('Course_name')
                student.Stream = request.POST.get('Stream')
                student.Facility = request.POST.get('Facility')
                student.save()
                student_det = Students_data.objects.all()
                context = {
                    'student_details': student_det,
                    'btn_text': "Insert"
                }
            return render(request, 'student_management/student.html', context)
        else:
            return render(request, 'student_management/error.html')


def edit_campus(request,id):
    edited_campus=Campus.objects.get(id=id)



    campus_det = Campus.objects.all()
    context = {
        'campus_details': campus_det,
        'edited_campus': edited_campus,
        'btn_text': "Update"
    }
    return render(request,'student_management/campus.html',context)


def edit_stream(request,id):
    edited_stream=Stream.objects.get(id=id)
    stream_det = Stream.objects.all()
    print(edited_stream.Stream_name)
    context = {
        'stream_details': stream_det,
        'edited_stream': edited_stream,
        'btn_text': "Update"
    }
    return render(request,'student_management/stream.html',context)


def edit_facility(request,id):
    edited_facility=Facility.objects.get(id=id)
    facility_det = Facility.objects.all()

    context = {
        'facility_details': facility_det,
        'edited_facility': edited_facility,
        'btn_text': "Update"
    }
    return render(request,'student_management/facility.html',context)


def edit_course(request,id):
    edited_course=Course.objects.get(id=id)
    course_det = Course.objects.all()

    context = {
        'course_details': course_det,
        'edited_course': edited_course,
        'btn_text': "Update"
    }
    return render(request,'student_management/course.html',context)


def edit_lab(request,id):
    edited_lab=Lab.objects.get(id=id)
    lab_det = Lab.objects.all()

    context = {
        'lab_details': lab_det,
        'edited_lab': edited_lab,
        'btn_text': "Update"
    }
    return render(request,'student_management/lab.html',context)

def edit_subject(request,id):
    edited_subject=Subject.objects.get(id=id)
    subject_det = Subject.objects.all()

    context = {
        'subject_details': subject_det,
        'edited_subject': edited_subject,
        'btn_text': "Update"
    }
    return render(request,'student_management/subject.html',context)


def edit_faculty(request,id):
    edited_faculty=Faculty.objects.get(id=id)
    faculty_det = Faculty.objects.all()

    context = {
        'faculty_details': faculty_det,
        'edited_faculty': edited_faculty,
        'btn_text': "Update"
    }
    return render(request,'student_management/faculty.html',context)

def edit_student(request,id):
    edited_student=Students_data.objects.get(id=id)
    student_det = Students_data.objects.all()

    context = {
        'student_details': student_det,
        'edited_student': edited_student,
        'btn_text': "Update"
    }
    return render(request,'student_management/student.html',context)




def delete_campus(request,id):
    edited_campus=Campus.objects.get(id=id)
    edited_campus.delete()
    campus_det = Campus.objects.all()
    context = {
        'campus_details': campus_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/campus.html',context)

def delete_stream(request,id):
    edited_stream=Stream.objects.get(id=id)
    edited_stream.delete()
    stream_det = Stream.objects.all()
    context = {
        'stream_details': stream_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/stream.html',context)


def delete_facility(request,id):
    edited_facility=Facility.objects.get(id=id)
    edited_facility.delete()
    facility_det = Facility.objects.all()
    context = {
        'facility_details': facility_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/facility.html',context)


def delete_course(request,id):
    edited_course=Course.objects.get(id=id)
    edited_course.delete()
    course_det = Course.objects.all()
    context = {
        'course_details': course_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/course.html',context)


def delete_lab(request,id):
    edited_lab=Lab.objects.get(id=id)
    edited_lab.delete()
    lab_det = Lab.objects.all()
    context = {
        'lab_details': lab_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/lab.html',context)

def delete_subject(request,id):
    edited_subject=Subject.objects.get(id=id)
    edited_subject.delete()
    subject_det = Subject.objects.all()
    context = {
        'subject_details': subject_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/subject.html',context)

def delete_faculty(request,id):
    edited_faculty=Faculty.objects.get(id=id)
    edited_faculty.delete()
    faculty_det = Faculty.objects.all()
    context = {
        'faculty_details': faculty_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/faculty.html',context)

def delete_student(request,id):
    edited_student=Students_data.objects.get(id=id)
    edited_student.delete()
    student_det = Students_data.objects.all()
    context = {
        'student_details': student_det,
        'btn_text': "Insert"
    }
    return render(request,'student_management/student.html',context)



def base_data(request):
    return render(request, 'student_management/base.html')
