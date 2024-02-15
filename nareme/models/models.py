from odoo import models, fields, api

class NaremeEmpresaContratadora(models.Model):
    _name = 'empresa_contratadora'
    _description = 'Nareme Empresa Contratadora'

    name = fields.Char(string="Nombre de la empresa")
    proyectos = fields.One2many("project.project", "name", string="Proyectos")

    @api.model
    def create(self, vals):
        registro = super().create(vals)
        self.env['registro_empresa'].create({
            'usuario': self.env.uid,
            'empresa': registro.id,
            'accion': 'creacion',
        })
        return registro

    def write(self, vals):
        resultado = super().write(vals)
        if resultado:
            self.env['registro_empresa'].create({
                'usuario': self.env.uid,
                'empresa': self.id,
                'accion': 'modificacion',
            })
        return resultado


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

class RegistroEmpresa(models.Model):
    _name = 'registro_empresa'
    _description = 'Registro de Creación y Modificación de Empresas'

    usuario = fields.Many2one('res.users', string="Usuario")
    empresa = fields.Many2one('empresa_contratadora', string="Empresa")
    fecha_hora = fields.Datetime(string="Fecha/Hora", default=fields.Datetime.now)
    accion = fields.Selection([('creacion', 'Creación'), ('modificacion', 'Modificación')], string="Acción")

