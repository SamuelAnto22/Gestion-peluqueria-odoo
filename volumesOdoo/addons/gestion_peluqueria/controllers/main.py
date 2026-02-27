from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/cita/consulta', type='http', auth='none', csrf=False)
    def consulta(self, telefono=None, **kwargs):
        cliente = request.env['salon.client'].sudo().search([
            ('telefono', '=', telefono)
        ], limit=1)
        if not cliente:
            return "No se encontró ningún cliente con ese teléfono"
        citas = request.env['salon.appointment'].sudo().search([
            ('cliente_id', '=', cliente.id)
        ])
        if not citas:
            return f"El cliente {cliente.nombre} no tiene citas registradas"
        resultado = f"<h1>Citas de {cliente.nombre}</h1>"

        for cita in citas:
            resultado += f"""
                <p> Fecha: {cita.fecha}</p>
                <p> Empleado: {cita.empleado_id.nombre}</p>
                <p> Estado: {cita.estado}</p>
                <p> Precio total: {cita.precio_total}€</p>
                <hr/>
            """

        return resultado

