# k attendance draft ma hoy and student ne terminate karvu hoy to warning aave 
# k aa attendance proceed karo
# See LICENSE file for full copyright and licensing details.


from odoo import models, _
from odoo.exceptions import ValidationError


class TerminateReasonFees(models.TransientModel):
    _inherit = 'terminate.reason'

    def save_terminate(self):
        '''Override method to raise warning when process of student Attendance is
        remaining when student is terminated'''
        student = self._context.get('active_id')
        student_obj = self.env['student.student'].browse(student)
        school_attendance = self.env['studentleave.request'].\
            search([('student_id', '=', student_obj.id),
                    ('state', 'in', ['toapprove', 'reject'])])
        if school_attendance:
            raise ValidationError(_('''You cannot terminate student , first you have to process of student attendance'''))
        return super(TerminateReasonFees, self).save_terminate()
