from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

import pandas as pd

STUDY_START = pd.Timestamp("2023-03-01 00:00:00", tz="UTC")
STUDY_END = pd.Timestamp("2023-03-21 23:59:00", tz="UTC")
CRISIS_START = pd.Timestamp("2023-03-10 00:00:00", tz="UTC")
CRISIS_END = pd.Timestamp("2023-03-13 00:00:00", tz="UTC")

PAPER_SHA256 = MappingProxyType(
    {
        "IAQF_Inefficient_Markets_2026.tex": (
            "8f645f8d7d97e0ef0042f4a1d10e206fb9c76be967224a9194e340b778973335"
        ),
        "IAQF_Inefficient_Markets_2026.pdf": (
            "b583b7051b00604af3da42559c287865335ea51b7afb2b590d60ff37f454025b"
        ),
    }
)

EXPECTED_FIGURES = frozenset(
    {
        "fig_arbitrage_after_fees.png",
        "fig_correlation_regime_heatmap.png",
        "fig_cross_exchange_basis.png",
        "fig_dispersion_vs_adjusted_kraken.png",
        "fig_half_life_robustness.png",
        "fig_liquidity_roll_amihud.png",
        "fig_realized_volatility.png",
        "fig_stablecoin_peg.png",
        "fig_stablecoin_substitution_scatter.png",
        "fig_svb_crisis_zoom.png",
        "fig_tail_blowout_kde.png",
        "fig_two_layer_persistence.png",
        "fig_var_irf.png",
        "fig_volume_share.png",
    }
)

EXPECTED_FIGURE_SHA256 = MappingProxyType(
    {
        "fig_arbitrage_after_fees.png": "14230b09124ff705ebd909af200a5a5754707fe6fecd2a26233b59d050238f5e",
        "fig_correlation_regime_heatmap.png": "eb45bbe935ea97d156c3ee4c1e2189b5ebf3333a7b095ac15777dbf22653b524",
        "fig_cross_exchange_basis.png": "eaf5f67d2d8864117d231a8488cb1d66b48944dfe2c10e8819d985c1ff224366",
        "fig_dispersion_vs_adjusted_kraken.png": "63d8b215788f12529520a3e44eea44312f267d6a08b226b866568999c9c92287",
        "fig_half_life_robustness.png": "a1ae8009444d5efb5cec70aca176c986d42749155ae1afcf1ab918172ec4e212",
        "fig_liquidity_roll_amihud.png": "599f22e55025a0e8ba0b84cf2aa29c2bfb55f3bde9d052723962dfb6d9af0824",
        "fig_realized_volatility.png": "6b6ff91a287accc989e8831ff6d2651b69cc28228e7a40a3deebf9ce58e243fe",
        "fig_stablecoin_peg.png": "2c2d3655692b2549e4519f418df396901ef7178ed2a032ffd313eb67f84e00e0",
        "fig_stablecoin_substitution_scatter.png": "5a9b09b9c24a9d9d105fbaaa75752cbeaa640449a2fa65719ebb864b2b1f3b5f",
        "fig_svb_crisis_zoom.png": "07d5d1f87650bd68503541ba5f3f0c38574262cdc8c582e8cfbd0369193ef520",
        "fig_tail_blowout_kde.png": "f8012a0045f93c83270d85f2594ea6d5934342a51abc8291ec44e6f98007776c",
        "fig_two_layer_persistence.png": "7e71f21d8370d1525e0fe362d2a677b4ae8ce6dc1e1c72d9fdd604ad71ec096a",
        "fig_var_irf.png": "3e601e51af3a8911668868f69057a5f2d1dc45b563ba8869a76af73ea474bd3b",
        "fig_volume_share.png": "f3cedca9e16f0a4ab6401c5a423e8f6c40637373a709579d86e24bb562a76ffb",
    }
)

EXPECTED_FIGURE_DIMENSIONS = MappingProxyType(
    {
        "fig_arbitrage_after_fees.png": (1049, 1381),
        "fig_correlation_regime_heatmap.png": (1949, 1787),
        "fig_cross_exchange_basis.png": (1049, 1681),
        "fig_dispersion_vs_adjusted_kraken.png": (1050, 1384),
        "fig_half_life_robustness.png": (1053, 889),
        "fig_liquidity_roll_amihud.png": (1043, 1379),
        "fig_realized_volatility.png": (1055, 934),
        "fig_stablecoin_peg.png": (1049, 1231),
        "fig_stablecoin_substitution_scatter.png": (1048, 1167),
        "fig_svb_crisis_zoom.png": (1043, 1384),
        "fig_tail_blowout_kde.png": (1056, 986),
        "fig_two_layer_persistence.png": (1041, 919),
        "fig_var_irf.png": (1066, 1048),
        "fig_volume_share.png": (1055, 937),
    }
)

EXPECTED_TABLES = frozenset(
    {
        "arbitrage_compact.tex",
        "arbitrage_summary.csv",
        "cointegration_johansen.csv",
        "cointegration_vecm_merged.tex",
        "contagion_intensity.csv",
        "contagion_intensity.tex",
        "data_coverage_core.csv",
        "data_coverage_core.tex",
        "depth_proxy_table.csv",
        "depth_proxy_table.tex",
        "dispersion_adjusted_identity_check.csv",
        "dispersion_adjusted_stats.csv",
        "dispersion_adjusted_stats.tex",
        "distributional_robustness.csv",
        "distributional_robustness.tex",
        "ff_sensitivity_core.csv",
        "genius_counterfactual.csv",
        "genius_counterfactual.tex",
        "granger_causality.csv",
        "granger_causality_fdr.csv",
        "hac_headline_metrics.csv",
        "half_life_robustness.csv",
        "half_life_sanity_grid.csv",
        "hasbrouck_is.csv",
        "liquidity_spread_table.tex",
        "ou_basis_stats.csv",
        "peg_recovery_thresholds.csv",
        "price_discovery_metrics.csv",
        "realized_vol_headline.csv",
        "realized_vol_regime_means.csv",
        "regression_hac.tex",
        "regression_results.txt",
        "regression_usdc.txt",
        "regression_usdt.txt",
        "volume_share_pair_regime.csv",
        "volume_share_quote_regime.csv",
    }
)


@dataclass(frozen=True)
class RepoPaths:
    root: Path
    raw: Path
    processed: Path
    tables: Path
    figures: Path
    paper_tex: Path
    paper_pdf: Path

    @classmethod
    def from_root(cls, root: Path) -> RepoPaths:
        root = Path(root)
        return cls(
            root=root,
            raw=root / "data_raw",
            processed=root / "data_processed",
            tables=root / "tables",
            figures=root / "figures_col",
            paper_tex=root / "IAQF_Inefficient_Markets_2026.tex",
            paper_pdf=root / "IAQF_Inefficient_Markets_2026.pdf",
        )
