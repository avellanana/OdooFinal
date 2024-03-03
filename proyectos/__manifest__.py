# -*- coding:utf-8 -*-

{
    'name': 'Proyecto',
    'version': '1.0',
    'depends': ['base'],
    'author': 'ana',
    'category': 'CatProyecto',
    'description': 'Descripción larga del módulo proyectos',
    'summary': 'Descripción corta del módulo proyectos',
    'data': [
        'views/menu.xml',
        'views/proyecto_form.xml',
        'views/tareas_form.xml',
        'report/hola_mundo_report.xml',
        'views/tareas_kanban.xml',
    ],
    'assets': {'web.assets_backend': [
            'proyectos/static/src/css/tareas_kanban.css',
        ],
    },
    'demo': [
        # Datos de demostración (opcional)
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}