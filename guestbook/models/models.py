# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProgramingLanguage(models.Model):
    _name = "guestbook.programing_language"
    name = fields.Char(required=True)
    color = fields.Integer(string='Color Index')
    

class Guest(models.Model):
    _name = 'guestbook.guest'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    phone = fields.Char()
    programing_language = fields.Many2many('guestbook.programing_language', column1='guest_id',
                                    column2='language_id', string='Programing Language')
    github = fields.Char()
    message = fields.Text(required=True)


    