"""This module implements the ClockGate."""
from __future__ import annotations

import numpy as np
import numpy.typing as npt

from bqskit.ir.gates.quditgate import QuditGate
from bqskit.qis.unitary.unitary import RealVector
from bqskit.qis.unitary.unitarymatrix import UnitaryMatrix
from bqskit.utils.typing import is_integer


class ClockGate(QuditGate):
    """
    The one-qudit clock (Z) gate. This is a Weyl-Heisenberg gate.

    The clock gate is given by the following formula:

    .. math::
        \\begin{equation}
            Z = \\sum_a \\exp(2\\pi ia/d) |a><a|
        \\end{equation}

    where d is the number of levels (2 levels is a qubit,
    3 levels is a qutrit, etc.)

    __init__() arguments:
        num_levels : int
            Number of levels in each qudit (d).
    """

    _num_qudits = 1
    _num_params = 0

    def __init__(self, num_levels: int):
        if num_levels < 2 or not is_integer(num_levels):
            raise ValueError(
                'Clock Gate num_levels must be a postive integer greater than or equal to 2.',
            )
        self.num_levels = num_levels

    def get_unitary(self) -> UnitaryMatrix:
        """Return the unitary for this gate, see :class:`Unitary` for more."""

        diags = np.zeros(self.num_levels, dtype=complex)
        for i in range(self.num_levels):
            diags[i] = np.exp(2j * np.pi * i / self.num_levels)
        u_mat = UnitaryMatrix(np.diag(diags), self.radixes)
        return u_mat

    def get_grad(self) -> npt.NDArray[np.complex128]:
        return np.array([])
