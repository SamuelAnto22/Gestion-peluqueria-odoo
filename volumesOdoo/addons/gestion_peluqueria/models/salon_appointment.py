from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SalonAppointment(models.Model):
    _name="salon.appointment"
    _description="Modelo de las citas"
    _order="fecha"
    _rec_name="cliente_id"

    cliente_id=fields.Many2one('salon.client',"nombre",required=True)
    empleado_id=fields.Many2one('salon.employee',"nombre",required=True)
    servicio_ids=fields.Many2many('salon.service',string="Servicios")
    fecha=fields.Datetime(string="Fecha",required=True)
    precio_total=fields.Float(string="Precio Total",compute='_compute_precio_total')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('en_curso', 'En Curso'),
        ('pagada', 'Pagada'),
        ('no_presentado', 'No Presentado'),
    ], string="Estado", default='pendiente')
    duracion_total = fields.Float(string="Duración Total (min)", compute='_compute_duracion_total')


    @api.depends('servicio_ids.precio')
    def _compute_precio_total(self):
        for record in self:
            record.precio_total=sum(record.servicio_ids.mapped('precio'))
    @api.depends('servicio_ids.duracion')
    def _compute_duracion_total(self):
        for record in self:
            record.duracion_total=sum(record.servicio_ids.mapped('duracion'))
    @api.constrains('empleado_id','servicio_ids')
    def _check_especialidad(self):
        for record in self:
            for servicio in record.servicio_ids:
                if servicio.especialidad != record.empleado_id.especialidad:
                    raise ValidationError("La especialidad del empleado debe ser igual a la del servicio")

    @api.constrains('fecha')
    def _check_date_(self):
        for record in self:
            if record.fecha < fields.Datetime.now():
                raise ValidationError("La fecha no puede ser anterior a la actual")

    @api.constrains('empleado_id','fecha')
    def _check_free_day_(self):
        dias = {
            0: 'lunes',
            1: 'martes',
            2: 'miercoles',
            3: 'jueves',
            4: 'viernes',
            5: 'sabado',
            6: 'domingo'
        }
        for record in self:
            if record.empleado_id.dia_libre == dias[record.fecha.weekday()]:
                raise ValidationError("El empleado no tiene disponibilidad para la fecha seleccionada")


