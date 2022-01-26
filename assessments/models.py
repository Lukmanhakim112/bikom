from django.db import models
from django.utils.translation import ugettext_lazy as _


class AssesmentModel(models.Model):
    name = models.CharField(
        _("Assesment Name"),
        max_length=120,
    )

    def __str__(self):
        return self.name

class QuestionModel(models.Model):
    assessment = models.ForeignKey(
        AssesmentModel,
        on_delete=models.CASCADE
    )
    question = models.CharField(
        _("Question"),
        max_length=120,
    )
    img_question = models.ImageField(
        _("Question Image"),
        upload_to="question_img/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.assessment}: {self.question}"

class AnswerModel(models.Model):
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE
    )
    answer = models.CharField(
        _("Answer"),
        max_length=120,
    )
    answer_img = models.ImageField(
        _("Question Image"),
        upload_to="answer_img/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.question}: {self.answer}"

