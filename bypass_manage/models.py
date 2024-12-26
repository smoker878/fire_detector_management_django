from django.db import models
from accounts.models import Employee


class BypassRequistion(models.Model):
    apply_date = models.DateTimeField(auto_now_add = True)
    applier_id = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='applier')
    predict_to_work_date = models.DateField()
    work_id = models.CharField(max_length=50)
    work_name = models.CharField(max_length=50)
    contractor = models.CharField(max_length=50)
    other_message = models.TextField()
    excute_date =  models.DateTimeField()
    excutor_id = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='excutor')
    reset_date = models.DateTimeField()
    reseter_id = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='reseter')

class Bypass_device(models.Model):
    requistion_id = models.ForeignKey(BypassRequistion, on_delete=models.CASCADE)
    device = models.CharField(max_length=50)