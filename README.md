#Gestión Peluquería - Módulo Odoo

Módulo de gestión completo para una peluquería / centro de estética desarrollado en Odoo 16.
Incluye gestión de citas, empleados, servicios y cobro rápido.

---

## 📋 Requisitos técnicos cubiertos

| Requisito | Descripción | Archivo |
|-----------|-------------|---------|
| a) 4 Vistas | Formulario, lista, kanban y calendar de citas | `views/` |
| b) 4 Métodos | Campos computados (precio total, duración) y restricciones de rol y horario | `models/salon_appointment.py` |
| c) Search | Filtro y ordenación de citas por estado, empleado y fecha | `views/salon_appointment_views.xml` |
| d) 2 Clases | Cita ↔ Empleado, Servicio (Many2One / Many2Many) | `models/` |
| e) Wizard | Cobro rápido con método de pago y descuento opcional | `wizard/` |
| f) Vistas especiales | Colores por estado, líneas editables, widgets de fecha y monetario | `views/salon_appointment_views.xml` |
| g) Report PDF | Ticket de caja con desglose de servicios y total | `report/appointment_report.xml` |
| h) Web Controller | Consulta del estado de la cita introduciendo el teléfono del cliente | `controllers/main.py` |

---

##Estructura del proyecto

```
gestion_peluqueria/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py                      # Requisito h - Web Controller
├── models/
│   ├── __init__.py
│   ├── salon_client.py              # Modelo Cliente
│   ├── salon_employee.py            # Modelo Empleado / Estilista
│   ├── salon_service.py             # Modelo Servicio (Corte, Tinte...)
│   └── salon_appointment.py        # Modelo Cita + métodos y restricciones
├── report/
│   └── appointment_report.xml      # Requisito g - Ticket PDF
├── security/
│   └── ir.model.access.csv         # Permisos de acceso
├── views/
│   ├── salon_client_views.xml
│   ├── salon_employee_views.xml
│   ├── salon_service_views.xml
│   ├── salon_appointment_views.xml  # Vistas principales + search + colores
│   └── salon_menus.xml
└── wizard/
    ├── __init__.py
    ├── payment_wizard.py            # Requisito e - Lógica de cobro
    └── payment_wizard_views.xml     # Requisito e - Ventana emergente
```

---

##Funcionalidades principales

- **Gestión de citas**: estados Pendiente → Confirmada → En curso → Pagada / No presentado
- **Restricción de roles**: no se puede asignar un servicio de Manicura a un empleado con rol exclusivo de Peluquero
- **Precio y duración automáticos**: campos computados que suman los valores de todos los servicios seleccionados
- **Validación de horario**: no se puede crear una cita si el empleado tiene el día libre
- **Cobro rápido**: wizard que permite elegir método de pago (Efectivo / Tarjeta) y aplicar un descuento antes de marcar la cita como Pagada
- **Ticket PDF**: recibo imprimible con el desglose de servicios y el total final
- **Consulta web**: endpoint público donde el cliente puede consultar el estado de su cita con su número de teléfono

---

##Capturas de pantalla

### Vista Kanban de Citas
![Kanban](docs/screenshots/01_vista_kanban.png)

### Formulario de Cita con líneas editables
![Formulario](docs/screenshots/02_formulario_cita.png)

### Wizard de Cobro Rápido
![Wizard](docs/screenshots/03_wizard_cobro.png)

### Ticket PDF generado
![Report](docs/screenshots/04_report_pdf.png)

### Web Controller - Consulta por teléfono
![Controller](docs/screenshots/05_web_controller.png)

---

##Instalación

1. Clona el repositorio en tu máquina local
```bash
git clone https://github.com/SamuelAnto22/Gestion-peluqueria-odoo
```

2. Copia la carpeta `gestion_peluqueria` dentro del directorio `addons` de tu instalación de Odoo

3. Activa el **modo desarrollador** en Odoo (Ajustes → Activar modo desarrollador)

4. Ve a **Aplicaciones**, haz clic en **Actualizar lista de aplicaciones** y busca `Gestión Peluquería`

5. Instala el módulo

---

## 🛠️ Tecnologías utilizadas

- **Odoo 16** - Framework ERP
- **Python 3.10** - Lógica de negocio y modelos
- **XML** - Definición de vistas y reportes
- **QWeb** - Motor de plantillas para el PDF
- **Docker** - Entorno de desarrollo

---

## 👤 Autor

**Samuel Cordova Rojas** · CFGS · IES Benigasló  
Módulo desarrollado como Proyecto Modular del módulo *Sistemes de Gestió Empresarial*
