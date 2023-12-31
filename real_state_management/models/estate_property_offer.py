from odoo import api, models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offers"

#   name = fields.Char()
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline")

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for rec in self:
            # rec.date_deadline = fields.Date.add(rec.create_date, days=rec.validity) if rec.create_date else False
            rec.date_deadline = False # Complete

    def refuse_offer(self):
        """ Permite marcar la oferta como rechazada """
        self.state = 'refused'

"""     @api.onchange('date_deadline')
    def _inverse_date_deadline(self):
        for rec in self:
            rec.validity = (rec.date_deadline - rec.create_date.date()).days if rec.create_date else 7 """
