from django.shortcuts import render, redirect
from .models import Programmer, Language
from django.forms import modelformset_factory, inlineformset_factory

def index(request, programmer_id):
    programmer = Programmer.objects.get(pk = programmer_id)
    # LanguageFormset = modelformset_factory(Language, fields = ('name',))
    LanguageFormset = inlineformset_factory(Programmer,Language, form= PostFileShareForm, extra = 1) #parent model , child model

    if request.method == 'POST':
        # formset = LanguageFormset(request.POST,queryset = Language.objects.filter(programmer__id = programmer_id))
        formset = LanguageFormset(request.POST,instance = programmer) #parent
        if formset.is_valid():
            # formset.save()
            instances = formset.save(commit = False)
            for instance in instances :
                instance.programmer_id = programmer.id
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('index', programmer.id)
    # formset = LanguageFormset(queryset = Language.objects.filter(programmer__id = programmer_id))
    formset = LanguageFormset(instance = programmer)

    return render(request, 'demo/index.html', {'formset' : formset})