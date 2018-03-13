# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.forms import ModelForm

from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    ALL_HOUSES = "AllHouses"
    SRISHTI = "Srishti"
    SAGAR = "Sagar"
    VASUNDHARA = "Vasundhara"
    HIMGIRI = "Himgiri"
    HOUSE_CHOICE = (
        (ALL_HOUSES, "AllHouses"),
        (SRISHTI, "Srishti"),
        (SAGAR, "Sagar"),
        (VASUNDHARA, "Vasundhara"),
        (HIMGIRI, "Himgiri"),
    )
    house = models.CharField(
        max_length = 30,
        choices = HOUSE_CHOICE,
        default = ALL_HOUSES,
    )

    ALL_SOCIETIES = "AllSocieties"
    COMPUTER = "Computer"
    DANCE = "Dance"
    DRAMA = "Drama"
    ECONOMICS = "Economics"
    HERITAGE = "Heritage"
    MATHS = "Maths"
    MUN = "MUN"
    MUSIC = "Music"
    PHOTOGRAPHY = "Photography"
    QUIZ = "Quiz"
    SCIENCE = "Science"
    SOCIETIES_CHOICE = (
        (ALL_SOCIETIES, "AllSocieties"),
        (COMPUTER, "Computer"),
        (DANCE, "Dance"),
        (DRAMA, "Drama"),
        (ECONOMICS, "Economics"),
        (MATHS, "Maths"),
        (MUN, "MUN"),
        (MUSIC, "Music"),
        (PHOTOGRAPHY, "Photography"),
        (QUIZ, "Quiz"),
        (SCIENCE, "Science"),
    )
    society = models.CharField(
        max_length = 30,
        choices = SOCIETIES_CHOICE,
        default = ALL_SOCIETIES,
    )

    SCHOOL_WIDE = "SchoolWide"
    ENVIRONMENTAL_INITIATIVES = "EnvironmentalInitiatives"
    INTERSCHOOL_EVENTS = "InterschoolEvents"
    INTRASCHOOL_EVENTS = "IntraschoolEvents"
    SOCIAL_PROJECTS = "SocialProjects"
    SPORTS = "Sports"
    CATEGORY_CHOICE = (
        (SCHOOL_WIDE, "SchoolWide"),
        (ENVIRONMENTAL_INITIATIVES, "EnvironmentalInitiatives"),
        (INTERSCHOOL_EVENTS, "InterschoolEvents"),
        (INTRASCHOOL_EVENTS, "IntraschoolEvents"),
        (SOCIAL_PROJECTS, "SocialProjects"),
        (SPORTS, "Sports"),
    )
    category = models.CharField(
        max_length = 30,
        choices = CATEGORY_CHOICE,
        default = SCHOOL_WIDE,
    )

    def __str__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "house", "society", "category")
