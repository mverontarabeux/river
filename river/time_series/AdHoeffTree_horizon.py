
from river import time_series
from river import tree
from river.tree.splitter import Splitter
from river import base

__all__ = ["Hoeffding_horizon"]


class AdaptHoeffdingHorizon(tree.HoeffdingTreeRegressor, time_series.base.Forecaster):
    """

    Parameters
    ----------
    time_series : _type_
        _description_
    """
    def __init__(
        self,
        grace_period: int = 200,
        max_depth: int = None,
        delta: float = 1e-7,
        tau: float = 0.05,
        leaf_prediction: str = "adaptive",
        leaf_model: base.Regressor = None,
        model_selector_decay: float = 0.95,
        nominal_attributes: list = None,
        splitter: Splitter = None,
        min_samples_split: int = 5,
        bootstrap_sampling: bool = True,
        drift_window_threshold: int = 300,
        switch_significance: float = 0.05,
        binary_split: bool = False,
        max_size: float = 500.0,
        memory_estimate_period: int = 1000000,
        stop_mem_management: bool = False,
        remove_poor_attrs: bool = False,
        merit_preprune: bool = True,
        seed: int = None,
    ):
        super(tree.HoeffdingTreeRegressor, self).__init__(
            grace_period=grace_period,
            max_depth=max_depth,
            delta=delta,
            tau=tau,
            leaf_prediction=leaf_prediction,
            leaf_model=leaf_model,
            model_selector_decay=model_selector_decay,
            nominal_attributes=nominal_attributes,
            splitter=splitter,
            min_samples_split=min_samples_split,
            bootstrap_sampling=bootstrap_sampling,
            drift_window_threshold=drift_window_threshold,
            switch_significance=switch_significance,
            binary_split=binary_split,
            max_size=max_size,
            memory_estimate_period=memory_estimate_period,
            stop_mem_management=stop_mem_management,
            remove_poor_attrs=remove_poor_attrs,
            merit_preprune=merit_preprune,
            seed=seed
        )

    def forecast(self, horizon, xs=None):
        last_pred = xs
        forecasted_horizon = []
        for h in range(horizon):
            forecasted_horizon.append(self.predict_one(last_pred))
            last_pred = forecasted_horizon[-1]

        return forecasted_horizon
