# Este archivo define el modelo "salon.service" que representa cada servicio
from odoo import models, fields, api

# Modelo que almacena información de los servicios dados.
class salonService(models.Model):
    _name="salon.service"
    _description="Modelo del servicio"
    _order="nombre"
    _rec_name="nombre"

    # === CAMPOS ===
    nombre=fields.Char(string="Nombre",required=True,index=True)
    precio=fields.Float(string="Precio", required=True,default=0.0)
    duracion=fields.Float(string="Duracion en minutos",required=True,default=30.0)
    especialidad=fields.Selection([('peluquero','Peluquero/a'),('manicurista','Manicurista'),('estetecista','Esteticista')],string="Especialidad")

    # campo que añade el tipo de moneda de la empresa al campo precio (en este caso es euro).
    currency_id = fields.Many2one('res.currency', string="Moneda",
                                  default=lambda self: self.env.company.currency_id)
