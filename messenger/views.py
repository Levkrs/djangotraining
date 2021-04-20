from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from applicantapp.models import Resume
from authapp.models import MyUser
from companyapp.models import Company
from mainapp.models import FullInvite
from messenger.models import MessengerModel
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


class DialogList(ListView):
    """
    Список диалогов по взаимным откликам
    """
    template_name = 'messenger/dialog-list.html'

    def get_queryset(self):
        """
        Получаем список диалогов
        """
        if self.request.user.role == "HR":
            object_list = FullInvite.objects.filter(hr=self.request.user.company, aprove_hr=True, aprove_recrut=True)
            print(object_list)
            return object_list
        elif self.request.user.role == "REC":
            my_resume = Resume.objects.filter(id=self.request.user.id)
            # print(my_resume)
            object_list = FullInvite.objects.filter(recrut_resume__in=my_resume, aprove_hr=True, aprove_recrut=True)
            print(object_list)
            return object_list
        else:
            return


class DialogDetail(ListView):
    # model = MessengerModel

    template_name = 'messenger/dialog_detail.html'

    def get_queryset(self):
        req = MessengerModel.objects.all()
        return req

    def get_context_data(self, **kwargs):
        context = super(DialogDetail, self).get_context_data(**kwargs)
        return context


def create_message(request, pk):
    """
    Создание сообщения
    """
    get_invite_object = FullInvite.objects.get(id=pk)
    hr = MyUser.objects.get(id=get_invite_object.hr.id)
    if request.user.role == "HR":
        message_object = MessengerModel(vacansy=get_invite_object.vacansy,
                                        msg_from=request.user,
                                        msg_to=MyUser.objects.get(id=get_invite_object.recrut_resume.user_id),
                                        msg_text=request.POST['message']
                                        )
        message_object.save()
        return HttpResponseRedirect(reverse('messenger:dialog_detail', kwargs={'pk': pk}))

    elif request.user.role == "REC":
        message_object = MessengerModel(vacansy=get_invite_object.vacansy,
                                        msg_from=request.user,
                                        msg_to=MyUser.objects.get(id=get_invite_object.hr.user_id),
                                        msg_text=request.POST['message']
                                        )
        message_object.save()
        return HttpResponseRedirect(reverse('messenger:dialog_detail', kwargs={'pk': pk}))
