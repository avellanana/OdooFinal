# -*- coding: utf-8 -*-
from odoo import fields, models

class Proyecto(models.Model):
		# El nombre técnico del modelo
		# Usualmente en formato 'nombre_del_modulo.nombre_del_modelo' 
    _name = "proyectos.proyecto"  
		# Una descripción para el modelo
    _description = 'Descripcion del modelo Proyecto, dentro del módulo Proyectos' 
		# Se define un primer campo de ejemplo llamado name 
		# 'string' es opcional y define el nombre del campo en la vista
    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    start_date = fields.Date(string='Fecha de inicio')
    end_date = fields.Date(string='Fecha de fin')
    manager_id = fields.Many2one('res.users', string='Responsable')
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en progreso', 'En progreso'),
        ('completado', 'Completado')
    ], string='Estado del proyecto')
    user_ids = fields.Many2many('res.users', string='Usuarios asignados')
    task_ids = fields.One2many('proyectos.tarea', 'project_id', string='Tareas')
    budget = fields.Float(string='Presupuesto')
    priority = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string='Prioridad')