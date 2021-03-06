# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#    Copyright (C) 2013-today Synconics Technologies Pvt. Ltd. (<http://www.synconics.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, api, _

class cm_postcode(models.Model):
    _name = 'cm.postcode'

    part_1 = fields.Char("Part 1",size=4, required=True) 
    part_2 = fields.Char("Part 2",size=3)
    postcode = fields.Char("Postcode",compute="_get_postcode")
    part_1_portion = fields.Char('Part_1 Portion', compute="get_part_1_portion_portion",store=True)

    @api.multi
    def name_get(self):
        res=[]
        for postcode in self:
            name = postcode.part_1 or '' + ' ' + postcode.part_2 or ''
            res.append((postcode.id,name))
        return res

    @api.one
    def _get_postcode(self):
        if self.part_1 or self.part_2:
            self.postcode = self.part_1 or '' + ' ' + self.part_2 or ''
        else:
            self.postcode = ""

    @api.one
    def get_part_1_portion_portion(self):
        if self.part_1:
            self.part_1_portion = self.part_1[:3]
        else:
            self.part_1_portion = ""
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
