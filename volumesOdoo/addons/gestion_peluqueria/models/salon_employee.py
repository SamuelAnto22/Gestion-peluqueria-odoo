# Este archivo define el modelo "salon.employee" que representa a cada empleado
from odoo import models, fields, api

# Modelo que almacena información de los empleados.
class salonEmployee(models.Model):
    _name="salon.employee"
    _description="Modelo de empleado"
    _order="nombre"
    _rec_name="nombre"

    # === CAMPOS ===
    nombre=fields.Char(string="Nombre",required=True,index=True)
    telefono=fields.Char(string="Telefono")
    especialidad=fields.Selection([('peluquero','Peluquero/a'),('manicurista','Manicurista'),('esteticista','Esteticista')],string="Especialidad")
    dia_libre=fields.Selection([('lunes','Lunes'),('martes','Martes'),('miercoles','Miercoles'),('jueves','Jueves'),('viernes','Viernes'),('sabado','Sabado'),('domingo','Domingo')],string="Dia libre")
    active=fields.Boolean(string="Activo", default=True)

    # Las citas que tiene el empleado. Relacion One2many con salon.appointment.
    cita_ids=fields.One2many('salon.appointment',"empleado_id",string="Cita")

    # Campo computado: total de citas (obteniendo la longitud de cita_ids).
    total_citas = fields.Integer(string="Total Citas", compute='_compute_total_citas')

    @api.depends('cita_ids')
    def _compute_total_citas(self):
        for record in self:
            record.total_citas = len(record.cita_ids)
