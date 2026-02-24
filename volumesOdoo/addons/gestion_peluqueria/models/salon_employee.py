from odoo import models, fields, api

class salonEmployee(models.Model):
    _name="salon.employee"
    _description="Modelo de empleado"
    _order="nombre"
    _rec_name="nombre"

    nombre=fields.Char(string="Nombre",required=True,index=True)
    telefono=fields.Char(string="Telefono")
    especialidad=fields.Selection([('peluquero','Peluquero/a'),('manicurista','Manicurista'),('estetecista','Esteticista')],string="Especialidad")
    dia_libre=fields.Selection([('lunes','Lunes'),('martes','Martes'),('miercoles','Miercoles'),('jueves','Jueves'),('viernes','Viernes'),('sabado','Sabado'),('domingo','Domingo')],string="Dia libre")
    active=fields.Boolean(string="Activo", default=True)
    cita_id=fields.One2many('salon.appointment',"empleado_id",string="Cita")
    total_citas = fields.Integer(string="Total Citas", compute='_compute_total_citas')

    @api.depends('cita_id')
    def _compute_total_citas(self):
        for record in self:
            record.total_citas = len(record.cita_id)
