# -*- coding: utf-8 -*-
# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).
import re
from odoo import api, fields, models, tools, _
from openerp.exceptions import ValidationError
from odoo.exceptions import ValidationError, except_orm
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round, float_compare, float_is_zero
from datetime import datetime, timedelta

class rom(models.Model):
    _name = "rom.dkkh"

    @api.model
    def _default_date_now(self):
        return datetime.today()

    @api.constrains('hoTenChong')
    def check_name(self):
        """ make sure name 10-15 alphabets and spaces"""
        for rec in self:
            # here i forced that the name should start with alphabets if it's not the case remove ^[a-zA-Z]
            # and just keep:  re.match(r"[ a-zA-Z]+", rec.name)
            if not 10 <= len(rec.hoTenChong) <= 15 or not re.match(r"^[a-zA-Z][ a-zA-Z]*", rec.hoTenChong):
                raise ValidationError(_('your message about 10-15 alphabets and spaces'))

    @api.constrains('hoTenVo')
    def check_namevo(self):
        for rec in self:
            if not 10 <= len(rec.hoTenVo) <= 15 or not re.match(r"^[a-zA-Z][ a-zA-Z]*", rec.hoTenVo):
                raise ValidationError(_("Ho ten phai trong khoang 10 den 15 ky tu"))

    ubndXa = fields.Char("Xã/Phường", required=True)
    ubndHuyen = fields.Char("Quận/Huyện", required=True)
    ubndTinh = fields.Many2one('rom.tinh', "Tỉnh/TP", )

    so = fields.Integer("Số", required=True, default='')
    quyenSo = fields.Integer("Quyển số", required=True)
    hoTenChong = fields.Char("Họ tên chồng", required=True)
    hoTenVo = fields.Char("Họ tên vợ", required=True)
    nSChong = fields.Date("Ngày sinh chồng", required=True)
    nSVo = fields.Date("Ngày sinh vợ", required=True)
    danTocChong = fields.Many2one('rom.dantoc', 'Dân tộc', required=True)
    danTocVo = fields.Many2one('rom.dantoc', 'Dân tộc', required=True)
    quocTichChong = fields.Many2one('rom.quoctich', "Quốc tịch", required=True)
    quocTichVo = fields.Many2one('rom.quoctich', "Quốc tịch", required=True)
    soCMNDChong = fields.Integer("Số giấy CMND/Hộ chiếu", size=12, required=True)
    soCMNDVo = fields.Integer("Số giấy CMND/Hộ chiếu", size=12, required=True)
    noiThuongTruChong = fields.Char("Nơi thường trú", required=True)
    noiThuongTruVo = fields.Char("Nơi thường trú", required=True)
    ngayCongNhan = fields.Date("Ngày quan hệ hôn nhân được công nhận", default=_default_date_now, required=True)

    # def name_get(self, cr, uid, context=None):
    #     if context is None:
    #         context = {}
    #     name = ""
    #     for record in self.browse(cr, uid, ids, context=context):
    #         name = record.name
    #     return name

    # def _get_default_dantoc(self, cr, uid, context=None):
    #     res = self.pool.get('rom.dantoc').search(cr, uid, [('danTocChong', '=', 'Kinh')], context=context)
    #     return res and res[0] or False

    # def get_name(self, cr, uid, ids, context=None):
    #     if context is None:
    #         context = {}
    #     if isinstance(ids, (int, int)):
    #         ids = [ids]
    #     res = []
    #     for record in self.browse(cr, uid, ids, context=context):
    #         name = record.name
    #         res.append(record.id, name + " - ahihi")
    #     return res

    @api.onchange('danTocChong')
    def _onchange_dan_toc_chong(self):
        self.name = self.danTocChong.name

    @api.multi
    def print_report(self):
        return {'type': 'ir.actions.report.xml', 'report_name': 'rom_py3o_docx'}


class rom_dantoc(models.Model):
    _name = "rom.dantoc"
    name = fields.Char("Tên dân tộc")


class rom_tinh(models.Model):
    _name = "rom.tinh"
    name = fields.Char("Tỉnh")


class rom_quoctich(models.Model):
    _name = "rom.quoctich"
    name = fields.Char("Quốc tịch")
