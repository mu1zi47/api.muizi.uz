from modeltranslation.translator import register, TranslationOptions
from .models import Projects, skills, Technology

@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(skills)
class SkillsTranslationOptions(TranslationOptions):
    fields = ('level',)

@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ()