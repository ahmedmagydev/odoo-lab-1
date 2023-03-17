from odoo import models ,fields



class Patient(models.Model):
    _name="hms.patient"
    firstname=fields.Char()
    lastname=fields.Char()
    birthday=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float()
    blood_type=fields.Selection([('a+',"a+"),("b+","b+"),("c+","c+"),("o+","o+"),("a-","a-"),("b-","b-"),("c-","c-"),("o-","o-")])
    bcr=fields.Boolean()
    images=fields.Image()
    adress=fields.Text()
    age=fields.Integer()