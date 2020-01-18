from django.db import models


# Create your models here.
class WechatRobotLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    open_id = models.CharField(max_length=32, blank=True, null=True)
    user_text = models.CharField(max_length=255, blank=True, null=True)
    reply_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    others = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wechat_robot_log'
