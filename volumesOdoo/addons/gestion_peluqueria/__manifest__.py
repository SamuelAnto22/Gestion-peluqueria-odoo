# -*- coding: utf-8 -*-
{
    # ─────────────────────────────────────────
    # Información principal del módulo
    # ─────────────────────────────────────────
    'name': 'Gestión Peluquería',
    'version': '17.0.1.0.0',
    'summary': 'Sistema de gestión para peluquerías y centros de estética',
    'description': """
        Módulo para gestionar citas, empleados, clientes y servicios
        de una peluquería o centro de estética.

        Funcionalidades:
        - Gestión de citas con estados
        - Control de empleados y sus roles
        - Catálogo de servicios con precio y duración
        - Cobro rápido mediante wizard
        - Generación de ticket PDF
        - Consulta de citas por web
    """,

    # ─────────────────────────────────────────
    # Autor y categoría
    # ─────────────────────────────────────────
    'author': 'Samuel Antolinos',
    'website': 'https://github.com/SamuelAnto22/Gestion-peluqueria-odoo',
    'category': 'Services',
    'license': 'LGPL-3',

    # ─────────────────────────────────────────
    # Dependencias (módulos de Odoo que necesitamos)
    # ─────────────────────────────────────────
    'depends': [
        'base',  # módulo base de Odoo, siempre necesario
        'mail',  # para poder añadir chatter/mensajes en los registros
    ],

    # ─────────────────────────────────────────
    # Archivos que carga el módulo
    # ─────────────────────────────────────────
    'data': [
        # Seguridad - siempre primero
        'security/ir.model.access.csv',

        # Vistas
        'views/salon_client_views.xml',
        'views/salon_employee_views.xml',
        'views/salon_service_views.xml',
        'views/salon_appointment_views.xml',
        'views/salon_menus.xml',

        # Wizard
        'wizard/payment_wizard_views.xml',

        # Reporte PDF
        'report/appointment_report.xml',
    ],

    # ─────────────────────────────────────────
    # Configuración extra
    # ─────────────────────────────────────────
    'installable': True,  # permite instalarlo desde el menú de apps
    'application': True,  # aparece como aplicación principal en el menú
    'auto_install': False,  # no se instala automáticamente
}