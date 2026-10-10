"""Export lightweight QuietAlert UI metadata from a campaign metrics CSV.

This keeps the demo contract simple: the production pipeline can replace this
module with the existing ps04 package while the UI continues to consume the
same public/data/*.json files.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "data"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="?", default=str(OUT / "daily_campaign_metrics.csv"))
    args = parser.parse_args()
    frame = pd.read_csv(args.csv)
    campaign_col = "campaign_id" if "campaign_id" in frame else "campaign"
    name_col = "campaign_name" if "campaign_name" in frame else campaign_col
    meta = []
    for cid, group in frame.groupby(campaign_col, sort=True):
        first = group.iloc[0]
        meta.append({
            "campaign_id": str(cid),
            "campaign_name": str(first[name_col]),
            "channel": str(first.get("channel", "Unknown")),
            "vertical": str(first.get("vertical", "ecommerce")),
            "landing_page_group": str(first.get("landing_page_group", "Unknown")),
            "rows": int(len(group)),
        })
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "campaigns.json").write_text(json.dumps(meta, indent=2) + "\n")
    summary = {
        "dataset": Path(args.csv).name,
        "rows": int(len(frame)),
        "campaigns": int(frame[campaign_col].nunique()),
        "days": int(frame["date"].nunique()) if "date" in frame else None,
        "date_start": str(frame["date"].min()) if "date" in frame else None,
        "date_end": str(frame["date"].max()) if "date" in frame else None,
        "label_free": True,
    }
    (OUT / "summary_from_csv.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"exported {summary['rows']} rows / {summary['campaigns']} campaigns to {OUT}")


if __name__ == "__main__":
    main()
