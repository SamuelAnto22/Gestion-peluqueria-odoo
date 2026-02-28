from odoo import http
from odoo.http import request
from datetime import timedelta


class Main(http.Controller):
    """
      Controlador principal para endpoints públicos del módulo de gestión de peluquería.
      Proporciona funcionalidades de consulta sin necesidad de autenticación.
      """

    @http.route('/cita/consulta', type='http', auth='none', csrf=False)
    def consulta(self, telefono=None, **kwargs):

        #Endpoint público para consultar las citas de un cliente por teléfono.
        #Uso:
        # localhost:8069/cita/consulta?telefono = 123456789

        if not telefono:
            return "Por favor, proporcione un número de teléfono"

        # Buscar el cliente en el modelo 'salon.client' usando el número de teléfono
        # Se usa sudo() para ejecutar sin restricciones de permisos
        cliente = request.env['salon.client'].sudo().search([
            ('telefono', '=', telefono)
        ], limit=1)

        if not cliente:
            return "No se encontró ningún cliente con ese teléfono"

        # Obtener todas las citas asociadas al cliente encontrado
        # Se busca en el modelo 'salon.appointment' por el ID del cliente
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

