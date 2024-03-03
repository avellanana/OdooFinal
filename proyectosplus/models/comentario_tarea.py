# -*- coding: utf-8 -*-
from odoo import fields, models

class Comentariotarea(models.Model):
		# El nombre técnico del modelo
		# Usualmente en formato 'nombre_del_modulo.nombre_del_modelo' 
    _name = "proyectosplus.comentario_tarea"  
		# Una descripción para el modelo
    _description = 'Este modelo facilita la comunicación y seguimiento de discusiones relacionadas con las tareas.' 
    author_id = fields.Many2one('res.users', string='Autor', required=True)
    task_id = fields.Many2one('proyectos.tarea', string="Tarea Asociada")
    comment = fields.Text(string='Comentario', required=True)
    timestamp = fields.Datetime(string='Fecha/Hora', default=fields.Datetime.now, required=True)
  
class TareaPlus(models.Model):
    _inherit = 'proyectos.tarea'
    
    registro_tiempo_ids = fields.One2many('proyectosplus.registro_tiempo', 'task_id', string='Registros')
    comentario_tarea_ids = fields.One2many('proyectosplus.comentario_tarea', 'task_id', string='Comentarios de la Tarea')