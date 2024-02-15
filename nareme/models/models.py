from odoo import models, fields, api

class NaremeEmpresaContratadora(models.Model):
    _name = 'empresa_contratadora'
    _description = 'Nareme Empresa Contratadora'

    name = fields.Char(string="Nombre de la empresa")
    proyectos = fields.One2many("project.project", "name", string="Proyectos")

class NaremeProyectos(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresa_contratadora = fields.Many2one("empresa_contratadora", string="Empresas a las que pertenece el proyecto")
    tareas = fields.One2many("project.task", "project_id", string="Tareas")

    ultima_tarea_fecha = fields.Date(string="Última Tarea", compute="_compute_ultima_tarea_fecha", store=True, readonly=True)

    @api.depends('tareas.date_deadline')
    def _compute_ultima_tarea_fecha(self):
        for proyecto in self:
            ultima_tarea = proyecto.tareas.sorted(key=lambda x: x.date_deadline, reverse=True)[:1]
            proyecto.ultima_tarea_fecha = ultima_tarea.date_deadline if ultima_tarea else None


   