from django.contrib import admin
from .models import Character, Race, SubRace, Guild, SubGuild, Item, Weapon, Armor, Spell, GuildSkill, Background, Skill
from .models import CharAbility, CharacterSpells, CharBadge, Achievement, CharQuest, Ability

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(SubRace)
admin.site.register(Guild)
admin.site.register(SubGuild)
admin.site.register(Item)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Spell)
admin.site.register(GuildSkill)
admin.site.register(Background)
admin.site.register(Skill)
admin.site.register(Ability)
admin.site.register(Achievement)
admin.site.register(CharAbility)
admin.site.register(CharBadge)