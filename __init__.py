# This file is part project_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .timesheet import *
from .work import *


def register():
    Pool.register(
        TimesheetWork,
        TimesheetLine,
        Work,
        module='project_timesheet', type_='model')
    Pool.register(
        WorkOpenTimesheetLine,
        module='project_timesheet', type_='wizard')
