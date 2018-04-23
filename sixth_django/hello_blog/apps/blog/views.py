from django.shortcuts import render

from .models import UserMessage
# Create your views here.

# def getform(request):
#     return render(request,'blog/blog_form.html')
# def getform(request):
#     all_messages=UserMessage.objects.all()
#     for message in all_messages:
#         print(message.name)
#     return render(request,'blog/blog_form.html')

# def getform(request):
#     user_message=UserMessage()
#     user_message.name='孙悟空'
#     user_message.email='hgs@1.com'
#     user_message.address='花果山'
#     user_message.message='齐天大圣'
#     user_message.object_id='hello玉帝'
#     user_message.save()
#     return render(request,'blog/blog_form.html')

# def getform(request):
#     if request.method=='POST':
#         name=request.POST.get('name','')
#         email=request.POST.get('email','')
#         address=request.POST.get('address','')
#         message=request.POST.get('message','')

#         user_message=UserMessage()
#         user_message.name=name
#         user_message.email=email
#         user_message.address=address
#         user_message.message=message
#         user_message.object_id='hello王母3'
#         user_message.save()
#     return render(request,'blog/blog_form.html')

# def getform(request):
#     all_messages=UserMessage.objects.filter(name='uuuuuu',address='tttttttttttttt')
#     for message in all_messages:
#         message.delete()
#     return render(request,'blog/blog_form.html')

def getform(request):
    message=None
    all_messages=UserMessage.objects.filter(name='杨过')
    if all_messages:
        message=all_messages[0]

    return render(request,'blog/blog_form.html',{'my_message':message})

