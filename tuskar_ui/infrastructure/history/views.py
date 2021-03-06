# -*- coding: utf8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from horizon import tables as horizon_tables

from tuskar_ui import api
from tuskar_ui.infrastructure.history import tables


class IndexView(horizon_tables.DataTableView):
    table_class = tables.HistoryTable
    template_name = "infrastructure/history/index.html"

    def get_data(self):
        plan = api.tuskar.Plan.get_the_plan(self.request)
        if plan:
            stack = api.heat.Stack.get_by_plan(self.request, plan)
            if stack:
                return stack.events
        return []
