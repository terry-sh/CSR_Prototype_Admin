from django.db import models
from .activity import Activity

# 活动的财务报告
# 启动资金，花销，盈利等
class ActivityFinancing(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity")
    # 活动的预算
    budget = models.DecimalField('Budget')
    # 收入目标
    earning_target = models.DecimalField('Earning Target')