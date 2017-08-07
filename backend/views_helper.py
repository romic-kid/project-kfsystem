from .models import Admin, CustomerService, SerialNumber
from django.core.mail import send_mail
import hashlib, random, string


def admin_is_existent_by_email(email):
    try:
        instance = Admin.objects.get(email=email)
        return True
    except Admin.DoesNotExist:
        return False


def admin_is_existent_by_nickname(nickname):
    try:
        instance = Admin.objects.get(nickname=nickname)
        return True
    except Admin.DoesNotExist:
        return False


def admin_is_valid_by_email_password(email, sha512_final_password):
    try:
        instance = Admin.objects.get(email=email, password=password)
        return True
    except Admin.DoesNotExist:
        return False


def admin_generate_password(email, sha512_frontend_password):
    hash_email = hashlib.sha512()
    hash_email.update(email.encode('utf-8'))
    sha512_email = hash_email.hexdigest()
    hash_password = hashlib.sha512()
    hash_password.update((sha512_frontend_password+sha512_email+'adminbig5').encode('utf-8'))
    return hash_password.hexdigest()


def admin_generate_communication_key(email):
    salt1 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    salt2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    hash_key = hashlib.md5()
    hash_key.update((salt1+email+salt2).encode('utf-8'))
    return hash_key.hexdigest()


def admin_get_communication_key(email):
    try:
        instance = Admin.objects.get(email=email)
        return instance.communication_key
    except Admin.DoesNotExist:
        return False


def admin_generate_vid(email):
    return admin_generate_communication_key(email)


def admin_send_email(email, content):
    send_mail('客服系统找回密码', content, 'big5_nankai@163.com', [email], fail_silently=True)


def admin_is_existent_by_vid(vid):
    try:
        instance = Admin.objects.get(vid=vid)
        return True
    except Admin.DoesNotExist:
        return False


def sn_is_serials_valid(serials):
    try:
        instance = SerialNumber.objects.get(serials=serials)
        if instance.is_used == True:
            return False
        else:
            return True
    except SerialNumber.DoesNotExist:
        return False


def sn_mark_used(serials):
    if sn_is_serials_valid(serials) == False:
        return False
    else:
        instance = SerialNumber.objects.get(serials=serials)
        instance.is_used = True
        instance.save()
        return True


def cs_is_existent_by_email(email):
    try:
        instance = CustomerService.objects.get(email=email)
        return True
    except CustomerService.DoesNotExist:
        return False


def cs_is_valid_by_email_password(email, sha512_final_password):
    try:
        instance = CustomerService.objects.get(email=email, password=password)
        return True
    except CustomerService.DoesNotExist:
        return False


def cs_generate_password(email, sha512_frontend_password):
    hash_email = hashlib.sha512()
    hash_email.update(email.encode('utf-8'))
    sha512_email = hash_email.hexdigest()
    hash_password = hashlib.sha512()
    hash_password.update((sha512_frontend_password+sha512_email+'customerservicebig5').encode('utf-8'))
    return hash_password.hexdigest()


def cs_generate_vid(email):
    return admin_generate_communication_key(email)


def cs_send_email(email, content):
    send_mail('客服系统找回密码', content, 'big5_nankai@163.com', [email], fail_silently=True)
