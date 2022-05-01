# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from ..utils.common import TICKET_CLASS, TICKET_LOCATIONS, TICKET_PASSENGER_CATEGORY


class TicketMaster(models.Model):
    _name = 'ticket.master'
    _description = 'Master Ticket Data'
    _order = 'id desc'

    ticket_code = fields.Char(string='Ticket Serial Number')
    place_origin = fields.Selection(
        TICKET_LOCATIONS,
        string='Ticket Locations Origin',
        default='manado')
    place_destination = fields.Selection(
        TICKET_LOCATIONS,
        string='Ticket Locations Destination')
    passenger_category = fields.Selection(
        TICKET_PASSENGER_CATEGORY,
        string='Passenger Category')
    ticket_class = fields.Selection(
        TICKET_CLASS,
        string='Ticket Classes')
    ticket_price = fields.Float(string='Ticket Price')

    @api.model
    def check(self, payload={}) -> dict:
        """ To check if ticket is available
            Args:
                payload: Dictionary of data
                    origin : Place of departure <string>
                    destination: Place of destination <string>
                    passenger_category: Category of passengers <list> ['anak', 'dewasa']
                    ticket_class : Ticket Class <string>
            Returns:
                List of ticket available
        """
        domain: list = [
            ('place_origin', 'ilike', payload.get('origin')),
            ('place_destination', 'ilike', payload.get('destination')),
            ('passenger_category', 'in', payload.get('passenger_category'))
        ]
        if not payload.get('origin'):
            raise ValidationError('Tempat Lokasi keberangkatan harus dipilih')
        if not payload.get('destination'):
            raise ValidationError('Tempat Lokasi tujuan harus dipilih')
        if not payload.get('passenger_category'):
            raise ValidationError('Jumlah penumpang dewasa atau anak harus dipilih')
        if payload.get('ticket_class'):
            domain.append(('ticket_class', '=', payload.get('ticket_class')),)

        return self.search_read(
            domain=domain,
            fields=[
            "ticket_code",
            "place_origin",
            "place_destination",
            "passenger_category",
            "ticket_class",
            "ticket_price"])

# class MasterOrderTicket(models.Model):
#     _name = "ticket.master"
#     _description = "Master Ticket Data"
#     _order = 'id desc'

#     ticket_number_reference = fields.Char(
#         string='Ticket Number Reference')
#     origin_id = fields.Many2one()
#     destination_id = fields.Many2one()
#     number_of_adult_passenger = fields.Integer(
#         string='Number of Adult Passenger')
#     number_of_child_passenger = fields.Integer(
#         string='Number of Child Passenger')
#     payment_method = fields.Selection([
#         ('cash', 'Cash'),
#         ('transfer', 'Transfer')
#     ], string='Payment Method')
#     seat_type = fields.Selection([
#         ('reguler', 'Regulaer'),
#         ('transfer', 'Transfer')
#     ], string='Payment Method')

#     ticket_slip_ids = fields.One2many(
#         'ticket.master.slip',
#         'ticket_master_id',
#         string='List of Tickets')

# class MasterOrderLineData(models.Model):
#     _name = "ticket.master.slip"
#     _description = "Slip Ticket Master"

#     ticket_master_id = fields.Many2one(
#         'ticket.master',
#         string='Ticket Master')
#     name = fields.Char(string='Person Name')
#     category = fields.Selection([
#         ('adult', 'Adult'),
#         ('child', 'Child'),
#     ], string='Category')
#     email = fields.Char(string='Email')
#     phone = fields.Char(string='Phone Number')

    
