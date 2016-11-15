#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" The interface for a dialog that displays a message. """


# Enthought library imports.
from builtins import object
from traits.api import Enum, Unicode

# Local imports.
from pyface.i_dialog import IDialog


class IMessageDialog(IDialog):
    """ The interface for a dialog that displays a message. """

    #### 'IMessageDialog' interface ###########################################

    #: The message to display in the dialog.
    message = Unicode

    #: More information about the message to be displayed.
    informative = Unicode

    #: More detail about the message to be displayed in the dialog.
    detail = Unicode

    #: The severity of the message.
    severity = Enum('information', 'warning', 'error')


class MMessageDialog(object):
    """ The mixin class that contains common code for toolkit specific
    implementations of the IMessageDialog interface.
    """
