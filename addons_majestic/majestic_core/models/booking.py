# -*- coding: utf-8 -*-
from email.policy import default
from odoo import api, fields, models
from ..utils.common import TICKET_PASSENGER_CATEGORY, PAYMENT_METHOD


class MasterBooking(models.Model):
    _name = 'booking.master'
    _description = 'Master Booking Data'
    _order = 'id desc'

    ticket_id = fields.Many2one('ticket.master', string='Ticket Master')
    ticket_number = fields.Char(
        string='Ticket Number',
        related='ticket_id.ticket_code')
    ticket_departure = fields.Selection(
        related='ticket_id.place_origin',
        string='Ticket Departure')
    ticket_destination = fields.Selection(
        related='ticket_id.place_destination',
        string='Ticket Destination')
    ticket_price = fields.Float(
        related='ticket_id.ticket_price',
        string='Ticket Price')
    departure_date = fields.Date(string='Booking Departure Date')
    passenger_name = fields.Char(string='Passenger Name')
    passenger_category = fields.Selection(
        TICKET_PASSENGER_CATEGORY,
        string='Passenger Category')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    payment_method = fields.Selection(
        PAYMENT_METHOD,
        string='Payment Method')
    is_confirmed = fields.Boolean(string='Confirmed', default=False)

    def confirm(self):
        self.write({
            'is_confirmed': True
        })

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
