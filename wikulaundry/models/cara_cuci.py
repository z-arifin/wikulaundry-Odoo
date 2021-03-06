#-*- coding: utf-8 -*-

from odoo import models, fields

class wikulaundry(models.Model):
    _name = 'wikulaundry.caracuci'
    _description = 'daftar teknik pencucian'

    name = fields.Selection(
        string='Nama Teknik',
        selection=[('light A', 'Light A'), ('light B', 'Light B'), ('medium A', 'Medium A'), ('medium B', 'Medium B'), ('heavy A', 'Heavy A'), ('heavy B', 'Heavy B'),('Super A', 'Super B')]
    )

    air = fields.Selection(
        string='Jenis Air',
        selection=[('air panas', 'Air Panas'), ('air dingin', 'Air Dingin'), ('cuci uap', 'Cuci Uap'), ('mesin khusus', 'Mesin Khusus')],
        required=True
    )

    harga = fields.Integer(
        string='harga_cuci',
        required=True
    )

    kotoran =  fields.Selection(
        string='Tipe Kotoran',
        selection=[('ringan', 'Ringan'), ('sedang', 'Sedang'), ('berat', 'Berat')],
        required=True
    )

    tersedia = fields.Boolean(
        string='tersedia',
        default=True
    )
    
    deskripsi = fields.Char(
        string='deskripsi',
        help='isi dengan alat yang digunakan untuk mencuci')

    models_ids = fields.One2many(
        comodel_name = 'wikulaundry.jeniscucian',
        inverse_name = 'teknik_id',
        string = 'jenis cucian'
    )

    pegawai_id = fields.Many2one(
        comodel_name = 'res.partner',
        string = 'MANAGER',
        domain = "[('is_pegawainya','=',True)]"
    )