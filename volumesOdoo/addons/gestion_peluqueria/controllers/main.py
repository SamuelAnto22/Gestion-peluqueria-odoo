from odoo import http
from odoo.http import request
from datetime import timedelta


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
            fecha_local = cita.fecha + timedelta(hours=1)  # sumo 1 hora por horario de invierno
            resultado += f"""
                <p> Fecha: {fecha_local}</p>
                <p> Empleado: {cita.empleado_id.nombre}</p>
                <p> Estado: {cita.estado}</p>
                <p> Precio total: {cita.precio_total}€</p>
                <hr/>
            """

        return resultado

