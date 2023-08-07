"""This module implements the CRYGate."""  # TODO convert to qudit
from __future__ import annotations

from bqskit.ir.gates.composed import ControlledGate
from bqskit.ir.gates.parameterized.ry import RYGate
from typing import Sequence


class CRYGate(ControlledGate):
    """
    A gate representing a controlled X rotation for qudits.

    This is equivalent to a controlled rotation by the Y Pauli Gate in the subspace of 2 levels
    """

    _num_qudits = 2
    _num_params = 1
    _qasm_name = 'cry'

    def __init__(
        self, 
        num_controls: int=1, 
        num_levels: Sequence[int] | int = 2, 
        level_1: int=0,
        level_2: int=1,
        level_of_each_control: Sequence[Sequence[int]] | None = None
    ) -> None:
        """Builds the CRXGate, see :class:`ControlledGate` for more information."""     
        super().__init__(
            RYGate(num_levels=num_levels, level_1=level_1, level_2=level_2),
            num_controls=num_controls,
            num_levels=num_levels,
            level_of_each_control = level_of_each_control
        )