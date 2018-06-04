from django.shortcuts import render
from . models import Guild, Race, SubRace, Background, GuildSkill, Skill, Character
from django.views.generic import ListView
from .forms import CreateCharForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse
import json
from django.core import serializers
from django.shortcuts import redirect, reverse
import pages.views

def char_create(request):
    c = CreateCharForm()
    return render(request, 'game/char_create.html', {'CreateCharForm' : c})

def get_guild_info(request):
    if request.method == 'POST':
        data = {}
        guildid = request.POST.get('id_guild')
        g = Guild.objects.get(pk=guildid)
        data['desc'] = g.desc
        data['g_img'] = "/game/static/game/"+g.name+".jpg"
        data['skill_points'] = g.skill_points
        return HttpResponse(json.dumps(data), content_type="application/json")

def get_race_info(request):
    if request.method == 'POST':
        data = {}
        raceid = request.POST.get('id_race')
        r = Race.objects.get(pk=raceid)
        data['desc'] = r.desc
        data['r_img'] = "/game/static/game/"+r.name+".jpg"
        data['str'] = r.str
        data['dex'] = r.dex
        data['con'] = r.con
        data['int'] = r.int
        data['wis'] = r.wis
        data['cha'] = r.cha
        return HttpResponse(json.dumps(data), content_type="application/json")

def get_subraces(request):
    if request.method == 'POST':
        raceid = request.POST.get('id_race')
        subraceobj = SubRace.objects.filter(race = raceid)
        data = {}
        for sr in subraceobj:
            data[sr.id] = sr.name
        return HttpResponse(json.dumps(data), content_type="application/json")

def get_subrace_stats(request):
    if request.method == 'POST':
        subraceid = request.POST.get('id_subrace')
        subraceobj = SubRace.objects.get(name=subraceid)
        data = {}
        data['str'] = subraceobj.sub_str
        data['dex'] = subraceobj.sub_dex
        data['con'] = subraceobj.sub_con
        data['int'] = subraceobj.sub_int
        data['wis'] = subraceobj.sub_wis
        data['cha'] = subraceobj.sub_cha
        data['desc'] = subraceobj.desc
        data['r_img'] = "/game/static/game/" + subraceobj.name + ".jpg"
        return HttpResponse(json.dumps(data), content_type="application/json")

def get_background_info(request):
    if request.method == 'POST':
        background_id = request.POST.get('id_background')
        data = {}
        if background_id != "":
            backgroundobj = Background.objects.get(id=background_id)
            # Get all skills default to 0
            skill_list = Skill.objects.all()
            for skill in skill_list:
                data[skill.name.replace(" ", "_")] = getattr(backgroundobj, skill.name.replace(" ", "_"))
            data['desc'] = backgroundobj.desc
            return HttpResponse(json.dumps(data), content_type="application/json")

def get_skill_proficiencies(request):
    if request.method == 'POST':
        data = {}
        #Get all skills default to 0
        skill_list = Skill.objects.all()
        for skill in skill_list:
            data[skill.name.replace(" ", "")] = False

        guild_id = request.POST.get('id_guild')
        background_id = request.POST.get('id_background')
        #Get all of the skills related to the guild
        if guild_id != '':
            guild_skills = GuildSkill.objects.filter(guild = guild_id)
            # Iterate through each skill and set the skill to 1 if there.
            for skill in guild_skills:
                data[skill.name.replace(" ", "")] = True
        return HttpResponse(json.dumps(data), content_type="application/json")

def post_character(request):
    if request.method == 'POST':
        error = False
        c = Character()
        c.account = request.user
        c.name = request.POST.get('name')
        c.strength = request.POST.get('strength')
        c.dexterity = request.POST.get('dexterity')
        c.constitution = request.POST.get('constitution')
        c.intelligence = request.POST.get('intelligence')
        c.wisdom = request.POST.get('wisdom')
        c.charisma = request.POST.get('charisma')
        c.class_id = request.POST.get('class')
        c.goodAlignment = request.POST.get('goodAlignment')
        c.lawfulAlignment = request.POST.get('lawfulAlignment')
        b = Background.objects.get(id=request.POST.get('background'))
        c.background = b
        try:
            g = Guild.objects.get(id=request.POST.get('guild'))
            c.guild = g
        except:
            error = True
            print("Guild")
        try:
            r = Race.objects.get(id=request.POST.get('race'))
            c.race = r
        except:
            error = True
            print("Race")
            #Check to see if sub races apply
        try:
            sub  = SubRace.objects.get(name=request.POST.get('subrace'))
            c.subrace = sub
        except:
            pass
        c.acrobatics = request.POST.get('acrobatics').replace("'", "").title()
        c.animal_handling = request.POST.get('animal_handling').replace("'", "").title()
        c.arcana = request.POST.get('arcana').replace("'", "").title()
        c.athletics= request.POST.get('athletics').replace("'", "").title()
        c.deception= request.POST.get('deception').replace("'", "").title()
        c.history= request.POST.get('history').replace("'", "").title()
        c.insight= request.POST.get('insight').replace("'", "").title()
        c.intimidation= request.POST.get('intimidation').replace("'", "").title()
        c.investigation= request.POST.get('investigation').replace("'", "").title()
        c.medicine= request.POST.get('medicine').replace("'", "").title()
        c.nature= request.POST.get('nature').replace("'", "").title()
        c.perception= request.POST.get('perception').replace("'", "").title()
        c.performance= request.POST.get('performance').replace("'", "").title()
        c.persuasion= request.POST.get('persuasion').replace("'", "").title()
        c.religion= request.POST.get('religion').replace("'", "").title()
        c.sleight_of_hand= request.POST.get('sleight_of_hand').replace("'", "").title()
        c.stealth= request.POST.get('stealth').replace("'", "").title()
        c.survival= request.POST.get('survival').replace("'", "").title()
        #Let's setup the character
        if error == False:
            c.save()
            c.max_hp = g.hit_dice + c.constitution_prof
            c.hp = c.max_hp
            if g.magic_dice > 0:
                if g.main_stat == "INT":
                    c.max_mp = g.magic_dice + c.intelligence_prof
                    c.mp = c.max_mp
                elif g.main_stat == "WIS":
                    c.max_mp = g.magic_dice + c.wisdom_prof
                    c.mp = c.max_mp
                else:
                    c.max_mp = g.magic_dice + c.charisma_prof
                    c.mp = c.max_mp
            c.save()
            return JsonResponse({
                'success': True,
                'url': reverse('home'),
            })
        else:
            return JsonResponse({"success": False, "error": "there was an error"})
    else:
        form = char_create(request)







