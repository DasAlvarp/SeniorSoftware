# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import ScoringCriteria, Category, Team, Score, Member
from django.contrib.auth.models import User, AnonymousUser

class TeamTestCase(TestCase):
    def test_member_name(self):
        mem = Member(memberName = "dale")
        self.assertEqual(mem.memberName, "dale")

    def test_team_name(self):
		team = Team(teamName="Magneto")
		self.assertEqual("Magneto", team.teamName)

    def test_crit_name(self):
		crit = ScoringCriteria(criteriaName="originality")
		self.assertEqual("originality", crit.criteriaName)

    def test_score_team_relationship(self):
		scr = Score(judge="Harry")
		team = Team(teamName = "Beast")
		scr.teamName = team
		self.assertEqual("Beast", scr.teamName.teamName)

    def test_score_category_relationship(self):
		scr = Score(judge="Harry")
		team = Team(teamName = "Beast")
		scr.teamName = team
		cat  = Category(category = "Hackathon")
		scr.category = cat
		self.assertEqual("Hackathon", scr.category.category)

    def test_score_scores(self):
		scr = Score(judge="Harry")
		scr.score1 = 1.1
		scr.score2 = 2.2
		scr.score3 = 3.3
		scr.score1 = scr.score2
		self.assertEqual(2.2, scr.score1)
