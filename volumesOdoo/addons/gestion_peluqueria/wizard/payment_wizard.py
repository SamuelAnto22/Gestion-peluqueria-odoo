from odoo import models, fields, api

class PaymentWizard(models.TransientModel):
    _name = "payment.wizard"
    _description = "Asistente para registrar pagos"

    cita_id = fields.Many2one('salon.appointment', string="Cita", required=True)
    metodo_pago=fields.Selection([('efectivo','Efectivo'),('tarjeta','Tarjeta de Credito')],string="Metodo de pago")
    descuento= fields.Float(string="Descuento")
    precio_final=fields.Float(string="Precio Total", compute='_compute_precio_final' )



    @api.depends('cita_id.precio_total','descuento')
    def _compute_precio_final(self):
        for record in self:
            record.precio_final = record.cita_id.precio_total - ( record.cita_id.precio_total * (record.descuento/100))


    def confirm_payment(self):
        for wiz in self:
            wiz.cita_id.write({
                'estado':'pagada',
                'precio_total' : wiz.precio_final
            })



