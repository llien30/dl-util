"""
Copyright (c) 2021 Mana Masuda
This software is released under the MIT License, see LICENSE.
"""

import torch.nn as nn
from torch import optim


def get_model_update_criterion(
    model: nn.Module,
    optimizer_name: str,
    learning_rate: float,
    scheduler_name: str = "N/A",
    gamma: float = 0,
    step: int = None,
):
    assert optimizer_name in [
        "Adam",
        "SGD",
    ], f"ERROR: There is no optimizer named `{optimizer_name}`"
    assert scheduler_name in [
        "N/A",
        "ExponentialLR",
        "StepLR",
    ], f"ERROR: There is no scheduler named `{scheduler_name}`"
    if scheduler_name == "StepLR":
        assert (
            step is not None
        ), "ERROR: To use the Step scheduler, you need to specify step."

    if optimizer_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    elif optimizer_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    if scheduler_name == "ExponentialLR":
        scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=gamma)
    if scheduler_name == "StepLR":
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=step, gamma=gamma)

    if scheduler_name == "N/A":
        return optimizer
    else:
        return optimizer, scheduler
