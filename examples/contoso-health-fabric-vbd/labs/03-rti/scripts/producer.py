"""producer.py — post synthetic claims to the Eventstream custom endpoint.

Usage:
    ENDPOINT_URL=https://... python producer.py --rate 50 --duration 300
"""
import os, json, time, random, argparse, uuid, datetime as dt
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--rate", type=int, default=50, help="events per second")
parser.add_argument("--duration", type=int, default=300, help="seconds to run")
args = parser.parse_args()

endpoint = os.environ["ENDPOINT_URL"]
providers = [f"P{ i:04d}" for i in range(2000)]

start = time.time()
while time.time() - start < args.duration:
    batch = [
        {
            "claim_id": str(uuid.uuid4()),
            "provider_id": random.choice(providers),
            "member_id": f"M{random.randint(0, 49999):05d}",
            "claim_amount": round(random.lognormvariate(4.5, 0.8), 2),
            "claim_time": dt.datetime.utcnow().isoformat() + "Z",
        }
        for _ in range(args.rate)
    ]
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(batch).encode(),
        headers={"Content-Type": "application/json"},
    )
    urllib.request.urlopen(req).read()
    time.sleep(1)
