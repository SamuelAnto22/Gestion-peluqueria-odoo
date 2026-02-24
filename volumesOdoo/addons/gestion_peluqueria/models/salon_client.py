from odoo import models, fields, api


class SalonClient(models.Model):
    _name="salon.client"
    _description="Modelo de cliente"
    _order="nombre"
    _rec_name="nombre"

    nombre = fields.Char(string="Nombre", required=True,index=True)
    telefono=fields.Char(string="Telefono")
    email=fields.Char(string="Email")
    edad=fields.Integer(string="Edad")
    observaciones=fields.Text(string="Observaciones")
    cita_id=fields.One2many('salon.appointment',"cliente_id",string="Cita")
    total_citas = fields.Integer(string="Total Citas", compute='_compute_appointments')
    total_pagado = fields.Float(string="Total Pagado", compute='_compute_total_pagado')

    @api.depends('cita_id')
    def _compute_appointments(self):
        for record in self:
            record.total_citas = len(record.cita_id)

    @api.depends('cita_id.estado', 'cita_id.precio_total')
    def _compute_total_pagado(self):
        for record in self:
            citas_pagadas = record.cita_id.filtered(lambda r: r.estado == 'Pagada')
            record.total_pagado= sum(citas_pagadas.mapped('precio_total'))









