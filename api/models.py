from django.db import models


class PeerUser(models.Model):
    name = models.CharField(max_length=100)


class RewardHistory(models.Model):
    datetime_stamp = models.DateTimeField(auto_now_add=True)
    points = models.FloatField(blank=False, null=False)
    given_by = models.ForeignKey(PeerUser, related_name="given_rewards", on_delete=models.DO_NOTHING, blank=False)
    given_to = models.ForeignKey(PeerUser, related_name="received_rewards", on_delete=models.DO_NOTHING, blank=False)


