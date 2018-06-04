from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User
from users.models import CustomUser
import math
import itertools

class Material(models.Model):
    name = models.CharField(max_length=500)

class Item(models.Model):
    weight = models.IntegerField(default=1)
    cost = models.IntegerField(default=1)
    can_pick_up = models.BooleanField(default=1)
    name = models.CharField(max_length=500)
    desc = models.TextField(default="")
    long_desc = models.CharField(max_length=1000)
    is_magical = models.BooleanField(default=0)
    is_cursed = models.BooleanField(default=0)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    appraise_dc = models.IntegerField(default=10)
    keywords = models.CharField(max_length=100)

class Armor(Item):
    slot = models.IntegerField(default=1)
    armor_ac = models.IntegerField(default=1)
    max_dex_bonus = models.IntegerField(default=0)
    armor_level = models.IntegerField(default=1)
    attribute_boost = models.IntegerField(default=0)
    attribute_type = models.CharField(max_length = 100)

class Weapon(Item):
    handed = models.IntegerField(default=1)
    offhand = models.BooleanField(default=0)
    weapon_type = models.CharField(max_length=100)
    damage_stat = models.CharField(max_length=10)
    damage_type = models.CharField(max_length=20)
    damage_hit_dice = models.IntegerField(default=0)
    const_damage = models.IntegerField(default=0)
    coefficient = models.IntegerField(default=0)

class Guild(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(default="")
    hit_dice = models.IntegerField(default=6)
    magic_dice = models.IntegerField(default=0)
    dex_save = models.BooleanField(default=0)
    str_save = models.BooleanField(default=0)
    con_save = models.BooleanField(default=0)
    wis_save = models.BooleanField(default=0)
    cha_save = models.BooleanField(default=0)
    int_save = models.BooleanField(default=0)
    skill_points = models.IntegerField(default=2)
    main_stat = models.CharField(default="DEX", max_length=3)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class SubGuild(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT)
    desc = models.TextField(default="")
    name = models.CharField(max_length=50)
    ki_points = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Race(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(default="")
    light_level = models.IntegerField(default=50)
    size = models.IntegerField(default=2)
    str = models.IntegerField(default=0)
    con = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    wis = models.IntegerField(default=0)
    cha = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    skill_points = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class SubRace(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, on_delete=models.PROTECT, default=None)
    desc = models.TextField(default="")
    sub_str = models.IntegerField(default=0)
    sub_con = models.IntegerField(default=0)
    sub_dex = models.IntegerField(default=0)
    sub_wis = models.IntegerField(default=0)
    sub_cha = models.IntegerField(default=0)
    sub_int = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

ALIGNMENTS = (
    (100, 'Good'),
    (50, 'Neutral'),
    (0, 'Evil')
)

LALIGNMENTS = (
    (100, 'Lawful'),
    (50, 'Neutral'),
    (0, 'Chaotic')
)

class Background(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(default="")
    Acrobatics = models.BooleanField(default=0)
    Animal_Handling = models.BooleanField(default=0)
    Arcana = models.BooleanField(default=0)
    Athletics = models.BooleanField(default=0)
    Deception = models.BooleanField(default=0)
    History = models.BooleanField(default=0)
    Insight = models.BooleanField(default=0)
    Intimidation = models.BooleanField(default=0)
    Investigation = models.BooleanField(default=0)
    Medicine = models.BooleanField(default=0)
    Nature = models.BooleanField(default=0)
    Perception = models.BooleanField(default=0)
    Performance = models.BooleanField(default=0)
    Persuasion = models.BooleanField(default=0)
    Religion = models.BooleanField(default=0)
    Sleight_of_Hand = models.BooleanField(default=0)
    Stealth = models.BooleanField(default=0)
    Survival = models.BooleanField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(default="")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    hp = models.IntegerField(default=1)
    mp = models.IntegerField(default=0)
    max_hp = models.IntegerField(default=1)
    max_mp = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    strength_prof = models.IntegerField(default=0)
    dexterity_prof = models.IntegerField(default=0)
    constitution_prof = models.IntegerField(default=0)
    intelligence_prof = models.IntegerField(default=0)
    wisdom_prof = models.IntegerField(default=0)
    charisma_prof = models.IntegerField(default=0)
    proficiency_bonus = models.IntegerField(default=0)
    max_encumbrance = models.IntegerField(default=10)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    subrace = models.ForeignKey(SubRace, on_delete=models.PROTECT, default= None, blank=True, null=True)
    guild = models.ForeignKey(Guild, on_delete= models.PROTECT)
    subguild = models.ForeignKey(SubGuild, on_delete=models.PROTECT, default=None, blank=True, null=True)
    spell_slot1 = models.IntegerField(default=0)
    spell_slot2 = models.IntegerField(default=0)
    spell_slot3 = models.IntegerField(default=0)
    spell_slot4 = models.IntegerField(default=0)
    spell_slot5 = models.IntegerField(default=0)
    spell_slot6 = models.IntegerField(default=0)
    spell_slot7 = models.IntegerField(default=0)
    spell_slot8 = models.IntegerField(default=0)
    spell_slot9 = models.IntegerField(default=0)
    acrobatics = models.BooleanField(default=0)
    animal_handling = models.BooleanField(default=0)
    arcana = models.BooleanField(default=0)
    athletics = models.BooleanField(default=0)
    deception = models.BooleanField(default=0)
    history = models.BooleanField(default=0)
    insight = models.BooleanField(default=0)
    intimidation = models.BooleanField(default=0)
    investigation = models.BooleanField(default=0)
    medicine = models.BooleanField(default=0)
    nature = models.BooleanField(default=0)
    perception = models.BooleanField(default=0)
    performance = models.BooleanField(default=0)
    persuasion = models.BooleanField(default=0)
    religion = models.BooleanField(default=0)
    sleight = models.BooleanField(default=0)
    stealth = models.BooleanField(default=0)
    survival = models.BooleanField(default=0)
    goodAlignment = models.IntegerField(choices=ALIGNMENTS, default=100)
    lawfulAlignment = models.IntegerField(choices=LALIGNMENTS, default=100)
    background = models.ForeignKey(Background, on_delete=models.PROTECT, default=None)
    account = models.ForeignKey(CustomUser, related_name='user', on_delete=models.PROTECT, default=None)
    AC = models.IntegerField(default=10)
    initiative = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def get_next_xp(self):
        if self.level == 1:
            return 500
        else:
            return self.level * (self.level-1) * 500
    def save(self, *args, **kwargs):
        self.strength_prof = (int(self.strength)/2)-5
        self.dexterity_prof = (int(self.dexterity) / 2) - 5
        self.constitution_prof = (int(self.constitution) / 2) - 5
        self.intelligence_prof = (int(self.intelligence) / 2) - 5
        self.wisdom_prof = (int(self.wisdom) / 2) - 5
        self.charisma_prof = (int(self.charisma) / 2) - 5
        self.proficiency_bonus = math.floor((int(self.level) + 7)/4)
        #Get all classes related to the character
        guild_list = CharGuild.objects.filter(account = self.account)
        lvl = 0
        for g in guild_list:
            lvl += g.level
        self.level = lvl
        super(Character, self).save(*args, **kwargs)  # Call the "real" save() method.

class CharGuild(models.Model):
    account = models.ForeignKey(Character, on_delete=models.PROTECT)
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT)
    level = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0)
    stat = models.CharField(max_length=20)
    statlevel = models.IntegerField(default=10)

class CharSubGuild(models.Model):
    account = models.ForeignKey(Character, on_delete=models.PROTECT)
    subguild = models.ForeignKey(SubGuild, on_delete=models.PROTECT)
    level = models.IntegerField(default=0)

class CharacterInventory(models.Model):
    owner = models.ForeignKey(Character, on_delete=models.PROTECT)
    weapon = models.ForeignKey(Weapon, on_delete=models.PROTECT)
    armor = models.ForeignKey(Armor, on_delete=models.PROTECT)

class Spell(models.Model):
    name = models.CharField(max_length = 50)
    level = models.IntegerField(default=1)
    desc = models.TextField(default="")
    min_spell_slot = models.IntegerField(default=1)
    damage_die = models.IntegerField(default=1)
    damage_coefficient = models.IntegerField(default=1)
    damage_constant = models.IntegerField(default=0)
    self_only = models.BooleanField(default=0)
    opponent_number = models.IntegerField(default=1)
    area_effect = models.BooleanField(default=0)
    save_stats = models.CharField(max_length = 3, default=None, blank=True, null=True)
    spell_save_dc = models.IntegerField(default=10)
    spell_status_effect = models.CharField(default=None, max_length=10, blank=True, null=True)
    spell_item = models.ForeignKey(Item, on_delete=models.PROTECT, default=None, blank=True, null=True)
    spell_class = models.ForeignKey(Guild, on_delete=models.PROTECT, default=None, blank=True, null=True)
    spell_ac_boost = models.IntegerField(default=0)
    spell_skill_boost_name = models.CharField(max_length=20, default=None, blank=True, null=True)
    spell_skill_boost_number = models.IntegerField(default=0)
    spell_length_rounds = models.IntegerField(default=1)
    on_reaction = models.BooleanField(default=0)
    concentration = models.BooleanField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class GuildSkill(models.Model):
    name = models.CharField(max_length = 50)
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class CharacterSpells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    spell = models.ForeignKey(Spell, on_delete=models.PROTECT)

class Achievement(models.Model):
    name = models.CharField(max_length=100, default='')
    desc = models.TextField(default="")

class CharBadge(models.Model):
    achievement_id = models.ForeignKey(Achievement, on_delete=models.PROTECT)
    character = models.ForeignKey(Character, on_delete=models.PROTECT)

class Ability(models.Model):
    desc = models.TextField(default="")
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT, default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete= models.PROTECT, default=None, blank=True, null=True)
    img = models.ImageField(upload_to='icons/')
    cooldown = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class CharAbility(models.Model):
    account = models.ForeignKey(Character, on_delete=models.PROTECT)
    ability = models.ForeignKey(Ability, on_delete=models.PROTECT)
    activated = models.BooleanField(default=1)
    remainingcooldown = models.IntegerField(default=0)

class Quest(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField

class CharQuest(models.Model):
    account = models.ForeignKey(Character, on_delete=models.PROTECT)
    is_finished = models.BooleanField(default=0)