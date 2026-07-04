import os
import sys
import argparse
from notebooklm_tools.cli.commands.notebook import get_client

# Force utf-8 stdout encoding for proper logging
sys.stdout.reconfigure(encoding='utf-8')

def setup_proxy(proxy_str=None):
    if proxy_str:
        os.environ['HTTP_PROXY'] = proxy_str
        os.environ['HTTPS_PROXY'] = proxy_str
        print(f"Using explicit proxy: {proxy_str}")
    elif 'HTTP_PROXY' in os.environ or 'HTTPS_PROXY' in os.environ:
        print("Using system environment proxy settings.")
    else:
        print("No proxy configured. Connecting directly.")

def cmd_mindmap(args):
    setup_proxy(args.proxy)
    print(f"Generating mind map for notebook {args.notebook_id}...")
    try:
        client = get_client()
        r = client.generate_mind_map(args.notebook_id)
        if not r or not r.get('mind_map_json'):
            print("[ERROR] Failed to generate mind map JSON.")
            sys.exit(1)
            
        print(f"Saving mind map as '{args.title}'...")
        s = client.save_mind_map(args.notebook_id, r['mind_map_json'], title=args.title)
        if s:
            print(f"[OK] Mind map saved successfully! Mind Map ID: {s.get('mind_map_id')}")
        else:
            print("[ERROR] Failed to save mind map.")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Error occurred: {e}")
        sys.exit(1)

def cmd_slides(args):
    setup_proxy(args.proxy)
    print(f"Generating slide deck for notebook {args.notebook_id}...")
    try:
        client = get_client()
        r = client.create_slide_deck(args.notebook_id, focus_prompt=args.prompt)
        if not r or not r.get('artifact_id'):
            print(f"[ERROR] Failed to generate slide deck: {r}")
            sys.exit(1)
            
        artifact_id = r.get('artifact_id')
        print(f"[OK] Slide deck generated successfully! Artifact ID: {artifact_id}")
        if args.title:
            print(f"Renaming slide deck to '{args.title}'...")
            success = client.rename_studio_artifact(artifact_id, args.title)
            if success:
                print("[OK] Renamed successfully.")
            else:
                print("[WARNING] Failed to rename slide deck.")
    except Exception as e:
        print(f"[ERROR] Error occurred: {e}")
        sys.exit(1)

def cmd_infographic(args):
    setup_proxy(args.proxy)
    print(f"Generating infographic for notebook {args.notebook_id}...")
    try:
        client = get_client()
        r = client.create_infographic(args.notebook_id, focus_prompt=args.prompt)
        if not r or not r.get('artifact_id'):
            print(f"[ERROR] Failed to generate infographic: {r}")
            sys.exit(1)
            
        artifact_id = r.get('artifact_id')
        print(f"[OK] Infographic generated successfully! Artifact ID: {artifact_id}")
        if args.title:
            print(f"Renaming infographic to '{args.title}'...")
            success = client.rename_studio_artifact(artifact_id, args.title)
            if success:
                print("[OK] Renamed successfully.")
            else:
                print("[WARNING] Failed to rename infographic.")
    except Exception as e:
        print(f"[ERROR] Error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="NotebookLM Visual Organizer")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Mind map subcommand
    mm_parser = subparsers.add_parser("mindmap", help="Generate a mind map")
    mm_parser.add_argument("--notebook-id", required=True, help="Target Notebook ID")
    mm_parser.add_argument("--title", default="Mind Map", help="Title for the saved mind map")
    mm_parser.add_argument("--proxy", help="Optional proxy URL (e.g. http://127.0.0.1:7897)")
    
    # Slides subcommand
    sd_parser = subparsers.add_parser("slides", help="Generate a slide deck")
    sd_parser.add_argument("--notebook-id", required=True, help="Target Notebook ID")
    sd_parser.add_argument("--title", default="Slide Deck", help="Title for the slide deck")
    sd_parser.add_argument("--prompt", default="", help="Focus prompt/instruction for slide creation")
    sd_parser.add_argument("--proxy", help="Optional proxy URL (e.g. http://127.0.0.1:7897)")
    
    # Infographic subcommand
    info_parser = subparsers.add_parser("infographic", help="Generate an infographic")
    info_parser.add_argument("--notebook-id", required=True, help="Target Notebook ID")
    info_parser.add_argument("--title", default="Infographic", help="Title for the infographic")
    info_parser.add_argument("--prompt", default="", help="Focus prompt/instruction for infographic creation")
    info_parser.add_argument("--proxy", help="Optional proxy URL (e.g. http://127.0.0.1:7897)")
    
    args = parser.parse_args()
    
    if args.command == "mindmap":
        cmd_mindmap(args)
    elif args.command == "slides":
        cmd_slides(args)
    elif args.command == "infographic":
        cmd_infographic(args)

if __name__ == "__main__":
    main()
