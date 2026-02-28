# Este archivo define el modelo "salon.client" que representa a cada cliente
from odoo import models, fields, api

# Modelo que almacena información de los clientes.
class SalonClient(models.Model):
    # Identificador técnico del modelo en Odoo.
    _name="salon.client"
    # Descripción legible del modelo
    _description="Modelo de cliente"
    # Orden por defecto en las vistas tipo tree o search.
    _order="nombre"
    # Indicamos qué campo se mostrará como el nombre del registro en campos Many2one.
    _rec_name="nombre"

    # === CAMPOS ===
    # Nombre, telefono, correo electronico, edad, observaciones del cliente.
    nombre = fields.Char(string="Nombre", required=True,index=True)
    telefono=fields.Char(string="Telefono")
    email=fields.Char(string="Email")
    edad=fields.Integer(string="Edad")
    observaciones=fields.Text(string="Observaciones")

    # Las citas que tiene el cliente. Relacion One2many con salon.appointment.
    cita_ids=fields.One2many('salon.appointment',"cliente_id",string="Cita")

    # Campo computado: total de citas (obteniendo la longitud de cita_ids).
    total_citas = fields.Integer(string="Total Citas", compute='_compute_appointments')

    # Campo computado: total pagado (sumando el precio de todas las citas pagadas del cliente).
    total_pagado = fields.Float(string="Total Pagado", compute='_compute_total_pagado')

    @api.depends('cita_ids')
    def _compute_appointments(self):
        for record in self:
            record.total_citas = len(record.cita_ids)

    @api.depends('cita_ids.estado', 'cita_ids.precio_total')
    def _compute_total_pagado(self):
        for record in self:
            citas_pagadas = record.cita_ids.filtered(lambda r: r.estado == 'pagada')
            record.total_pagado= sum(citas_pagadas.mapped('precio_total'))









