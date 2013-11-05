# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Firewall(horizon.Panel):
    name = _("Firewalls")
    slug = "firewalls"
    permissions = ('openstack.services.network',)


if getattr(settings,
           'OPENSTACK_NEUTRON_NETWORK',
           {}).get('enable_firewall', False):
    dashboard.Project.register(Firewall)
