# -*- coding: utf-8 -*-
# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).
from odoo import api, fields, models,_

class rom(models.Model):
    _name = "rom.dkkh"
    ubndXa = fields.Char("Xã/Phường",required=True)
    ubndHuyen = fields.Char("Quận/Huyện",required=True)
    ubndTinh = fields.Many2one('rom.Tinh',"Tỉnh/TP",)

    so = fields.Integer("Số")
    quyenSo = fields.Integer("Quyển số")
    hoTenChong = fields.Char("Họ tên chồng")
    hoTenVo = fields.Char("Họ tên vợ")
    nSChong = fields.Date("Ngày sinh chồng")
    nSVo = fields.Date("Ngày sinh vợ")
    danTocChong = fields.Many2one('rom.dantoc','Dân tộc')
    danTocVo = fields.Many2one('rom.dantoc','Dân tộc')
    quocTichChong = fields.Many2one('rom.quoctich',"Quốc tịch")
    quocTichVo = fields.Many2one('rom.quoctich',"Quốc tịch")
    soCMNDChong = fields.Integer("Số giấy CMND/Hộ chiếu",size=12)
    soCMNDVo = fields.Integer("Số giấy CMND/Hộ chiếu",size=12)


class rom_dantoc(models.Model):
    _name = "rom.dantoc"
    name = fields.Char("Tên dân tộc")

class rom_tinh(models.Model):
    _name = "rom.tinh"
    name = fields.Char("Tỉnh")