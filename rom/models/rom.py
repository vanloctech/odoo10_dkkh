# -*- coding: utf-8 -*-
# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).
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


class rom_dantoc(models.Model):
    _name = "rom.dantoc"
    name = fields.Char("Tên dân tộc")


class rom_tinh(models.Model):
    _name = "rom.tinh"
    name = fields.Char("Tỉnh")


class rom_quoctich(models.Model):
    _name = "rom.quoctich"
    name = fields.Char("Quốc tịch")
