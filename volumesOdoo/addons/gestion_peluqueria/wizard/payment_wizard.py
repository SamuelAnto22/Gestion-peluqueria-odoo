from odoo import models, fields, api

# ==============================================================
#  MODELO TRANSIENTE (WIZARD)
# ==============================================================
# Este modelo es temporal. Los datos se guardan sólo mientras
# el asistente (wizard) está abierto. Luego, Odoo borra el registro.
# Muy útil para pantallas interactivas, confirmaciones o creación rápida.
# ==============================================================

class PaymentWizard(models.TransientModel):
    _name = "payment.wizard"
    _description = "Asistente para registrar pagos"

    # --------------------------------------------------------------
    # CAMPOS DEL WIZARD
    # --------------------------------------------------------------
    cita_id = fields.Many2one('salon.appointment', string="Cita", required=True)
    metodo_pago=fields.Selection([('efectivo','Efectivo'),('tarjeta','Tarjeta de Credito')],string="Metodo de pago")
    descuento= fields.Float(string="Descuento")

    # computado: precio final (precio total - descuento).
    precio_final=fields.Float(string="Precio Total", compute='_compute_precio_final' )



    @api.depends('cita_id.precio_total','descuento')
    def _compute_precio_final(self):
        for record in self:
            record.precio_final = record.cita_id.precio_total - ( record.cita_id.precio_total * (record.descuento/100))


    # --------------------------------------------------------------
    # MÉTODO PRINCIPAL DEL WIZARD
    # --------------------------------------------------------------
    """
    Método que se ejecuta cuando el usuario pulsa el botón "Confirmar pago"
    dentro del wizard. modifica el estado de la cita a pagada y actualiza el precio total.
    """
    def confirm_payment(self):
        # self puede contener varios registros del wizard
        for wiz in self:
            wiz.cita_id.write({
                'estado':'pagada',
                'precio_total' : wiz.precio_final
            })



