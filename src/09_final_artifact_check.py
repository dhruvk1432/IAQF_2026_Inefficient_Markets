"""
Verify final-paper artifacts against the February 27 final-column source.

The paper text may be edited for clarity, so this check treats captions as
manuscript prose. It verifies byte-identical referenced PNGs and caption-free
table bodies/values from IAQF_Inefficient_Markets_2026.tex.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_PATH = os.path.join(ROOT, "IAQF_Inefficient_Markets_2026.tex")

SOURCE_COMMIT = "c819e1f9aabf4457ed876d7aa7ab376166bec4ab"

FIG_HASHES = {
    "figures_col/fig_stablecoin_peg.png": "2c2d3655692b2549e4519f418df396901ef7178ed2a032ffd313eb67f84e00e0",
    "figures_col/fig_dispersion_vs_adjusted_kraken.png": "63d8b215788f12529520a3e44eea44312f267d6a08b226b866568999c9c92287",
    "figures_col/fig_stablecoin_substitution_scatter.png": "5a9b09b9c24a9d9d105fbaaa75752cbeaa640449a2fa65719ebb864b2b1f3b5f",
    "figures_col/fig_half_life_robustness.png": "a1ae8009444d5efb5cec70aca176c986d42749155ae1afcf1ab918172ec4e212",
    "figures_col/fig_two_layer_persistence.png": "7e71f21d8370d1525e0fe362d2a677b4ae8ce6dc1e1c72d9fdd604ad71ec096a",
    "figures_col/fig_svb_crisis_zoom.png": "07d5d1f87650bd68503541ba5f3f0c38574262cdc8c582e8cfbd0369193ef520",
    "figures_col/fig_cross_exchange_basis.png": "eaf5f67d2d8864117d231a8488cb1d66b48944dfe2c10e8819d985c1ff224366",
    "figures_col/fig_liquidity_roll_amihud.png": "599f22e55025a0e8ba0b84cf2aa29c2bfb55f3bde9d052723962dfb6d9af0824",
    "figures_col/fig_volume_share.png": "f3cedca9e16f0a4ab6401c5a423e8f6c40637373a709579d86e24bb562a76ffb",
    "figures_col/fig_realized_volatility.png": "6b6ff91a287accc989e8831ff6d2651b69cc28228e7a40a3deebf9ce58e243fe",
    "figures_col/fig_tail_blowout_kde.png": "f8012a0045f93c83270d85f2594ea6d5934342a51abc8291ec44e6f98007776c",
    "figures_col/fig_correlation_regime_heatmap.png": "eb45bbe935ea97d156c3ee4c1e2189b5ebf3333a7b095ac15777dbf22653b524",
    "figures_col/fig_var_irf.png": "3e601e51af3a8911668868f69057a5f2d1dc45b563ba8869a76af73ea474bd3b",
    "figures_col/fig_arbitrage_after_fees.png": "14230b09124ff705ebd909af200a5a5754707fe6fecd2a26233b59d050238f5e",
}

TABLE_BODY_HASHES = {
    "tab:arb": "af97f28c8c86740bd2f63b5a784f7f4eafd11f40b3d7f3098f132c22b6a33777",
    "tab:coint_vecm": "0303a92f95658087ce973ef55016a1348893b8704bdf0705759f038c284f6b8b",
    "tab:contagion": "4422ff1238ccb725646c4d2442c41ae714ad729e8a6b8e9d4309ab20a7c06c84",
    "tab:data_coverage": "2278fd40d25b32f30b7306d486b48123b0b8db33cc9ccf97d43e5bd9511e9472",
    "tab:depth_proxy": "adafcc9cbe92e2403c0c19f4be3a4916b2e0642d63036ba25e0432944a969656",
    "tab:dispersion_vs_adjusted": "1fcaca1410242f7a686d3bca83a0e56daaab50558b74601c6578ee0b0424472f",
    "tab:dist_robust": "9e310131e852e9b8d4e02069c402b03266c06cd804d83af368253039d3d40668",
    "tab:genius_cf": "fc28385909d5e42e32a63ec99a3f3ee18caa1777a0255e2ceb45e8642c701a7f",
    "tab:liquidity_spread": "2f21c85dd4fc71b10ff7d2966fe5fa462a859e44920fa403fd7a1f89a44b9887",
    "tab:regression_hac": "1dfa1909b717e67046b3d84a2624d744245513243fecc2c1d0875d7545ccdfb6",
}


def sha256_bytes(path: str) -> str:
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def table_blocks(tex: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    for match in re.finditer(r"\\begin\{table\}.*?\\end\{table\}", tex, flags=re.S):
        block = match.group(0)
        label = re.search(r"\\label\{([^}]+)\}", block)
        if label:
            blocks[label.group(1)] = block
    return blocks


def table_body(block: str) -> str:
    block = block.replace(r"\begin{table}[H]", r"\begin{table}")
    lines = []
    for line in block.strip().splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith(r"\caption"):
            lines.append(line.rstrip())
    return "\n".join(lines)


def main() -> int:
    with open(TEX_PATH, "r", encoding="utf-8") as handle:
        tex = handle.read()

    errors: list[str] = []
    referenced_figures = re.findall(
        r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex
    )
    if sorted(referenced_figures) != sorted(FIG_HASHES):
        errors.append("Referenced figure set differs from February 27 final-column paper.")

    for rel_path, expected_hash in FIG_HASHES.items():
        path = os.path.join(ROOT, rel_path)
        if not os.path.exists(path):
            errors.append(f"Missing final-paper figure: {rel_path}")
            continue
        actual_hash = sha256_bytes(path)
        if actual_hash != expected_hash:
            errors.append(
                f"Figure hash mismatch for {rel_path}: {actual_hash} != {expected_hash}"
            )

    blocks = table_blocks(tex)
    if sorted(blocks) != sorted(TABLE_BODY_HASHES):
        errors.append("Final-column table label set differs from February 27 paper.")

    for label, expected_hash in TABLE_BODY_HASHES.items():
        block = blocks.get(label)
        if block is None:
            errors.append(f"Missing final-paper table label: {label}")
            continue
        actual_hash = sha256_text(table_body(block))
        if actual_hash != expected_hash:
            errors.append(
                f"Table body mismatch for {label}: {actual_hash} != {expected_hash}"
            )

    print("Final artifact integrity check")
    print(f"  Source commit: {SOURCE_COMMIT}")
    print(f"  Figure artifacts checked: {len(FIG_HASHES)}")
    print(f"  Table bodies checked: {len(TABLE_BODY_HASHES)}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Final artifact integrity check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
