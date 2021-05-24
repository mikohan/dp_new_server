from django.shortcuts import render, redirect
from .forms import EmailFormLight
from .models import EmailModel
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
import re
from django.contrib import messages
from accounts.models import BlackListEmail


def e_form_view(request, *args, **kwargs):

    e_form = EmailFormLight(request.POST or None)
    if e_form.is_valid():
        phone = e_form.cleaned_data.get("phone")
        email_name = e_form.cleaned_data.get("email_name")
        capcha = e_form.cleaned_data.get("captcha")
        callback, created = EmailModel.objects.get_or_create(
            phone=phone, name=email_name
        )
        if capcha == "7":
            try:
                black = BlackListEmail.objects.all()
                black_list = [x.email for x in black]
                if email_name.strip() in black_list or phone.strip() in black_list:
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

            except:
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

            send_mail(
                "Заказ звонка с Ducatoparts.ru",
                f"Пришел запрос на обратный звонок. Телефон - {phone}. Имя - {email_name}",
                settings.SHOP_EMAIL_FROM,
                settings.SHOP_EMAILS_MANAGERS,
                fail_silently=False,
            )
            storage = messages.get_messages(request)
            storage.used = True

            return redirect("thankyoucall")

        else:
            messages.add_message(
                request, messages.INFO, "Заказ звонка не отправлен! Попробуйте снова."
            )

            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def footer_form(request):
    phone = request.POST.get("phone")
    if phone:
        phone = re.sub(r"[^\d]", "", phone)
        callback, created = EmailModel.objects.get_or_create(phone=phone)
        send_mail(
            "Заказ звонка с Ducatoparts.ru",
            f"Пришел запрос на обратный звонок. Телефон - {phone}",
            settings.SHOP_EMAIL_FROM,
            settings.SHOP_EMAILS_MANAGERS,
            fail_silently=False,
        )
    return redirect("thankyoucall")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
