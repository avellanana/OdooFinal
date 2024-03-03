# -*- coding: utf-8 -*-
from odoo import fields, models

class Tarea(models.Model):
		# El nombre técnico del modelo
		# Usualmente en formato 'nombre_del_modulo.nombre_del_modelo' 
    _name = "proyectos.tarea"  
		# Una descripción para el modelo
    _description = 'Descripcion del modelo Tarea, dentro del módulo Proyectos' 
		# Se define un primer campo de ejemplo llamado name 
		# 'string' es opcional y define el nombre del campo en la vista
    name = fields.Char(string='Nombre')  
    description = fields.Text(string='Descripción')
    start_date = fields.Date(string='Fecha de inicio')
    due_date = fields.Date(string='Fecha de vencimiento')
    priority = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string='Prioridad')
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en progreso', 'En progreso'),
        ('completado', 'Completado')
    ], string='Estado')
    project_id = fields.Many2one('proyectos.proyecto', string='Proyecto')
    assigned_user_ids = fields.Many2many('res.users', string='Asignado a')
    estimated_hours = fields.Float(string='Horas estimadas')
    spent_hours = fields.Float(string='Horas trabajadas')