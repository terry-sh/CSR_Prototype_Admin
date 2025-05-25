from django.db import models
from django.contrib.auth.models import User
from .activity import Activity

# 活动中多人组成的小组
class Team(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="all_teams",
        db_column="activity")
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')

# 角色类型
TEAM_ROLE = (
    (0, 'Owner'),
    (1, 'Manager'),
    (2, 'Member'),
)

class TeamMember(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="all_members",
        db_column="team")

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="all_teams",
        db_column="member")

    role = models.IntegerField('Role', db_column = 'Role', default=2, choices=TEAM_ROLE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'member'],
                name='unique_team_member__team_member'
            ),
        ]