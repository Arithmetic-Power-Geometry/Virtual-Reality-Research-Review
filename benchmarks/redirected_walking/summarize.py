"""Summarize an RDW results CSV and emit provenance-friendly JSON."""
import argparse,csv,json,hashlib
from collections import defaultdict
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--out",default="summary.json")
    a=ap.parse_args(); p=Path(a.csv); rows=list(csv.DictReader(p.open()))
    groups=defaultdict(list)
    for r in rows: groups[(r["space"],r["controller"])].append(r)
    summary=[]
    for (space,controller),rs in sorted(groups.items()):
        n=len(rs)
        summary.append({
          "space":space,"controller":controller,"n":n,
          "mean_resets":sum(float(x["resets"]) for x in rs)/n,
          "mean_boundary_violations":sum(float(x["boundary_violations"]) for x in rs)/n,
          "mean_min_clearance_m":sum(float(x["min_clearance_m"]) for x in rs)/n,
          "mean_injected_rotation_deg":sum(float(x["mean_abs_injected_rotation_deg"]) for x in rs)/n
        })
    out={"input_file":p.name,"input_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"runs":len(rows),"groups":summary}
    Path(a.out).write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
