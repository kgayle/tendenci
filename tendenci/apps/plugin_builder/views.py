from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from tendenci.core.base.http import Http403
from tendenci.core.perms.utils import update_perms_and_save, has_perm
from tendenci.apps.plugin_builder.models import Plugin
from tendenci.apps.plugin_builder.utils import build_plugin

@login_required
def build(request, id):
    if not request.user.profile.is_superuser:
        raise Http403
    
    plugin = get_object_or_404(Plugin, id=id)

    build_plugin(plugin)
    messages.add_message(request, messages.SUCCESS, 'Successfully built %s' % plugin)
    
    return redirect("admin:plugin_builder_plugin_change",plugin.pk)