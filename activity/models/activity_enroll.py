from django.db import models
from django.contrib.auth.models import User
from .activity import Activity
from .enum import APPROVE_STATUS_CHOICE

# 活动报名
# 一个用户只能在一个活动中有一条纪录
class ActivityEnroll(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="enrolls",
        db_column="activity")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="activity_enrolls",
        db_column="user")

    # **报名时间**
    enroll_time = models.DateTimeField('Enroll Time', auto_now_add=True)

    # **批准状态**
    # 管理员可以审核
    status = models.IntegerField(
        'Status',
        db_column = 'status',
        default=1,
        choices=APPROVE_STATUS_CHOICE)

    # **批准报名的时间**
    approve_time = models.DateTimeField('Approve Time', null=True)

    # **批准报名的管理员**
    approver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="approved_enrolls",
        db_column="approver",
        null=True)

    def __str__(self):
        return self.user.username + ' → ' + self.activity.name 

    def activity_name(self):
        return self.activity.name 
    
    def user_name(self):
        return self.user.username
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['activity', 'user'],
                name='activity_enroll__activity_user'
            ),
        ]