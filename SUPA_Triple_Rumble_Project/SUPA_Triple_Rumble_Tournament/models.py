from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tournament(models.Model):
    NAME_MAX_LEN = 128

    name = models.CharField(max_length=NAME_MAX_LEN)
    category = models.CharField(max_length=80)
    bio = models.CharField(max_length=1500)
    max_ent = models.IntegerField(default=16)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tournament, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tournaments'

    def __str__(self):
        return self.name


class TeamTournament(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE)

    max_team_players = models.IntegerField(default=4)
    valid_team = models.BooleanField(default=False)

    def __str__(self):
        return self.tournament.name


class IndividualTournament(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE)

    max_rank = models.IntegerField(default=0)
    min_rank = models.IntegerField(default=0)

    def __str__(self):
        return self.tournament.name


class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    team_pic = models.ImageField(upload_to='team_image', blank=True)
    slug = models.SlugField(unique=True)
    team_captain = models.OneToOneField('UserProfile', on_delete=models.CASCADE, related_name='team_captain')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = (
        (1, "competitor"),
        (2, "staff"),
        (3, "admin")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,
                                                 default=1)  # Default to 1 for competitor, change to 2 or three if
    # staff member
    pfp = models.ImageField(upload_to='profile_images', blank=True)  # Can be used for both staff and competitor users
    pronouns = models.CharField(max_length=20)  # Can be used for both staff and competitor users#
    discord = models.CharField(max_length=50)
    score_saber = models.URLField(blank=True)  # Can be used for both staff and competitor users
    bio = models.CharField(max_length=1000, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username
