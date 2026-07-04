import os
import sys
import glob
import argparse
from notebooklm_tools.cli.commands.notebook import get_client

# Force utf-8 stdout encoding for proper console logging
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

def cmd_sync(args):
    setup_proxy(args.proxy)
    
    notebook_id = args.notebook_id
    workspace_dir = args.dir
    exts = args.exts.split(',') if args.exts else ["*.md", "*.png"]
    
    if not os.path.exists(workspace_dir):
        print(f"[ERROR] Workspace directory does not exist: {workspace_dir}")
        sys.exit(1)
        
    print(f"Connecting to NotebookLM client...")
    try:
        client = get_client()
    except Exception as e:
        print(f"[ERROR] Failed to initialize NotebookLM client: {e}")
        sys.exit(1)
        
    print(f"Fetching existing sources from notebook ID: {notebook_id}...")
    try:
        sources = client.get_notebook_sources_with_types(notebook_id)
        existing_titles = {s['title'].lower() for s in sources if s.get('title')}
        print(f"Found {len(existing_titles)} existing sources in the notebook.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch notebook sources: {e}")
        sys.exit(1)
        
    # Scan local files
    local_files = []
    for ext in exts:
        pattern = os.path.join(workspace_dir, ext.strip())
        local_files.extend(glob.glob(pattern))
        
    print(f"Scanned {len(local_files)} local files matching {exts} in {workspace_dir}.")
    
    uploaded_count = 0
    skipped_count = 0
    failed_count = 0
    
    for filepath in local_files:
        filename = os.path.basename(filepath)
        filename_lower = filename.lower()
        
        if filename_lower in existing_titles:
            print(f"[SKIP] '{filename}' is already uploaded.")
            skipped_count += 1
            continue
            
        print(f"[UPLOAD] Uploading '{filename}'...")
        try:
            # We set wait=True to block until processing completes
            result = client.add_file(notebook_id, filepath, wait=True, wait_timeout=180.0)
            print(f"  [OK] Uploaded successfully! Source ID: {result.get('id')}")
            uploaded_count += 1
        except Exception as e:
            print(f"  [ERROR] Failed to upload '{filename}': {e}")
            failed_count += 1
            
    print("\n--- Sync Summary ---")
    print(f"  Skipped (Already present): {skipped_count}")
    print(f"  Uploaded successfully:     {uploaded_count}")
    print(f"  Failed:                     {failed_count}")
    
    if failed_count > 0:
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="NotebookLM Workspace Syncer")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    sync_parser = subparsers.add_parser("sync", help="Sync workspace files to NotebookLM")
    sync_parser.add_argument("--notebook-id", required=True, help="Target Notebook ID")
    sync_parser.add_argument("--dir", required=True, help="Workspace directory to scan")
    sync_parser.add_argument("--proxy", help="Optional proxy URL (e.g. http://127.0.0.1:7897)")
    sync_parser.add_argument("--exts", default="*.md,*.png", help="Comma-separated file patterns (default: *.md,*.png)")
    
    args = parser.parse_args()
    
    if args.command == "sync":
        cmd_sync(args)

if __name__ == "__main__":
    main()
