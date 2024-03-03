# -*- coding: utf-8 -*-
from odoo import fields, models

class Registrotiempo(models.Model):
		# El nombre técnico del modelo
		# Usualmente en formato 'nombre_del_modulo.nombre_del_modelo' 
    _name = "proyectosplus.registro_tiempo"  
		# Una descripción para el modelo
    _description = 'Registro de tiempo' 
		# Se define un primer campo de ejemplo llamado name 
		# 'string' es opcional y define el nombre del campo en la vista
    
    task_id = fields.Many2one('proyectos.tarea', string="Tarea Asociada", required=True)
    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    date = fields.Date(string='Fecha')
    hours = fields.Float(string='Horas')
    # Opcionalmente, si decides agregar un campo de descripción adicional
    description = fields.Text(string='Descripción Detallada')