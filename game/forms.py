from django.forms import ModelForm
from django import forms
from . models import Guild, Character, GuildSkill, SubRace, SubGuild, Spell
from django.utils.translation import ugettext_lazy as _

class CreateCharForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCharForm, self).__init__(*args, **kwargs)
        self.fields['subrace'].queryset = SubRace.objects.none()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class' : 'form-control'
            })
    class Meta:
        model = Character
        fields = ['name', 'background', 'race', 'subrace', 'guild', 'subguild', 'strength', 'dexterity','constitution','wisdom','intelligence','charisma', 'goodAlignment', 'lawfulAlignment']
        labels = {
            "name" : _("What's your character's name?"),
            "background" : _("What is your character's background?")
        }





