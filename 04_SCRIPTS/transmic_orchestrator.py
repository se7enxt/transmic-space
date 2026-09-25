#!/usr/bin/env python3
"""
Transmic Space Orchestrator Manager CLI (TRANSMIC-ORCHESTRATOR)
Maintains living context, evolutionary ledger, catalog state, and communication staging.
"""

import sys
import os
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
WORKSPACE_ROOT = PROJECT_DIR.parent.parent
CONTEXT_FILE = PROJECT_DIR / "00_CONTEXT" / "context_state.json"
WA_STAGING_FILE = PROJECT_DIR / "05_COMMUNICATIONS" / "wa_staging.json"
CATALOG_DB = PROJECT_DIR / "01_DATABASE" / "transmic_space_catalog.json"


def load_json(filepath: Path) -> dict:
    if not filepath.exists():
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath: Path, data: dict) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def cmd_status(args):
    """Display rich status of Transmic Space Orchestrator and Context."""
    state = load_json(CONTEXT_FILE)
    if not state:
        print("❌ Error: context_state.json not found!")
        sys.exit(1)

    orch = state.get("orchestrator", {})
    entity = state.get("entity_identity", {})
    benchmarks = state.get("catalog_benchmarks", {})
    phase = state.get("active_phase", {})
    comms = state.get("communication_channels", {})
    ledger = state.get("evolution_ledger", [])

    print("\n" + "=" * 76)
    print(" 🔮 TRANSMIC SPACE ORCHESTRATOR MANAGER (A Lab for Magic)")
    print("=" * 76)
    print(f" Status:        [{orch.get('status', 'UNKNOWN')}] v{orch.get('version', '1.0')} ({orch.get('mode', 'AUTONOMOUS')})")
    print(f" Last Updated:  {orch.get('last_updated', 'N/A')}")
    print(f" Entity:        {entity.get('name', 'Transmic Space')} • {entity.get('brand_tagline', '')}")
    print(f" Identifiers:   IPI: {entity.get('ipi_entity_number', 'N/A')} | Share: {entity.get('statutory_publishing_share', 'N/A')}")
    print(f" YouTube:       {entity.get('official_youtube_channel', 'N/A')}")
    print(f" Collaborator:  {entity.get('associated_creator', 'N/A')}")
    print("-" * 76)
    print(f" 🎯 ACTIVE PHASE: {phase.get('phase_name', 'N/A')} ({phase.get('status', 'N/A')})")
    for d in phase.get("active_directives", []):
        print(f"   • {d}")
    print("-" * 76)
    print(f" 🎵 CATALOG BENCHMARKS:")
    print(f"   • YouTube Video Productions: {benchmarks.get('total_youtube_productions', 0)}")
    print(f"   • IPRS Registered Works:     {benchmarks.get('total_iprs_registered_works', 0)}")
    flagship = benchmarks.get("flagship_work", {})
    print(f"   • Flagship Release:          {flagship.get('title', 'N/A')} ({flagship.get('bengali_title', '')})")
    print(f"     - Canonical Genesis:       {flagship.get('canonical_release_genesis', 'N/A')}")
    print(f"     - ISRC: {flagship.get('track_isrc', 'N/A')} | UPC: {flagship.get('soundrop_upc', 'N/A')} | Work No: {flagship.get('iprs_work_no', 'N/A')}")
    print("-" * 76)
    wa = comms.get("whatsapp_channel", {})
    print(f" 💬 WHATSAPP BRIDGE STATUS: [{wa.get('status', 'UNKNOWN')}]")
    print(f"   • Target Chat: {wa.get('target_chat', 'Notes')} | Daemon: {wa.get('daemon', 'DAEMON-WA')}")
    print(f"   • Staging File: {wa.get('staging_file', 'N/A')}")
    print("-" * 76)
    print(f" 📜 RECENT EVOLUTION LEDGER (Last 5 Milestones):")
    for ev in ledger[-5:]:
        ts = ev.get("timestamp", "").split("T")[0]
        print(f"   [{ev.get('id', 'EVT')}] {ts} [{ev.get('category', 'GEN')}] {ev.get('summary', '')}")
    print("=" * 76 + "\n")


def cmd_sync(args):
    """Synchronize context with workspace files and catalog database."""
    print("🔄 Synchronizing Transmic Space context...")
    state = load_json(CONTEXT_FILE)
    if not state:
        state = {}

    catalog = load_json(CATALOG_DB)
    if catalog:
        works = catalog.get("repertoire_works", [])
        yt_releases = catalog.get("youtube_releases", [])
        if "catalog_benchmarks" not in state:
            state["catalog_benchmarks"] = {}
        if yt_releases:
            state["catalog_benchmarks"]["total_youtube_productions"] = len(yt_releases)
        if works:
            state["catalog_benchmarks"]["total_iprs_registered_works"] = len(works)

    now_iso = datetime.now().astimezone().isoformat()
    if "orchestrator" not in state:
        state["orchestrator"] = {}
    state["orchestrator"]["last_updated"] = now_iso

    # File counts
    subdirs = ["00_CONTEXT", "01_DATABASE", "02_DOCS", "03_ASSETS", "04_SCRIPTS", "05_COMMUNICATIONS", "04_LINKTREE"]
    stats = {}
    for sd in subdirs:
        p = PROJECT_DIR / sd
        if p.exists():
            stats[sd] = len([f for f in p.rglob("*") if f.is_file()])
        else:
            stats[sd] = 0

    state["workspace_metrics"] = {
        "file_distribution": stats,
        "last_scan": now_iso
    }

    save_json(CONTEXT_FILE, state)
    print(f"✅ Context synchronized successfully at {now_iso}")
    print(f"   File inventory: {stats}")


def cmd_log_event(args):
    """Log a new milestone or directorial decision into the evolution ledger."""
    state = load_json(CONTEXT_FILE)
    if not state:
        print("❌ Error: context_state.json not found!")
        sys.exit(1)

    ledger = state.setdefault("evolution_ledger", [])
    next_num = len(ledger) + 1
    event_id = f"EVT-{next_num:03d}"
    now_iso = datetime.now().astimezone().isoformat()

    new_event = {
        "id": event_id,
        "timestamp": now_iso,
        "category": args.category.upper(),
        "summary": args.summary
    }
    ledger.append(new_event)
    state["orchestrator"]["last_updated"] = now_iso
    save_json(CONTEXT_FILE, state)

    print(f"✅ Logged event {event_id} [{args.category.upper()}]: {args.summary}")


def cmd_audit(args):
    """Run workspace compliance audit for Transmic files."""
    audit_script = WORKSPACE_ROOT / "_SYSTEM" / "scripts" / "audit_compliance.py"
    if not audit_script.exists():
        print(f"❌ Error: {audit_script} not found!")
        sys.exit(1)

    print("🔍 Running compliance audit for TRANSMIC...")
    cmd = [sys.executable, str(audit_script), "--root", str(WORKSPACE_ROOT), "--project", "TRANSMIC"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(res.stderr)


def main():
    parser = argparse.ArgumentParser(description="Transmic Space Orchestrator Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # status
    p_status = subparsers.add_parser("status", help="Show orchestrator status and living context")
    p_status.set_defaults(func=cmd_status)

    # sync
    p_sync = subparsers.add_parser("sync", help="Synchronize context with catalog and files")
    p_sync.set_defaults(func=cmd_sync)

    # log-event
    p_log = subparsers.add_parser("log-event", help="Log an evolutionary milestone event")
    p_log.add_argument("--category", required=True, help="Category (e.g., RELEASE, DIRECTIVE, DECISION, ASSET)")
    p_log.add_argument("--summary", required=True, help="One-line summary of the event")
    p_log.add_argument("--author", default="Transmic Space Orchestrator", help="Author of the entry")
    p_log.set_defaults(func=cmd_log_event)

    # audit
    p_audit = subparsers.add_parser("audit", help="Audit Transmic Space compliance")
    p_audit.set_defaults(func=cmd_audit)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
