from odoo import models, fields, api

class salonService(models.Model):
    _name="salon.service"
    _description="Modelo del servicio"
    _order="nombre"
    _rec_name="nombre"

    nombre=fields.Char(string="Nombre",required=True,index=True)
    precio=fields.Float(string="Precio", required=True,default=0.0)
    duracion=fields.Float(string="Duracion en minutos",required=True,default=30.0)
    especialidad=fields.Selection([('peluquero','Peluquero/a'),('manicurista','Manicurista'),('estetecista','Esteticista')],string="Especialidad")
